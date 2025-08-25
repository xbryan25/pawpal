
import { defineStore } from 'pinia';
import { ref, watch } from 'vue';

export const useThemeStore = defineStore('theme', () => {
  const currentTheme = ref<'caramellatte' | 'luxury'>('caramellatte');

  watch(currentTheme, (newTheme) => {
    document.documentElement.setAttribute('data-theme', newTheme);
  }, { immediate: true });

  function toggleTheme() {
    currentTheme.value = currentTheme.value === 'caramellatte' ? 'luxury' : 'caramellatte';
  }

  return { currentTheme, toggleTheme };
});