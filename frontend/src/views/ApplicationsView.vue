<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import PageControls from '@/components/PageControls.vue';
import ApplicationsViewContent from '@/components/ApplicationsViewContent.vue';
</script>

<template>
  <div class="flex h-screen">
    <NavBar />

    <div class="flex flex-col w-[87vw] h-full">
        <ApplicationsViewContent />
        <PageControls />
    </div>
  </div>
</template>
