<script setup lang="ts">
import PetCard from './PetCard.vue'
import SearchAndSortHeader from './SearchAndSortHeader.vue'
</script>

<template>
  <section class="h-[90vh] w-[87vw]">
    <div class="p-5 h-full flex flex-col">
      <h1 class="text-6xl font-semibold">Pets</h1>

      <SearchAndSortHeader />

      <div class="flex-1 grid grid-cols-5 place-items-center gap-4">
        <PetCard v-for="n in 10" :key="n" />
      </div>
    </div>
  </section>
</template>
