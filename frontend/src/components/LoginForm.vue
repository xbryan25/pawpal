<script setup lang="ts">
import { withDefaults, defineProps, reactive } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import axios from 'axios'
import Cookies from 'universal-cookie'
import { useToast, POSITION } from 'vue-toastification'
import { useAuthStore } from '@/stores/useAuthStore'

import ThemeToggle from './ThemeToggle.vue'

interface Props {
  loginType?: string
}

interface UserCredentials {
  email: string
  password: string
  loginType: string
}

const props = withDefaults(defineProps<Props>(), {
  loginType: 'adopter',
})

const userForm = reactive<UserCredentials>({
  email: '',
  password: '',
  loginType: '',
})

const router = useRouter()
const apiUrl = import.meta.env.VITE_API_URL

// import.meta.env.VITE_COOKIE_SECURE is a string
const isSecure = import.meta.env.VITE_COOKIE_SECURE === 'true'

const cookies = new Cookies()

const auth = useAuthStore()

const toast = useToast()

const handleSubmit = async () => {
  const userCredentials: UserCredentials = {
    email: userForm.email,
    password: userForm.password,
    loginType: props.loginType,
  }

  try {
    const response = await axios.post(`${apiUrl}/user/login`, userCredentials)

    const accessToken = response.data.accessToken
    const role = response.data.userRole
    const userId = response.data.userId
    const shelterId = response.data.shelterId
    const profileImageUrl = response.data.profileImageUrl

    cookies.set('access_token', accessToken, {
      path: '/',
      maxAge: 60 * 15, // Per minute * 15, so 15 mins
      sameSite: 'strict',
      secure: isSecure,
    })

    toast.success('Login success!', {
      position: POSITION.TOP_RIGHT,
      timeout: 5000,
      closeOnClick: true,
      pauseOnFocusLoss: true,
      pauseOnHover: true,
      draggable: true,
      draggablePercent: 0.6,
      showCloseButtonOnHover: true,
      hideProgressBar: false,
      closeButton: 'button',
      icon: true,
      rtl: false,
    })

    auth.setAuth(profileImageUrl, role, userId, shelterId)

    if (role === 'admin') {
      router.push('/breeds/view')
    } else {
      router.push('/pets/view')
    }
  } catch (error: unknown) {
    let errorMessage: string = ''

    if (axios.isAxiosError(error) && error.response) {
      errorMessage = error.response.data.error
    } else {
      errorMessage = 'Unexpected error.'
    }

    toast.error(`Login failed. ${errorMessage}`, {
      position: POSITION.TOP_RIGHT,
      timeout: 5000,
      closeOnClick: true,
      pauseOnFocusLoss: true,
      pauseOnHover: true,
      draggable: true,
      draggablePercent: 0.6,
      showCloseButtonOnHover: true,
      hideProgressBar: false,
      closeButton: 'button',
      icon: true,
      rtl: false,
    })

    console.error('Error logging in', error)
  }
}
</script>

<template>
  <section class="flex-1 max-w-[50vw] h-[calc(100vh-2rem)] m-4 pl-10 pt-5">
    <ThemeToggle />

    <h2
      class="text-2xl my-10 font-extrabold font-rethink text-base-content"
      v-if="loginType === 'adopter'"
    >
      PawPal
    </h2>

    <h2 class="text-2xl my-10 font-extrabold font-rethink text-base-content" v-else>
      PawPal | Shelter Staff
    </h2>

    <h1 class="text-5xl my-1 font-semibold font-fredoka text-base-content">Hello,</h1>

    <h1 class="text-5xl my-1 font-semibold font-fredoka text-base-content">welcome back!</h1>

    <p
      class="font-medium my-5 text-xl font-fredoka text-base-content"
      v-if="loginType === 'adopter'"
    >
      These pets need a loving home!
    </p>
    <p class="font-medium my-5 text-xl font-fredoka text-base-content" v-else>
      People are looking for pets to adopt!
    </p>

    <form class="flex flex-col gap-4 my-10 mr-[25vw]" @submit.prevent="handleSubmit">
      <!-- Email field group -->
      <div class="flex flex-col">
        <label class="dui-input dui-validator">
          <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <g
              stroke-linejoin="round"
              stroke-linecap="round"
              stroke-width="2.5"
              fill="none"
              stroke="currentColor"
            >
              <rect width="20" height="16" x="2" y="4" rx="2"></rect>
              <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
            </g>
          </svg>
          <input v-model="userForm.email" type="email" placeholder="mail@site.com" required />
        </label>
        <div class="dui-validator-hint hidden text-error">Enter valid email address</div>
      </div>

      <!-- Password field group -->
      <div class="flex flex-col">
        <label class="dui-input">
          <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <g
              stroke-linejoin="round"
              stroke-linecap="round"
              stroke-width="2.5"
              fill="none"
              stroke="currentColor"
            >
              <path
                d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"
              ></path>
              <circle cx="16.5" cy="7.5" r=".5" fill="currentColor"></circle>
            </g>
          </svg>
          <input
            v-model="userForm.password"
            type="password"
            required
            placeholder="Password"
            minlength="8"
            title="Must be more than 8 characters, including number, lowercase letter, uppercase letter"
          />
        </label>

        <div>
          <button class="mt-2 text-info font-semibold cursor-pointer font-fredoka" type="button">
            Forgot password?
          </button>
        </div>

        <button class="dui-btn dark:dui-btn-secondary max-w-[7vw] mt-7 font-fredoka" type="submit">
          Sign In
        </button>
      </div>
    </form>

    <div class="mt-15 flex flex-col gap-1">
      <p class="font-fredoka font-medium text-base-content">
        Don't have an account?
        <RouterLink to="/user/signup" class="ml-1 font-semibold text-info">Sign Up</RouterLink>
      </p>
      <p class="font-fredoka font-medium text-base-content" v-if="loginType === 'adopter'">
        Are you a shelter staff?
        <RouterLink to="/user/shelter-staff-login" class="ml-1 font-semibold text-info"
          >Sign In Here</RouterLink
        >
      </p>

      <p class="font-fredoka font-medium text-base-content" v-else>
        Are you an adopter?
        <RouterLink to="/user/login" class="ml-1 font-semibold text-info">Sign In Here</RouterLink>
      </p>
    </div>
  </section>
</template>
