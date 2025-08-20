import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const role = ref<string | null>(null)
  const userId = ref<string | null>(null)
  const shelterId = ref<string | null>(null)

  const isAdmin = computed(() => role.value === 'admin')
  const isUser = computed(() => role.value === 'adopter')
  const isShelterStaff = computed(() => role.value === 'shelter_staff')

  const setAuth = (newRole: string, newUserId: string, newShelterId: string) => {
    role.value = newRole
    userId.value = newUserId
    shelterId.value = newShelterId
  }

  const logout = () => {
    role.value = null
    userId.value = null
    shelterId.value = null
  }

  return {
    role,
    userId,
    shelterId,
    isAdmin,
    isUser,
    isShelterStaff,
    setAuth,
    logout
  }
}, {
  persist: true
})