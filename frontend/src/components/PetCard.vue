<script setup lang="ts">
import statusIcon from '@/assets/images/status-icon.svg'

import { RouterLink } from 'vue-router'
</script>

<template>
  <div
    class="dui-card relative flex flex-col bg-[#D9D9D9] w-full h-full items-center shadow-[6px_6px_4px_rgba(0,0,0,0.375)] transition-transform duration-300 hover:scale-105"
  >
    <div class="absolute w-full flex pt-2 pl-2">
      <div
        class="flex w-[40%] h-[90%] 2xl:w-[30%] bg-green-500 rounded-full justify-center items-center"
      >
        <img :src="statusIcon" class="w-[15%] h-[50%] 2xl:w-[17%]" />
        <p class="font-semibold text-white">Available</p>
      </div>
    </div>

    <div
      class="dui-avatar w-[9vw] h-[9vw] 2xl:w-[10.5vw] 2xl:h-[10.5vw] overflow-hidden rounded-full mt-9"
    >
      <img
        src="https://img.daisyui.com/images/profile/demo/yellingcat@192.webp"
        class="w-full h-full object-cover"
        alt="Tabby"
      />
    </div>

    <div
      class="dui-card-body flex flex-col justify-center gap-[10%] p-0 pb-2 2xl:pb-3 pt-2 max-h-[40%]"
    >
      <h2 class="dui-card-title justify-center text-xl 2xl:text-2xl font-bold">Tabby</h2>
      <p class="text-center max-h-5 font-bold text-[#989595]">Pugaan Shelter</p>
      <div class="dui-card-actions justify-center">
        <RouterLink class="btn btn-primary font-bold cursor-pointer hover:underline" to="/pets/view/sample-id">
          View Details
        </RouterLink>
      </div>
    </div>
  </div>

  <!-- <div
    class="dui-card flex flex-row bg-[#D9D9D9] w-full h-full justify-center items-center shadow-[6px_6px_4px_rgba(0,0,0,0.375)] transition-transform duration-300 hover:scale-105"
    p0-
  >
    <div class="dui-avatar w-[9.5vw] h-[9.5vw] overflow-hidden rounded-full ml-5">
      <img
        src="https://img.daisyui.com/images/profile/demo/yellingcat@192.webp"
        class="w-full h-full object-cover"
        alt="Tabby"
      />
    </div>

    <div class="dui-card-body p-0 flex flex-col justify-center gap-6">
      <h2 class="dui-card-title justify-center text-2xl font-bold">Tabby</h2>
      <p class="text-center max-h-5 font-bold text-[#989595]">Pugaan Shelter</p>
      <div class="dui-card-actions justify-center">
        <button class="btn btn-primary font-bold">View Details</button>
      </div>
    </div>
  </div> -->
</template>
