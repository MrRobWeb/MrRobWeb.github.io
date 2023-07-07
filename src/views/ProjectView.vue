<template>

<div class="flex my-10 justify-center sm:w-8/12 mx-auto animate-fade">
    <div class="flex flex-col mb-auto ">
        <div class="divide-y divide-gray-200 dark:divide-gray-700">
            <div class="space-y-2 pt-6 pb-8 md:space-y-5">
                <h1
                    class="text-3xl font-extrabold leading-9 tracking-tight text-gray-900 dark:text-gray-100 sm:text-4xl sm:leading-10 md:text-6xl md:leading-14">
                    Projects
                </h1>
                <p class="text-lg leading-7 text-gray-500 dark:text-gray-400">A blog created with Next.js and Tailwind.css
                </p>
            </div>
            <transition-group 
                appear
                tag="ul"
                @before-enter="beforeEnter"
                @enter="enter"
                class="divide-y divide-gray-200 dark:divide-gray-700">
                <li v-for="(icon, index) in icons" :key="icon.name" :data-index="index" class="py-12">
                    <article>
                        <div class="space-y-2 xl:grid xl:grid-cols-4 xl:items-baseline xl:space-y-0">
                            <dl>
                                <dt class="sr-only">Published on</dt>
                                <dd class="text-base font-medium leading-6 text-gray-500 dark:text-gray-400"><time
                                        datetime="2021-08-07T15:32:14.000Z">August 7, 2021</time></dd>
                            </dl>
                            <div class="space-y-5 xl:col-span-3">
                                <div class="space-y-6">
                                    <div>
                                        <h2 class="text-2xl font-bold leading-8 tracking-tight"><a
                                                class="text-gray-900 dark:text-gray-100" href="/blog/new-features-in-v1">New
                                                features in v1</a></h2>
                                    <div class="flex flex-wrap"><a
                                            class="mr-3 text-sm font-medium uppercase text-primary-500 hover:text-primary-600 dark:hover:text-primary-400"
                                            href="/tags/next-js">next-js</a><a
                                            class="mr-3 text-sm font-medium uppercase text-primary-500 hover:text-primary-600 dark:hover:text-primary-400"
                                            href="/tags/tailwind">tailwind</a><a
                                            class="mr-3 text-sm font-medium uppercase text-primary-500 hover:text-primary-600 dark:hover:text-primary-400"
                                            href="/tags/guide">guide</a></div>
                                </div>
                                <div class="prose max-w-none text-gray-500 dark:text-gray-400">An overview of the new
                                    features released in v1 - code block copy, multiple authors, frontmatter layout and
                                    more</div>
                            </div>
                            <div class="text-base font-medium leading-6"><a
                                    class="text-primary-500 hover:text-primary-600 dark:hover:text-primary-400"
                                    aria-label="Read &quot;New features in v1&quot;"
                                    href="/blog/new-features-in-v1">Read more →</a></div>
                            </div>
                        </div>
                    </article>
                </li>
            </transition-group >
        </div>
    </div>
</div>
</template>
<script setup>
import { ref, onMounted } from 'vue';
import Loader from '../components/Loader.vue';
import gsap from 'gsap'
const projects = ref([]);
const loading = ref(false);
const error = ref(null);

onMounted(async () => {
    try {
        loading.value = true;
        const res = await fetch('https://api.github.com/users/saileshrijal/repos');
        projects.value = await res.json();
        loading.value = false;
    } catch (ex) {
        error.value = ex;
        loading.value = false;
    }
});


const icons = ref([
    {name: 'E-mail', icon: 'fa-solid fa-envelope'},
    {name: 'linkedin', icon: 'fa-brands fa-linkedin'},
    {name: 'github', icon: 'fa-brands fa-github'},
    {name: 'gitlab', icon: 'fa-brands fa-gitlab'},
])

const beforeEnter = (el) => {
    el.style.opacity = 0;
    el.style.transform = 'translateX(100px)'

}

const enter = (el,done) => {
    gsap.to(el,{
        opacity: 1,
        x: 0,
        duration: 0.8,
        onComplete: done,
        delay: el.dataset.index * 0.2
    })
    
}

</script>