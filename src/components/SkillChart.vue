<template>
  <p class="text-block my-2">
    {{ props.skills.programmingLanguages.description }}
  </p>
  <div class="md:w-8/12 mx-auto">
    <canvas ref="programmingLanguages" :id="`toolstack-1-${props.index}`" class="my-5">

    </canvas>
  </div>
  <p class="text-block my-2">
    {{ props.skills.programmingLanguages.description }}
  </p>
  <div class="md:w-8/12 mx-auto">
    <canvas ref="frameworks" :id="`toolstack-2-${props.index}`" class="my-5">

    </canvas>
  </div>
  <p class="text-block my-2">
    {{ props.skills.programmingLanguages.description }}
  </p>
  <div class="md:w-8/12 mx-auto">
    <canvas ref="libraries" :id="`toolstack-3-${props.index}`" class="my-5">

    </canvas>
  </div>
</template>

<script setup>
import { ref, onActivated, onUpdated, onUnmounted, onMounted, onBeforeMount, watch } from 'vue'
import { storeToRefs } from 'pinia';
import { Chart } from 'chart.js/auto';
import { useAppStore } from '../stores/appStore.js'

// access the `store` variable anywhere in the component ✨
const { theme } = storeToRefs(useAppStore());
console.info(theme.value);
watch(theme, (theme, prevTheme) => {
  programmingLanguagesChart.value.destroy();
  frameworksChart.value.destroy();
  librariesChart.value.destroy();
  createSkillCharts(theme);

});

const props = defineProps({
  index: {
    type: String,
    default: '0'
  },
  skills: {
    type: Object,
    default: {}
  }
});


const programmingLanguages = ref(null);
const frameworks = ref(null);
const libraries = ref(null);

const programmingLanguagesChart = ref(null);
const frameworksChart = ref(null);
const librariesChart = ref(null);



const createSkillCharts = (theme) => {
  let config;
  let data;
  let rgba_value;
  let font_color;
  if (theme === 'light') {
    console.info('Create Chart for light theme.')
    rgba_value = '0';
    font_color = 'black';

  } else {
    console.info('Create Chart for dark theme.')
    rgba_value = '255';
    font_color = 'white';

  }
  for (const key in props.skills) {
    if (Object.hasOwnProperty.call(props.skills, key)) {
      let element = props.skills[key];
      let labels = element.values.map((el) => el.name);
      let dataValues = element.values.map((el) => el.skillValue * 100);
      let backgroundColor = element.values.map((el) => `rgba(${rgba_value}, ${rgba_value}, ${rgba_value}, ${el.skillValue})`);

      data = {
        labels: labels,
        datasets: [{
          label: 'Knowledge in [%]',
          data: dataValues,
          backgroundColor: backgroundColor,
          borderWidth: 0
        }]
      };

      config = {
        type: 'bar',
        data,
        options: {
          // indexAxis: 'y',
          scales: {
            x: {
              ticks: {
                color: font_color
              }
            },
            x: {
              ticks: {
                color: font_color
              }
            }
          }
        },
      };
      switch (key) {
        case 'programmingLanguages':
          programmingLanguagesChart.value = new Chart(programmingLanguages.value, config);
          break;
        case 'frameworks':
          frameworksChart.value = new Chart(frameworks.value, config);
          break;
        case 'libraries':
          librariesChart.value = new Chart(libraries.value, config);
          break;

        default:
          console.warn('NO CANVAS FOR THIS SKILL')
          break;
      }
    }
  }

}


onMounted(() => {
  createSkillCharts(theme.value);
})
</script>