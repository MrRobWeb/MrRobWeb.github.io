<template>
  <div class="section">
    <div class="container-corporate">
      <div class="max-w-2xl mx-auto text-center">
        <h1 class="text-hero text-mckinsey-navy dark:text-white mb-4">
          Contact
        </h1>
        <p class="text-body-lg text-corporate-mid-gray dark:text-corporate-light-gray mb-12">
          I'd love to hear from you. Choose your preferred method of contact.
        </p>

        <!-- Contact Cards - clean grid -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <a
            v-for="(contact, index) in contacts"
            :key="contact.name"
            :href="contact.href || undefined"
            @click="!contact.href && (showModal = true)"
            :target="contact.href ? '_blank' : undefined"
            rel="noopener noreferrer"
            class="p-6 bg-corporate-off-white dark:bg-mckinsey-navy border border-corporate-light-gray dark:border-mckinsey-navy-light hover:border-mckinsey-teal dark:hover:border-mckinsey-teal transition-all duration-200 cursor-pointer opacity-0 animate-fade-in group"
            :style="{ animationDelay: `${index * 0.1}s` }"
          >
            <font-awesome-icon
              :icon="contact.icon"
              class="text-3xl text-corporate-mid-gray group-hover:text-mckinsey-teal dark:text-corporate-light-gray dark:group-hover:text-mckinsey-teal-light transition-colors duration-200 mb-3"
            />
            <p class="text-sm font-medium text-corporate-dark-gray dark:text-corporate-light-gray capitalize">
              {{ contact.name }}
            </p>
          </a>
        </div>
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

const showModal = ref(false)

const contacts = ref([
  { name: 'Message', icon: 'fa-solid fa-envelope' },
  { name: 'LinkedIn', icon: 'fa-brands fa-linkedin', href: 'https://www.linkedin.com/in/robert-w-300922158/' },
  { name: 'GitHub', icon: 'fa-brands fa-github', href: 'https://github.com/MrRobWeb' },
  { name: 'GitLab', icon: 'fa-brands fa-gitlab', href: 'https://gitlab.com/MrRobWeb' },
])

onMounted(() => {
  window.scrollTo({ top: 0 })
})
</script>
