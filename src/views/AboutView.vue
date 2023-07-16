
<template>
    <!-- Component: Activity feed -->

    <div class="flex flex-col my-10  sm:w-8/12 mx-auto animate-fade dark:text-white">
        <!-- Component: Horizontal card-->
        <div
            class="flex flex-col my-5 overflow-hidden bg-white rounded shadow-md sm:flex-row text-slate-500 shadow-slate-200">
            <!-- Image
            <figure class="flex-1">
                <img src="https://picsum.photos/id/118/800/600" alt="card image"
                    class="object-cover min-h-full aspect-auto" />
            </figure> -->
            <!-- Body-->
            <div class="flex-1 p-6 sm:mx-6 sm:px-0">
                <header class="flex gap-4 mb-4">
                    <a href="#" class="relative inline-flex items-center justify-center w-12 h-12 text-white rounded-full">
                        <img src="../assets/imgs/1523715750245.jpeg" alt="user name" title="user name" width="48"
                            height="48" class="max-w-full rounded-full" />
                    </a>
                    <div>
                        <h3 class="text-xl font-medium text-slate-700">HELLO</h3>
                        <p class="text-sm text-slate-400"> By Robert, july 3 2023</p>
                    </div>
                </header>
                <p>
                    Welcome to my portfolio website. I'm a humble leader and a unicorn mix of business and tech, who loves to design effective, minimal and beautifull software products.
                  
                </p>
                <p class="font-bold">
                    <q >
                        Learning never exhaust the mind.
                    </q>
                    - Leonardo da Vinci
                </p>
                <p>
                    Started my academic education in Applied Quantum Physics and careerwise, moved into IT consulting 9 years ago, have worked as
                    data architect, software architect, technical trainer, pre-sales consultant
                    in several industries, for instance, in
                    energy, HR, automotive, aviation, retail and pharmarceutical industry.
                </p>
                <p>
                    You can find all detailed information about work and education background on my Linkedin.
                </p>

                <RouterLink to="/contact" class="contact border-4 hover:border-blue-950 rounded">
                    CONTACT ME
                </RouterLink>
            </div>
        </div>
        <!-- End Horizontal card-->
        <h1 class="mt-8 mb-4 text-left text-3xl sm:text-4xl uppercase font-bold dark:text-white animate-fade">Technology
            Stack</h1>
        <TransitionGroup tag="ul" name="fade" aria-label="Activity feed" role="feed"
            class="relative flex flex-col gap-12 py-12 pl-8 before:absolute before:top-0 before:left-8 before:h-full before:border before:-translate-x-1/2 before:border-slate-200 before:border-dashed after:absolute after:top-6 after:left-8 after:bottom-6 after:border after:-translate-x-1/2 after:border-slate-200 ">
            <li v-for="(toolStack, index) in toolStacks" :key="toolStack.header" :data-index="index"
                @click="toggleShow(index)" role="article" class="relative pl-8 ">
                <button
                    class="absolute left-0 z-10 flex items-center justify-center w-10 h-10 -translate-x-1/2 rounded-full text-slate-700 ring-2 ring-white bg-slate-200 ">
                    <font-awesome-icon :icon="toolStack.icon" />
                </button>
                <div class="flex flex-col flex-1 gap-0">
                    <h4 class="text-base font-medium "> {{ toolStack.header }}</h4>
                    <p v-if="show != index" class="self-start animate-pulse text-sm text-black border border-orange-700 dark:text-white rounded">click to get more details</p>
                    <p v-if="show == index" class="text-sm text-slate-500">Tools for ...</p>
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
import { ref, onActivated, onUpdated, onUnmounted, onMounted } from 'vue'
import SkillChart from '../components/SkillChart.vue';
const toolStacks = ref([
    {
        header: 'Data Engineering | Data Analytics | Machine Learning',
        icon: 'fa-solid fa-chart-column',
        description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea 
                takimata sanctus est Lorem ipsum dolor sit amet.`,
        skills: {
            programmingLanguages: {
                description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua.`,
                values:
                    [
                        {
                            name: 'Python',
                            skillValue: '0.9'
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
                        }
                    ]
            },
            frameworks: {
                description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua.`,
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
                            name: 'Scala',
                            skillValue: '0.5'
                        }
                    ]
            },
            libraries: {
                description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua.`,
                values:
                    [
                        {
                            name: 'Pandas',
                            skillValue: '0.9'
                        },
                        {
                            name: 'scikit-learn',
                            skillValue: '0.65'
                        },
                        {
                            name: 'tensorflow',
                            skillValue: '0.65'
                        },
                        {
                            name: 'boto3',
                            skillValue: '0.9'
                        },
                        {
                            name: 'awswrangler',
                            skillValue: '0.9'
                        }
                    ]
            },
        },

    },
    {
        header: 'Frontend',
        icon: 'fa-solid fa-image',
        description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea 
                takimata sanctus est Lorem ipsum dolor sit amet.`,
        skills: {
            programmingLanguages: {
                description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua.`,
                values:
                    [
                        {
                            name: 'Javscript',
                            skillValue: '0.93'
                        },
                        {
                            name: 'Typescript',
                            skillValue: '0.85'
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
                description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua.`,
                values:
                    [
                        {
                            name: 'Vue.js',
                            skillValue: '0.9'
                        },
                        {
                            name: 'React',
                            skillValue: '0.75'
                        },
                        {
                            name: 'Angular',
                            skillValue: '0.4'
                        }
                    ]
            },
            libraries: {
                description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua.`,
                values:
                    [
                        {
                            name: 'Pandas',
                            skillValue: '0.9'
                        },
                        {
                            name: 'scikit-learn',
                            skillValue: '0.65'
                        },
                        {
                            name: 'tensorflow',
                            skillValue: '0.65'
                        },
                        {
                            name: 'boto3',
                            skillValue: '0.9'
                        },
                        {
                            name: 'awswrangler',
                            skillValue: '0.9'
                        }
                    ]
            },
        },
    },
    {
        header: 'Backend',
        icon: 'fa-solid fa-server',
        description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea 
                takimata sanctus est Lorem ipsum dolor sit amet.`,
        skills: {
            programmingLanguages: {
                description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua.`,
                values:

                    [
                        {
                            name: 'Python',
                            skillValue: '0.9'
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
                        }
                    ]
            },
            frameworks: {
                description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua.`,
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
                            name: 'Scala',
                            skillValue: '0.5'
                        }
                    ]
            },
            libraries: {
                description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua.`,
                values:
                    [
                        {
                            name: 'Pandas',
                            skillValue: '0.9'
                        },
                        {
                            name: 'scikit-learn',
                            skillValue: '0.65'
                        },
                        {
                            name: 'tensorflow',
                            skillValue: '0.65'
                        },
                        {
                            name: 'boto3',
                            skillValue: '0.9'
                        },
                        {
                            name: 'awswrangler',
                            skillValue: '0.9'
                        }
                    ]
            },
        },
    },
    {
        header: 'DevOps',
        icon: 'fa-solid fa-gears',
        description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea 
                takimata sanctus est Lorem ipsum dolor sit amet.`,
        skills: {
            programmingLanguages: {
                description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua.`,
                values:

                    [
                        {
                            name: 'Python',
                            skillValue: '0.9'
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
                        }
                    ]
            },
            frameworks: {
                description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua.`,
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
                            name: 'Scala',
                            skillValue: '0.5'
                        }
                    ]
            },
            libraries: {
                description: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua.`,
                values:
                    [
                        {
                            name: 'Pandas',
                            skillValue: '0.9'
                        },
                        {
                            name: 'scikit-learn',
                            skillValue: '0.65'
                        },
                        {
                            name: 'tensorflow',
                            skillValue: '0.65'
                        },
                        {
                            name: 'boto3',
                            skillValue: '0.9'
                        },
                        {
                            name: 'awswrangler',
                            skillValue: '0.9'
                        }
                    ]
            },
        },
    },
])

const show = ref(-1);


const ctx = ref(null);

const toggleShow = (index) => {
    if (show.value == index) {
        show.value = -1;
    } else {
        show.value = index
    }

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