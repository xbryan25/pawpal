import { createRouter, createWebHistory } from 'vue-router'
import AdopterLoginView from '@/views/AdopterLoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'adopterLoginView',
      component: AdopterLoginView,
      meta: { title: 'Login' },
    },
  ],
})

export default router
