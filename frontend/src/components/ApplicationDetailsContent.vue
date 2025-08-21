<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { RouterLink, useRoute } from 'vue-router'
import axios from 'axios'

interface AdopterDetails {
  adopterName: string
  adopterGender: string
  adopterPhoneNumber: string
  adopterBirthDate: string
  adopterEmail: string
  adopterTotalApplications: number
  adopterAcceptedApplications: number
}

interface PetDetails {
  petId: string
  petName: string
  petFirstImageUrl: string
}

interface ApplicationDetails {
  applicationStatus: string
  adopterDetails: AdopterDetails
  petDetails: PetDetails
}

const applicationDetails = reactive<ApplicationDetails>({
  applicationStatus: '',
  adopterDetails: {
    adopterName: '',
    adopterGender: '',
    adopterPhoneNumber: '',
    adopterBirthDate: '',
    adopterEmail: '',
    adopterTotalApplications: 0,
    adopterAcceptedApplications: 0,
  },
  petDetails: {
    petId: '',
    petName: '',
    petFirstImageUrl: '',
  },
})

const route = useRoute()

const applicationId: string = route.params.applicationId as string

const apiUrl: string = import.meta.env.VITE_API_URL

const isLoading = ref(true)

onMounted(async () => {
  try {
    const applicationDetailsResponse = await axios.get(
      `${apiUrl}/adoption-applications/get-application-details`,
      {
        params: {
          applicationId: applicationId,
        },
      },
    )

    // while response.data gives what Pet interface wants, this approach is careless, will improve this soon
    Object.assign(applicationDetails, applicationDetailsResponse.data)

    isLoading.value = false

    console.log(applicationDetails)
  } catch (error) {
    console.error('Error retrieving pet details', error)
  }
})
</script>

<template>
  <section class="h-full">
    <div class="p-5 h-full flex flex-col">
      <h1 class="text-6xl font-semibold">Application Details</h1>
      <div class="flex pt-10 px-[15%] gap-x-[5%]">
        <div class="flex flex-col gap-y-[2%] flex-[2]">
          <div class="text-center">
            <h2 class="text-4xl font-semibold">Adopter</h2>
          </div>

          <div class="flex flex-col bg-gray-400 h-115 rounded-lg" v-if="isLoading">
            <div class="dui-skeleton w-full h-full rounded-lg bg-gray-400"></div>
          </div>

          <div class="flex flex-col bg-gray-400 h-115 rounded-lg p-5" v-else>
            <div class="flex dui-avatar justify-center py-2">
              <div class="ring-primary ring-offset-base-100 w-35 rounded-full ring-2 ring-offset-2">
                <img src="https://img.daisyui.com/images/profile/demo/spiderperson@192.webp" />
              </div>
            </div>

            <div class="flex flex-col gap-y-2 px-10 pt-5">
              <div class="flex justify-center">
                <div class="flex-1">
                  <p class="font-bold text-xl">Name</p>
                  <p class="pl-5 font-semibold">
                    {{ isLoading ? '-' : applicationDetails.adopterDetails.adopterName }}
                  </p>
                </div>

                <div class="flex-1">
                  <p class="font-bold text-xl">Gender</p>
                  <p class="pl-5 font-semibold">
                    {{ isLoading ? '-' : applicationDetails.adopterDetails.adopterGender }}
                  </p>
                </div>
              </div>
              <div class="flex justify-center">
                <div class="flex-1">
                  <p class="font-bold text-xl">Phone Number</p>
                  <p class="pl-5 font-semibold">
                    {{ isLoading ? '-' : applicationDetails.adopterDetails.adopterPhoneNumber }}
                  </p>
                </div>

                <div class="flex-1">
                  <p class="font-bold text-xl">Birth Date</p>
                  <p class="pl-5 font-semibold">
                    {{ isLoading ? '-' : applicationDetails.adopterDetails.adopterBirthDate }}
                  </p>
                </div>
              </div>
              <div class="flex justify-center">
                <div class="flex-1">
                  <p class="font-bold text-xl">Email</p>
                  <p class="pl-5 font-semibold">
                    {{ isLoading ? '-' : applicationDetails.adopterDetails.adopterEmail }}
                  </p>
                </div>
              </div>
              <div class="flex justify-center">
                <div class="flex-1">
                  <p class="font-bold text-xl">Total Applications</p>
                  <p class="pl-5 font-semibold">
                    {{
                      isLoading ? '-' : applicationDetails.adopterDetails.adopterTotalApplications
                    }}
                  </p>
                </div>

                <div class="flex-1">
                  <p class="font-bold text-xl">Accepted Applications</p>
                  <p class="pl-5 font-semibold">
                    {{
                      isLoading
                        ? '-'
                        : applicationDetails.adopterDetails.adopterAcceptedApplications
                    }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="flex flex-col gap-y-[2%] justify-center flex-1">
          <div class="text-center">
            <h2 class="text-4xl font-semibold">Pet</h2>
          </div>

          <div class="flex flex-col bg-gray-400 h-60 rounded-lg" v-if="isLoading">
            <div class="dui-skeleton w-full h-full rounded-lg bg-gray-400"></div>
          </div>

          <div class="flex flex-col bg-gray-400 h-60 rounded-lg p-5" v-else>
            <div class="flex dui-avatar justify-center">
              <div
                class="ring-primary ring-offset-base-100 w-35 rounded-full ring-2 ring-offset-2 dui-skeleton"
                v-if="isLoading"
              ></div>

              <div
                class="ring-primary ring-offset-base-100 w-35 rounded-full ring-2 ring-offset-2"
                v-else
              >
                <img :src="applicationDetails.petDetails.petFirstImageUrl" />
              </div>
            </div>

            <div class="flex flex-col gap-y-1 pt-2 items-center">
              <p class="text-2xl font-bold">
                {{ isLoading ? '-' : applicationDetails.petDetails.petName }}
              </p>
              <RouterLink
                class="font-bold"
                :to="`/pets/view/${applicationDetails.petDetails.petId}`"
                >View details</RouterLink
              >
            </div>
          </div>
        </div>
      </div>

      <div class="flex gap-5 pt-10 px-[40%]">
        <button class="flex-1 dui-btn dui-btn-success text-3xl h-15">Approve</button>
      </div>
    </div>
  </section>
</template>
