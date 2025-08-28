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
    class="dui-card relative flex flex-col w-full h-full items-center transition-transform duration-300 hover:scale-105 hover:bg-base-100 border-base-content border-3"
    v-if="props.isNotDummy"
  >
    <div class="absolute w-full flex pt-2 pl-2">
      <div
        class="flex w-[40%] h-[90%] 2xl:w-[30%] bg-green-500 rounded-full justify-center items-center"
        v-if="props.status === 'available'"
      >
        <img :src="statusIcon" class="w-[15%] h-[50%] 2xl:w-[17%]" />
        <p class="font-medium text-white font-fredoka">Available</p>
      </div>

      <div
        class="flex w-[40%] h-[90%] 2xl:w-[30%] bg-gray-500 rounded-full justify-center items-center"
        v-if="props.status === 'adopted'"
      >
        <img :src="statusIcon" class="w-[15%] h-[50%] 2xl:w-[17%]" />
        <p class="font-medium text-white font-fredoka">Adopted</p>
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
      <h2
        class="dui-card-title justify-center text-xl 2xl:text-2xl font-medium font-fredoka text-base-content"
      >
        {{ props.name }}
      </h2>
      <p class="text-center max-h-5 font-medium font-fredoka text-warning dark:text-accent-content">
        {{ props.petShelter }}
      </p>
      <div class="dui-card-actions justify-center">
        <RouterLink
          class="btn btn-primary cursor-pointer font-medium font-fredoka hover:underline text-base-content"
          :to="`/pets/view/${props.petId}`"
        >
          View Details
        </RouterLink>
      </div>
    </div>
  </div>

  <div class="w-full h-full invisible pointer-events-none select-none" v-else></div>
</template>
