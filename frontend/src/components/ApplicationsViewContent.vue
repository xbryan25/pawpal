<script setup lang="ts">
import SearchAndSortHeader from './SearchAndSortHeader.vue'
import TableRow from './TableRow.vue'

import samplePet1 from '@/assets/images/sample-pet-1.jpg'
import samplePet2 from '@/assets/images/sample-pet-2.jpg'
import samplePet3 from '@/assets/images/sample-pet-3.jpg'
import samplePet4 from '@/assets/images/sample-pet-4.jpg'
import samplePet5 from '@/assets/images/sample-pet-5.webp'
</script>

<template>
  <section class="h-[90vh] w-[87vw]">
    <div class="p-5 h-full flex flex-col">
      <h1 class="text-6xl font-semibold">Applications</h1>

      <SearchAndSortHeader />

      <div class="overflow-x-auto">
        <table class="dui-table">
          <!-- head -->
          <thead>
            <tr>
              <th class="text-center text-2xl w-1/2">Pet</th>
              <th class="text-center text-2xl">Application Date</th>
              <th class="text-center text-2xl">Application Status</th>
            </tr>
          </thead>
          <tbody>
            <TableRow />
            <TableRow />
            <TableRow />
            <TableRow />
            <TableRow />
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
