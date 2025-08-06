<script setup lang="ts">
import { onMounted } from 'vue'
import axios from 'axios'

import PetCard from './PetCard.vue'
import SearchAndSortHeader from './SearchAndSortHeader.vue'

const apiUrl = import.meta.env.VITE_API_URL

let petList: { name: string; petFirstImageUrl: string; petId: string; shelterId: string }[] = []

// Make get request to get pets, also get 1st petPhoto url

onMounted(async () => {
  try {
    const response = await axios.get(`${apiUrl}/pets/list`)

    petList = response.data

    console.log(petList)
  } catch (error) {
    console.error('Error retrieving pet list', error)
  }
})
</script>

<template>
  <section class="h-[90vh] w-[87vw]">
    <div class="p-5 h-full flex flex-col">
      <h1 class="text-6xl font-semibold">Pets</h1>

      <SearchAndSortHeader />

      <div class="flex-1 grid grid-cols-5 place-items-center gap-4">
        <PetCard v-for="n in 10" :key="n" />
      </div>
    </div>
  </section>
</template>
