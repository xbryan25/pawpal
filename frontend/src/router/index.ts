import { createRouter, createWebHistory } from 'vue-router'
import AdopterLoginView from '@/views/AdopterLoginView.vue'
import ShelterStaffLoginView from '@/views/ShelterStaffLoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'adopterLoginView',
      component: AdopterLoginView,
      meta: { title: 'Login' },
    },
    {
      path: '/shelter-staff-login',
      name: 'shelterStaffLoginView',
      component: ShelterStaffLoginView,
      meta: { title: 'Login' },
    },
  ],
})

export default router
