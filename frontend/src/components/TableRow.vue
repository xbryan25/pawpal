<script setup lang="ts">
interface Props {
  applicationDate: string
  petFirstImageUrl: string
  petName: string
  shelterName: string
  status: string
}

const props = defineProps<Props>()
</script>

<template>
  <tr class="hover:bg-base-300 text-center">
    <td>
      <div class="flex items-center justify-center gap-3">
        <div class="avatar">
          <div class="mask mask-squircle h-12 w-12">
            <img
              :src="props.petFirstImageUrl"
              alt="Avatar Tailwind CSS Component"
              class="w-full h-full object-cover"
            />
          </div>
        </div>
        <div>
          <div class="font-bold text-xl">{{ props.petName }}</div>
          <div class="text-base opacity-50">{{ props.shelterName }}</div>
        </div>
      </div>
    </td>
    <td class="text-xl font-medium">{{ props.applicationDate }}</td>
    <td class="text-xl font-medium">{{ props.status }}</td>
  </tr>
</template>
