
<template>
    <!-- Component: Activity feed -->

    <div class="flex flex-col  sm:w-8/12 md:mx-auto animate-fade dark:text-white">
        <!-- Component: Horizontal card-->
        <div
            class="flex flex-col overflow-hidden bg-white rounded shadow-md sm:flex-row text-slate-500 shadow-slate-200">
            <!-- Image
            <figure class="flex-1">
                <img src="https://picsum.photos/id/118/800/600" alt="card image"
                    class="object-cover min-h-full aspect-auto" />
            </figure> -->
            <!-- Body-->
            <div class="flex-1 p-6 sm:mx-6 sm:px-0">
                <span class="flex gap-4 ">
                    <a href="#" class="relative inline-flex items-center justify-center w-12 h-12 text-white rounded-full">
                        <img src="../assets/imgs/1523715750245.jpeg" alt="user name" title="user name" width="48"
                            height="48" class="max-w-full rounded-full" />
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
                    You can find all detailed information about work and education background on my Linkedin profile. Also you can drop me a message or reach out to me at Linkedin. 
                </p>

                <RouterLink to="/contact" class="contact border-4 hover:border-blue-950 rounded">
                    CONTACT ME
                </RouterLink>
            </div>
        </div>
        <!-- End Horizontal card-->
        <h1 ref="tech_stack" class="mt-8 mb-4 text-left text-3xl sm:text-4xl uppercase font-bold dark:text-white animate-fade"  >Technology
            Stack</h1>
        <TransitionGroup tag="ul" name="fade" aria-label="Activity feed" role="feed"
            class="relative flex flex-col gap-12 py-12 pl-8 before:absolute before:top-0 before:left-8 before:h-full before:border before:-translate-x-1/2 before:border-slate-200 before:border-dashed after:absolute after:top-6 after:left-8 after:bottom-6 after:border after:-translate-x-1/2 after:border-slate-200 ">
            <li :ref="setItemRef" v-for="(toolStack, index) in toolStacks" :key="toolStack.title" :data-index="index"
                @click="toggleShow(index)" role="article" class="relative pl-8 "
            >
                <button
                    class="absolute left-0 z-10 flex items-center justify-center w-10 h-10 -translate-x-1/2 rounded-full text-slate-700 ring-2 ring-white bg-slate-200 ">
                    <font-awesome-icon :icon="toolStack.icon" />
                </button>
                <div class="flex flex-col flex-1 gap-0">
                    <h4 class="text-base font-medium "> {{ toolStack.title }}</h4><p class="text-sm text-slate-500">{{ toolStack.subTitle }}</p>
                    <p v-if="show != index" class="self-start animate-pulse text-sm text-black border border-orange-700 dark:text-white rounded">click - to get more details</p>
                    
                    <p v-if="show == index" class="text-block">
                        {{ toolStack.description }}
                        <SkillChart :index="index" :skills="toolStack.skills">

                        </SkillChart>


                    </p>
                </div>
            </li>
        </TransitionGroup>
    </div>
</template>


<script setup>
import { ref, onActivated, onUpdated, onBeforeUpdate, onMounted } from 'vue'
import {storeToRefs} from 'pinia'
import SkillChart from '../components/SkillChart.vue';
import { useAppStore } from '../stores/appStore.js'

const {heightHeader, workAge} = storeToRefs(useAppStore());
// refs for scrolling
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
const toolStacks = ref([
    {
        title: 'Data Engineering | Data Analytics | Machine Learning',
        subTitle: 'The art of getting insights from data.',
        icon: 'fa-solid fa-chart-column',
        description:    `Being a data magician in the first place, I've been working in this area since finishing my studies ${workAge.value} ago.
                        `,
        skills: {
            programmingLanguages: {
                description: `In the data world, programming languages are your hammer and chissel to form your data. For this reason these skills are essential:`,
                values:
                    [
                        {
                            name: 'Python',
                            skillValue: '0.95'
                        },
                        {
                            name: 'SQL',
                            skillValue: '0.95'
                        },
                        {
                            name: 'Scala',
                            skillValue: '0.5'
                        },
                        {
                            name: 'Qlik ETL',
                            skillValue: '0.98'
                        },
                        {
                            name: 'Java',
                            skillValue: '0.7'
                        },
                        {
                            name: 'SAP ABAB',
                            skillValue: '0.6'
                        }
                    ]
            },
            frameworks: {
                description: `I've been working with the following tools and frameworks:`,
                values:
                    [
                        {
                            name: 'Spark | AWS Glue',
                            skillValue: '0.9'
                        },
                        {
                            name: 'Presto | AWS Athena',
                            skillValue: '0.95'
                        },
                        {
                            name: 'Kafka',
                            skillValue: '0.5'
                        },
                        {
                            name: 'Qlik',
                            skillValue: '0.95'
                        },
                        {
                            name: 'Power BI',
                            skillValue: '0.9'
                        },
                    ]
            },
            libraries: {
                description: `These are noteworthy libraries:`,
                values:
                    [
                        {
                            name: 'Pandas',
                            skillValue: '0.95'
                        },
                        {
                            name: 'scikit-learn',
                            skillValue: '0.65'
                        },
                        {
                            name: 'tensorflow',
                            skillValue: '0.4'
                        },
                        {
                            name: 'boto3',
                            skillValue: '0.95'
                        },
                        {
                            name: 'awswrangler',
                            skillValue: '0.95'
                        }
                    ]
            },
        },

    },
    {
        title: 'Frontend',
        subTitle: 'Generate user friendly interaction between human and machines.',
        icon: 'fa-solid fa-image',
        description: `Creating a user friendly UI in data analytics is key. Foremost, it's important that every user interpretates the depicted data in the same way. Nothing is worse then creating discussion in the analytics world.`,
        skills: {
            programmingLanguages: {
                description: `Programming languages I've been using:`,
                values:
                    [
                        {
                            name: 'Javascript',
                            skillValue: '0.93'
                        },
                        {
                            name: 'Typescript',
                            skillValue: '0.9'
                        },
                        {
                            name: 'Dart',
                            skillValue: '0.5'
                        },
                        {
                            name: 'HTML',
                            skillValue: '0.75'
                        },
                        {
                            name: 'CSS',
                            skillValue: '0.7'
                        }
                    ]
            },
            frameworks: {
                description: `Even, my favourite frontend setup consists of Vue 3, Tailwind CSS created with Vite and Pinia as statemanagement library, I took a plunge into several other frameworks and libraries:`,
                values:
                    [
                        {
                            name: 'Vue.js',
                            skillValue: '0.95'
                        },
                        {
                            name: 'Vite',
                            skillValue: '0.8'
                        },
                        {
                            name: 'Angular',
                            skillValue: '0.4'
                        },
                        {
                            name: 'Flutter',
                            skillValue: '0.5'
                        },
                        {
                            name: 'Tailwind CSS',
                            skillValue: '0.9'
                        }
                    ]
            },
            libraries: {
                description: `Noteworthy libraries:`,
                values:
                    [
                        {
                            name: 'Babylon JS',
                            skillValue: '0.75'
                        },
                        {
                            name: 'React',
                            skillValue: '0.65'
                        },
                        {
                            name: 'Chart JS',
                            skillValue: '0.8'
                        },
                        {
                            name: 'Pinia',
                            skillValue: '0.9'
                        },
                        {
                            name: 'aws-sdk',
                            skillValue: '0.7'
                        },
                        {
                            name: 'webpack',
                            skillValue: '0.7'
                        },
                        {
                            name: '.env',
                            skillValue: '0.9'
                        }
                    ]
            },
        },
    },
    {
        title: 'Backend',
        subTitle: 'The fundament of every great application.',
        icon: 'fa-solid fa-server',
        description: `My experience regarding backend technologies is quite ok. I've been working on building REST APIs using Node.js, Flask/Django and Spring. Nevertheless, I am not a backend expert.`,
        skills: {
            programmingLanguages: {
                description: `Programming languages:`,
                values:

                    [
                        {
                            name: 'Python',
                            skillValue: '0.94'
                        },
                        {
                            name: 'Javascript',
                            skillValue: '0.93'
                        },
                        {
                            name: 'Java|Maven',
                            skillValue: '0.6'
                        },
                    ]
            },
            frameworks: {
                description: `Frameworks I took a plunge into:`,
                values:
                    [
                        {
                            name: 'Node',
                            skillValue: '0.85'
                        },
                        {
                            name: 'Flask',
                            skillValue: '0.5'
                        },
                        {
                            name: 'Django',
                            skillValue: '0.5'
                        },
                        {
                            name: 'Spring | Spring Boot',
                            skillValue: '0.5'
                        }
                    ]
            },
            libraries: {
                description: `Noteworthy tools & libraries:`,
                values:
                    [
                        {
                            name: 'Express JS',
                            skillValue: '0.8'
                        },
                        {
                            name: 'Postman',
                            skillValue: '0.7'
                        },
                    ]
            },
        },
    },
    {
        title: 'DevOps',
        subTitle: 'The philosophy to automate the integration of great devolopment work into operation.',
        icon: 'fa-solid fa-gears',
        description: `In my opinion DevOps is not about coding, It's about knowing your business & IT operation, defining a release and update process and then building the analogue CI/CD structure as well as version management, which fits your needs.`,
        skills: {
            programmingLanguages: {
                description: `Essential tools & programming languages:`,
                values:

                    [
                        {
                            name: 'Python',
                            skillValue: '0.94'
                        },
                        {
                            name: 'Javascript',
                            skillValue: '0.93'
                        },
                        {
                            name: 'Git',
                            skillValue: '0.9'
                        },
                        {
                            name: 'Bash | Shell',
                            skillValue: '0.9'
                        },
                        {
                            name: 'Docker',
                            skillValue: '0.8'
                        },
                        {
                            name: 'Docker Compose',
                            skillValue: '0.7'
                        },
                        {
                            name: 'Kubernetes',
                            skillValue: '0.3'
                        },
                    ]
            },
            frameworks: {
                description: `Cloud Environments:`,
                values:
                    [
                        {
                            name: 'AWS - Codepipeline | Codebuild | Codecommit',
                            skillValue: '0.95'
                        },
                        {
                            name: 'Azure DevOps',
                            skillValue: '0.6'
                        },
                    ]
            },
            libraries: {
                description: `Additional tools and knwowledge:`,
                values:
                    [
                        {
                            name: 'Linux',
                            skillValue: '0.9'
                        },
                        {
                            name: 'Node.js',
                            skillValue: '0.85'
                        },
                        {
                            name: 'Networks',
                            skillValue: '0.85'
                        },
                        {
                            name: 'Postman',
                            skillValue: '0.7'
                        },
                        {
                            name: 'IAM management',
                            skillValue: '0.95'
                        },
                    ]
            },
        },
    },
])


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