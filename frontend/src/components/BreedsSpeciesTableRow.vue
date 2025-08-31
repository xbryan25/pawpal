<script setup lang="ts">
interface Props {
  breedName?: string
  speciesName: string
  numOfRegisteredPets: number
  rowType: string
}

const props = defineProps<Props>()
</script>

<template>
  <tr class="hover:bg-base-300 text-center">
    <td class="text-xl font-medium px-2 font-fredoka text-base-content" v-if="rowType == 'breed'">
      {{ props.breedName }}
    </td>
    <td class="text-xl font-medium px-2 font-fredoka text-base-content">{{ props.speciesName }}</td>
    <td class="text-xl font-medium px-2 font-fredoka text-base-content">
      {{ props.numOfRegisteredPets }}
    </td>
  </tr>
</template>
