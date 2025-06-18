<script setup lang="ts"></script>

<template>
  <section class="flex h-10 my-5 gap-[15vw]">
    <div class="flex-1 grid grid-cols-[0.3fr_0.7fr_0.7fr] gap-4 min-w-0 flex-row pr-[5%]">
      <div class="flex items-center min-w-0">
        <p class="font-semibold text-xl">Sort By</p>
      </div>
      <select class="bg-[#D9D9D9] rounded-lg border border-black text-xl font-semibold">
        <option value="All">Name</option>
        <option value="Title">Shelter</option>
        <option value="Genre">Status</option>
      </select>
      <select class="bg-[#D9D9D9] rounded-lg border border-black text-xl font-semibold">
        <option value="All">Ascending</option>
        <option value="Title">Descending</option>
      </select>
    </div>
    <div class="flex-1 grid grid-cols-[0.3fr_0.7fr_0.7fr] gap-4 min-w-0 flex-row pl-[5%]">
      <div class="flex items-center min-w-0">
        <p class="font-semibold text-xl">Search</p>
      </div>
      <select class="bg-[#D9D9D9] rounded-lg border border-black text-xl font-semibold">
        <option value="All">Name</option>
        <option value="Title">Shelter</option>
        <option value="Genre">Status</option>
      </select>
      <label class="dui-input">
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
