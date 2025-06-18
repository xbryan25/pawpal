<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav class="h-screen w-[13vw] bg-[#f2f2f2] dark:bg-[#434343]">
    <div class="h-screen flex flex-col items-center justify-between">
      <div class="h-[10vh] w-full bg-[#D9D9D9] flex items-center justify-center">
        <h2 class="font-bold text-3xl">PawPal</h2>
      </div>
      <div class="flex-1 w-full bg-[#AAAAAA]">
        <div class="mx-10 my-10 flex flex-col gap-3">
          <RouterLink class="font-semibold text-xl" to="/pets/view">Pets</RouterLink>
          <p class="font-semibold text-xl">Applications</p>
          <p class="font-semibold text-xl">Reports</p>
        </div>
      </div>
      <div class="h-[10vh] w-full bg-[#D9D9D9] flex items-center">
        <div class="mx-2 w-full flex">
          <div class="rounded-full bg-[#707070] h-15 min-w-15"></div>
          <div class="w-full h-15 flex flex-col justify-center pl-2">
            <p class="font-bold max-h-5 text-sm">Bryan Agan</p>
            <p class="max-h-5 text-sm">Adopter</p>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
