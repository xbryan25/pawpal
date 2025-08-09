<script setup lang="ts">
import statusIcon from '@/assets/images/status-icon.svg'

import { defineProps } from 'vue'
import { RouterLink } from 'vue-router'

interface Props {
  name?: string
  status?: string
  petFirstImageUrl?: string
  petId?: string
  petShelter?: string
  isNotDummy: boolean
}

const props = defineProps<Props>()
</script>

<template>
  <div
    class="dui-card relative flex flex-col bg-[#D9D9D9] w-full h-full items-center shadow-[6px_6px_4px_rgba(0,0,0,0.375)] transition-transform duration-300 hover:scale-105"
    v-if="props.isNotDummy"
  >
    <div class="absolute w-full flex pt-2 pl-2">
      <div
        class="flex w-[40%] h-[90%] 2xl:w-[30%] bg-green-500 rounded-full justify-center items-center"
        v-if="props.status === 'available'"
      >
        <img :src="statusIcon" class="w-[15%] h-[50%] 2xl:w-[17%]" />
        <p class="font-semibold text-white">Available</p>
      </div>
    </div>

    <div
      class="dui-avatar w-[9vw] h-[9vw] 2xl:w-[10.5vw] 2xl:h-[10.5vw] overflow-hidden rounded-full mt-9"
    >
      <img :src="petFirstImageUrl" class="w-full h-full object-cover" alt="Tabby" />
    </div>

    <div
      class="dui-card-body flex flex-col justify-center gap-[10%] p-0 pb-2 2xl:pb-3 pt-2 max-h-[40%]"
    >
      <h2 class="dui-card-title justify-center text-xl 2xl:text-2xl font-bold">{{ props.name }}</h2>
      <p class="text-center max-h-5 font-bold text-[#989595]">{{ props.petShelter }}</p>
      <div class="dui-card-actions justify-center">
        <RouterLink
          class="btn btn-primary font-bold cursor-pointer hover:underline"
          :to="`/pets/view/${props.petId}`"
        >
          View Details
        </RouterLink>
      </div>
    </div>
  </div>

  <div class="w-full h-full invisible pointer-events-none select-none" v-else></div>
</template>
