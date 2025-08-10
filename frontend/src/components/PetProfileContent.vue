<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/useAuthStore'
import axios from 'axios'

import PetProfileImageCard from './PetProfileImageCard.vue'

import statusIcon from '@/assets/images/status-icon.svg'

interface PetImage {
  image_url: string
  sort_order: number
}

interface Pet {
  name: string
  birthDate: string
  description: string
  sex: string
  status: string
  breed: string
  species: string
  shelter: string
  petImages: PetImage[]
}

const route = useRoute()
const auth = useAuthStore()

const petId: string = route.params.id as string
const selectedPetImageUrl = ref('')

const apiUrl: string = import.meta.env.VITE_API_URL

const selectedPet = reactive<Pet>({
  name: '',
  birthDate: '',
  sex: '',
  status: '',
  description: '',
  breed: '',
  species: '',
  shelter: '',
  petImages: [],
})

function handleSelectPhoto(petImageUrl: string) {
  selectedPetImageUrl.value = petImageUrl
}

onMounted(async () => {
  try {
    const response = await axios.get(`${apiUrl}/pets/get-details`, {
      params: {
        petId: petId,
      },
    })

    // while response.data gives what Pet interface wants, this approach is careless, will improve this soon
    Object.assign(selectedPet, response.data)

    selectedPetImageUrl.value = selectedPet.petImages[0].image_url
  } catch (error) {
    console.error('Error retrieving pet details', error)
  }
})
</script>

<template>
  <section class="h-full w-[87vw]">
    <div class="p-5 h-full flex flex-col">
      <h1 class="text-6xl font-semibold">Pets</h1>

      <div class="flex flex-row gap-4 mt-6 h-[80%] w-full">
        <div class="flex-1 flex flex-row gap-2">
          <div class="flex flex-col gap-2">
            <PetProfileImageCard
              v-for="petImageUrl in selectedPet.petImages"
              :key="petImageUrl.image_url"
              :petImageUrl="petImageUrl.image_url"
              :sortOrder="petImageUrl.sort_order"
              @selectPhoto="handleSelectPhoto"
            />
          </div>

          <div class="flex-1 rounded-lg" v-if="selectedPet?.petImages?.length">
            <img :src="selectedPetImageUrl" class="w-full h-full object-cover rounded-lg" />
          </div>
        </div>

        <div class="flex flex-col w-[40%] pt-0">
          <div class="flex flex-row mr-10">
            <div
              class="flex w-[22%] h-[100%] 2xl:w-[17%] bg-green-500 rounded-full justify-center items-center"
              v-if="selectedPet.status === 'available'"
            >
              <!-- <img :src="statusIcon" class="w-[15%] h-[50%] 2xl:w-[17%]" /> -->
              <svg
                xmlns="http://www.w3.org/2000/svg"
                height="18px"
                viewBox="0 -960 960 960"
                width="18px"
                fill="#FFFFFF"
              >
                <path
                  d="M480-280q83 0 141.5-58.5T680-480q0-83-58.5-141.5T480-680q-83 0-141.5 58.5T280-480q0 83 58.5 141.5T480-280Zm0 200q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Z"
                />
              </svg>
              <p class="font-semibold text-white">&nbsp;Available</p>
            </div>

            <div class="flex flex-1 gap-2 justify-end">
              <!-- edit-icon.svg -->
              <RouterLink :to="{ path: '/pets/edit-pet', query: { petId } }">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  height="24px"
                  viewBox="0 -960 960 960"
                  width="24px"
                  fill="#000000"
                  class="cursor-pointer"
                >
                  <path
                    d="M200-200h57l391-391-57-57-391 391v57Zm-80 80v-170l528-527q12-11 26.5-17t30.5-6q16 0 31 6t26 18l55 56q12 11 17.5 26t5.5 30q0 16-5.5 30.5T817-647L290-120H120Zm640-584-56-56 56 56Zm-141 85-28-29 57 57-29-28Z"
                  />
                </svg>
              </RouterLink>

              <!-- delete-icon.svg -->
              <svg
                xmlns="http://www.w3.org/2000/svg"
                height="24px"
                viewBox="0 -960 960 960"
                width="24px"
                fill="#000000"
                class="cursor-pointer"
                @click="console.log('delete')"
              >
                <path
                  d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm400-600H280v520h400v-520ZM360-280h80v-360h-80v360Zm160 0h80v-360h-80v360ZM280-720v520-520Z"
                />
              </svg>
            </div>
          </div>

          <p class="font-bold text-6xl">{{ selectedPet.name }}</p>

          <div class="flex flex-col mt-5 mb-10 gap-3">
            <div class="flex-1">
              <p class="font-bold text-xl">Shelter</p>
              <p class="pl-5 font-semibold">{{ selectedPet.shelter }}</p>
            </div>

            <div class="flex-1 flex flex-row">
              <div class="flex-1">
                <p class="font-bold text-xl">Sex</p>
                <p class="pl-5 font-semibold">
                  {{ selectedPet.sex.charAt(0).toUpperCase() + selectedPet.sex.slice(1) }}
                </p>
              </div>

              <div class="flex-1">
                <p class="font-bold text-xl">Adoption Applications</p>
                <p class="pl-5 font-semibold">??? (Not yet implemented)</p>
              </div>
            </div>

            <div class="flex-1 flex flex-row">
              <div class="flex-1">
                <p class="font-bold text-xl">Species</p>
                <p class="pl-5 font-semibold">{{ selectedPet.species }}</p>
              </div>

              <div class="flex-1">
                <p class="font-bold text-xl">Breed</p>
                <p class="pl-5 font-semibold">{{ selectedPet.breed }}</p>
              </div>
            </div>

            <div class="flex-1">
              <p class="font-bold text-xl">Description</p>
              <p class="pl-5 font-semibold">
                {{ selectedPet.description }}
              </p>
            </div>
          </div>

          <!-- This blank div is for spacing purposes -->
          <div class="flex-1"></div>

          <button class="h-[10%] bg-gray-200 font-bold text-3xl dui-btn" v-if="auth.isUser">
            Adopt
          </button>
        </div>
      </div>
    </div>
  </section>
</template>
