<script setup lang="ts">
import { withDefaults, reactive } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import axios from 'axios'

import lightModeImage from '@/assets/images/light-mode.png'
import darkModeImage from '@/assets/images/dark-mode.png'

interface NewUser {
  firstName: string
  lastName: string
  gender: string
  birthDate: string
  address: string
  phoneNumber: string
  email: string
  password: string
  role: string
}

const newUserForm = reactive<NewUser>({
  firstName: '',
  lastName: '',
  gender: '',
  birthDate: '',
  address: '',
  phoneNumber: '',
  email: '',
  password: '',
  role: '',
})

const router = useRouter()
const apiUrl = import.meta.env.VITE_API_URL

const handleSubmit = async () => {
  const newUser: NewUser = {
    firstName: newUserForm.firstName,
    lastName: newUserForm.lastName,
    gender: newUserForm.gender,
    birthDate: newUserForm.birthDate,
    address: newUserForm.address,
    phoneNumber: newUserForm.phoneNumber,
    email: newUserForm.email,
    password: newUserForm.password,
    role: newUserForm.role,
  }

  try {
    const response = await axios.post(`${apiUrl}/user/signup`, newUser)

    console.log(response.data)

    router.push('/user/login')
  } catch (error) {
    console.error('Error adding account', error)
  }
}
</script>

<template>
  <section
    class="flex flex-col items-center flex-1 max-w-[50vw] h-[calc(100vh-2rem)] m-4 mx-10 pl-10 pt-5"
  >
    <div class="flex flex-row w-full">
      <h2 class="flex-1 text-black text-xl font-semibold">PawPal</h2>
      <label class="dui-swap dui-swap-rotate">
        <input type="checkbox" class="dui-theme-controller" value="synthwave" />
        <img :src="darkModeImage" class="dui-swap-off h-10 w-10" />
        <img :src="lightModeImage" class="dui-swap-on h-10 w-10" />
      </label>
    </div>

    <h1 class="text-black text-center text-5xl font-bold">Create an account</h1>

    <div class="flex flex-col items-center w-[80%]">
      <form class="flex flex-col gap-2 mb-2 w-full" @submit.prevent="handleSubmit">
        <div class="flex dui-join gap-2 pt-5 mb-3 w-full">
          <input
            v-model="newUserForm.role"
            class="flex-1 dui-join-item dui-btn"
            type="radio"
            name="options"
            value="adopter"
            aria-label="Adopter"
            required
          />
          <input
            v-model="newUserForm.role"
            class="flex-1 dui-join-item dui-btn"
            type="radio"
            name="options"
            value="shelter_staff"
            aria-label="Shelter Staff"
          />
        </div>

        <!-- First name and last name group -->
        <div>
          <!-- First name and last name labels -->
          <div class="flex flex-row gap-2 mb-1">
            <h3 class="flex-1 font-medium">First Name</h3>
            <h3 class="flex-1 font-medium">Last Name</h3>
          </div>

          <div class="flex flex-row gap-2">
            <!-- First name input -->
            <div class="flex-1 flex flex-col">
              <label class="dui-input w-full">
                <input
                  v-model="newUserForm.firstName"
                  maxlength="127"
                  type="text"
                  placeholder="e.g. John"
                  required
                />
              </label>
            </div>

            <!-- Last name input -->
            <div class="flex-1 flex flex-col">
              <label class="dui-input w-full">
                <input
                  v-model="newUserForm.lastName"
                  maxlength="127"
                  type="text"
                  placeholder="e.g. Doe"
                  required
                />
              </label>
            </div>
          </div>
        </div>

        <!-- Gender and birth date group -->
        <div>
          <!-- Gender and birth date labels -->
          <div class="flex flex-row gap-2 mb-1">
            <h3 class="flex-1 font-medium">Gender</h3>
            <h3 class="flex-1 font-medium">Birth Date</h3>
          </div>

          <div class="flex gap-2">
            <!-- Gender select -->
            <div class="flex-1">
              <select
                v-model="newUserForm.gender"
                class="dui-select w-full appearance-none px-3 py-2"
                required
              >
                <option value="" disabled selected>-</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="others">Others</option>
                <option value="prefer-not-to-say">Prefer not to say</option>
              </select>
            </div>

            <!-- Birth date input -->
            <div class="flex-1">
              <input
                v-model="newUserForm.birthDate"
                type="date"
                class="dui-input w-full px-3 py-2"
                required
              />
            </div>
          </div>
        </div>

        <!-- Address group -->
        <div>
          <!-- Gender and birth date labels -->
          <div class="flex flex-row gap-2 mb-1">
            <h3 class="flex-1 font-medium">Address</h3>
          </div>

          <label class="dui-input w-full">
            <input
              v-model="newUserForm.address"
              maxlength="255"
              type="text"
              placeholder="e.g. John"
              required
            />
          </label>
        </div>

        <!-- Phone number group -->
        <div>
          <!-- Phone number label -->
          <div class="flex flex-row gap-2 mb-1">
            <h3 class="flex-1 font-medium">Phone Number</h3>
          </div>

          <div class="flex flex-row gap-2">
            <!-- Phone number input -->
            <div class="flex flex-col w-[50%]">
              <label class="dui-input w-full">
                <input
                  v-model="newUserForm.phoneNumber"
                  maxlength="11"
                  type="tel"
                  id="mobile"
                  name="mobile"
                  placeholder="e.g. 09171234567"
                  pattern="^09\d{9}$"
                  required
                />
              </label>
            </div>
          </div>
        </div>

        <!-- Email group -->
        <div>
          <!-- Email label -->
          <div class="flex flex-row gap-2 mb-1">
            <h3 class="flex-1 font-medium">Email</h3>
          </div>

          <label class="dui-input w-full">
            <input
              v-model="newUserForm.email"
              maxlength="255"
              type="email"
              placeholder="e.g. test@test.com"
              required
            />
          </label>
        </div>

        <!-- Password group -->
        <div>
          <!-- Password label -->
          <div class="flex flex-row gap-2 mb-1">
            <h3 class="flex-1 font-medium">Password</h3>
          </div>

          <label class="dui-input w-full">
            <input
              v-model="newUserForm.password"
              maxlength="255"
              type="password"
              placeholder="Enter your password"
              required
            />
          </label>
        </div>

        <button class="dui-btn dui-btn-primary w-full mt-5 text-xl" type="submit">
          Create account
        </button>
      </form>
    </div>

    <div class="mt-3 flex flex-col gap-1">
      <p>
        Don't have an account?<RouterLink to="/user/login" class="ml-1 font-bold text-violet-500"
          >Log in</RouterLink
        >
      </p>
    </div>
  </section>
</template>
