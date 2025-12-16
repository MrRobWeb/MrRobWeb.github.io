<template>
  <div class="space-y-8">
    <div>
      <p class="text-body text-corporate-dark-gray dark:text-corporate-light-gray mb-4">
        {{ props.skills.programmingLanguages.description }}
      </p>
      <div class="md:w-10/12 mx-auto">
        <canvas ref="programmingLanguages" :id="`toolstack-1-${props.index}`"></canvas>
      </div>
    </div>

    <div>
      <p class="text-body text-corporate-dark-gray dark:text-corporate-light-gray mb-4">
        {{ props.skills.frameworks.description }}
      </p>
      <div class="md:w-10/12 mx-auto">
        <canvas ref="frameworks" :id="`toolstack-2-${props.index}`"></canvas>
      </div>
    </div>

    <div>
      <p class="text-body text-corporate-dark-gray dark:text-corporate-light-gray mb-4">
        {{ props.skills.libraries.description }}
      </p>
      <div class="md:w-10/12 mx-auto">
        <canvas ref="libraries" :id="`toolstack-3-${props.index}`"></canvas>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onUnmounted, onMounted, watch } from 'vue'
import { storeToRefs } from 'pinia'
import { Chart } from 'chart.js/auto'
import { useAppStore } from '../stores/appStore.js'

const { theme } = storeToRefs(useAppStore())

watch(theme, (newTheme) => {
  if (programmingLanguagesChart.value) programmingLanguagesChart.value.destroy()
  if (frameworksChart.value) frameworksChart.value.destroy()
  if (librariesChart.value) librariesChart.value.destroy()
  createSkillCharts(newTheme)
})

const props = defineProps({
  index: {
    type: String,
    default: '0'
  },
  skills: {
    type: Object,
    default: () => ({})
  }
})

const programmingLanguages = ref(null)
const frameworks = ref(null)
const libraries = ref(null)

const programmingLanguagesChart = ref(null)
const frameworksChart = ref(null)
const librariesChart = ref(null)

// McKinsey color palette
const MCKINSEY_NAVY = '#00205B'
const MCKINSEY_TEAL = '#007FA3'
const CORPORATE_DARK_GRAY = '#343A40'
const CORPORATE_LIGHT_GRAY = '#E9ECEF'
const MCKINSEY_NAVY_LIGHT = '#003380'

const createSkillCharts = (currentTheme) => {
  let barColor, fontColor, gridColor

  if (currentTheme === 'light') {
    barColor = MCKINSEY_NAVY
    fontColor = CORPORATE_DARK_GRAY
    gridColor = CORPORATE_LIGHT_GRAY
  } else {
    barColor = MCKINSEY_TEAL
    fontColor = CORPORATE_LIGHT_GRAY
    gridColor = MCKINSEY_NAVY_LIGHT
  }

  for (const key in props.skills) {
    if (Object.hasOwnProperty.call(props.skills, key)) {
      const element = props.skills[key]
      element.values.sort((a, b) => b.skillValue - a.skillValue)
      const labels = element.values.map((el) => el.name)
      const dataValues = element.values.map((el) => el.skillValue * 100)

      // Create gradient opacity based on skill value
      const backgroundColor = element.values.map((el) => {
        const opacity = 0.3 + (el.skillValue * 0.7)
        if (currentTheme === 'light') {
          return `rgba(0, 32, 91, ${opacity})` // Navy with varying opacity
        } else {
          return `rgba(0, 127, 163, ${opacity})` // Teal with varying opacity
        }
      })

      const data = {
        labels: labels,
        datasets: [{
          label: 'Proficiency (%)',
          data: dataValues,
          backgroundColor: backgroundColor,
          borderWidth: 0,
          borderRadius: 2,
        }]
      }

      const config = {
        type: 'bar',
        data,
        options: {
          responsive: true,
          maintainAspectRatio: true,
          plugins: {
            legend: {
              display: false
            }
          },
          scales: {
            x: {
              grid: {
                display: false
              },
              ticks: {
                color: fontColor,
                font: {
                  family: 'Inter',
                  size: 11
                }
              }
            },
            y: {
              min: 0,
              max: 100,
              grid: {
                color: gridColor
              },
              ticks: {
                color: fontColor,
                font: {
                  family: 'Inter',
                  size: 11
                },
                callback: (value) => value + '%'
              }
            }
          }
        }
      }

      switch (key) {
        case 'programmingLanguages':
          programmingLanguagesChart.value = new Chart(programmingLanguages.value, config)
          break
        case 'frameworks':
          frameworksChart.value = new Chart(frameworks.value, config)
          break
        case 'libraries':
          librariesChart.value = new Chart(libraries.value, config)
          break
        default:
          break
      }
    }
  }
}

onMounted(() => {
  createSkillCharts(theme.value)
})

onUnmounted(() => {
  if (programmingLanguagesChart.value) programmingLanguagesChart.value.destroy()
  if (frameworksChart.value) frameworksChart.value.destroy()
  if (librariesChart.value) librariesChart.value.destroy()
})
</script>
