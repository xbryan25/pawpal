import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const profileImageUrl = ref<string | null>(null)
  const role = ref<string | null>(null)
  const userId = ref<string | null>(null)
  const shelterId = ref<string | null>(null)

  const isAdmin = computed(() => role.value === 'admin')
  const isUser = computed(() => role.value === 'adopter')
  const isShelterStaff = computed(() => role.value === 'shelter_staff')

  const setAuth = (newProfileImageUrl: string, newRole: string, newUserId: string, newShelterId: string) => {
    profileImageUrl.value = newProfileImageUrl
    role.value = newRole
    userId.value = newUserId
    shelterId.value = newShelterId
  }

  const logout = () => {
    profileImageUrl.value = null
    role.value = null
    userId.value = null
    shelterId.value = null
  }

  return {
    profileImageUrl,
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