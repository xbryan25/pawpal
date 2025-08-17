<script setup lang="ts">
import { onMounted, ref, type Ref } from 'vue'
import axios from 'axios'

import { useAuthStore } from '@/stores/useAuthStore'

import SearchAndSortHeader from './SearchAndSortHeader.vue'
import TableRow from './TableRow.vue'

interface AdoptionApplicationDetails {
  applicationDate: string
  petFirstImageUrl: string
  petName: string
  shelterName: string
  status: string
}

const apiUrl = import.meta.env.VITE_API_URL

const auth = useAuthStore()

const adoptionApplications: Ref<AdoptionApplicationDetails[]> = ref([])

onMounted(async () => {
  try {
    const adoptionApplicationsResponse = await axios.get(
      `${apiUrl}/adoption-applications/get-adopter-applications`,
      {
        params: {
          userId: auth.userId,
        },
      },
    )

    adoptionApplicationsResponse.data.adopterApplications.forEach(
      (adoptionApplication: AdoptionApplicationDetails) => {
        adoptionApplications.value.push(adoptionApplication)
      },
    )

    console.log(adoptionApplications.value)
  } catch (error) {
    console.error('Error retrieving data from backend', error)
  }
})
</script>

<template>
  <section class="h-[90vh] w-[87vw]">
    <div class="p-5 h-full flex flex-col">
      <h1 class="text-6xl font-semibold">Applications</h1>

      <SearchAndSortHeader />

      <div class="overflow-x-auto">
        <table class="dui-table">
          <thead>
            <tr>
              <th class="text-center text-2xl w-1/2">Pet</th>
              <th class="text-center text-2xl">Application Date</th>
              <th class="text-center text-2xl">Application Status</th>
            </tr>
          </thead>
          <tbody>
            <TableRow
              v-for="(adoptionApplication, index) in adoptionApplications"
              :key="index"
              :applicationDate="adoptionApplication.applicationDate"
              v-bind:petFirstImageUrl="adoptionApplication.petFirstImageUrl"
              :petName="adoptionApplication.petName"
              :shelterName="adoptionApplication.shelterName"
              :status="adoptionApplication.status"
            />
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
