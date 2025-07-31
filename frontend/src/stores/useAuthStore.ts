import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const role = ref<string | null>(null)

  const isAdmin = computed(() => role.value === 'admin')
  const isUser = computed(() => role.value === 'user')
  const isShelterStaff = computed(() => role.value === 'shelter_staff')

  const setRole = (newRole: string) => {
    role.value = newRole
  }

  const logout = () => {
    role.value = null
  }

  return {
    role,
    isAdmin,
    isUser,
    isShelterStaff,
    setRole,
    logout
  }
})