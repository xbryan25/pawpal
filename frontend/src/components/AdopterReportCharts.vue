<script setup lang="ts">
import { reactive, ref } from 'vue'
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
  Filler,
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
  Filler,
)

const lineData = reactive<ChartData<'line'>>({
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
})

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

const selectedRange = ref('monthly')
const chartKey = ref(0)

const updateChart = () => {
  if (selectedRange.value === 'yearly') {
    lineData.labels = getLast5Years()

    lineData.datasets[0].data = [5, 8, 12, 10, 6]
  } else {
    lineData.labels = getLast12Months()

    lineData.datasets[0].data = [0, 2, 1, 2, 1, 0, 0, 1, 1, 0, 0, 1]
  }

  chartKey.value++
}

const getLast12Months = () => {
  const monthNames = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
  ]

  let last12Months: string[] = []

  const now: Date = new Date()
  let currentMonth: number = now.getMonth()
  let currentYear: number = now.getFullYear()

  for (let i = 0; i < 12; i++) {
    last12Months.push(`${monthNames[currentMonth]} ${currentYear}`)

    currentMonth--

    if (currentMonth == -1) {
      currentMonth = 11
      currentYear--
    }
  }

  return last12Months.reverse()
}

const getLast5Years = () => {
  let last5Years: string[] = []

  const now: Date = new Date()
  let currentYear: number = now.getFullYear()

  for (let i = 0; i < 5; i++) {
    last5Years.push(`${currentYear - i}`)
  }

  return last5Years.reverse()
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
          <div class="flex flex-row">
            <div class="flex-1">
              <h1 class="font-bold text-xl">Adoption Timeline</h1>
            </div>

            <div class="flex-1">
              <select
                v-model="selectedRange"
                @change="updateChart"
                class="dui-select ml-auto block"
              >
                <option value="monthly">Past 12 months</option>
                <option value="yearly">Past 5 years</option>
              </select>
            </div>
          </div>

          <div class="w-full h-full relative pb-10">
            <Line :data="lineData" :options="lineOptions" :key="chartKey" />
          </div>
        </div>

        <div class="flex-1 flex min-h-0 overflow-hidden pt-5">
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
