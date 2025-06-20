<script setup lang="ts">
import SearchAndSortHeader from './SearchAndSortHeader.vue'

import samplePet1 from '@/assets/images/sample-pet-1.jpg'
import samplePet2 from '@/assets/images/sample-pet-2.jpg'
import samplePet3 from '@/assets/images/sample-pet-3.jpg'
import samplePet4 from '@/assets/images/sample-pet-4.jpg'
import samplePet5 from '@/assets/images/sample-pet-5.webp'
</script>

<template>
  <section class="h-[90vh] w-[87vw]">
    <div class="p-5 h-full flex flex-col">
      <h1 class="text-6xl font-semibold">Applications</h1>

      <SearchAndSortHeader />

      <div class="overflow-x-auto">
        <table class="dui-table">
          <!-- head -->
          <thead>
            <tr>
              <th class="text-center text-2xl w-1/2">Pet</th>
              <th class="text-center text-2xl">Application Date</th>
              <th class="text-center text-2xl">Application Status</th>
            </tr>
          </thead>
          <tbody>
            <!-- row 1 -->
            <tr class="hover:bg-base-300 text-center">
              <td>
                <div class="flex items-center justify-center gap-3">
                  <div class="avatar">
                    <div class="mask mask-squircle h-12 w-12">
                      <img
                        :src="samplePet1"
                        alt="Avatar Tailwind CSS Component"
                        class="w-full h-full object-cover"
                      />
                    </div>
                  </div>
                  <div>
                    <div class="font-bold text-xl">Tabby</div>
                    <div class="text-base opacity-50">Corva Shelter</div>
                  </div>
                </div>
              </td>
              <td class="text-xl font-medium">September 24, 2025 12:23 PM</td>
              <td class="text-xl font-medium">Approved</td>
            </tr>
            <!-- row 2 -->
            <tr class="hover:bg-base-300 text-center">
              <td>
                <div class="flex items-center justify-center gap-3">
                  <div class="avatar">
                    <div class="mask mask-squircle h-12 w-12">
                      <img
                        :src="samplePet2"
                        alt="Avatar Tailwind CSS Component"
                        class="w-full h-full object-cover"
                      />
                    </div>
                  </div>
                  <div>
                    <div class="font-bold text-xl">Tabby</div>
                    <div class="text-base opacity-50">Corva Shelter</div>
                  </div>
                </div>
              </td>
              <td class="text-xl font-medium">September 24, 2025 12:23 PM</td>
              <td class="text-xl font-medium">Approved</td>
            </tr>
            <!-- row 3 -->
            <tr class="hover:bg-base-300 text-center">
              <td>
                <div class="flex items-center justify-center gap-3">
                  <div class="avatar">
                    <div class="mask mask-squircle h-12 w-12">
                      <img
                        :src="samplePet3"
                        alt="Avatar Tailwind CSS Component"
                        class="w-full h-full object-cover"
                      />
                    </div>
                  </div>
                  <div>
                    <div class="font-bold text-xl">Tabby</div>
                    <div class="text-base opacity-50">Corva Shelter</div>
                  </div>
                </div>
              </td>
              <td class="text-xl font-medium">September 24, 2025 12:23 PM</td>
              <td class="text-xl font-medium">Approved</td>
            </tr>
            <!-- row 4 -->
            <tr class="hover:bg-base-300 text-center">
              <td>
                <div class="flex items-center justify-center gap-3">
                  <div class="avatar">
                    <div class="mask mask-squircle h-12 w-12">
                      <img
                        :src="samplePet4"
                        alt="Avatar Tailwind CSS Component"
                        class="w-full h-full object-cover"
                      />
                    </div>
                  </div>
                  <div>
                    <div class="font-bold text-xl">Tabby</div>
                    <div class="text-base opacity-50">Corva Shelter</div>
                  </div>
                </div>
              </td>
              <td class="text-xl font-medium">September 24, 2025 12:23 PM</td>
              <td class="text-xl font-medium">Approved</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
