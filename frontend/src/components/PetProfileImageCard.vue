<script setup lang="ts">
import { defineProps } from 'vue'

interface Props {
  petImageUrl: string
  sortOrder: number
}

const props = defineProps<Props>()

console.log(props.petImageUrl)
</script>

<template>
  <div class="h-[5vw] w-[5vw] transition-transform duration-300 hover:scale-105 cursor-pointer">
    <img :src="props.petImageUrl" class="w-full h-full object-cover rounded-lg" />
  </div>
</template>
