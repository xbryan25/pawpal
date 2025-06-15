<script setup lang="ts">
import PetCard from './PetCard.vue'
</script>

<template>
  <section class="h-[90vh] w-[87vw]">
    <div class="p-5 h-full flex flex-col">
      <h1 class="text-6xl font-semibold">Pets</h1>

      <div class="h-10 bg-amber-900 my-5 text-white">Sort and search header</div>

      <div class="flex-1 grid grid-cols-4 place-items-center gap-4">
        <PetCard v-for="n in 12" :key="n" />
      </div>
    </div>
  </section>
</template>
