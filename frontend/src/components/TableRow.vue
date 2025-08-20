<script setup lang="ts">
import { RouterLink } from 'vue-router'

import { useAuthStore } from '@/stores/useAuthStore'

interface Props {
  userName: string | undefined
  userProfileUrl: string | undefined
  petId: string
  applicationDate: string
  petFirstImageUrl: string
  petName: string
  shelterName: string
  status: string
}

const props = defineProps<Props>()

const auth = useAuthStore()

const dateObject = new Date(props.applicationDate)

const date = dateObject.toLocaleDateString('en-US', {
  year: 'numeric',
  month: 'long',
  day: 'numeric',
})
const time = dateObject.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' })
</script>

<template>
  <tr class="hover:bg-base-300 text-center">
    <td v-if="auth.isShelterStaff">
      <div class="flex items-center justify-center gap-3">
        <div class="avatar">
          <div class="mask mask-squircle h-12 w-12">
            <img
              :src="props.userProfileUrl"
              alt="Avatar Tailwind CSS Component"
              class="w-full h-full object-cover"
            />
          </div>
        </div>
        <div>
          <div class="font-bold text-xl">{{ props.userName }}</div>
        </div>
      </div>
    </td>
    <td>
      <RouterLink
        class="flex items-center justify-center gap-3 cursor-pointer"
        :to="`/pets/view/${props.petId}`"
      >
        <div class="avatar">
          <div class="mask mask-squircle h-12 w-12">
            <img
              :src="props.petFirstImageUrl"
              alt="Avatar Tailwind CSS Component"
              class="w-full h-full object-cover"
            />
          </div>
        </div>
        <div>
          <div class="font-bold text-xl">{{ props.petName }}</div>
          <div class="text-base opacity-50">{{ props.shelterName }}</div>
        </div>
      </RouterLink>
    </td>
    <td class="text-xl font-medium px-2">
      <div class="flex flex-col">
        <p>{{ date }}</p>
        <p>{{ time }}</p>
      </div>
    </td>
    <td class="text-xl font-medium px-2">{{ props.status }}</td>
    <td class="px-0" v-if="auth.isShelterStaff">
      <RouterLink
        class="flex items-center justify-center gap-3 cursor-pointer"
        :to="`/applications/application-details/${props.petId}`"
        ><svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 -960 960 960"
          class="w-8 h-8 fill-black transition-transform duration-200 hover:scale-[1.15]"
        >
          <path
            d="M440-280h80v-240h-80v240Zm40-320q17 0 28.5-11.5T520-640q0-17-11.5-28.5T480-680q-17 0-28.5 11.5T440-640q0 17 11.5 28.5T480-600Zm0 520q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"
          />
        </svg>
      </RouterLink>
    </td>
  </tr>
</template>
