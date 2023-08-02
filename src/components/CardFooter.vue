<template>
    <div class="">
        <hr class="border-1 my-8 border-gray-400 sm:w-8/12 mx-auto">
        <div class="text-center my-4 dark:text-white flex items-center justify-center">
            Data Engineering Manager at ... 
        </div>
        
        <div class="text-center">
            <a @click="showModal = true" id="show-modal" class="m-1 p-1 text-gray-600 text-2xl hover:text-blue-600 dark:text-gray-400"> 
                <font-awesome-icon icon="fa-solid fa-envelope" />
            </a>
            <Teleport to="body">
                <modal :show="showModal" @close="showModal = false">
                <template #header>
                    <h3>Drop me a message:</h3>
                </template>
                </modal>
            </Teleport>
            <a href="https://www.linkedin.com/in/robert-w-300922158/" target="_blank" class="m-1 p-1 text-gray-600 text-2xl hover:text-blue-600 dark:text-gray-400">
                <font-awesome-icon icon="fa-brands fa-linkedin" />
            </a>
            <a href="https://github.com/MrRobWeb" target="_blank" class="m-1 p-1 text-gray-600 text-2xl hover:text-blue-600 dark:text-gray-400"> 
                <font-awesome-icon icon="fa-brands fa-github" />
            </a>
        </div>
        <div class="text-center my-4 dark:text-white flex items-center justify-center">

            <RouterLink to="/privacyPolicy">
                Privacy Policy
            </RouterLink>
        </div>
    </div>
</template>
<script setup>

import {ref} from 'vue'
import Modal from '../components/Modal.vue'

const showModal = ref(false)
</script>