<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import PageControls from '@/components/PageControls.vue'
import SpeciesViewContent from '@/components/SpeciesViewContent.vue'
</script>

<template>
  <div class="flex h-screen">
    <NavBar />

    <div class="flex flex-col w-[87vw] h-full">
      <SpeciesViewContent />
      <PageControls />
    </div>
  </div>
</template>
