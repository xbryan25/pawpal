<script setup lang="ts">
// TODO: Add dummy pet cards for pet view

import { onMounted, ref, type Ref } from 'vue'
import axios from 'axios'

import PetCard from './PetCard.vue'
import SearchAndSortHeader from './SearchAndSortHeader.vue'
import ThemeToggle from './ThemeToggle.vue'

const apiUrl = import.meta.env.VITE_API_URL

interface Pet {
  petId: string
  name: string
  status: string
  petFirstImageUrl: string
  petShelter: string
}

const petList: Ref<Pet[]> = ref<Pet[]>([])
const dummyFramesToLoad: Ref<number> = ref(0)

// Make get request to get pets, also get 1st petPhoto url

onMounted(async () => {
  try {
    const response = await axios.get(`${apiUrl}/pets/list`)

    petList.value = response.data

    dummyFramesToLoad.value = 10 - petList.value.length
  } catch (error) {
    console.error('Error retrieving pet list', error)
  }
})
</script>

<template>
  <section class="h-[90vh] w-[87vw] bg-primary-content">
    <div class="p-5 h-full flex flex-col">
      <div class="flex">
        <h1 class="flex-1 text-6xl font-semibold font-fredoka text-base-content">Pets</h1>
        <ThemeToggle />
      </div>

      <SearchAndSortHeader />

      <div class="flex-1 grid grid-rows-2 grid-cols-5 place-items-center gap-4">
        <PetCard
          v-for="pet in petList"
          :key="pet.petId"
          :name="pet.name"
          :status="pet.status"
          :petFirstImageUrl="pet.petFirstImageUrl"
          :petId="pet.petId"
          :petShelter="pet.petShelter"
          :isNotDummy="true"
        />

        <PetCard v-for="_ in dummyFramesToLoad" :key="_" :isNotDummy="false" />
      </div>
    </div>
  </section>
</template>
