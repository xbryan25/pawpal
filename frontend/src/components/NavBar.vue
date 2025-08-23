<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/useAuthStore'
import Cookies from 'universal-cookie'

const showDropdown = ref<boolean>(false)
const dropdownRef = ref<HTMLElement | null>(null)

const router = useRouter()
const auth = useAuthStore()

console.log(auth.profileImageUrl)

const cookies = new Cookies()

const toggleDropdown = () => {
  showDropdown.value = !showDropdown.value
}

const logout = () => {
  cookies.remove('access_token', { path: '/' })
  router.push('/user/login')
}

const handleClickOutside = (event: MouseEvent) => {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target as Node)) {
    showDropdown.value = false
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
  <nav class="h-screen w-[13vw] bg-[#f2f2f2] dark:bg-[#434343]">
    <div class="h-screen flex flex-col items-center justify-between">
      <div class="h-[10vh] w-full bg-[#D9D9D9] flex items-center justify-center">
        <h2 class="font-bold text-3xl">PawPal</h2>
      </div>

      <div class="flex-1 w-full bg-[#AAAAAA]">
        <div class="mx-10 my-10 flex flex-col gap-3">
          <RouterLink class="font-semibold text-xl" to="/pets/view">Pets</RouterLink>
          <RouterLink class="font-semibold text-xl" to="/applications/view"
            >Applications</RouterLink
          >
          <RouterLink class="font-semibold text-xl" to="/reports/user/view">Reports</RouterLink>
        </div>
      </div>

      <div ref="dropdownRef" class="relative h-[10vh] w-full bg-[#D9D9D9] flex items-center">
        <div class="mx-2 w-full flex cursor-pointer gap-3" @click="toggleDropdown">
          <div class="flex dui-avatar justify-center">
            <div class="ring-primary ring-offset-base-100 w-15 rounded-full ring-2 ring-offset-2">
              <img :src="auth.profileImageUrl || ''" />
            </div>
          </div>
          <div class="w-full h-15 flex flex-col justify-center">
            <p class="font-bold max-h-5 text-sm">Bryan Agan</p>
            <p class="max-h-5 text-sm">Adopter</p>
          </div>
        </div>

        <div v-if="showDropdown" class="absolute bottom-[100%] left-2 w-[90%] mb-2">
          <button @click="logout" class="block w-full text-left px-4 py-2 text-sm dui-btn">
            Logout
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>
