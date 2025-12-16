<template>
  <div class="page-with-sidebar">
    <!-- Vertical Navigation -->
    <nav class="vertical-nav">
      <div class="nav-inner">
        <!-- Connecting Line -->
        <div class="nav-line"></div>

        <button
          v-for="(section, index) in sections"
          :key="section.id"
          @click="scrollToSection(section.id)"
          :class="['nav-item', 'group', { active: activeSection === section.id }]"
        >
          <span class="nav-number">{{ String(index + 1).padStart(2, '0') }}</span>
          <span class="nav-label">{{ section.label }}</span>
        </button>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="main-content">
      <!-- Section 1: About -->
      <section id="about" ref="aboutRef" class="content-section">
        <div class="section-inner">
          <div class="max-w-3xl">
            <div class="flex items-start gap-6 mb-8">
              <img
                src="../assets/imgs/IMG_7440_1.jpeg"
                alt="Robert Weber"
                class="w-20 h-20 md:w-24 md:h-24 rounded-full flex-shrink-0"
              >
              <div>
                <h1 class="text-heading-1 text-mckinsey-navy dark:text-white mb-2">Robert Weber</h1>
                <p class="text-body-lg text-corporate-mid-gray">Data Engineering Manager</p>
              </div>
            </div>

            <div class="space-y-6">
              <p class="text-body-lg text-corporate-dark-gray dark:text-corporate-light-gray">
                Data Engineering Manager with expertise in agentic AI, cloud architecture, data platform development,
                and engineering team leadership. Delivering scalable solutions that transform how
                organizations leverage data for strategic decision-making.
              </p>

              <blockquote class="border-l-4 border-mckinsey-teal pl-6 my-8 italic text-corporate-mid-gray">
                "Learning never exhausts the mind." — Leonardo da Vinci
              </blockquote>

              <p class="text-body text-corporate-dark-gray dark:text-corporate-light-gray">
                {{ workAge }} of consulting experience following an academic foundation in applied quantum physics.
                Core competencies include DevOps engineering, enterprise data architecture, project delivery,
                and fullstack development. Industry expertise spans energy, human resources, automotive,
                aviation, retail, and pharmaceutical sectors.
              </p>
            </div>

            <!-- Quick Links -->
            <div class="flex flex-wrap gap-4 mt-8">
              <button @click="scrollToSection('expertise')" class="btn-secondary text-sm">
                Functional Expertise
              </button>
              <button @click="scrollToSection('projects')" class="btn-secondary text-sm">
                View Projects
              </button>
              <RouterLink to="/contact" class="btn-primary text-sm">
                Contact Me
              </RouterLink>
            </div>
          </div>
        </div>
      </section>

      <!-- Section 2: Functional Expertise -->
      <section id="expertise" ref="expertiseRef" class="content-section bg-corporate-off-white dark:bg-mckinsey-navy">
        <div class="section-inner">
          <div class="max-w-5xl">
            <h2 class="text-heading-1 text-mckinsey-navy dark:text-white mb-8">
              Functional Expertise
            </h2>

            <!-- McKinsey Slide Deck -->
            <div class="mckinsey-slide">
              <!-- Navy Header Bar -->
              <div class="slide-header-bar">
                <div class="header-content">
                  <span class="header-label">Core Capabilities</span>
                  <h3 class="header-title">{{ expertiseAreas[currentSlide].title }}</h3>
                </div>
                <span class="slide-number">{{ currentSlide + 1 }}</span>
              </div>

              <!-- White Content Area -->
              <div class="slide-body">
                <Transition name="slide" mode="out-in">
                  <div :key="currentSlide" class="slide-content-wrapper">
                    <!-- Left Column: Key Message -->
                    <div class="slide-main">
                      <div class="category-badge">
                        <font-awesome-icon :icon="['fas', expertiseAreas[currentSlide].icon]" class="mr-2" />
                        {{ expertiseAreas[currentSlide].subtitle }}
                      </div>

                      <p class="key-message">
                        {{ expertiseAreas[currentSlide].keyMessage }}
                      </p>

                      <ul class="capability-list">
                        <li v-for="point in expertiseAreas[currentSlide].capabilities" :key="point">
                          {{ point }}
                        </li>
                      </ul>
                    </div>

                    <!-- Right Column: Technologies -->
                    <div class="slide-sidebar">
                      <h4 class="sidebar-title">Core Technologies</h4>
                      <div class="tech-stack">
                        <div
                          v-for="tech in expertiseAreas[currentSlide].technologies"
                          :key="tech"
                          class="tech-item"
                        >
                          {{ tech }}
                        </div>
                      </div>
                    </div>
                  </div>
                </Transition>
              </div>

              <!-- Footer Bar -->
              <div class="slide-footer-bar">
                <!-- Pagination Dots -->
                <div class="pagination">
                  <button
                    v-for="(_, index) in expertiseAreas"
                    :key="index"
                    @click="goToSlide(index)"
                    :class="['page-dot', { active: currentSlide === index }]"
                    :aria-label="`Go to slide ${index + 1}`"
                  ></button>
                </div>

                <!-- Navigation -->
                <div class="nav-controls">
                  <button
                    @click="prevSlide"
                    :disabled="currentSlide === 0"
                    class="slide-nav-btn"
                    aria-label="Previous slide"
                  >
                    <font-awesome-icon :icon="['fas', 'arrow-left']" />
                  </button>
                  <span class="nav-counter">{{ currentSlide + 1 }} of {{ expertiseAreas.length }}</span>
                  <button
                    @click="nextSlide"
                    :disabled="currentSlide === expertiseAreas.length - 1"
                    class="slide-nav-btn"
                    aria-label="Next slide"
                  >
                    <font-awesome-icon :icon="['fas', 'arrow-right']" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Section 3: Projects -->
      <section id="projects" ref="projectsRef" class="content-section">
        <div class="section-inner">
          <div class="max-w-4xl">
            <h2 class="text-heading-1 text-mckinsey-navy dark:text-white mb-4">
              Projects
            </h2>
            <p class="text-body-lg text-corporate-mid-gray dark:text-corporate-light-gray mb-12">
              A selection of engagements across various roles and industries.
            </p>

            <!-- Projects List -->
            <div class="divide-y divide-corporate-light-gray dark:divide-mckinsey-navy-light">
              <article
                v-for="(project, index) in projects"
                :key="project.title"
                class="py-10 first:pt-0"
              >
                <div class="grid md:grid-cols-4 gap-6">
                  <!-- Meta -->
                  <div class="md:col-span-1">
                    <p class="font-medium text-mckinsey-navy dark:text-white">
                      {{ project.role }}
                    </p>
                    <p class="text-small text-corporate-mid-gray">
                      {{ project.date }}
                    </p>
                    <p class="text-small italic text-corporate-mid-gray mt-1">
                      {{ project.industry }}
                    </p>
                  </div>

                  <!-- Content -->
                  <div class="md:col-span-3">
                    <h3 class="text-heading-3 text-mckinsey-navy dark:text-white mb-3">
                      {{ project.title }}
                    </h3>

                    <!-- Technologies -->
                    <div class="flex flex-wrap gap-2 mb-4">
                      <span
                        v-for="tech in project.technologies"
                        :key="tech"
                        class="px-3 py-1 text-sm bg-corporate-off-white dark:bg-mckinsey-navy text-corporate-dark-gray dark:text-corporate-light-gray rounded"
                      >
                        {{ tech }}
                      </span>
                    </div>

                    <!-- Description -->
                    <p class="text-body text-corporate-dark-gray dark:text-corporate-light-gray mb-4">
                      {{ showProject === index ? project.description : project.description.substring(0, 150) + '...' }}
                    </p>

                    <button
                      @click="toggleProject(index)"
                      class="link-corporate text-sm font-medium"
                    >
                      {{ showProject === index ? 'Read less' : 'Read more' }}
                    </button>
                  </div>
                </div>
              </article>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useAppStore } from '../stores/appStore.js'
import { projects as projectsData } from '../data/projects.js'

const { heightHeader, workAge } = storeToRefs(useAppStore())

// Section navigation
const sections = [
  { id: 'about', label: 'About' },
  { id: 'expertise', label: 'Expertise' },
  { id: 'projects', label: 'Projects' }
]

const activeSection = ref('about')
const aboutRef = ref(null)
const expertiseRef = ref(null)
const projectsRef = ref(null)

const scrollToSection = (id) => {
  const refs = { about: aboutRef, expertise: expertiseRef, projects: projectsRef }
  const el = refs[id]?.value
  if (el) {
    window.scrollTo({
      behavior: 'smooth',
      top: el.offsetTop - heightHeader.value - 20
    })
  }
}

// Intersection Observer for active section
const observerCallback = (entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      activeSection.value = entry.target.id
    }
  })
}

let observer = null

onMounted(() => {
  window.scrollTo({ top: 0 })

  observer = new IntersectionObserver(observerCallback, {
    rootMargin: '-20% 0px -60% 0px',
    threshold: 0
  })

  if (aboutRef.value) observer.observe(aboutRef.value)
  if (expertiseRef.value) observer.observe(expertiseRef.value)
  if (projectsRef.value) observer.observe(projectsRef.value)

  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  if (observer) observer.disconnect()
  window.removeEventListener('keydown', handleKeydown)
})

// Expertise slide deck
const expertiseAreas = [
  {
    icon: 'handshake',
    title: 'Driving Strategic Technology Decisions',
    subtitle: 'Consulting / Advisory',
    keyMessage: 'Partnering with stakeholders to translate business objectives into technology roadmaps and actionable implementation strategies.',
    capabilities: [
      'Conduct technology assessments and define modernization roadmaps for enterprises',
      'Advise C-level executives on data strategy, cloud adoption, and digital transformation',
      'Lead vendor evaluations and technology selection for strategic initiatives',
      'Deliver training programs building organizational technical capabilities'
    ],
    technologies: ['Strategy', 'Roadmapping', 'Stakeholder Management', 'Vendor Evaluation', 'Training', 'Digital Transformation', 'Change Management', 'Business Analysis']
  },
  {
    icon: 'users',
    title: 'Leading High-Performance Teams',
    subtitle: 'Leadership',
    keyMessage: 'Building and mentoring global engineering teams that deliver excellence through collaboration, clear standards, and continuous improvement.',
    capabilities: [
      'Build and scale distributed engineering teams across multiple time zones',
      'Establish code review standards, release processes, and engineering best practices',
      'Mentor engineers through technical growth paths and career development',
      'Drive agile delivery with bi-weekly release cycles and semantic versioning'
    ],
    technologies: ['Team Building', 'Agile', 'Scrum', 'Code Review', 'Mentoring', 'Release Management', 'OKRs', 'Performance Management']
  },
  {
    icon: 'robot',
    title: 'Architecting Agentic AI Solutions',
    subtitle: 'Agentic AI / Generative AI',
    keyMessage: 'Designing production-grade AI systems that transform business operations through intelligent automation and natural language interfaces.',
    capabilities: [
      'Build multi-agent workflows using Langgraph and Langchain for complex task orchestration',
      'Implement RAG architectures with vector search for context-aware AI responses',
      'Deploy conversational interfaces enabling natural language interaction with enterprise systems',
      'Integrate LLM orchestration with existing data pipelines and business logic'
    ],
    technologies: ['Langgraph', 'Langchain', 'OpenAI', 'RAG', 'Vector Search', 'Supabase', 'FastAPI', 'Redis']
  },
  {
    icon: 'cloud',
    title: 'Engineering Cloud-Native Platforms',
    subtitle: 'Cloud Development',
    keyMessage: 'Building scalable, secure infrastructure on AWS using Infrastructure as Code principles and modern DevOps practices.',
    capabilities: [
      'Design enterprise CI/CD pipelines supporting 100+ concurrent deployments',
      'Implement Infrastructure as Code with Terraform and AWS CDK',
      'Architect container orchestration with Docker and Kubernetes (EKS)',
      'Establish comprehensive observability with Prometheus, Grafana, and CloudWatch'
    ],
    technologies: ['AWS', 'Terraform', 'Docker', 'Kubernetes', 'CDK', 'CloudFormation', 'GitHub Actions', 'Prometheus']
  },
  {
    icon: 'layer-group',
    title: 'Delivering Full-Stack Applications',
    subtitle: 'Fullstack Software Engineering',
    keyMessage: 'Developing modern web applications from concept to deployment with focus on user experience and scalable architectures.',
    capabilities: [
      'Build responsive frontends with React and Vue.js using TypeScript',
      'Develop backend services with Python/FastAPI and Node.js',
      'Implement serverless architectures with AWS Lambda and App Runner',
      'Create progressive web applications with offline-first capabilities'
    ],
    technologies: ['React', 'Vue.js', 'TypeScript', 'FastAPI', 'Node.js', 'Tailwind', 'Vite', 'PostgreSQL']
  },
  {
    icon: 'chart-column',
    title: 'Transforming Data into Insights',
    subtitle: 'Data Engineering / Data Analytics',
    keyMessage: 'Architecting enterprise data platforms that enable data-informed decision making across organizations.',
    capabilities: [
      'Design ETL pipelines processing billions of records with Spark and AWS Glue',
      'Build semantic data models and executive dashboards for stakeholders',
      'Implement self-service analytics platforms with Qlik and Power BI',
      'Deliver analytics capabilities to 10,000+ end users across enterprises'
    ],
    technologies: ['Python', 'Spark', 'SQL', 'AWS Glue', 'Athena', 'Qlik', 'Power BI', 'Redshift']
  }
]

const currentSlide = ref(0)

const nextSlide = () => {
  if (currentSlide.value < expertiseAreas.length - 1) {
    currentSlide.value++
  }
}

const prevSlide = () => {
  if (currentSlide.value > 0) {
    currentSlide.value--
  }
}

const goToSlide = (index) => {
  currentSlide.value = index
}

const handleKeydown = (e) => {
  if (e.key === 'ArrowRight') nextSlide()
  if (e.key === 'ArrowLeft') prevSlide()
}

// Projects
const projects = ref(projectsData)
const showProject = ref(-1)

const toggleProject = (index) => {
  showProject.value = showProject.value === index ? -1 : index
}
</script>

<style scoped>
/* Page Layout with Sidebar */
.page-with-sidebar {
  @apply flex min-h-screen;
}

/* Vertical Navigation */
.vertical-nav {
  @apply fixed left-0 top-1/2 -translate-y-1/2 z-40;
  @apply hidden lg:block;
  @apply pl-4 xl:pl-8;
}

.nav-inner {
  @apply relative flex flex-col gap-0;
}

/* Connecting Line */
.nav-line {
  @apply absolute left-4 top-5 bottom-5 w-px;
  @apply bg-corporate-light-gray dark:bg-mckinsey-navy-light;
}

.nav-item {
  @apply relative flex items-center gap-4 py-4 cursor-pointer;
  @apply transition-all duration-200;
}

.nav-number {
  @apply relative z-10 w-8 h-8 flex items-center justify-center;
  @apply text-xs font-bold rounded-full;
  @apply bg-white dark:bg-mckinsey-navy-dark;
  @apply border-2 border-corporate-light-gray dark:border-mckinsey-navy-light;
  @apply text-corporate-mid-gray;
  @apply group-hover:border-mckinsey-teal group-hover:text-mckinsey-teal;
  @apply transition-all duration-200;
}

.nav-item.active .nav-number {
  @apply bg-mckinsey-teal border-mckinsey-teal text-white;
}

.nav-label {
  @apply text-sm font-medium;
  @apply text-corporate-mid-gray;
  @apply opacity-0 group-hover:opacity-100;
  @apply translate-x-0 group-hover:translate-x-1;
  @apply transition-all duration-200;
  @apply whitespace-nowrap;
}

.nav-item.active .nav-label {
  @apply opacity-100 text-mckinsey-navy dark:text-white font-semibold;
}

/* Main Content */
.main-content {
  @apply flex-1 w-full;
}

.content-section {
  @apply min-h-screen py-20;
}

.section-inner {
  @apply container mx-auto px-6 lg:px-20;
}

/* McKinsey Slide Deck */
.mckinsey-slide {
  @apply bg-white dark:bg-mckinsey-navy-dark;
  @apply shadow-2xl rounded-sm overflow-hidden;
  @apply flex flex-col;
  min-height: 500px;
}

@media (min-width: 768px) {
  .mckinsey-slide {
    aspect-ratio: 16 / 10;
  }
}

.slide-header-bar {
  @apply px-6 md:px-8 py-4 md:py-5 flex items-center justify-between;
  background: linear-gradient(135deg, #00205B 0%, #001845 100%);
}

.header-content {
  @apply flex-1;
}

.header-label {
  @apply text-xs uppercase tracking-widest text-mckinsey-teal font-medium mb-1 block;
}

.header-title {
  @apply text-lg md:text-2xl font-semibold text-white leading-tight;
}

.slide-number {
  @apply w-8 h-8 md:w-10 md:h-10 rounded-full flex items-center justify-center;
  @apply text-base md:text-lg font-bold text-white;
  @apply bg-white/10 border border-white/20;
}

.slide-body {
  @apply flex-1 p-6 md:p-10 overflow-hidden;
  @apply bg-white dark:bg-mckinsey-navy-dark;
}

.slide-content-wrapper {
  @apply h-full grid md:grid-cols-3 gap-6 md:gap-8;
}

.slide-main {
  @apply md:col-span-2;
}

.category-badge {
  @apply inline-flex items-center px-3 py-1 mb-4;
  @apply text-xs font-semibold uppercase tracking-wider;
  @apply text-mckinsey-teal bg-mckinsey-teal/10 rounded;
}

.key-message {
  @apply text-base md:text-xl font-medium leading-relaxed mb-6;
  @apply text-mckinsey-navy dark:text-white;
  @apply border-l-4 border-mckinsey-teal pl-4;
}

.capability-list {
  @apply space-y-2 md:space-y-3;
}

.capability-list li {
  @apply flex items-start text-sm md:text-base;
  @apply text-corporate-dark-gray dark:text-corporate-light-gray;
  @apply leading-relaxed;
}

.capability-list li::before {
  content: '';
  @apply w-2 h-2 rounded-full bg-mckinsey-teal mr-3 mt-2 flex-shrink-0;
}

.slide-sidebar {
  @apply md:border-l md:border-corporate-light-gray md:dark:border-mckinsey-navy-light md:pl-6;
}

.sidebar-title {
  @apply text-xs uppercase tracking-widest font-semibold mb-4;
  @apply text-corporate-mid-gray;
}

.tech-stack {
  @apply flex flex-wrap gap-2;
}

.tech-item {
  @apply px-3 py-1.5 text-sm font-medium;
  @apply bg-corporate-off-white dark:bg-mckinsey-navy text-corporate-dark-gray dark:text-corporate-light-gray;
  @apply border border-corporate-light-gray dark:border-mckinsey-navy-light;
  @apply rounded;
}

.slide-footer-bar {
  @apply px-6 md:px-8 py-3 md:py-4 flex items-center justify-between;
  @apply bg-corporate-off-white dark:bg-mckinsey-navy;
  @apply border-t border-corporate-light-gray dark:border-mckinsey-navy-light;
}

.pagination {
  @apply flex gap-2;
}

.page-dot {
  @apply w-3 h-3 rounded-full transition-all duration-200;
  @apply bg-corporate-light-gray dark:bg-mckinsey-navy-light;
  @apply hover:bg-mckinsey-teal/50;
}

.page-dot.active {
  @apply bg-mckinsey-navy dark:bg-mckinsey-teal;
}

.nav-controls {
  @apply flex items-center gap-3 md:gap-4;
}

.slide-nav-btn {
  @apply w-8 h-8 md:w-9 md:h-9 rounded-full flex items-center justify-center;
  @apply text-mckinsey-navy dark:text-white text-sm;
  @apply border border-corporate-light-gray dark:border-mckinsey-navy-light;
  @apply hover:bg-mckinsey-navy hover:text-white hover:border-mckinsey-navy;
  @apply dark:hover:bg-mckinsey-teal dark:hover:border-mckinsey-teal;
  @apply transition-all duration-200;
  @apply disabled:opacity-30 disabled:cursor-not-allowed disabled:hover:bg-transparent disabled:hover:text-mckinsey-navy dark:disabled:hover:text-white disabled:hover:border-corporate-light-gray;
}

.nav-counter {
  @apply text-sm font-medium text-corporate-mid-gray min-w-[50px] md:min-w-[60px] text-center;
}

/* Slide Transitions */
.slide-enter-active,
.slide-leave-active {
  transition: opacity 0.25s ease, transform 0.25s ease;
}

.slide-enter-from {
  opacity: 0;
  transform: translateX(16px);
}

.slide-leave-to {
  opacity: 0;
  transform: translateX(-16px);
}
</style>
