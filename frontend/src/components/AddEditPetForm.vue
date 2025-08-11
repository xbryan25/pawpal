<script setup lang="ts">
import axios from 'axios'
import { reactive, onMounted, ref, watch, type Ref, defineProps, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { useToast, POSITION } from 'vue-toastification'

import SearchableCombobox from './SearchableCombobox.vue'
import ImageInput from './ImageInput.vue'

interface NewPet {
  name: string
  birthDate: string
  sex: string
  status: string
  description: string
  breed: string
  species: string
  shelter: string
  petImages: File[]
}

interface PetImage {
  imageUrl: string
  sortOrder: number
}

interface ExistingPet {
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

const props = defineProps<Props>()

const newPetForm = reactive<NewPet>({
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

const existingPetImages = ref<PetImage[]>([])

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

const counter = ref(1)
const counterLowerLimit = ref(1)
const showAddImageInput = ref(false)

function loadPetForEdit(existing: ExistingPet) {
  newPetForm.name = existing.name
  newPetForm.birthDate = formatDateForInput(existing.birthDate)
  newPetForm.sex = existing.sex
  newPetForm.status = existing.status
  newPetForm.description = existing.description

  newPetForm.species = existing.species
  selectedSpecies.value = newPetForm.species

  newPetForm.breed = existing.breed
  selectedBreed.value = newPetForm.breed

  newPetForm.shelter = existing.shelter
  selectedShelter.value = newPetForm.shelter

  // Map each field to convert from snakecase to camelcase
  existingPetImages.value = existing.petImages.map((img: any) => ({
    imageUrl: img.image_url,
    sortOrder: img.sort_order,
  }))

  console.log('bacon')
  console.log(existingPetImages.value)

  counterLowerLimit.value = existingPetImages.value.length
}

function formatDateForInput(dateString: string): string {
  // Returns YYYY-MM-DD

  const date = new Date(dateString)
  return date.toISOString().split('T')[0]
}

const handleSubmit = async () => {
  isLoading.value = true

  const petFormData = new FormData()

  petFormData.append('name', newPetForm.name)
  petFormData.append('birthDate', newPetForm.birthDate)
  petFormData.append('sex', newPetForm.sex)
  petFormData.append('status', newPetForm.status)
  petFormData.append('description', newPetForm.description)
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

  newPetForm.petImages.forEach((file, index) => {
    petFormData.append('petPhotos', file)
  })

  try {
    const response = await axios.post(`${apiUrl}/pets/register-pet`, petFormData)

    const responseMessage: string = response.data.message

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

    router.push('/pets/view')
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

function test(imageFile: File) {
  console.log(imageFile)
}

const setShowAddImageInput = (state: boolean) => {
  showAddImageInput.value = state
}

const changeCounter = (operation: string) => {
  console.log(`counter.value ${counter.value}`)
  console.log(`counterLowerLimit.value ${counterLowerLimit.value}`)

  if (operation == 'add' && !showAddImageInput.value) {
    setShowAddImageInput(true)
    return
  } else if (
    operation == 'subtract' &&
    showAddImageInput.value &&
    counter.value == counterLowerLimit.value
  ) {
    setShowAddImageInput(false)
    return
  }

  if (operation == 'add' && counter.value < 5) {
    counter.value++
  } else if (operation == 'subtract' && counter.value > counterLowerLimit.value) {
    counter.value--
  }
}

function handlePhotoChange(event: Event, index: number) {
  const input = event.target as HTMLInputElement

  const file = input.files?.[0]

  if (!file) return

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

    input.value = ''
    return
  }

  newPetForm.petImages[index] = file
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
  <section class="relative h-[90vh] w-[87vw]">
    <div class="flex flex-col">
      <div class="p-5 h-full">
        <h1 class="text-6xl font-semibold" v-if="props.mode === 'add-pet'">Add Pet</h1>
        <h1 class="text-6xl font-semibold" v-else>Edit Pet</h1>
      </div>

      <form @submit.prevent="handleSubmit" enctype="multipart/form-data">
        <div class="flex flex-1 pt-15 px-15 gap-20 w-full">
          <div class="flex flex-col gap-4 flex-1">
            <div>
              <h3 class="text-lg font-semibold">Pet Name</h3>
              <label class="dui-input w-full">
                <input
                  v-model="newPetForm.name"
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
                <h3 class="text-lg font-semibold">Species</h3>
                <SearchableCombobox
                  v-if="ready"
                  v-model="selectedSpecies"
                  :options="species_names"
                  placeholder="Select a species"
                  :isDisabled="isLoading"
                />
              </div>

              <div class="flex-1">
                <h3 class="text-lg font-semibold">Breed</h3>
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
                <h3 class="text-lg font-semibold">Sex</h3>
                <select
                  v-model="newPetForm.sex"
                  class="dui-select w-full"
                  required
                  :disabled="isLoading"
                >
                  <option value="male">Male</option>
                  <option value="female">Female</option>
                </select>
              </div>

              <div class="flex-1">
                <h3 class="text-lg font-semibold">Birth Date</h3>
                <input
                  v-model="newPetForm.birthDate"
                  type="date"
                  class="dui-input w-full px-3 py-2"
                  required
                  :disabled="isLoading"
                />
              </div>
            </div>

            <div>
              <h3 class="text-lg font-semibold">Shelter</h3>
              <SearchableCombobox
                v-if="ready"
                v-model="selectedShelter"
                :options="shelter_names"
                placeholder="Select a shelter"
                :isDisabled="isLoading"
              />
            </div>

            <div>
              <h3 class="text-lg font-semibold">Description</h3>
              <textarea
                v-model="newPetForm.description"
                class="dui-textarea resize-none w-full h-24"
                placeholder="Bio"
                :disabled="isLoading"
              ></textarea>
            </div>
          </div>

          <div class="flex flex-col min-w-0 gap-4 flex-1">
            <ImageInput
              v-if="existingPetImages.length > 0"
              v-for="n in existingPetImages.length"
              :key="n"
              :mode="'edit'"
              :imageUrl="existingPetImages[n - 1]?.imageUrl"
              :index="n"
              @selectImage="(file) => console.log(file)"
              @deleteImage="() => changeCounter('subtract')"
            />
            <ImageInput
              v-if="showAddImageInput"
              v-for="n in counter"
              :key="n"
              :mode="'add'"
              :index="n + existingPetImages.length"
              @selectImage="(file) => console.log(file)"
              @deleteImage="() => changeCounter('subtract')"
            />
            <button class="dui-btn" type="button" @click="changeCounter('add')">+</button>
          </div>
        </div>

        <div class="pt-15 flex justify-center">
          <button
            class="dui-btn dui-btn-primary w-[15%] text-xl"
            type="submit"
            :disabled="isLoading"
          >
            Create Pet
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
