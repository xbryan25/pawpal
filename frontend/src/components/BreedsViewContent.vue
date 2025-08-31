<script setup lang="ts">
import { onMounted, ref, type Ref } from 'vue'
import axios from 'axios'

import SearchAndSortHeader from './SearchAndSortHeader.vue'
import BreedsTableRow from './BreedsSpeciesTableRow.vue'
import ThemeToggle from './ThemeToggle.vue'

interface BreedDetails {
  breedName: string
  speciesName: string
  numOfRegisteredPets: number
}

const apiUrl = import.meta.env.VITE_API_URL

const allBreedDetails: Ref<BreedDetails[]> = ref([])

onMounted(async () => {
  try {
    const breedDetailsResponse = await axios.get(`${apiUrl}/breed/get-all-breed-details`)

    console.log(breedDetailsResponse.data)

    breedDetailsResponse.data.allBreedDetails.forEach((breedDetails: BreedDetails) =>
      allBreedDetails.value.push(breedDetails),
    )
  } catch (error) {
    console.error('Error retrieving data from backend', error)
  }
})
</script>

<template>
  <section class="h-[90vh] w-[87vw] bg-primary-content">
    <div class="p-5 h-full flex flex-col">
      <div class="flex">
        <h1 class="flex-1 text-6xl font-semibold font-fredoka text-base-content">Breeds</h1>
        <ThemeToggle />
      </div>

      <SearchAndSortHeader />

      <div class="overflow-x-auto">
        <table class="dui-table">
          <thead>
            <tr>
              <th class="text-center text-3xl w-1/4 font-fredoka font-medium text-base-content">
                Breed
              </th>
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
            <BreedsTableRow
              v-for="(breedDetails, index) in allBreedDetails"
              :key="index"
              :breedName="breedDetails.breedName"
              :speciesName="breedDetails.speciesName"
              :numOfRegisteredPets="breedDetails.numOfRegisteredPets"
              :rowType="'breed'"
            />
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
