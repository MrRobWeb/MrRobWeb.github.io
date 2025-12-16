
<template>
    <div class="flex flex-col  sm:w-8/12 md:mx-auto animate-fade dark:text-white">
        <div
            class="flex flex-col overflow-hidden bg-white rounded shadow-md sm:flex-row text-slate-500 shadow-slate-200">
            <div class="flex-1 p-6 sm:mx-6 sm:px-0">
                <span class="flex gap-4 ">
                    <a href="#" class="relative inline-flex items-center justify-center w-12 h-12 text-white rounded-full">
                        <img src="../assets/imgs/IMG_7440_1.jpeg" alt="Robert Weber" title="Robert Weber" width="48"
                            height="48" loading="lazy" class="max-w-full rounded-full" />
                    </a>
                    <div>
                        <div class="text-xl font-medium  text-slate-700">HELLO</div>
                        <div class="text-sm font-medium  text-slate-400"> By Robert, July 16 2023</div>
                    </div>
                </span>
                <p>
                    Currently, working as Data Engineering Manager. I'm a passionate techchnology lead, who loves to design effective,
                    minimal and beautifull software products.

                </p>
                <p class="font-bold">
                    <q >
                        Learning never exhaust the mind.
                    </q>
                    - Leonardo da Vinci
                </p>
                <p>
                    Started my academic education in applied quantum physics and careerwise, moved into IT consulting {{ workAge }} ago, have worked as
                    devops engineer, data architect, data engineer, trainer, project manager, fullstack developer and pre-sales consultant
                    in several industries, for instance, in
                    energy, HR, automotive, aviation, retail and pharmarceutical industry.
                </p>
                <RouterLink to="/about" @click="scrollToTechStack" class="contact border-4 hover:border-blue-950 rounded">
                    TECHNOLOGY STACK
                </RouterLink>

                <RouterLink to="/project" class="contact border-4 hover:border-blue-950 rounded">
                    PROJECTS
                </RouterLink>
                <p>
                    You can find all detailed information about my work and educational background on my Linkedin profile. Feel free to drop me a message or reach out to me directly through Linkedin.
                </p>

                <RouterLink to="/contact" class="contact border-4 hover:border-blue-950 rounded">
                    CONTACT ME
                </RouterLink>
            </div>
        </div>
        <h1 ref="tech_stack" id="tech-stack" class="mt-8 mb-4 text-left text-3xl sm:text-4xl uppercase font-bold dark:text-white animate-fade">Technology
            Stack</h1>
        <TransitionGroup tag="ul" name="fade" aria-label="Technology stack categories" role="feed"
            class="relative flex flex-col gap-12 py-12 pl-8 before:absolute before:top-0 before:left-8 before:h-full before:border before:-translate-x-1/2 before:border-slate-200 before:border-dashed after:absolute after:top-6 after:left-8 after:bottom-6 after:border after:-translate-x-1/2 after:border-slate-200 ">
            <li :ref="setItemRef" v-for="(toolStack, index) in toolStacks" :key="toolStack.title" :data-index="index"
                @click="toggleShow(index)" role="article" class="relative pl-8 cursor-pointer"
                :aria-expanded="show === index"
            >
                <button
                    class="absolute left-0 z-10 flex items-center justify-center w-10 h-10 -translate-x-1/2 rounded-full text-slate-700 ring-2 ring-white bg-slate-200 "
                    :aria-label="`Toggle ${toolStack.title} details`">
                    <font-awesome-icon :icon="toolStack.icon" />
                </button>
                <div class="flex flex-col flex-1 gap-0">
                    <h4 class="text-base font-medium "> {{ toolStack.title }}</h4><p class="text-sm text-slate-500">{{ toolStack.subTitle }}</p>
                    <p v-if="show != index" class="self-start animate-pulse text-sm text-black border border-orange-700 dark:text-white rounded">click - to get more details</p>

                    <p v-if="show == index" class="text-block">
                        {{ getDescription(toolStack, index) }}
                        <SkillChart :index="index" :skills="toolStack.skills">

                        </SkillChart>
                    </p>
                </div>
            </li>
        </TransitionGroup>
    </div>
</template>


<script setup>
import { ref, onMounted, computed } from 'vue'
import { storeToRefs } from 'pinia'
import SkillChart from '../components/SkillChart.vue';
import { useAppStore } from '../stores/appStore.js'
import { toolStacks as skillsData } from '../data/skills.js'

const { heightHeader, workAge } = storeToRefs(useAppStore());

const toolStacks = ref(skillsData);

const itemRefs = ref([])
const setItemRef = (el) => {
    if (el) {
    itemRefs.value.push(el);
    }
}

onMounted(() => {
    window.scrollTo({
    top: 0
  })
})

const tech_stack = ref(null);

const scrollToTechStack = () => {

    setTimeout(function(){
        scrollIntoViewWithOffset(tech_stack.value, heightHeader.value)

    }, 200);
}

const scrollIntoViewWithOffset = (el, offset) => {
  window.scrollTo({
    behavior: 'smooth',
    top:
        el.getBoundingClientRect().top -
        document.body.getBoundingClientRect().top -
        offset-30,
  })
}

const getDescription = (toolStack, index) => {
    if (index === 1) {
        return `Being a data magician in the first place, I've been working in this area since finishing my studies ${workAge.value} ago.`;
    }
    return toolStack.description;
}

const show = ref(-1);

const toggleShow = (index) => {
    if (show.value == index) {
        show.value = -1;
    } else {
        show.value = index;
    }
    setTimeout(function(){
        scrollIntoViewWithOffset(itemRefs.value[index], heightHeader.value)

    }, 500);


}

</script>
<style>
/* 1. declare transition */
.fade-move,
.fade-enter-active,
.fade-leave-active {
    transition: all 0.5s cubic-bezier(0.55, 0, 0.1, 1);
}

/* 2. declare enter from and leave to state */
.fade-enter-from,
.fade-leave-to {
    opacity: 0;
    transform: scaleY(0.01) translate(30px, 0);
}

/* 3. ensure leaving items are taken out of layout flow so that moving
      animations can be calculated correctly. */
.fade-leave-active {
    position: absolute;
}</style>
