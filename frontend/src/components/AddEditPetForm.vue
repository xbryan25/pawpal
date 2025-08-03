<script setup lang="ts">
import axios from 'axios'
import { reactive, onMounted, ref, type Ref } from 'vue'
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

const selectedSpecies = ref<string>('')
let species: { species_id: string; species_name: string }[] = []
const species_names: Ref<string[]> = ref<string[]>([])

const selectedShelter = ref<string>('')
let shelters: { shelter_id: string; name: string }[] = []
const shelter_names: Ref<string[]> = ref<string[]>([])

const handleSubmit = async () => {
  const petFormData = new FormData()

  petFormData.append('name', newPetForm.name)
  petFormData.append('birthDate', newPetForm.birthDate)
  petFormData.append('sex', newPetForm.sex)
  petFormData.append('status', newPetForm.status)
  petFormData.append('description', newPetForm.description)
  petFormData.append('breed', newPetForm.breed)
  petFormData.append('species', newPetForm.species)
  petFormData.append('shelter', newPetForm.shelter)

  newPetForm.petPhotos.forEach((file, index) => {
    petFormData.append('petPhotos', file)
  })

  try {
    const response = await axios.post(`${apiUrl}/pets/register-pet`, petFormData)
  } catch (error) {
    console.error('Error adding pet', error)
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
  <section class="h-[90vh] w-[87vw]">
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
                />
              </div>

              <div class="flex-1">
                <h3 class="text-lg font-semibold">Breed</h3>
                <label class="dui-input w-full">
                  <input
                    v-model="newPetForm.breed"
                    maxlength="127"
                    type="text"
                    placeholder="e.g. John"
                    required
                  />
                </label>
              </div>
            </div>

            <div class="flex gap-4">
              <div class="flex-1">
                <h3 class="text-lg font-semibold">Sex</h3>
                <label class="dui-input w-full">
                  <input
                    v-model="newPetForm.sex"
                    maxlength="127"
                    type="text"
                    placeholder="e.g. John"
                    required
                  />
                </label>
              </div>

              <div class="flex-1">
                <h3 class="text-lg font-semibold">Birth Date</h3>
                <input
                  v-model="newPetForm.birthDate"
                  type="date"
                  class="dui-input w-full px-3 py-2"
                  required
                />
              </div>
            </div>

            <div>
              <h3 class="text-lg font-semibold">Shelter</h3>
              <SearchableCombobox
                v-model="selectedShelter"
                :options="shelter_names"
                placeholder="Select a shelter"
              />
            </div>

            <div>
              <h3 class="text-lg font-semibold">Description</h3>
              <textarea
                v-model="newPetForm.description"
                class="dui-textarea resize-none w-full"
                placeholder="Bio"
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
                />
              </div>
            </div>
          </div>
        </div>

        <div class="pt-15 flex justify-center">
          <button class="dui-btn dui-btn-primary w-[15%] text-xl" type="submit">Create Pet</button>
        </div>
      </form>
    </div>
  </section>
</template>
