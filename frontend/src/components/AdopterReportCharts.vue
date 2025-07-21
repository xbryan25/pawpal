<script setup lang="ts">
import { Line, Pie } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  ArcElement,
  type ChartOptions,
  type ChartData,
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  PointElement,
  ArcElement,
  CategoryScale,
  LinearScale,
)

const lineData: ChartData<'line'> = {
  labels: [
    'January 2025',
    'February 2025',
    'March 2025',
    'April 2025',
    'May 2025',
    'June 2025',
    'July 2025',
    'August 2025',
    'September 2025',
    'October 2025',
    'November 2025',
    'December 2025',
  ],
  datasets: [
    {
      label: 'Revenue',
      data: [0, 2, 1, 2, 1, 0, 0, 1, 1, 0, 0, 1],
      borderColor: '#42A5F5',
      backgroundColor: 'rgba(66, 165, 245, 0.2)',
      fill: true, // Area under the line
    },
  ],
}

const lineOptions: ChartOptions<'line'> = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { position: 'top' },
    title: { display: true, text: 'Monthly Revenue (Line)' },
  },
  scales: {
    y: {
      beginAtZero: true,
      ticks: {
        stepSize: 1,
      },
    },
  },
}

const applicationStatusPieData: ChartData<'pie'> = {
  labels: ['Accepted', 'Rejected', 'Pending'],
  datasets: [
    {
      label: 'Revenue',
      data: [3, 7, 5],
      backgroundColor: ['#66BB6A', '#BA2D1E', '#FFA726'],
    },
  ],
}

const adoptedTypePieData: ChartData<'pie'> = {
  labels: ['Cat', 'Dog', 'Bird', 'Guinea Pig', 'Others'],
  datasets: [
    {
      label: 'Revenue',
      data: [3, 7, 5, 5, 1],
      backgroundColor: ['#825b57', '#BA2D1E', '#FFA726', '#95c91a', '#0f9482'],
    },
  ],
}

const pieOptions: ChartOptions<'pie'> = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    title: { display: true, text: 'Pie Chart' },
  },
}
</script>

<template>
  <section class="h-screen w-[87vw]">
    <div class="p-5 h-full flex flex-col box-border">
      <h1 class="text-6xl font-semibold">Reports</h1>

      <div class="pt-5 flex flex-col flex-1 min-h-0">
        <div class="mb-4">
          <h1 class="font-bold text-xl">Longest Pet Ownership</h1>
          <p class="pl-5">
            Your first adopted pet, Max (Cat/Puspin), has been with you for
            <u>2 years and 4 months.</u>
          </p>
        </div>

        <div class="flex-1 min-h-0 overflow-hidden">
          <h1 class="font-bold text-xl">Adoption Timeline</h1>
          <div class="w-full h-full relative pb-10">
            <Line :data="lineData" :options="lineOptions" />
          </div>
        </div>

        <div class="flex-1 flex min-h-0 overflow-hidden">
          <div class="flex-1 min-h-0 overflow-hidden">
            <h1 class="font-bold text-xl">Application Status</h1>
            <div class="w-full h-full relative pb-10">
              <Pie :data="applicationStatusPieData" :options="pieOptions" />
            </div>
          </div>
          <div class="flex-1 min-h-0 overflow-hidden">
            <h1 class="font-bold text-xl">Types of Pets Adopted</h1>
            <div class="w-full h-full relative pb-10">
              <Pie :data="adoptedTypePieData" :options="pieOptions" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
