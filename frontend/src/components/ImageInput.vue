<script setup lang="ts">
import { defineEmits, defineProps, ref } from 'vue'

interface Props {
  mode?: string
  imageUrl?: any
  fileName?: string
  index?: number
}

const props = defineProps<Props>()

const emit = defineEmits<{
  (e: 'selectImage', imageLocation: File): void
  (e: 'deleteImage', index: number | undefined): void
}>()

const selectedImage = ref()
const selectedImageFileName = ref(props.imageUrl || props.fileName)

console.log('props.mode ' + props.mode)

const numberToOrdinal = (index: number | undefined) => {
  if (!index) {
    return 'Error'
  }

  if (index == 1) {
    return 'First'
  } else if (index == 2) {
    return 'Second'
  } else if (index == 3) {
    return 'Third'
  } else if (index == 4) {
    return 'Fourth'
  } else if (index == 5) {
    return 'Fifth'
  }
}

function openFilePicker(accept: string[] = [], multiple = false) {
  return new Promise<FileList | null>((resolve) => {
    const input = document.createElement('input')
    input.type = 'file'
    input.style.display = 'none'

    if (accept.length) {
      input.accept = accept.join(',')
    }

    input.multiple = multiple

    input.addEventListener('change', () => {
      resolve(input.files)
      input.remove()
    })

    document.body.appendChild(input)
    input.click()
  })
}

async function handleSelectFile() {
  const file = await openFilePicker(['image/png', 'image/jpeg'])
  if (file) {
    selectedImage.value = file[0]
    selectedImageFileName.value = file[0].name

    emit('selectImage', file[0])
  }
}

const deleteImage = () => {
  emit('deleteImage', props.index)
}

const viewImage = () => {
  window.open(props.imageUrl, '_blank')
}
</script>

<template>
  <div class="">
    <h3 class="text-lg font-semibold">{{ numberToOrdinal(props.index) }} Photo</h3>
    <div class="flex gap-4 h-10 border-1 border-gray-300 rounded-sm pr-4">
      <div class="flex rounded-xs w-[6.65rem]">
        <div class="flex-1 flex justify-center items-center border-r-1 border-gray-300">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            height="24px"
            viewBox="0 -960 960 960"
            width="24px"
            fill="#000000"
            class="cursor-pointer"
            @click="deleteImage"
          >
            <path
              d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm400-600H280v520h400v-520ZM360-280h80v-360h-80v360Zm160 0h80v-360h-80v360ZM280-720v520-520Z"
            />
          </svg>
        </div>

        <div
          class="flex-1 flex justify-center items-center border-r-1 border-gray-300"
          v-if="props.mode === 'edit'"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            height="24px"
            viewBox="0 -960 960 960"
            width="24px"
            fill="#000000"
            class="cursor-pointer"
            @click="viewImage"
          >
            <path
              d="M480-320q75 0 127.5-52.5T660-500q0-75-52.5-127.5T480-680q-75 0-127.5 52.5T300-500q0 75 52.5 127.5T480-320Zm0-72q-45 0-76.5-31.5T372-500q0-45 31.5-76.5T480-608q45 0 76.5 31.5T588-500q0 45-31.5 76.5T480-392Zm0 192q-146 0-266-81.5T40-500q54-137 174-218.5T480-800q146 0 266 81.5T920-500q-54 137-174 218.5T480-200Zm0-300Zm0 220q113 0 207.5-59.5T832-500q-50-101-144.5-160.5T480-720q-113 0-207.5 59.5T128-500q50 101 144.5 160.5T480-280Z"
            />
          </svg>
        </div>

        <div class="flex-1 flex justify-center items-center border-r-1 border-gray-300">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            height="24px"
            viewBox="0 -960 960 960"
            width="24px"
            fill="#000000"
            class="cursor-pointer"
            @click="handleSelectFile"
          >
            <path
              d="M440-320v-326L336-542l-56-58 200-200 200 200-56 58-104-104v326h-80ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z"
            />
          </svg>
        </div>
      </div>

      <div
        class="flex-1 flex items-center text-sm truncate whitespace-nowrap overflow-x-scroll overflow-y-hidden scrollbar-hide"
      >
        {{ selectedImageFileName || 'No file chosen' }}
      </div>
    </div>
  </div>
</template>
