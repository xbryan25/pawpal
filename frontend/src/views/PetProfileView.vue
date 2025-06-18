<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import PetProfileContent from '@/components/PetProfileContent.vue'
</script>

<template>
  <div class="flex h-screen">
    <NavBar />

    <div class="flex flex-col w-[87vw] h-full">
      <PetProfileContent />
    </div>
  </div>
</template>
