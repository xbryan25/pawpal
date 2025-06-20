<script setup lang="ts">
import samplePet1 from '@/assets/images/sample-pet-1.jpg'
</script>

<template>
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
</template>
