<template>
  <div class="section">
    <div class="container-corporate">
      <!-- Introduction Section -->
      <div class="max-w-3xl mx-auto mb-16">
        <div class="flex items-start gap-6 mb-8">
          <img
            src="../assets/imgs/IMG_7440_1.jpeg"
            alt="Robert Weber"
            class="w-20 h-20 md:w-24 md:h-24 rounded-full flex-shrink-0"
          >
          <div>
            <h2 class="text-heading-2 text-mckinsey-navy dark:text-white mb-2">About</h2>
            <p class="text-small text-corporate-mid-gray">Data Engineering Manager</p>
          </div>
        </div>

        <div class="space-y-6">
          <p class="text-body-lg text-corporate-dark-gray dark:text-corporate-light-gray">
            Data Engineering Manager with expertise in agentic AI, cloud architecture, data platform development,
            and engineering team leadership. Delivering scalable solutions that transform how
            organizations leverage data for strategic decision-making.
          </p>

          <blockquote class="border-l-4 border-mckinsey-teal pl-6 my-8 italic text-corporate-mid-gray">
            "Learning never exhausts the mind." — Leonardo da Vinci
          </blockquote>

          <p class="text-body text-corporate-dark-gray dark:text-corporate-light-gray">
            {{ workAge }} of consulting experience following an academic foundation in applied quantum physics.
            Core competencies include DevOps engineering, enterprise data architecture, project delivery,
            and fullstack development. Industry expertise spans energy, human resources, automotive,
            aviation, retail, and pharmaceutical sectors.
          </p>
        </div>

        <!-- Quick Links -->
        <div class="flex flex-wrap gap-4 mt-8">
          <button @click="scrollToTechStack" class="btn-secondary text-sm">
            Technology Stack
          </button>
          <RouterLink to="/project" class="btn-secondary text-sm">
            View Projects
          </RouterLink>
          <RouterLink to="/contact" class="btn-primary text-sm">
            Contact Me
          </RouterLink>
        </div>
      </div>

      <!-- Technology Stack Section -->
      <section id="tech-stack" ref="tech_stack" class="pt-16">
        <div class="max-w-3xl mx-auto">
          <h2 class="text-heading-1 text-mckinsey-navy dark:text-white mb-12">
            Technology Stack
          </h2>

          <!-- Timeline - clean McKinsey style -->
          <div class="space-y-0">
            <article
              v-for="(toolStack, index) in toolStacks"
              :key="toolStack.title"
              :ref="setItemRef"
              class="relative pl-8 border-l-2 border-corporate-light-gray dark:border-mckinsey-navy-light hover:border-mckinsey-teal transition-colors duration-300"
            >
              <!-- Timeline dot -->
              <button
                class="absolute left-0 top-0 w-4 h-4 -translate-x-[9px] rounded-full bg-corporate-light-gray dark:bg-mckinsey-navy-light border-2 border-white dark:border-mckinsey-navy-dark hover:bg-mckinsey-teal transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-mckinsey-teal"
                @click="toggleShow(index)"
                :aria-expanded="show === index"
                :aria-label="`Toggle ${toolStack.title} details`"
              ></button>

              <div class="pb-12 cursor-pointer" @click="toggleShow(index)">
                <h3 class="text-heading-3 text-mckinsey-navy dark:text-white mb-1">
                  {{ toolStack.title }}
                </h3>
                <p class="text-small text-corporate-mid-gray mb-2">
                  {{ toolStack.subTitle }}
                </p>
                <span v-if="show !== index" class="text-sm text-mckinsey-teal">
                  Click to expand
                </span>

                <!-- Expanded content with simple fade -->
                <Transition name="fade">
                  <div v-if="show === index" class="mt-4">
                    <p class="text-body text-corporate-dark-gray dark:text-corporate-light-gray mb-6">
                      {{ getDescription(toolStack, index) }}
                    </p>
                    <SkillChart :index="String(index)" :skills="toolStack.skills" />
                  </div>
                </Transition>
              </div>
            </article>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import SkillChart from '../components/SkillChart.vue'
import { useAppStore } from '../stores/appStore.js'
import { toolStacks as skillsData } from '../data/skills.js'

const { heightHeader, workAge } = storeToRefs(useAppStore())

const toolStacks = ref(skillsData)

const itemRefs = ref([])
const setItemRef = (el) => {
  if (el) {
    itemRefs.value.push(el)
  }
}

onMounted(() => {
  window.scrollTo({ top: 0 })
})

const tech_stack = ref(null)

const scrollToTechStack = () => {
  setTimeout(() => {
    scrollIntoViewWithOffset(tech_stack.value, heightHeader.value)
  }, 200)
}

const scrollIntoViewWithOffset = (el, offset) => {
  window.scrollTo({
    behavior: 'smooth',
    top:
      el.getBoundingClientRect().top -
      document.body.getBoundingClientRect().top -
      offset - 30,
  })
}

const getDescription = (toolStack, index) => {
  if (index === 1) {
    return `Being a data magician in the first place, I've been working in this area since finishing my studies ${workAge.value} ago.`
  }
  return toolStack.description
}

const show = ref(-1)

const toggleShow = (index) => {
  if (show.value === index) {
    show.value = -1
  } else {
    show.value = index
  }
  setTimeout(() => {
    if (itemRefs.value[index]) {
      scrollIntoViewWithOffset(itemRefs.value[index], heightHeader.value)
    }
  }, 300)
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
