<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'

interface Props {
  petImageUrl: string
  sortOrder: number
}

const props = defineProps<Props>()
const emit = defineEmits<{
  (e: 'selectPhoto', petImageUrl: string): void
}>()

function selectPhoto() {
  emit('selectPhoto', props.petImageUrl)
}
</script>

<template>
  <div
    class="h-[5vw] w-[5vw] transition-transform duration-300 hover:scale-105 cursor-pointer"
    @click="selectPhoto"
  >
    <img :src="props.petImageUrl" class="w-full h-full object-cover rounded-lg" />
  </div>
</template>
