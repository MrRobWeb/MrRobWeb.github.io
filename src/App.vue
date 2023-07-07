<template>
  <div :class="isDarkMode ? 'dark' : ''">
    <div
      class="bg-[#ffffff] min-h-screen  flex flex-col justify-between  dark:bg-[#0F172A] duration-500 transition-all ease-in-out">
      <div class="sticky top-0 z-50 flex flex-col justify-center  bg-[#ffffff] dark:bg-[#0F172A] duration-500 transition-all ease-in-out">
        <button @click="toggleDarkMode" class="animate-pulse my-4 right-3 sm:top-6 sm:right-6 ">
          <ModeToggler :class="isDarkMode ? 'fa-solid fa-sun' : 'fa-solid fa-moon'" />
        </button>
        <CardHeader />
      </div>
      <RouterView />

      
      <CardFooter />
    </div>
  </div>
</template>

<script setup>
import ModeToggler from './components/ModeToggler.vue';
import CardHeader from './components/CardHeader.vue';
import CardFooter from './components/CardFooter.vue';


import { ref, onMounted } from 'vue';
import {storeToRefs} from 'pinia';
import { useAppStore } from './stores/appStore.js'

const {theme} = storeToRefs(useAppStore());

const isDarkMode = ref(false);

onMounted(() => {
  if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    isDarkMode.value = true;
  } else {
    isDarkMode.value = false;
  }
})

const toggleDarkMode = () => {
  if (isDarkMode.value) {
    localStorage.theme = 'light';
    theme.value='light';
    isDarkMode.value = false;
  } else {
    localStorage.theme = 'dark';
    theme.value='dark';
    isDarkMode.value = true;
  }
}


</script>



