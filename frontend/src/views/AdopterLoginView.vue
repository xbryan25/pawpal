<script setup lang="ts">
import LoginForm from '@/components/LoginForm.vue'
import loginImage1 from '@/assets/images/login-image-1.jpg'
</script>

<template>
  <div class="flex bg-primary-content">
    <LoginForm loginType="adopter" />
    <div class="flex-1 w-[50vw] h-[calc(100vh-2rem)] m-4">
      <img :src="loginImage1" class="w-full h-full object-cover rounded-xl" />
    </div>
  </div>
</template>
