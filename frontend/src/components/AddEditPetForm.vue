<script setup lang="ts">
import axios from 'axios'
import { reactive, onMounted, ref, watch, type Ref, defineProps } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { useToast, POSITION } from 'vue-toastification'
import * as uuid from 'uuid'

import SearchableCombobox from './SearchableCombobox.vue'
import ImageInput from './ImageInput.vue'

interface PetImage {
  imageUrl: string
  sortOrder: number
}

interface ExistingPet {
  petId: string
  name: string
  birthDate: string
  sex: string
  status: string
  description: string
  breed: string
  species: string
  shelter: string
  petImages: PetImage[]
}

interface Props {
  mode: string
  petId?: string
}

interface ImageSlot {
  id: string
  mode: 'edit' | 'add'
  imageUrl?: string
  file?: File
  sortOrder: number
  resetCounter: number
}

const props = defineProps<Props>()

console.log('props.mode addeditform ' + props.mode)

const petForm = reactive<ExistingPet>({
  petId: '',
  name: '',
  birthDate: '',
  sex: '',
  status: 'available',
  description: '',
  breed: '',
  species: '',
  shelter: '',
  petImages: [],
})

const apiUrl = import.meta.env.VITE_API_URL
const toast = useToast()
const isLoading: Ref<boolean> = ref(false)
const router = useRouter()

let originalImageSlots: ImageSlot[] = []
const imageSlots = ref<ImageSlot[]>([])

const selectedBreed = ref<string>('')
let breeds: { breed_id: string; breed_name: string }[] = []
const breed_names: Ref<string[]> = ref<string[]>([])

const selectedSpecies = ref<string>('')
let species: { species_id: string; species_name: string }[] = []
const species_names: Ref<string[]> = ref<string[]>([])

const selectedShelter = ref<string>('')
let shelters: { shelter_id: string; name: string }[] = []
const shelter_names: Ref<string[]> = ref<string[]>([])

const ready = ref(false)

const isAddImageInputDisabled = ref(false)
const hasNoImageChanges = ref(true)

function loadPetForEdit(existing: ExistingPet) {
  petForm.petId = existing.petId
  petForm.name = existing.name
  petForm.birthDate = formatDateForInput(existing.birthDate)
  petForm.sex = existing.sex
  petForm.status = existing.status
  petForm.description = existing.description

  petForm.species = existing.species
  selectedSpecies.value = petForm.species

  petForm.breed = existing.breed
  selectedBreed.value = petForm.breed

  petForm.shelter = existing.shelter
  selectedShelter.value = petForm.shelter

  // Map each field to convert from snakecase to camelcase
  imageSlots.value = existing.petImages.map((img: any) => ({
    id: uuid.v4(),
    mode: 'edit',
    imageUrl: img.image_url,
    sortOrder: img.sort_order,
    resetCounter: 0,
  }))

  originalImageSlots = existing.petImages.map((img: any) => ({
    id: uuid.v4(),
    mode: 'edit',
    imageUrl: img.image_url,
    sortOrder: img.sort_order,
    resetCounter: 0,
  }))
}

function formatDateForInput(dateString: string): string {
  // Returns YYYY-MM-DD

  const date = new Date(dateString)
  return date.toISOString().split('T')[0]
}

const handleSubmit = async () => {
  isLoading.value = true

  const petFormData = new FormData()

  petFormData.append('name', petForm.name)
  petFormData.append('birthDate', petForm.birthDate)
  petFormData.append('sex', petForm.sex)
  petFormData.append('status', petForm.status)
  petFormData.append('description', petForm.description)
  petFormData.append(
    'breedId',
    breeds.find((breed) => breed.breed_name === selectedBreed.value)?.breed_id || '',
  )
  petFormData.append(
    'speciesId',
    species.find((species_singular) => species_singular.species_name === selectedSpecies.value)
      ?.species_id || '',
  )
  petFormData.append(
    'shelterId',
    shelters.find((shelter) => shelter.name === selectedShelter.value)?.shelter_id || '',
  )

  // counter is put outside so that it won't increment if blank image file and image.mode == 'add'
  let counter: number = 0

  imageSlots.value.forEach((image) => {
    if (!image.file && image.mode == 'add') {
      return
    }

    petFormData.append(
      `petImagesMeta-${counter + 1}`,
      JSON.stringify({
        mode: image.mode,
        imageUrl: image.imageUrl,
        sortOrder: image.sortOrder,
      }),
    )

    if (image.file) {
      petFormData.append(`petImagesFile-${counter + 1}`, image.file)
    }

    counter++
  })

  // If imageSlots is blank
  if (counter == 0) {
    isLoading.value = false
    return
  }

  try {
    let responseMessage: string = 'Unexpected error.'

    if (props.mode == 'add-pet') {
      const addPetResponse = await axios.post(`${apiUrl}/pets/register-pet`, petFormData)

      responseMessage = addPetResponse.data.message
    } else {
      petFormData.append('petId', petForm.petId)

      const editPetResponse = await axios.post(`${apiUrl}/pets/edit-pet`, petFormData)

      responseMessage = editPetResponse.data.message

      console.log(responseMessage)
    }

    toast.success(responseMessage, {
      position: POSITION.TOP_RIGHT,
      timeout: 5000,
      closeOnClick: true,
      pauseOnFocusLoss: true,
      pauseOnHover: true,
      draggable: true,
      draggablePercent: 0.6,
      showCloseButtonOnHover: true,
      hideProgressBar: false,
      closeButton: 'button',
      icon: true,
      rtl: false,
    })

    if (props.mode == 'add-pet') {
      router.push('/pets/view')
    } else {
      router.push(`/pets/view/${props.petId}`)
    }
  } catch (error) {
    let errorMessage: string = ''

    if (axios.isAxiosError(error) && error.response) {
      errorMessage = error.response.data.error
    } else {
      errorMessage = 'Unexpected error.'
    }

    toast.error(`Failed to add pet. ${errorMessage}`, {
      position: POSITION.TOP_RIGHT,
      timeout: 5000,
      closeOnClick: true,
      pauseOnFocusLoss: true,
      pauseOnHover: true,
      draggable: true,
      draggablePercent: 0.6,
      showCloseButtonOnHover: true,
      hideProgressBar: false,
      closeButton: 'button',
      icon: true,
      rtl: false,
    })
  } finally {
    isLoading.value = false
  }
}

function selectImage(index: number, file: File) {
  const MAX_SIZE_MB = 10
  const MAX_SIZE_BYTES = MAX_SIZE_MB * 1024 * 1024

  if (file.size > MAX_SIZE_BYTES) {
    toast.error('Images should not exceed 10 MB. Choose another pic.', {
      position: POSITION.TOP_RIGHT,
      timeout: 5000,
      closeOnClick: true,
      pauseOnFocusLoss: true,
      pauseOnHover: true,
      draggable: true,
      draggablePercent: 0.6,
      showCloseButtonOnHover: true,
      hideProgressBar: false,
      closeButton: 'button',
      icon: true,
      rtl: false,
    })

    // Update reset counter so that ImageInput watch() will activate

    imageSlots.value[index].resetCounter = (imageSlots.value[index].resetCounter ?? 0) + 1

    return
  }

  compareCurrentImageSlotsToOriginal()

  const newSlots = [...imageSlots.value]
  newSlots[index] = {
    id: uuid.v4(),
    mode: 'add',
    file,
    sortOrder: index + 1,
    resetCounter: 0,
  }

  imageSlots.value = newSlots

  console.log(imageSlots.value)
}

function deleteImage(index: number) {
  compareCurrentImageSlotsToOriginal()

  isAddImageInputDisabled.value = false

  const newSlots = [...imageSlots.value]

  if (newSlots.length > 1) {
    newSlots.splice(index, 1)

    imageSlots.value = newSlots
  }
}

function addImageInput() {
  compareCurrentImageSlotsToOriginal()

  const newSlots = [...imageSlots.value]

  if (newSlots.length < 5) {
    newSlots.push({
      id: uuid.v4(),
      mode: 'add',
      sortOrder: newSlots.length,
      resetCounter: 0,
    })
  }

  if (newSlots.length == 5) {
    isAddImageInputDisabled.value = true
  }

  imageSlots.value = newSlots

  console.log(imageSlots.value)
}

function moveImageInput(index: number | undefined) {
  const newSlots = [...imageSlots.value]

  if (!index) {
    return
  } else {
    index--
  }

  if (index == 0) {
    return
  } else {
    ;[newSlots[index], newSlots[index - 1]] = [newSlots[index - 1], newSlots[index]]

    newSlots[index].sortOrder = index + 1
    newSlots[index - 1].sortOrder = index
  }

  imageSlots.value = newSlots
}

function resetImageInput() {
  const newSlots = [...originalImageSlots]

  imageSlots.value = newSlots

  hasNoImageChanges.value = true
}

const compareCurrentImageSlotsToOriginal = () => {
  hasNoImageChanges.value =
    imageSlots.value.length === originalImageSlots.length &&
    imageSlots.value.every((val, index) => val === originalImageSlots[index])
}

watch(selectedSpecies, async (newVal) => {
  const breed_response = await axios.get(`${apiUrl}/breed/list`, {
    params: {
      species_name: selectedSpecies.value,
    },
  })

  breeds = breed_response.data
  breed_names.value = breeds.map((breed) => breed.breed_name)

  if (!newVal) selectedBreed.value = ''
})

onMounted(async () => {
  try {
    const speciesResponse = await axios.get(`${apiUrl}/species/list`)
    const shelterResponse = await axios.get(`${apiUrl}/shelter/list`)

    species = speciesResponse.data
    species_names.value = species.map((species_singular) => species_singular.species_name)

    shelters = shelterResponse.data
    shelter_names.value = shelters.map((shelter) => shelter.name)

    if (props.mode === 'edit-pet') {
      const petDetailsResponse = await axios.get(`${apiUrl}/pets/get-details`, {
        params: {
          petId: props.petId,
        },
      })

      loadPetForEdit(petDetailsResponse.data)
    }

    ready.value = true
  } catch (error) {
    console.error('Error retrieving data from backend', error)
  }
})
</script>

<template>
  <section class="relative h-full w-[87vw] bg-primary-content">
    <div class="flex flex-col">
      <div class="p-5 h-full">
        <h1
          class="text-6xl font-semibold font-fredoka text-base-content"
          v-if="props.mode === 'add-pet'"
        >
          Add Pet
        </h1>
        <h1 class="text-6xl font-semibold font-fredoka text-base-content" v-else>Edit Pet</h1>
      </div>

      <form @submit.prevent="handleSubmit" enctype="multipart/form-data">
        <div class="flex flex-1 pt-15 px-15 gap-20 w-full">
          <div class="flex flex-col gap-4 flex-1">
            <div>
              <h3 class="font-medium text-xl font-fredoka text-base-content">Pet Name</h3>
              <label class="dui-input w-full font-fredoka text-base-content">
                <input
                  v-model="petForm.name"
                  maxlength="127"
                  type="text"
                  placeholder="e.g. John"
                  required
                  :disabled="isLoading"
                />
              </label>
            </div>

            <div class="flex gap-4">
              <div class="flex-1">
                <h3 class="font-medium text-xl font-fredoka text-base-content">Species</h3>
                <SearchableCombobox
                  v-if="ready"
                  v-model="selectedSpecies"
                  :options="species_names"
                  placeholder="Select a species"
                  :isDisabled="isLoading"
                />
              </div>

              <div class="flex-1">
                <h3 class="font-medium text-xl font-fredoka text-base-content">Breed</h3>
                <SearchableCombobox
                  v-if="ready"
                  v-model="selectedBreed"
                  :options="breed_names"
                  placeholder="Select a breed"
                  :isDisabled="isLoading"
                />
              </div>
            </div>

            <div class="flex gap-4">
              <div class="flex-1">
                <h3 class="font-medium text-xl font-fredoka text-base-content">Sex</h3>
                <select
                  v-model="petForm.sex"
                  class="dui-select w-full font-fredoka text-base-conten"
                  required
                  :disabled="isLoading"
                >
                  <option value="male">Male</option>
                  <option value="female">Female</option>
                </select>
              </div>

              <div class="flex-1">
                <h3 class="font-medium text-xl font-fredoka text-base-content">Birth Date</h3>
                <input
                  v-model="petForm.birthDate"
                  type="date"
                  class="dui-input w-full px-3 py-2 font-fredoka text-base-conten"
                  required
                  :disabled="isLoading"
                />
              </div>
            </div>

            <div>
              <h3 class="font-medium text-xl font-fredoka text-base-content">Shelter</h3>
              <SearchableCombobox
                v-if="ready"
                v-model="selectedShelter"
                :options="shelter_names"
                placeholder="Select a shelter"
                :isDisabled="isLoading"
              />
            </div>

            <div>
              <h3 class="font-medium text-xl font-fredoka text-base-content">Short Description</h3>
              <textarea
                v-model="petForm.description"
                class="dui-textarea resize-none w-full h-24 font-fredoka text-base-conten"
                placeholder="Bio..."
                :disabled="isLoading"
              ></textarea>
            </div>
          </div>

          <div class="flex flex-col min-w-0 gap-4 flex-1">
            <ImageInput
              v-for="(image, index) in imageSlots"
              :key="image.id"
              :mode="image.mode"
              :imageUrl="image.imageUrl"
              :fileName="image?.file?.name"
              :index="index + 1"
              :resetCounter="image.resetCounter"
              @selectImage="(file) => selectImage(index, file)"
              @deleteImage="() => deleteImage(index)"
              @moveImage="(index) => moveImageInput(index)"
            />

            <div class="flex px-[40%] gap-[5%]">
              <button
                :disabled="isAddImageInputDisabled"
                class="flex-1 dui-btn dui-tooltip disabled:opacity-50 hover:bg-primary-content bg-base-100 border-base-content/25 transition-transform duration-200 hover:scale-[1.10]"
                data-tip="Add image input"
                type="button"
                @click="addImageInput"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 -960 960 960"
                  fill="currentColor"
                  class="w-6 h-6 text-accent dark:text-base-content"
                >
                  <path d="M440-120v-320H120v-80h320v-320h80v320h320v80H520v320h-80Z" />
                </svg>
              </button>
              <button
                :disabled="hasNoImageChanges"
                class="flex-1 dui-btn dui-tooltip disabled:opacity-50 hover:bg-primary-content bg-base-100 border-base-content/25 transition-transform duration-200 hover:scale-[1.10]"
                data-tip="Reset changes"
                type="button"
                @click="resetImageInput"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 -960 960 960"
                  fill="currentColor"
                  class="w-6 h-6 text-accent dark:text-base-content"
                >
                  <path
                    d="m656-120-56-56 84-84-84-84 56-56 84 84 84-84 56 56-83 84 83 84-56 56-84-83-84 83Zm-176 0q-138 0-240.5-91.5T122-440h82q14 104 92.5 172T480-200q11 0 20.5-.5T520-203v81q-10 1-19.5 1.5t-20.5.5ZM120-560v-240h80v94q51-64 124.5-99T480-840q150 0 255 105t105 255h-80q0-117-81.5-198.5T480-760q-69 0-129 32t-101 88h110v80H120Zm414 190-94-94v-216h80v184l56 56-42 70Z"
                  />
                </svg>
              </button>
            </div>
          </div>
        </div>

        <div class="pt-15 flex gap-3 justify-center">
          <RouterLink
            class="dui-btn dark:bg-red-900 w-[12%] text-xl font-medium font-fredoka text-base-content border-base-content border-2"
            :to="`/pets/view/${props.petId}`"
          >
            Cancel
          </RouterLink>

          <button
            class="dui-btn dark:bg-green-900 w-[12%] text-xl font-medium font-fredoka text-base-content border-base-content border-2"
            type="submit"
            :disabled="isLoading"
          >
            {{ props.mode === 'add-pet' ? 'Create Pet' : 'Edit Pet' }}
          </button>
        </div>
      </form>
    </div>

    <div
      v-if="isLoading"
      class="absolute inset-0 bg-white/50 flex items-center justify-center z-50 rounded-lg"
    >
      <span class="dui-loading dui-loading-spinner w-16 h-16 text-primary"></span>
    </div>
  </section>
</template>
