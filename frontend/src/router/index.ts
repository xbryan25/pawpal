import { createRouter, createWebHistory } from 'vue-router'
import AdopterLoginView from '@/views/AdopterLoginView.vue'
import ShelterStaffLoginView from '@/views/ShelterStaffLoginView.vue'
import PetsView from '@/views/PetsView.vue'
import PetProfileView from '@/views/PetProfileView.vue'

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
    {
      path: '/pets/view',
      name: 'adopterPetsView',
      component: PetsView,
      meta: { title: 'Pets View' },
    },
    {
      path: '/pets/view/sample-id',
      name: 'adopterPetProfileView',
      component: PetProfileView,
      meta: { title: 'Pet Profile' },
    },
  ],
})

export default router
