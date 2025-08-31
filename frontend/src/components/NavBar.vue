<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/useAuthStore'
import Cookies from 'universal-cookie'

const showDropdown = ref<boolean>(false)
const dropdownRef = ref<HTMLElement | null>(null)

const router = useRouter()
const auth = useAuthStore()

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
  <nav class="h-screen w-[13vw] bg-secondary-content dark:bg-neutral">
    <div class="h-screen flex flex-col items-center justify-between">
      <div
        class="h-[10vh] w-full flex items-center justify-center bg-secondary-content dark:bg-neutral"
      >
        <h2 class="font-rethink font-extrabold text-3xl text-accent dark:text-neutral-content">
          PawPal
        </h2>
      </div>

      <div class="h-[2px] bg-secondary dark:bg-primary w-full"></div>

      <div class="flex-1 w-full" v-if="auth.isShelterStaff || auth.isUser">
        <div class="mx-5 my-7 flex flex-col gap-3">
          <div class="flex gap-2 cursor-pointer transition-transform duration-300 hover:scale-110">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              height="24px"
              viewBox="0 -960 960 960"
              width="24px"
              fill="currentColor"
              class="text-accent dark:text-neutral-content"
            >
              <path
                d="M180-475q-42 0-71-29t-29-71q0-42 29-71t71-29q42 0 71 29t29 71q0 42-29 71t-71 29Zm180-160q-42 0-71-29t-29-71q0-42 29-71t71-29q42 0 71 29t29 71q0 42-29 71t-71 29Zm240 0q-42 0-71-29t-29-71q0-42 29-71t71-29q42 0 71 29t29 71q0 42-29 71t-71 29Zm180 160q-42 0-71-29t-29-71q0-42 29-71t71-29q42 0 71 29t29 71q0 42-29 71t-71 29ZM266-75q-45 0-75.5-34.5T160-191q0-52 35.5-91t70.5-77q29-31 50-67.5t50-68.5q22-26 51-43t63-17q34 0 63 16t51 42q28 32 49.5 69t50.5 69q35 38 70.5 77t35.5 91q0 47-30.5 81.5T694-75q-54 0-107-9t-107-9q-54 0-107 9t-107 9Z"
              />
            </svg>

            <RouterLink
              class="font-fredoka font-medium text-xl text-accent dark:text-neutral-content"
              to="/pets/view"
              >Pets</RouterLink
            >
          </div>

          <div class="flex gap-2 cursor-pointer transition-transform duration-300 hover:scale-110">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              height="25px"
              viewBox="0 -960 960 960"
              width="24px"
              fill="currentColor"
              class="text-accent dark:text-neutral-content"
            >
              <path
                d="M240-80q-50 0-85-35t-35-85v-120h120v-560h600v680q0 50-35 85t-85 35H240Zm480-80q17 0 28.5-11.5T760-200v-600H320v480h360v120q0 17 11.5 28.5T720-160ZM360-600v-80h360v80H360Zm0 120v-80h360v80H360ZM240-160h360v-80H200v40q0 17 11.5 28.5T240-160Zm0 0h-40 400-360Z"
              />
            </svg>

            <RouterLink
              class="font-fredoka font-medium text-xl text-accent dark:text-neutral-content"
              to="/applications/view"
              >Applications</RouterLink
            >
          </div>

          <div class="flex gap-2 cursor-pointer transition-transform duration-300 hover:scale-110">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              height="26px"
              viewBox="0 -960 960 960"
              width="24px"
              fill="currentColor"
              class="text-accent dark:text-neutral-content"
            >
              <path
                d="M280-280h80v-200h-80v200Zm320 0h80v-400h-80v400Zm-160 0h80v-120h-80v120Zm0-200h80v-80h-80v80ZM200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm0-80h560v-560H200v560Zm0-560v560-560Z"
              />
            </svg>

            <RouterLink
              class="font-fredoka font-medium text-xl text-accent dark:text-neutral-content"
              to="/reports/user/view"
              >Reports</RouterLink
            >
          </div>
        </div>
      </div>

      <div class="flex-1 w-full" v-if="auth.isAdmin">
        <div class="mx-5 my-7 flex flex-col gap-3">
          <div class="flex gap-2 cursor-pointer transition-transform duration-300 hover:scale-110">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              height="24px"
              viewBox="0 -960 960 960"
              width="24px"
              fill="currentColor"
              class="text-accent dark:text-neutral-content"
            >
              <path
                d="M180-475q-42 0-71-29t-29-71q0-42 29-71t71-29q42 0 71 29t29 71q0 42-29 71t-71 29Zm180-160q-42 0-71-29t-29-71q0-42 29-71t71-29q42 0 71 29t29 71q0 42-29 71t-71 29Zm240 0q-42 0-71-29t-29-71q0-42 29-71t71-29q42 0 71 29t29 71q0 42-29 71t-71 29Zm180 160q-42 0-71-29t-29-71q0-42 29-71t71-29q42 0 71 29t29 71q0 42-29 71t-71 29ZM266-75q-45 0-75.5-34.5T160-191q0-52 35.5-91t70.5-77q29-31 50-67.5t50-68.5q22-26 51-43t63-17q34 0 63 16t51 42q28 32 49.5 69t50.5 69q35 38 70.5 77t35.5 91q0 47-30.5 81.5T694-75q-54 0-107-9t-107-9q-54 0-107 9t-107 9Z"
              />
            </svg>

            <RouterLink
              class="font-fredoka font-medium text-xl text-accent dark:text-neutral-content"
              to="/breeds/view"
              >Breeds</RouterLink
            >
          </div>

          <div class="flex gap-2 cursor-pointer transition-transform duration-300 hover:scale-110">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              height="25px"
              viewBox="0 -960 960 960"
              width="24px"
              fill="currentColor"
              class="text-accent dark:text-neutral-content"
            >
              <path
                d="M240-80q-50 0-85-35t-35-85v-120h120v-560h600v680q0 50-35 85t-85 35H240Zm480-80q17 0 28.5-11.5T760-200v-600H320v480h360v120q0 17 11.5 28.5T720-160ZM360-600v-80h360v80H360Zm0 120v-80h360v80H360ZM240-160h360v-80H200v40q0 17 11.5 28.5T240-160Zm0 0h-40 400-360Z"
              />
            </svg>

            <RouterLink
              class="font-fredoka font-medium text-xl text-accent dark:text-neutral-content"
              to="/species/view"
              >Species</RouterLink
            >
          </div>

          <div class="flex gap-2 cursor-pointer transition-transform duration-300 hover:scale-110">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              height="26px"
              viewBox="0 -960 960 960"
              width="24px"
              fill="currentColor"
              class="text-accent dark:text-neutral-content"
            >
              <path
                d="M280-280h80v-200h-80v200Zm320 0h80v-400h-80v400Zm-160 0h80v-120h-80v120Zm0-200h80v-80h-80v80ZM200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm0-80h560v-560H200v560Zm0-560v560-560Z"
              />
            </svg>

            <RouterLink
              class="font-fredoka font-medium text-xl text-accent dark:text-neutral-content"
              to="/reports/user/view"
              >Shelters</RouterLink
            >
          </div>
        </div>
      </div>

      <div class="h-[2px] bg-secondary dark:bg-primary w-full mb-2"></div>

      <div ref="dropdownRef" class="relative h-[10vh] w-full flex items-center">
        <div class="mx-2 w-full flex cursor-pointer gap-3" @click="toggleDropdown">
          <div class="flex dui-avatar justify-center">
            <div
              class="ring-accent ring-offset-base-300 dark:ring-neutral-content dark:ring-offset-base-100 w-15 rounded-full ring-2 ring-offset-2"
            >
              <img :src="auth.profileImageUrl || ''" />
            </div>
          </div>
          <div class="w-full h-15 flex flex-col justify-center">
            <p
              class="font-fredoka font-semibold max-h-5 text-sm text-accent dark:text-neutral-content"
            >
              Bryan Agan
            </p>
            <p class="max-h-5 font-fredoka text-sm text-accent dark:text-neutral-content">
              Adopter
            </p>
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
