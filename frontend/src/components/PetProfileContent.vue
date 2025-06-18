<script setup lang="ts">
import PetCard from './PetCard.vue'
import SearchAndSortHeader from './SearchAndSortHeader.vue'

import samplePet1 from '@/assets/images/sample-pet-1.jpg'
import samplePet2 from '@/assets/images/sample-pet-2.jpg'
import samplePet3 from '@/assets/images/sample-pet-3.jpg'
import samplePet4 from '@/assets/images/sample-pet-4.jpg'
import samplePet5 from '@/assets/images/sample-pet-5.webp'
</script>

<template>
  <section class="h-full w-[87vw]">
    <div class="p-5 h-full flex flex-col">
      <h1 class="text-6xl font-semibold">Pets</h1>

      <div class="flex flex-row gap-4 mt-6 h-[80%] w-full">
        <div class="flex-1 flex flex-row gap-2">
          <div class="flex flex-col gap-2">
            <div
              class="h-[5vw] w-[5vw] bg-green-200 transition-transform duration-300 hover:scale-105 cursor-pointer"
            >
              <img :src="samplePet1" class="w-full h-full object-cover rounded-lg" />
            </div>
            <div
              class="h-[5vw] w-[5vw] bg-green-200 transition-transform duration-300 hover:scale-105 cursor-pointer"
            >
              <img :src="samplePet2" class="w-full h-full object-cover rounded-lg" />
            </div>
            <div
              class="h-[5vw] w-[5vw] bg-green-200 transition-transform duration-300 hover:scale-105 cursor-pointer"
            >
              <img :src="samplePet3" class="w-full h-full object-cover rounded-lg" />
            </div>
            <div
              class="h-[5vw] w-[5vw] bg-green-200 transition-transform duration-300 hover:scale-105 cursor-pointer"
            >
              <img :src="samplePet4" class="w-full h-full object-cover rounded-lg" />
            </div>
            <div
              class="h-[5vw] w-[5vw] bg-green-200 transition-transform duration-300 hover:scale-105 cursor-pointer"
            >
              <img :src="samplePet5" class="w-full h-full object-cover rounded-lg" />
            </div>
          </div>
          <div class="flex-1 bg-green-200 rounded-lg">
            <img :src="samplePet1" class="w-full h-full object-cover rounded-lg" />
          </div>
        </div>

        <div class="flex flex-col w-[40%] pt-5">
          <p class="font-bold text-6xl">Tabby</p>

          <div class="flex flex-col mt-5 mb-10 gap-3">
            <div class="flex-1">
              <p class="font-bold text-xl">Shelter</p>
              <p class="pl-5 font-semibold">Corva Shelter</p>
            </div>

            <div class="flex-1 flex flex-row">
              <div class="flex-1">
                <p class="font-bold text-xl">Sex</p>
                <p class="pl-5 font-semibold">Male</p>
              </div>

              <div class="flex-1">
                <p class="font-bold text-xl">Adoption Applications</p>
                <p class="pl-5 font-semibold">1</p>
              </div>
            </div>

            <div class="flex-1 flex flex-row">
              <div class="flex-1">
                <p class="font-bold text-xl">Species</p>
                <p class="pl-5 font-semibold">Cat</p>
              </div>

              <div class="flex-1">
                <p class="font-bold text-xl">Breed</p>
                <p class="pl-5 font-semibold">Puspin</p>
              </div>
            </div>

            <div class="flex-1">
              <p class="font-bold text-xl">Description</p>
              <p class="pl-5 font-semibold">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
              </p>
            </div>
          </div>

          <!-- This blank div is for spacing purposes -->
          <div class="flex-1"></div>

          <button class="h-[10%] bg-gray-200 font-bold text-3xl dui-btn">Adopt</button>
        </div>
      </div>
    </div>
  </section>
</template>
