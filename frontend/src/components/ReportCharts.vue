<script setup lang="ts">
import { onMounted, reactive, ref, watch } from 'vue'
import { Line, Pie } from 'vue-chartjs'

import axios from 'axios'
import { useAuthStore } from '@/stores/useAuthStore'
import { useThemeStore } from '@/stores/useThemeStore'

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

type SpeciesFrequency = {
  speciesFrequency: number
}

// Chart data------------------------------------

const lineData = reactive<ChartData<'line'>>({
  labels: [],
  datasets: [
    {
      label: 'Frequency',
      data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      borderColor: '#dca54d',
      backgroundColor: '#152747',
      fill: true,
    },
  ],
})

const applicationStatusPieData: ChartData<'pie'> = {
  labels: ['Approved', 'Rejected', 'Pending', 'Cancelled'],
  datasets: [
    {
      label: 'Frequency',
      data: [0, 0, 0],
      backgroundColor: ['#66BB6A', '#BA2D1E', '#FFA726', '#B0BEC5'],
    },
  ],
}

const preferredPetSpeciesPieData: ChartData<'pie'> = {
  labels: [],
  datasets: [
    {
      label: 'Frequency',
      data: [],
      backgroundColor: ['#BA2D1E', '#825b57', '#FFA726', '#95c91a', '#0f9482'],
    },
  ],
}

// Chart options------------------------------------

const lineOptions = reactive<ChartOptions<'line'>>({
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      labels: {
        font: { family: 'RethinkSans, sans-serif', size: 14, weight: 500 },
        color: '#000000',
      },
    },
    tooltip: {
      enabled: true,
      bodyFont: { family: 'RethinkSans, sans-serif', size: 14, weight: 500 },
      titleFont: { family: 'RethinkSans, sans-serif', size: 14, weight: 600 },
      bodyColor: '#000000',
      titleColor: '#000000',
    },
  },
  scales: {
    y: {
      ticks: { font: { family: 'RethinkSans, sans-serif', size: 12 }, color: '#000000' },
      grid: {
        color: '#152747',
      },
    },
    x: {
      ticks: { font: { family: 'RethinkSans, sans-serif', size: 12 }, color: '#000000' },
      grid: {
        color: '#152747',
      },
    },
  },
})

const pieOptions = reactive<ChartOptions<'pie'>>({
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      labels: {
        font: { family: 'RethinkSans, sans-serif', size: 14, weight: 500 },
        color: '#000000',
      },
    },
    tooltip: {
      enabled: true,
      bodyFont: { family: 'RethinkSans, sans-serif', size: 14, weight: 500 },
      titleFont: { family: 'RethinkSans, sans-serif', size: 14, weight: 600 },
      bodyColor: '#000000',
      titleColor: '#000000',
    },
  },
  elements: {
    arc: {
      borderWidth: 0,
    },
  },
})

const selectedRange = ref('monthly')
const chartKey = ref(0)

const auth = useAuthStore()
const theme = useThemeStore()

const apiUrl = import.meta.env.VITE_API_URL

const longestPetOwnership = reactive({
  adoptedPetName: '',
  breedName: '',
  speciesName: '',
  timeSinceAdoption: '',
})

const showLongestPetOwnership = ref(false)

function getAdditionalUiColors() {
  if (theme.currentTheme == 'luxury') {
    return {
      fontColor: '#dca54d',
      lineColor: '#dca54d',
      fillColor: '#152747',
      scalesColor: '#152747',
    }
  } else {
    return {
      fontColor: '#7c2808',
      lineColor: '#7c2808',
      fillColor: '#ffd6a7',
      scalesColor: '#ffd6a7',
    }
  }
}

const updateChart = async () => {
  if (selectedRange.value === 'yearly') {
    lineData.labels = getLast5Years()

    lineData.datasets[0].data = [5, 8, 12, 10, 6]
  } else {
    lineData.labels = getLast12Months()
  }

  await fetchApplicationReports()

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

  const last12Months: string[] = []

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
  const last5Years: string[] = []

  const now: Date = new Date()
  const currentYear: number = now.getFullYear()

  for (let i = 0; i < 5; i++) {
    last5Years.push(`${currentYear - i}`)
  }

  return last5Years.reverse()
}

const fetchApplicationReports = async () => {
  const response = await axios.get(`${apiUrl}/adoption-applications/get-application-reports`, {
    params: {
      selectedRange: selectedRange.value,
      firstValue: lineData.labels ? lineData.labels[0] : '',
      shelterId: auth.isShelterStaff ? auth.shelterId : null,
      userId: auth.isUser ? auth.userId : null,
      fetchType: auth.isShelterStaff ? 'shelter_staff' : 'adopter',
    },
  })

  lineData.datasets[0].data = response.data.applicationsFrequency

  applicationStatusPieData.datasets[0].data = response.data.applicationStatusFrequency

  updatePreferredPetSpeciesPieData(response.data.preferredPetSpeciesFrequency)
  chartKey.value++
}

const updatePreferredPetSpeciesPieData = (preferredPetSpeciesData: SpeciesFrequency[]) => {
  preferredPetSpeciesData.forEach((speciesFrequency: SpeciesFrequency) => {
    Object.entries(speciesFrequency).forEach(([key, value]) => {
      preferredPetSpeciesPieData.labels?.push(key)
      preferredPetSpeciesPieData.datasets[0].data.push(value)
    })
  })
}

const fetchLongestPetOwnership = async () => {
  const response = await axios.get(`${apiUrl}/adoption-applications/get-longest-pet-ownership`, {
    params: {
      userId: auth.isUser ? auth.userId : null,
    },
  })

  if (response.data.longestPetOwnership) {
    Object.assign(longestPetOwnership, response.data.longestPetOwnership)
    showLongestPetOwnership.value = true
  }
}

watch(
  () => theme.currentTheme,
  () => {
    const additionalUiColors = getAdditionalUiColors()

    lineOptions.plugins!.legend!.labels!.color = additionalUiColors.fontColor
    lineOptions.plugins!.tooltip!.bodyColor = additionalUiColors.fontColor
    lineOptions.plugins!.tooltip!.titleColor = additionalUiColors.fontColor
    lineOptions.scales!.x!.ticks!.color = additionalUiColors.fontColor
    lineOptions.scales!.y!.ticks!.color = additionalUiColors.fontColor

    pieOptions.plugins!.legend!.labels!.color = additionalUiColors.fontColor
    pieOptions.plugins!.tooltip!.bodyColor = additionalUiColors.fontColor
    pieOptions.plugins!.tooltip!.titleColor = additionalUiColors.fontColor

    lineOptions.scales!.x!.grid!.color = additionalUiColors.scalesColor
    lineOptions.scales!.y!.grid!.color = additionalUiColors.scalesColor

    lineData.datasets[0]!.borderColor = additionalUiColors.lineColor
    lineData.datasets[0]!.backgroundColor = additionalUiColors.fillColor

    chartKey.value++
  },
  { immediate: true },
)

onMounted(async () => {
  try {
    if (auth.isUser) {
      await fetchLongestPetOwnership()
    }

    updateChart()
  } catch (error) {
    console.error('Error retrieving data from backend', error)
  }
})
</script>

<template>
  <section class="h-screen w-[87vw] bg-primary-content">
    <div class="p-5 h-full flex flex-col box-border">
      <h1 class="text-6xl font-semibold font-fredoka text-base-content">Reports</h1>

      <div class="pt-5 flex flex-col flex-1 min-h-0">
        <div class="mb-4" v-if="auth.isUser && showLongestPetOwnership">
          <h1 class="font-medium text-xl font-fredoka text-base-content">Longest Pet Ownership</h1>
          <p class="pl-5 font-medium font-fredoka text-base-content">
            {{
              `Your first adopted pet, ${longestPetOwnership.adoptedPetName} (${longestPetOwnership.speciesName}/${longestPetOwnership.breedName}), has been with you for `
            }}
            <u>{{ `${longestPetOwnership.timeSinceAdoption}` }}.</u>
          </p>
        </div>

        <div class="flex-1 min-h-0 overflow-hidden">
          <div class="flex flex-row">
            <div class="flex-1">
              <h1 class="font-medium text-xl font-fredoka text-base-content">
                Application Frequency
              </h1>
            </div>

            <div class="flex-1">
              <select
                v-model="selectedRange"
                @change="updateChart"
                class="dui-select ml-auto block font-fredoka font-medium text-base-content"
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
            <h1 class="font-medium text-xl font-fredoka text-base-content">Application Status</h1>
            <div class="w-full h-full relative pb-10">
              <Pie :data="applicationStatusPieData" :options="pieOptions" :key="chartKey" />
            </div>
          </div>
          <div class="flex-1 min-h-0 overflow-hidden">
            <h1 class="font-medium text-xl font-fredoka text-base-content">
              Preferred Pet Species
            </h1>
            <div class="w-full h-full relative pb-10">
              <Pie :data="preferredPetSpeciesPieData" :options="pieOptions" :key="chartKey" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
