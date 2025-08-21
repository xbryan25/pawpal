<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import ApplicationDetailsContent from '@/components/ApplicationDetailsContent.vue'
</script>

<template>
  <div class="flex h-screen">
    <NavBar />

    <div class="flex flex-col w-[87vw] h-full"><ApplicationDetailsContent /></div>
  </div>
</template>
