<script setup lang="ts">
import { reactive, ref, onMounted } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useToast, POSITION } from 'vue-toastification'
import axios from 'axios'

import lightModeImage from '@/assets/images/light-mode.png'
import darkModeImage from '@/assets/images/dark-mode.png'
import SearchableCombobox from './SearchableCombobox.vue'

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
  shelterId: string
  selectedImage: File | null
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
  shelterId: '',
  selectedImage: null,
})

const selectedShelter = ref<string>('')

const router = useRouter()
const toast = useToast()

const apiUrl = import.meta.env.VITE_API_URL

let shelters: { shelter_id: string; name: string }[] = []
let shelter_names: string[] = []

const handleImageChange = (event: Event) => {
  const MAX_SIZE_MB = 10
  const MAX_SIZE_BYTES = MAX_SIZE_MB * 1024 * 1024

  const target = event.target as HTMLInputElement
  const file = target.files?.[0]

  if (!file) return

  if (!file.type.startsWith('image/')) {
    toast.error('Please choose an image.', {
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

    newUserForm.selectedImage = null
    target.value = ''

    return
  }

  if (file.size > MAX_SIZE_BYTES) {
    toast.error('Images should not exceed 10 MB. Choose another image.', {
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

    newUserForm.selectedImage = null
    target.value = ''

    return
  }

  newUserForm.selectedImage = file
}

const handleSubmit = async () => {
  const shelterId =
    shelters.find((shelter) => shelter.name === selectedShelter.value)?.shelter_id || ''

  const newUserFormData = new FormData()

  newUserFormData.append('firstName', newUserForm.firstName)
  newUserFormData.append('lastName', newUserForm.lastName)
  newUserFormData.append('gender', newUserForm.gender)
  newUserFormData.append('birthDate', newUserForm.birthDate)
  newUserFormData.append('address', newUserForm.address)
  newUserFormData.append('phoneNumber', newUserForm.phoneNumber)
  newUserFormData.append('email', newUserForm.email)
  newUserFormData.append('password', newUserForm.password)
  newUserFormData.append('role', newUserForm.role)
  newUserFormData.append('shelterId', shelterId)

  if (newUserForm.selectedImage) {
    newUserFormData.append('selectedImage', newUserForm.selectedImage)
  } else {
    throw new Error('Unexpected error.')
  }

  try {
    const response = await axios.post(`${apiUrl}/user/signup`, newUserFormData)

    console.log(response.data)

    router.push('/user/login')
  } catch (error) {
    console.error('Error adding account', error)
  }
}

onMounted(async () => {
  try {
    const response = await axios.get(`${apiUrl}/shelter/list`)

    shelters = response.data
    shelter_names = shelters.map((shelter) => shelter.name)
  } catch (error) {
    console.error('Error retrieving shelter list', error)
  }
})
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
          <!-- Address label -->
          <div class="flex flex-row gap-2 mb-1">
            <h3 class="flex-1 font-medium">Address</h3>
            <h3 class="flex-1 font-medium">Profile Picture</h3>
          </div>

          <div class="flex flex-row gap-2">
            <label class="flex-1 dui-input w-full px-[6px]">
              <input
                v-model="newUserForm.address"
                maxlength="255"
                type="text"
                placeholder="e.g. John"
                required
              />
            </label>

            <input
              type="file"
              accept="image/*"
              class="flex-1 dui-file-input"
              @change="handleImageChange"
              required
            />
          </div>
        </div>

        <!-- Phone number group -->
        <div>
          <!-- Phone number label -->
          <div class="flex flex-row gap-2 mb-1">
            <h3 class="flex-1 font-medium">Phone Number</h3>
            <h3 v-if="newUserForm.role === 'shelter_staff'" class="flex-1 font-medium">
              Assigned Shelter
            </h3>
          </div>

          <div class="flex flex-row gap-2">
            <!-- Phone number input -->
            <div class="flex flex-col flex-1">
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

            <div v-if="newUserForm.role === 'shelter_staff'" class="flex flex-col flex-1">
              <SearchableCombobox
                v-model="selectedShelter"
                :options="shelter_names"
                placeholder="Select a shelter"
              />
            </div>

            <div v-else class="flex-1"></div>
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
              minlength="8"
              maxlength="255"
              type="password"
              placeholder="Enter your password"
              pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
              title="Must be more than 8 characters, including number, lowercase letter, uppercase letter"
              required
            />
          </label>
        </div>

        <button
          v-if="newUserForm.role === 'adopter'"
          class="dui-btn dui-btn-primary w-full mt-5 text-xl"
          type="submit"
        >
          Create account
        </button>

        <button v-else class="dui-btn dui-btn-primary w-full mt-5 text-xl" type="submit">
          Proceed
        </button>
      </form>
    </div>

    <div class="mt-3 flex flex-col gap-1">
      <p>
        Already have an account?
        <RouterLink to="/user/login" class="ml-1 font-bold text-violet-500">Log in</RouterLink>
      </p>
    </div>
  </section>
</template>
