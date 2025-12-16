<template>
    <div class="flex sm:w-8/12 xs:w-full mx-auto animate-fade">
        <div class="flex xs:w-full flex-col mb-auto ">
            <div class="divide-y divide-gray-200 dark:divide-gray-700">
                <div class="space-y-2 md:space-y-5">
                    <h1
                        class="text-3xl font-extrabold leading-9 tracking-tight text-gray-900 dark:text-gray-100 sm:text-4xl sm:leading-10 md:text-6xl md:leading-14">
                        Projects
                    </h1>
                    <p class="text-lg leading-7 text-gray-500 dark:text-gray-400">
                        This is an exerpt of project types I've managed in differnt roles, during my work life:
                    </p>
                    <p class="text-lg leading-7 text-gray-500 dark:text-gray-400">
                        If you've questions, feel free to leave a message:
                        <button @click="showModal = true" id="show-modal"
                            class="m-1 p-1 text-gray-600 text-2xl hover:text-blue-600 dark:text-gray-400"
                            aria-label="Open contact form">
                            <font-awesome-icon icon="fa-solid fa-envelope" />
                        </button>
                        <Teleport to="body">
                            <modal :show="showModal" @close="showModal = false">
                                <template #header>
                                    <h3>Drop me a message:</h3>
                                </template>
                            </modal>
                        </Teleport>
                    </p>
                </div>
                <transition-group
                    appear
                    tag="ul"
                    :name="isAppeared ? 'fade' : ''"
                    @before-enter="beforeEnter"
                    @enter="enter"
                    class="divide-y divide-gray-200 dark:divide-gray-700 sm:w-8/12"
                    aria-label="Project list">
                    <li v-for="(project, index) in projects" :key="project.title" :data-index="index" class="py-12">
                        <article>
                            <div class="space-y-2 xl:grid xl:grid-cols-4 xl:items-baseline xl:space-y-0">
                                <dl>
                                    <dt class="sr-only">Role and date</dt>
                                    <dd class="text-base font-medium leading-6 dark:text-white">{{ project.role }} </dd>
                                    <dd class="text-base font-medium leading-6 text-gray-500 dark:text-gray-400">{{
                                        project.date }} </dd>
                                    <dd class="text-xs font-small italic leading-6 text-gray-500 dark:text-gray-400">{{
                                        project.industry }} </dd>
                                </dl>
                                <div class="space-y-5 xl:col-span-3">
                                    <div class="space-y-6">
                                        <div>
                                            <h2 :ref="setItemRef" class="text-2xl font-bold leading-8 tracking-tight"><a
                                                    class="text-gray-900 dark:text-white">{{ project.title }}</a></h2>
                                            <div class="flex flex-wrap ">
                                                <span class="mr-3 text-sm font-medium  text-primary-500 dark:text-white hover:text-primary-600 dark:hover:text-primary-400"
                                                    v-for="technology in project.technologies" :key="technology">
                                                    {{ technology }}
                                                </span>
                                            </div>
                                        </div>
                                        <div v-if="show != index" class="text-gray-500 dark:text-gray-400">
                                            {{ project.description.substring(0, 90) }} ...
                                        </div>
                                        <div v-if="show == index" class=" text-gray-500 dark:text-gray-400">
                                            {{ project.description }}
                                        </div>
                                    </div>
                                    <div class="text-base font-medium leading-6  dark:text-white">
                                        <button v-if="show != index"
                                            class="text-primary-500 hover:text-primary-600 dark:hover:text-primary-400"
                                            :aria-label="`Read more about ${project.title}`" @click="toggleShow(index)">
                                            Read more
                                        </button>

                                        <button v-if="show == index"
                                            class="text-primary-500 hover:text-primary-600 dark:hover:text-primary-400"
                                            :aria-label="`Read less about ${project.title}`" @click="toggleShow(index)">
                                            Read less
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </article>
                    </li>
                </transition-group>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref, onMounted } from 'vue';
import Modal from '../components/Modal.vue'
import gsap from 'gsap'
import { projects as projectsData } from '../data/projects.js'

onMounted(() => {
    window.scrollTo({
        top: 0
    })
})

const isAppeared = ref(false);
const projects = ref(projectsData);

const itemRefs = ref([])
const setItemRef = (el) => {
    if (el) {
        itemRefs.value.push(el);
    }
}

const show = ref(-1);
const showModal = ref(false)
const toggleShow = (index) => {
    if (show.value == index) {
        show.value = -1;
    } else {
        show.value = index;
    }
}

const beforeEnter = (el) => {
    if (isAppeared.value) return;
    el.style.opacity = 0;
    el.style.transform = 'translateX(100px)'
}

const enter = (el, done) => {
    if (isAppeared.value) {
        done();
        return;
    }
    const duration = 0.8;
    const delay = el.dataset.index * 0.2;
    gsap.to(el, {
        opacity: 1,
        x: 0,
        duration: duration,
        onComplete: done,
        delay: delay
    })

    setTimeout(function () {
        if (Number(el.dataset.index) + 1 === projects.value.length) {
            isAppeared.value = true;
        }
    }, (duration + delay) * 1000)
}
</script>
