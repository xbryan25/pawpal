<script setup lang="ts">
import axios from 'axios'
import { reactive, onMounted, ref, watch, type Ref } from 'vue'
import { useRouter } from 'vue-router'
import { useToast, POSITION } from 'vue-toastification'

import SearchableCombobox from './SearchableCombobox.vue'

interface NewPet {
  name: string
  birthDate: string
  sex: string
  status: string
  description: string
  breed: string
  species: string
  shelter: string
  petPhotos: File[]
}

const newPetForm = reactive<NewPet>({
  name: '',
  birthDate: '',
  sex: '',
  status: 'available',
  description: '',
  breed: '',
  species: '',
  shelter: '',
  petPhotos: [],
})

const apiUrl = import.meta.env.VITE_API_URL
const toast = useToast()
const isLoading: Ref<boolean> = ref(false)
const router = useRouter()

const selectedBreed = ref<string>('')
let breeds: { breed_id: string; breed_name: string }[] = []
const breed_names: Ref<string[]> = ref<string[]>([])

const selectedSpecies = ref<string>('')
let species: { species_id: string; species_name: string }[] = []
const species_names: Ref<string[]> = ref<string[]>([])

const selectedShelter = ref<string>('')
let shelters: { shelter_id: string; name: string }[] = []
const shelter_names: Ref<string[]> = ref<string[]>([])

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

  newPetForm.petPhotos.forEach((file, index) => {
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

  newPetForm.petPhotos[index] = file
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
    // const breed_response = await axios.get(`${apiUrl}/breed/list`)
    const species_response = await axios.get(`${apiUrl}/species/list`)
    const shelter_response = await axios.get(`${apiUrl}/shelter/list`)

    species = species_response.data
    species_names.value = species.map((species_singular) => species_singular.species_name)

    shelters = shelter_response.data
    shelter_names.value = shelters.map((shelter) => shelter.name)
  } catch (error) {
    console.error('Error retrieving data from backend', error)
  }
})
</script>

<template>
  <section class="relative h-[90vh] w-[87vw]">
    <div class="flex flex-col">
      <div class="p-5 h-full">
        <h1 class="text-6xl font-semibold">Add Pet</h1>
      </div>

      <form @submit.prevent="handleSubmit" enctype="multipart/form-data">
        <div class="flex flex-1 pt-15 px-15 gap-20">
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
                  v-model="selectedSpecies"
                  :options="species_names"
                  placeholder="Select a species"
                  :isDisabled="isLoading"
                />
              </div>

              <div class="flex-1">
                <h3 class="text-lg font-semibold">Breed</h3>
                <SearchableCombobox
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
                class="dui-textarea resize-none w-full"
                placeholder="Bio"
                :disabled="isLoading"
              ></textarea>
            </div>
          </div>

          <div class="flex flex-col gap-4 flex-1">
            <div>
              <h3 class="text-lg font-semibold">First Photo</h3>
              <div>
                <input
                  type="file"
                  class="dui-file-input w-full"
                  accept="image/*"
                  required
                  @change="(e) => handlePhotoChange(e, 0)"
                  :disabled="isLoading"
                />
              </div>
            </div>

            <div>
              <h3 class="text-lg font-semibold">Second Photo</h3>
              <div>
                <input
                  type="file"
                  class="dui-file-input w-full"
                  accept="image/*"
                  @change="(e) => handlePhotoChange(e, 1)"
                  :disabled="isLoading"
                />
              </div>
            </div>

            <div>
              <h3 class="text-lg font-semibold">Third Photo</h3>
              <div>
                <input
                  type="file"
                  class="dui-file-input w-full"
                  accept="image/*"
                  @change="(e) => handlePhotoChange(e, 2)"
                  :disabled="isLoading"
                />
              </div>
            </div>

            <div>
              <h3 class="text-lg font-semibold">Fourth Photo</h3>
              <div>
                <input
                  type="file"
                  class="dui-file-input w-full"
                  accept="image/*"
                  @change="(e) => handlePhotoChange(e, 3)"
                  :disabled="isLoading"
                />
              </div>
            </div>

            <div>
              <h3 class="text-lg font-semibold">Fifth Photo</h3>
              <div>
                <input
                  type="file"
                  class="dui-file-input w-full"
                  accept="image/*"
                  @change="(e) => handlePhotoChange(e, 4)"
                  :disabled="isLoading"
                />
              </div>
            </div>
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
