<script setup lang="ts">
import SignupForm from '@/components/SignupForm.vue'
import loginImage1 from '@/assets/images/login-image-1.jpg'
</script>

<template>
  <div class="flex bg-primary-content">
    <div class="flex-1 w-[50vw] h-[calc(100vh-2rem)] m-4">
      <img :src="loginImage1" class="w-full h-full object-cover rounded-xl" />
    </div>
    <SignupForm />
  </div>
</template>
