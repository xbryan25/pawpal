<script setup lang="ts">
import { useThemeStore } from '@/stores/useThemeStore'

import lightModeImage from '@/assets/images/light-mode.png'
import darkModeImage from '@/assets/images/dark-mode.png'

const theme = useThemeStore()
</script>

<template>
  <label class="dui-swap dui-swap-rotate">
    <input
      type="checkbox"
      class="dui-theme-controller"
      :checked="theme.currentTheme === 'luxury'"
      @change="theme.toggleTheme"
    />
    <img :src="darkModeImage" class="dui-swap-off h-10 w-10" />
    <img :src="lightModeImage" class="dui-swap-on h-10 w-10" />
  </label>
</template>
