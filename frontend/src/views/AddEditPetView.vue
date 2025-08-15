<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import AddEditPetForm from '@/components/AddEditPetForm.vue'

interface Props {
  mode: string
  petId?: string
}

const props = defineProps<Props>()
</script>

<template>
  <div class="flex h-screen">
    <NavBar />

    <AddEditPetForm :mode="props.mode" :petId="props.petId" />
  </div>
</template>
