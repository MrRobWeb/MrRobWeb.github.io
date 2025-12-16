<template>
  <div :class="isDarkMode ? 'dark' : ''">
    <div class="bg-corporate-white dark:bg-mckinsey-navy-dark min-h-screen transition-colors duration-300">
      <!-- Header with constrained width -->
      <header
        ref="header"
        class="sticky top-0 z-50 bg-corporate-white/95 dark:bg-mckinsey-navy-dark/95 backdrop-blur-sm border-b border-corporate-light-gray dark:border-mckinsey-navy-light transition-colors duration-300"
      >
        <div class="container-corporate">
          <div class="flex items-center justify-between py-4">
            <CardHeader />
            <button
              @click="toggleDarkMode"
              class="p-2 text-corporate-mid-gray hover:text-mckinsey-navy dark:text-corporate-light-gray dark:hover:text-white transition-colors duration-200"
              aria-label="Toggle dark mode"
            >
              <ModeToggler :class="isDarkMode ? 'fa-solid fa-sun' : 'fa-solid fa-moon'" />
            </button>
          </div>
        </div>
      </header>

      <!-- Main content -->
      <main class="flex-grow">
        <RouterView />
      </main>

      <!-- Footer -->
      <CardFooter />
    </div>
  </div>
</template>

<script setup>
import ModeToggler from './components/ModeToggler.vue';
import CardHeader from './components/CardHeader.vue';
import CardFooter from './components/CardFooter.vue';

import { ref, onMounted } from 'vue';
import { storeToRefs } from 'pinia';
import { useAppStore } from './stores/appStore.js'

const header = ref(null);

const { theme, heightHeader } = storeToRefs(useAppStore());

const isDarkMode = ref(false);

onMounted(() => {
  if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    isDarkMode.value = true;
  } else {
    isDarkMode.value = false;
  }
  heightHeader.value = header.value.offsetHeight;
})

const toggleDarkMode = () => {
  if (isDarkMode.value) {
    localStorage.theme = 'light';
    theme.value = 'light';
    isDarkMode.value = false;
  } else {
    localStorage.theme = 'dark';
    theme.value = 'dark';
    isDarkMode.value = true;
  }
}
</script>
