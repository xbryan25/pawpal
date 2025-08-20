<script setup lang="ts"></script>

<template>
  <section class="h-full">
    <div class="p-5 h-full flex flex-col">
      <h1 class="text-6xl font-semibold">Application Details</h1>
      <div class="flex pt-10 px-[15%] gap-x-[5%]">
        <div class="flex flex-col gap-y-[2%] flex-[2]">
          <div class="text-center">
            <h2 class="text-4xl font-semibold">Adopter</h2>
          </div>
          <div class="flex flex-col bg-gray-400 h-110 rounded-lg p-5">
            <div class="flex dui-avatar justify-center">
              <div class="ring-primary ring-offset-base-100 w-35 rounded-full ring-2 ring-offset-2">
                <img src="https://img.daisyui.com/images/profile/demo/spiderperson@192.webp" />
              </div>
            </div>

            <div class="flex flex-col gap-y-2 px-10 pt-5">
              <div class="flex justify-center">
                <div class="flex-1">
                  <p class="font-bold text-xl">Name</p>
                  <p class="pl-5 font-semibold">Test Name</p>
                </div>

                <div class="flex-1">
                  <p class="font-bold text-xl">Gender</p>
                  <p class="pl-5 font-semibold">Prefer not to say</p>
                </div>
              </div>
              <div class="flex justify-center">
                <div class="flex-1">
                  <p class="font-bold text-xl">Phone Number</p>
                  <p class="pl-5 font-semibold">651</p>
                </div>

                <div class="flex-1">
                  <p class="font-bold text-xl">Birth Date</p>
                  <p class="pl-5 font-semibold">Septeber 23, 2402</p>
                </div>
              </div>
              <div class="flex justify-center">
                <div class="flex-1">
                  <p class="font-bold text-xl">Email</p>
                  <p class="pl-5 font-semibold">testmail@gmail.com</p>
                </div>
              </div>
              <div class="flex justify-center">
                <div class="flex-1">
                  <p class="font-bold text-xl">Total Applications</p>
                  <p class="pl-5 font-semibold">56</p>
                </div>

                <div class="flex-1">
                  <p class="font-bold text-xl">Accepted Applications</p>
                  <p class="pl-5 font-semibold">0</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="flex flex-col gap-y-[2%] justify-center flex-1">
          <div class="text-center">
            <h2 class="text-4xl font-semibold">Pet</h2>
          </div>
          <div class="flex flex-col bg-gray-400 h-60 rounded-lg p-5">
            <div class="flex dui-avatar justify-center">
              <div class="ring-primary ring-offset-base-100 w-35 rounded-full ring-2 ring-offset-2">
                <img src="https://img.daisyui.com/images/profile/demo/spiderperson@192.webp" />
              </div>
            </div>

            <div class="flex flex-col gap-y-1 pt-2 items-center">
              <p class="text-2xl font-bold">Tabby</p>
              <p class="font-bold">View details</p>
            </div>
          </div>
        </div>
      </div>

      <div class="flex gap-5 pt-10 px-[30%]">
        <button class="flex-1 dui-btn dui-btn-success text-3xl h-15">Approve</button>
        <button class="flex-1 dui-btn dui-btn-error text-3xl h-15">Reject</button>
      </div>
    </div>
  </section>
</template>
