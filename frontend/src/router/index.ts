import { createRouter, createWebHistory, type RouteRecordRaw} from 'vue-router'
import { getToken } from '@/utils/getToken'
import { isTokenValid } from '@/utils/isTokenValid'

import AdopterLoginView from '@/views/AdopterLoginView.vue'
import ShelterStaffLoginView from '@/views/ShelterStaffLoginView.vue'
import PetsView from '@/views/PetsView.vue'
import PetProfileView from '@/views/PetProfileView.vue'
import ApplicationsView from '@/views/ApplicationsView.vue'
import SignupView from '@/views/SignupView.vue'
import ReportsView from '@/views/ReportsView.vue'
import AddEditPetView from '@/views/AddEditPetView.vue'
import ApplicationDetailsView from '@/views/ApplicationDetailsView.vue'
import BreedsView from '@/views/BreedsView.vue'
import SpeciesView from '@/views/SpeciesView.vue'


const routes: RouteRecordRaw[] = [
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
      path: '/pets/view/:id',
      name: 'adopterPetProfileView',
      component: PetProfileView,
      meta: { title: 'Pet Profile' },
    },
    {
      path: '/pets/view/shelter-staff/:id',
      name: 'shelterStaffPetProfileView',
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
      name: 'reportsView',
      component: ReportsView,
      meta: { title: 'Reports View' },
    },
    {
      path: '/pets/add-pet',
      name: 'addPetView',
      component: AddEditPetView,
      meta: { title: 'Add Pet' },
      props: { mode: 'add-pet' }
    },
    {
      path: '/pets/edit-pet',
      name: 'editPetView',
      component: AddEditPetView,
      meta: { title: 'Add Pet' },
      props: route => ({
        mode: 'edit-pet',
        petId: route.query.petId
      })
    },
    {
      path: '/applications/application-details/:applicationId',
      name: 'applicationDetailsView',
      component: ApplicationDetailsView,
      meta: { title: 'Application Details' },
    },
    {
      path: '/breeds/view',
      name: 'breedsView',
      component: BreedsView,
      meta: { title: 'Breeds View' },
    },
    {
      path: '/species/view',
      name: 'speciesView',
      component: SpeciesView,
      meta: { title: 'Breeds View' },
    }
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
