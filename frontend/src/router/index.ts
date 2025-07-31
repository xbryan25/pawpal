import { createRouter, createWebHistory } from 'vue-router'
import { getToken } from '@/utils/getToken'
import { isTokenValid } from '@/utils/isTokenValid'
import AdopterLoginView from '@/views/AdopterLoginView.vue'
import ShelterStaffLoginView from '@/views/ShelterStaffLoginView.vue'
import PetsView from '@/views/PetsView.vue'
import PetProfileView from '@/views/PetProfileView.vue'
import ApplicationsView from '@/views/ApplicationsView.vue'
import SignupView from '@/views/SignupView.vue'
import AdopterReportsView from '@/views/AdopterReportsView.vue'
import AddEditPetView from '@/views/AddEditPetView.vue'


const routes = [
    {
      path: '/user/login',
      name: 'adopterLoginView',
      component: AdopterLoginView,
      meta: { title: 'Login' },
    },
    {
      path: '/user/shelter-staff-login',
      name: 'shelterStaffLoginView',
      component: ShelterStaffLoginView,
      meta: { title: 'Login' },
    },
    {
      path: '/pets/view',
      name: 'adopterPetsView',
      component: PetsView,
      meta: { title: 'Pets View', requiresAuth: true },
    },
    {
      path: '/pets/view/sample-id',
      name: 'adopterPetProfileView',
      component: PetProfileView,
      meta: { title: 'Pet Profile' },
    },
    {
      path: '/applications/view',
      name: 'adopterApplicationsView',
      component: ApplicationsView,
      meta: { title: 'Applications View' },
    },
    {
      path: '/user/signup',
      name: 'SignupView',
      component: SignupView,
      meta: { title: 'Signup View' },
    },
    {
      path: '/reports/user/view',
      name: 'adopterReportsView',
      component: AdopterReportsView,
      meta: { title: 'Adopter Reports View' },
    },
    {
      path: '/pets/add-pet',
      name: 'addPetView',
      component: AddEditPetView,
      meta: { title: 'Add Pet' },
    },
  ]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

router.beforeEach((to, from, next) => {
  // Use getToken because router is outside Vue3
  const token = getToken()

  if (to.meta.requiresAuth && (!token || !isTokenValid(token))) {
    next('/user/login')
  } else {
    next()
  }
})

export default router
