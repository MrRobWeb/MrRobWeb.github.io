<template>
    <div class="flex my-10 justify-center sm:w-8/12 mx-auto animate-fade">
        <div class="flex flex-col mb-auto ">
            
            <h1 class="mt-8 mb-4 text-center text-3xl sm:text-4xl uppercase font-bold dark:text-white animate-fade">Contact me</h1>
            <transition-group 
                appear
                tag="ul"
                @before-enter="beforeEnter"
                @enter="enter"
                class="grid grid-cols-2 gap-10 text-center ">
                <div v-for="(icon, index) in icons" :key="icon.name" :data-index="index">
                    <a v-if="icon.href"
                        :href="icon.href" target="_blank"
                        class="m-1 p-1 text-2xl hover:text-blue-600 ">
                        <div class="flex flex-col rounded-lg bg-white p-6 shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)]">
                            <font-awesome-icon :icon="icon.icon" />
                            <h5 class="my-1">{{ icon.name }}</h5>
                        </div>
                    </a>
                    <a v-else="icon.href"
                        @click="showModal = true" id="show-modal" 
                        target="_blank"
                        class="m-1 p-1 text-2xl hover:text-blue-600 ">
                        <div class="flex flex-col rounded-lg bg-white p-6 shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)]">
                            <font-awesome-icon :icon="icon.icon" />
                            <h5 class="my-1">{{ icon.name }}</h5>
                        </div>
                    </a>
                    <Teleport to="body">
                        <modal :show="showModal" @close="showModal = false">
                        <template #header>
                            <h3>Drop me a message:</h3>
                        </template>
                        </modal>
                    </Teleport>

                </div>
            </transition-group>
        </div>
    </div>
</template>

<script setup> 

import { text } from '@fortawesome/fontawesome-svg-core';
import {ref, onMounted} from 'vue'
import gsap from 'gsap'
import Modal from '../components/Modal.vue'

onMounted(() => {
    window.scrollTo({
    top: 0
  })
})

const showModal = ref(false)
const icons = ref([
    {name: 'Message', icon: 'fa-solid fa-envelope'},
    {name: 'linkedin', icon: 'fa-brands fa-linkedin', href: 'https://www.linkedin.com/in/robert-w-300922158/'},
    {name: 'github', icon: 'fa-brands fa-github', href: 'https://github.com/MrRobWeb'},
    {name: 'gitlab', icon: 'fa-brands fa-gitlab', href: 'https://www.linkedin.com/in/robert-w-300922158/'},
])

const beforeEnter = (el) => {
    el.style.opacity = 0;
    el.style.transform = 'translateY(100px)'

}

const enter = (el,done) => {
    gsap.to(el,{
        opacity: 1,
        y: 0,
        duration: 0.8,
        onComplete: done,
        delay: el.dataset.index * 0.2
    })
    
}
</script>