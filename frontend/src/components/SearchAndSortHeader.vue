<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/useAuthStore'

const auth = useAuthStore()
</script>

<template>
  <section class="flex h-10 my-5 gap-[1vw] bg-primary-content">
    <div class="flex-1 grid grid-cols-[0.3fr_0.7fr_0.7fr] gap-4 min-w-0 flex-row pr-[3%]">
      <div class="flex items-center min-w-0">
        <p class="font-fredoka font-medium text-base text-base-content">Sort By</p>
      </div>
      <select class="dui-select ml-auto block font-fredoka font-medium text-base text-base-content">
        <option value="All">Name</option>
        <option value="Title">Shelter</option>
        <option value="Genre">Status</option>
      </select>
      <select class="dui-select ml-auto block font-fredoka font-medium text-base text-base-content">
        <option value="All">Ascending</option>
        <option value="Title">Descending</option>
      </select>
    </div>

    <div class="w-[20%] min-w-0 flex-row px-[5%]" v-if="auth.isShelterStaff">
      <RouterLink
        class="dui-btn w-full h-full font-fredoka font-medium text-base text-base-content hover:dark:bg-primary-content dark:bg-base-100 dark:border-base-content/25"
        to="/pets/add-pet"
        >Add Pet</RouterLink
      >
    </div>

    <div class="flex-1 grid grid-cols-[0.4fr_0.7fr_0.7fr] gap-4 min-w-0 flex-row pl-[3%]">
      <div class="flex items-center min-w-0">
        <p class="font-fredoka font-medium text-base">Search By</p>
      </div>
      <select class="dui-select ml-auto block font-fredoka font-medium text-base text-base-content">
        <option value="name">Name</option>
        <option value="applicationDate">Application Date</option>
        <option value="shelter">Shelter</option>
        <option value="status">Status</option>
      </select>
      <label class="dui-input font-fredoka font-medium text-base text-base-content">
        <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
          <g
            stroke-linejoin="round"
            stroke-linecap="round"
            stroke-width="2.5"
            fill="none"
            stroke="currentColor"
          >
            <circle cx="11" cy="11" r="8"></circle>
            <path d="m21 21-4.3-4.3"></path>
          </g>
        </svg>
        <input type="search" required placeholder="Search" />
      </label>
    </div>
  </section>
</template>
