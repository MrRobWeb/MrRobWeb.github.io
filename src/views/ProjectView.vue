<template>
    <div class="flex sm:w-8/12 mx-auto animate-fade">
        <div class="flex flex-col mb-auto ">
            <div class="divide-y divide-gray-200 dark:divide-gray-700">
                <div class="space-y-2 md:space-y-5">
                    <div
                        class="text-3xl font-extrabold leading-9 tracking-tight text-gray-900 dark:text-gray-100 sm:text-4xl sm:leading-10 md:text-6xl md:leading-14">
                        Projects
                    </div>
                    <p class="text-lg leading-7 text-gray-500 dark:text-gray-400">
                        This is an exerpt of project types I've managed in differnt roles, during my work life:
                        <!-- as data
                        engineer, data architect, frontend engineer, lead consultant, trainer and DevOps engineer. -->

                    </p>
                    <p class="text-lg leading-7 text-gray-500 dark:text-gray-400">
                        If you've questions, feel free to leave a message: →
                        <button @click="showModal = true" id="show-modal"
                            class="m-1 p-1 text-gray-600 text-2xl hover:text-blue-600 dark:text-gray-400">
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
                <transition-group v-if="!isAppeared" appear tag="ul" @before-enter="beforeEnter" @enter="enter"
                    class="divide-y divide-gray-200 dark:divide-gray-700">
                    <li v-for="(project, index) in projects" :key="project.title" :data-index="index" class="py-12">
                        <article>
                            <div class="space-y-2 xl:grid xl:grid-cols-4 xl:items-baseline xl:space-y-0">
                                <dl>
                                    <dt class="sr-only">Published on</dt>
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
                                                <a class="mr-3 text-sm font-medium  text-primary-500 dark:text-white hover:text-primary-600 dark:hover:text-primary-400"
                                                    v-for="technology in project.technologies">
                                                    {{ technology }}
                                                </a>
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
                                            aria-label="Read &quot;New features in v1&quot;" @click="toggleShow(index)">
                                            Read more →
                                        </button>

                                        <button v-if="show == index"
                                            class="text-primary-500 hover:text-primary-600 dark:hover:text-primary-400"
                                            aria-label="Read &quot;New features in v1&quot;" @click="toggleShow(index)">
                                            Read less →
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </article>
                    </li>
                </transition-group>

                <transition-group v-if="isAppeared" name="fade" tag="ul"
                    class="divide-y divide-gray-200 dark:divide-gray-700">
                    <li v-for="(project, index) in projects" :key="project.title" :data-index="index" class="py-12">
                        <article>
                            <div class="space-y-2 xl:grid xl:grid-cols-4 xl:items-baseline xl:space-y-0">
                                <dl>
                                    <dt class="sr-only">Published on</dt>
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
                                                <a class="mr-3 text-sm font-medium  text-primary-500 dark:text-white hover:text-primary-600 dark:hover:text-primary-400"
                                                    v-for="technology in project.technologies">
                                                    {{ technology }}
                                                </a>
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
                                            aria-label="Read &quot;New features in v1&quot;" @click="toggleShow(index)">
                                            Read more →
                                        </button>

                                        <button v-if="show == index"
                                            class="text-primary-500 hover:text-primary-600 dark:hover:text-primary-400"
                                            aria-label="Read &quot;New features in v1&quot;" @click="toggleShow(index)">
                                            Read less →
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
import { storeToRefs } from 'pinia'
import Loader from '../components/Loader.vue';
import { useAppStore } from '../stores/appStore.js'
import Modal from '../components/Modal.vue'
import gsap from 'gsap'

onMounted(() => {
    window.scrollTo({
        top: 0
    })
})

const isAppeared = ref(false);

const { heightHeader, workAge } = storeToRefs(useAppStore());
// refs for scrolling
const itemRefs = ref([])
const setItemRef = (el) => {
    if (el) {
        itemRefs.value.push(el);
    }
}
const scrollIntoViewWithOffset = (el, offset) => {
    window.scrollTo({
        behavior: 'smooth',
        top:
            el.getBoundingClientRect().top -
            document.body.getBoundingClientRect().top -
            offset - 30,
    })
}

const show = ref(-1);
const showModal = ref(false)
const toggleShow = (index) => {
    if (show.value == index) {
        show.value = -1;
    } else {
        show.value = index;
    }
    // setTimeout(function () {
    //     scrollIntoViewWithOffset(itemRefs.value[index], heightHeader.value)
    //     console.log('scroll')

    // }, 200);


}

const projects = ref([
    {
        title: 'CI/CD and version management implementation of dozens of data migration pipelines for more then 100 customers',
        role: 'DevOps Engineer',
        industry: 'Energy Services',
        technologies: ['Terraform', 'AWS Codebuild|Codepipeline|Codecommit', 'Git', 'CDK', 'AWS CloudFormation'],
        date: 'April 2022 - Today',
        description: `For a large vendor in the energy service sector a new billing platform will be introduced. 
        It is planned that dozens of public utility companies with even more legal entites will be onboarded to this new billing platform. 
        Therefore, a data migration from the legacy ERP system (SAP IS-U) to this billing platform needs to be conducted.
        To ensure data separation between legal entities during migration, I've developed a deployment and integration process using Terraform, Docker and AWS DevOps capabilites (Codebuild,Codepipeline,Codecommit, ECR). 
        Additionally, I've been working on a proper git branching strategy, which fits to the size of project regarding amount of developers and used release managent process. `
    },
    {
        title: 'Data pipelines architecture based on AWS resources',
        role: 'Data Architect | Data Engineer',
        industry: 'Energy Services',
        technologies: ['AWS Step Functions|State Machines|Activites', 'Spark|AWS Glue', 'Presto|AWS Athena', 'AWS Lambda', 'AWS - S3|SNS|CloudWatch|DynamoDB|EC2|Cloud9'],
        date: 'April 2022 - Today',
        description: `For a large vendor in the energy service sector a new billing platform will be introduced. 
        It is planned that dozens of public utility companies with even more legal entites will be onboarded to this new billing platform. 
        Therefore, a data migration from the legacy ERP system (SAP IS-U) to this billing platform needs to be conducted. 
        I am in charge to enhance and maintain a private framework, which is build up on Terraform and AWS Step Functions, and this, in turn, 
        consists of AWS Glue, -Athena jobs and Lambda Functions mainly.
        Besides, this framework is used to build a standardized set of data migration pipelines to prepare the data from the legacy system. 
        For this reason I am managing and guiding through trainings Offshore, Nearshore and Onsite coworkes.`,
    },
    {
        title: 'Design, developement and architecture of a progressive webapp to configure data pipelines',
        role: 'Frontend Engineer',
        industry: 'Energy Services',
        technologies: ['Vite', 'Vue3', 'Tailwind CSS', 'aws-sdk', 'AWS DynamoDB', 'AWS App Runner'],
        date: 'April 2022 - Today',
        description: `For a large vendor in the energy service sector a new billing platform will be introduced. 
        It is planned that dozens of public utility companies with even more legal entites will be onboarded to this new billing platform. 
        Therefore, a data migration from the legacy ERP system (SAP IS-U) to this billing platform needs to be conducted. It is planned to prepare
        highly scalable but standardized migration pipelines, which can be configured. Therefore, I am designing and developing a progressive webapp, which is running on AWS App Runner using my favourite
        frontend tech stack, which consists of Vite, Vue3 and Tailwind. AWS is used as Cloud environment. For this reason I leverage the capabilites of DynamoDB as configuration data storage service. Therfore, aws-sdk is used to develope the webapp. 
        the `,
    },
    {
        title: 'Developement & architecture of custom analytics webapps',
        role: 'Frontend Engineer | Lead Consultant',
        industry: 'Fincancial Services - Healthcare',
        technologies: ['Vite', 'Vue3', 'Tailwind CSS', 'Javascript', 'Qlik APIs', 'Power BI-REST-APIs'],
        date: 'January 2017 - March 2022',
        description: `As analytics expert and frontend engineer you can leverage the strengths of web programming and the analytics engines of leading BI vendors like Qlik and Power BI. Both offer
                        APIs to integrate already created analytics dashboard into customizable progressive web apps. This enables powerfull applications, where it is possible to design beautifull interactive dashboards with a unique analytics path for an astonishing end user experience.`
    },
    {
        title: 'Implementation of data analytics architecture for enterprise level reporting',
        role: 'Data Engineer | Lead Consultant',
        industry: 'Manufacturing - Automotive - Fincancial Services - Healthcare - Insurance - Public Services - Energy Services',
        technologies: ['Qlik', 'Microsoft SSAS & SSIS', 'PowerBI', 'AWS', 'Python'],
        date: 'September 2014 - March 2022',
        description: `During my time as Data Engineer | Lead Consultant I was in charge of a full IT analytics architecture integration of a new BI software into the current IT landscape of the customer.
                        This includes project management from the start as well as technical consulting such as the sizing of servers and installation of software,  data extraction and connectivity provisioning of the BI software to ERP systems such as SAP, Microsoft Dynamics,
                         and CRM systems like SalesForce. Usually, in colaboration with ERP & CRM consultants a data valuation was conducted and based on this data models, analytics reports and dashboards were designed - developed. 
                         Finally, a customized user administration process was implemented, which is especially important for highly sensitive data. `
    },
    {
        title: 'Trainings in data analytics and data engineering',
        role: 'Trainer',
        industry: 'Energy Services',
        technologies: ['Data Literacy', 'BI Design', 'Data Modelling', 'Data Transformation', 'Qlik Deep Dive'],
        date: 'September 2014 - March 2022',
        description: `As trainer I worked on the creation of several trainings in  data analytics and data engineering area.  
                        This includes teaching general designing concepts to create beautiful dashboards, data modelling fundamentals as well as general data literacy topics.
                        Additionally, I've designed deep dive trainings using advanced Qlik ETL techniques and Qlik Administration for a world wide audience.`
    },
])

const beforeEnter = (el) => {
    el.style.opacity = 0;
    el.style.transform = 'translateX(100px)'

}

const enter = (el, done) => {
    const duration = 0.8;
    const delay = el.dataset.index * 0.2;
    gsap.to(el, {
        opacity: 1,
        x: 0,
        duration: duration,
        onComplete: done,
        delay: delay
    })

    console.info('Appeared:', Number(el.dataset.index) + 1, 'of', projects.value.length)
    setTimeout(function () {
        if (Number(el.dataset.index) + 1 === projects.value.length) {
            isAppeared.value = true;
        }
    }, (duration + delay) * 1000)

}

</script>

