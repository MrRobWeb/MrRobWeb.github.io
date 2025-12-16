<template>
  <footer class="border-t border-corporate-light-gray dark:border-mckinsey-navy-light bg-corporate-off-white dark:bg-mckinsey-navy-dark">
    <div class="container-corporate py-12">
      <div class="flex flex-col md:flex-row items-center justify-between gap-6">
        <!-- Title/Role -->
        <div class="text-center md:text-left">
          <p class="text-corporate-dark-gray dark:text-corporate-light-gray font-medium">
            Data Engineering Manager
          </p>
        </div>

        <!-- Social Links - minimalist icons -->
        <div class="flex items-center space-x-6">
          <a
            @click="showModal = true"
            class="text-corporate-mid-gray hover:text-mckinsey-teal dark:text-corporate-light-gray dark:hover:text-mckinsey-teal-light transition-colors duration-200 cursor-pointer"
            aria-label="Send email"
          >
            <font-awesome-icon icon="fa-solid fa-envelope" class="text-xl" />
          </a>
          <a
            href="https://www.linkedin.com/in/robert-w-300922158/"
            target="_blank"
            rel="noopener noreferrer"
            class="text-corporate-mid-gray hover:text-mckinsey-teal dark:text-corporate-light-gray dark:hover:text-mckinsey-teal-light transition-colors duration-200"
            aria-label="LinkedIn profile"
          >
            <font-awesome-icon icon="fa-brands fa-linkedin" class="text-xl" />
          </a>
          <a
            href="https://github.com/MrRobWeb"
            target="_blank"
            rel="noopener noreferrer"
            class="text-corporate-mid-gray hover:text-mckinsey-teal dark:text-corporate-light-gray dark:hover:text-mckinsey-teal-light transition-colors duration-200"
            aria-label="GitHub profile"
          >
            <font-awesome-icon icon="fa-brands fa-github" class="text-xl" />
          </a>
        </div>

        <!-- Privacy/Legal -->
        <div class="text-center md:text-right">
          <RouterLink
            to="/privacyPolicy"
            class="text-sm text-corporate-mid-gray hover:text-mckinsey-navy dark:text-corporate-light-gray dark:hover:text-white transition-colors duration-200"
          >
            Privacy Policy
          </RouterLink>
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
  </footer>
</template>

<script setup>
import { ref } from 'vue'
import Modal from '../components/Modal.vue'

const showModal = ref(false)
</script>
