<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount, defineProps, defineEmits } from 'vue'

const props = defineProps<{
  modelValue: string | null
  options: string[]
  placeholder?: string
}>()

// Emits
const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()

// Internal state
const query = ref(props.modelValue || '')
const isOpen = ref(false)
const comboRef = ref<HTMLElement | null>(null)

const filteredOptions = computed(() => {
  if (!query.value) return props.options
  return props.options.filter((option) => option.toLowerCase().includes(query.value.toLowerCase()))
})

function selectOption(option: string) {
  query.value = option
  emit('update:modelValue', option)
  isOpen.value = false
}

// Close on outside click
function handleClickOutside(event: MouseEvent) {
  if (comboRef.value && !comboRef.value.contains(event.target as Node)) {
    isOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<template>
  <div ref="comboRef" class="relative w-full max-w-xs">
    <div class="relative">
      <input
        type="text"
        v-model="query"
        @focus="isOpen = true"
        @input="isOpen = true"
        @keydown.escape="isOpen = false"
        :placeholder="props.placeholder || 'Select an option'"
        class="dui-input dui-input-bordered w-full pr-10"
      />

      <svg
        class="absolute right-2 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-500 transition-transform duration-200 cursor-pointer z-10"
        :class="{ 'rotate-180': isOpen }"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        @mousedown.stop="isOpen = !isOpen"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </div>

    <ul
      v-if="isOpen && filteredOptions.length"
      class="absolute z-10 mt-1 w-full bg-base-100 shadow rounded-box max-h-60 overflow-auto"
    >
      <li
        v-for="option in filteredOptions"
        :key="option"
        @click="selectOption(option)"
        class="cursor-pointer p-2 hover:bg-base-200"
      >
        {{ option }}
      </li>
    </ul>

    <div
      v-else-if="isOpen && !filteredOptions.length"
      class="absolute z-10 mt-1 w-full bg-base-100 shadow rounded-box p-2 text-gray-400"
    >
      No results
    </div>
  </div>
</template>
