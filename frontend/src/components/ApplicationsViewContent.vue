<script setup lang="ts">
import { onMounted, ref, type Ref } from 'vue'
import axios from 'axios'

import { useAuthStore } from '@/stores/useAuthStore'

import SearchAndSortHeader from './SearchAndSortHeader.vue'
import TableRow from './TableRow.vue'

interface AdoptionApplicationDetails {
  applicationId?: string
  userName?: string
  userProfileUrl?: string
  petId: string
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
    let apiUrlExtension: string = ''
    let params = {}

    if (auth.isUser) {
      apiUrlExtension = '/adoption-applications/get-adopter-applications'

      params = { userId: auth.userId }
    } else {
      apiUrlExtension = '/adoption-applications/get-shelter-applications'

      params = { shelterId: auth.shelterId }
    }

    const adoptionApplicationsResponse = await axios.get(`${apiUrl}${apiUrlExtension}`, {
      params: params,
    })

    if (auth.isUser) {
      adoptionApplicationsResponse.data.adopterApplications.forEach(
        (adoptionApplication: AdoptionApplicationDetails) => {
          adoptionApplications.value.push(adoptionApplication)
        },
      )
    } else {
      adoptionApplicationsResponse.data.shelterApplications.forEach(
        (adoptionApplication: AdoptionApplicationDetails) => {
          adoptionApplications.value.push(adoptionApplication)
        },
      )
    }
  } catch (error) {
    console.error('Error retrieving data from backend', error)
  }
})
</script>

<template>
  <section class="h-[90vh] w-[87vw] bg-primary-content">
    <div class="p-5 h-full flex flex-col">
      <h1 class="text-6xl font-fredoka font-semibold text-base-content">Applications</h1>

      <SearchAndSortHeader />

      <div class="overflow-x-auto">
        <table class="dui-table">
          <thead>
            <tr>
              <th
                class="text-center text-3xl w-1/4 font-fredoka font-medium text-base-content"
                v-if="auth.isShelterStaff"
              >
                Adopter
              </th>
              <th class="text-center text-3xl w-1/4 font-fredoka font-medium text-base-content">
                Pet
              </th>
              <th
                class="text-center text-3xl px-2 w-1/5 font-fredoka font-medium text-base-content"
              >
                Application Date
              </th>
              <th
                class="text-center text-3xl px-2 w-1/5 font-fredoka font-medium text-base-content"
              >
                Application Status
              </th>
              <th class="text-center text-3xl w-1/4" v-if="auth.isShelterStaff"></th>
            </tr>
          </thead>
          <tbody>
            <TableRow
              v-for="(adoptionApplication, index) in adoptionApplications"
              :key="index"
              :applicationId="adoptionApplication.applicationId"
              :userName="adoptionApplication.userName"
              :userProfileUrl="adoptionApplication.userProfileUrl"
              :petId="adoptionApplication.petId"
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
