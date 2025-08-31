<script setup lang="ts">
import { onMounted, ref, type Ref } from 'vue'
import axios from 'axios'

import SearchAndSortHeader from './SearchAndSortHeader.vue'
import SpeciesTableRow from './BreedsSpeciesTableRow.vue'
import ThemeToggle from './ThemeToggle.vue'

interface SpeciesDetails {
  speciesName: string
  numOfRegisteredPets: number
}

const apiUrl = import.meta.env.VITE_API_URL

const allSpeciesDetails: Ref<SpeciesDetails[]> = ref([])

onMounted(async () => {
  try {
    const speciesDetailsResponse = await axios.get(`${apiUrl}/species/get-all-species-details`)

    speciesDetailsResponse.data.allSpeciesDetails.forEach((speciesDetails: SpeciesDetails) =>
      allSpeciesDetails.value.push(speciesDetails),
    )

    console.log(allSpeciesDetails.value)
  } catch (error) {
    console.error('Error retrieving data from backend', error)
  }
})
</script>

<template>
  <section class="h-[90vh] w-[87vw] bg-primary-content">
    <div class="p-5 h-full flex flex-col">
      <div class="flex">
        <h1 class="flex-1 text-6xl font-semibold font-fredoka text-base-content">Species</h1>
        <ThemeToggle />
      </div>

      <SearchAndSortHeader />

      <div class="overflow-x-auto">
        <table class="dui-table">
          <thead>
            <tr>
              <th
                class="text-center text-3xl px-2 w-1/5 font-fredoka font-medium text-base-content"
              >
                Species
              </th>
              <th
                class="text-center text-3xl px-2 w-1/5 font-fredoka font-medium text-base-content"
              >
                No. of Registered Pets
              </th>
            </tr>
          </thead>
          <tbody>
            <SpeciesTableRow
              v-for="(speciesDetails, index) in allSpeciesDetails"
              :key="index"
              :speciesName="speciesDetails.speciesName"
              :numOfRegisteredPets="speciesDetails.numOfRegisteredPets"
              :rowType="'species'"
            />
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
