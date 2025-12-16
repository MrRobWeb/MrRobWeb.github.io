<template>
  <div class="section">
    <div class="container-corporate">
      <!-- Page Header -->
      <header class="max-w-3xl mb-16">
        <h1 class="text-hero text-mckinsey-navy dark:text-white mb-4">
          Projects
        </h1>
        <p class="text-body-lg text-corporate-mid-gray dark:text-corporate-light-gray mb-6">
          A selection of project types managed across various roles and industries.
        </p>
        <button
          @click="showModal = true"
          class="link-corporate inline-flex items-center gap-2"
        >
          <font-awesome-icon icon="fa-solid fa-envelope" />
          Have questions? Get in touch
        </button>
      </header>

      <!-- Projects List -->
      <div class="max-w-4xl divide-y divide-corporate-light-gray dark:divide-mckinsey-navy-light">
        <article
          v-for="(project, index) in projects"
          :key="project.title"
          class="py-10 first:pt-0 opacity-0 animate-fade-in"
          :style="{ animationDelay: `${index * 0.1}s` }"
        >
          <div class="grid md:grid-cols-4 gap-6">
            <!-- Meta -->
            <div class="md:col-span-1">
              <p class="font-medium text-mckinsey-navy dark:text-white">
                {{ project.role }}
              </p>
              <p class="text-small text-corporate-mid-gray">
                {{ project.date }}
              </p>
              <p class="text-small italic text-corporate-mid-gray mt-1">
                {{ project.industry }}
              </p>
            </div>

            <!-- Content -->
            <div class="md:col-span-3">
              <h2 class="text-heading-3 text-mckinsey-navy dark:text-white mb-3">
                {{ project.title }}
              </h2>

              <!-- Technologies -->
              <div class="flex flex-wrap gap-2 mb-4">
                <span
                  v-for="tech in project.technologies"
                  :key="tech"
                  class="px-3 py-1 text-sm bg-corporate-off-white dark:bg-mckinsey-navy text-corporate-dark-gray dark:text-corporate-light-gray rounded"
                >
                  {{ tech }}
                </span>
              </div>

              <!-- Description -->
              <p class="text-body text-corporate-dark-gray dark:text-corporate-light-gray mb-4">
                {{ show === index ? project.description : project.description.substring(0, 150) + '...' }}
              </p>

              <button
                @click="toggleShow(index)"
                class="link-corporate text-sm font-medium"
                :aria-label="show === index ? `Read less about ${project.title}` : `Read more about ${project.title}`"
              >
                {{ show === index ? 'Read less' : 'Read more' }}
              </button>
            </div>
          </div>
        </article>
      </div>
    </div>

    <!-- Modal -->
    <Teleport to="body">
      <Modal :show="showModal" @close="showModal = false">
        <template #header>
          <h3>Drop me a message:</h3>
        </template>
      </Modal>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Modal from '../components/Modal.vue'
import { projects as projectsData } from '../data/projects.js'

const projects = ref(projectsData)
const show = ref(-1)
const showModal = ref(false)

const toggleShow = (index) => {
  show.value = show.value === index ? -1 : index
}

onMounted(() => {
  window.scrollTo({ top: 0 })
})
</script>
