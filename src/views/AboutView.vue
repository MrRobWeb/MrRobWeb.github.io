<template>
  <div class="page-with-sidebar">
    <!-- Section Navigation -->
    <nav class="horizontal-nav" :style="{ top: heightHeader + 'px' }">
      <div class="container-corporate">
        <div class="horizontal-nav-inner">
          <!-- Connecting Line -->
          <div class="horizontal-nav-line"></div>

          <button
            v-for="(section, index) in sections"
            :key="section.id"
            @click="scrollToSection(section.id)"
            :class="['horizontal-nav-item', 'group', { active: activeSection === section.id }]"
          >
            <span class="horizontal-nav-number">{{ String(index + 1).padStart(2, '0') }}</span>
            <span class="horizontal-nav-label">{{ section.label }}</span>
          </button>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="main-content">
      <!-- Section 1: About -->
      <section id="about" ref="aboutRef" class="content-section">
        <div class="section-inner">
          <div class="max-w-3xl mx-auto">
            <div class="flex items-start gap-6 mb-8">
              <img
                src="../assets/imgs/profile.jpg"
                alt="Robert Weber"
                class="w-20 h-20 md:w-24 md:h-24 rounded-full flex-shrink-0"
              >
              <div>
                <h1 class="text-heading-1 text-mckinsey-navy dark:text-white mb-2">Robert Weber</h1>
                <p class="text-body-lg text-corporate-mid-gray">Technology Lead</p>
              </div>
            </div>

            <div class="space-y-6">
              <p class="text-body-lg text-corporate-dark-gray dark:text-corporate-light-gray">
                Technology Lead with expertise in agentic AI, cloud architecture, data platform development,
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
          <div class="max-w-5xl mx-auto">
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
          <div class="max-w-4xl mx-auto">
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
import { expertiseAreas } from '../data/expertise.js'

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
/* Page Layout */
.page-with-sidebar {
  @apply flex flex-col min-h-screen;
}

/* Section Navigation */
.horizontal-nav {
  @apply sticky z-40;
  @apply bg-corporate-white dark:bg-mckinsey-navy-dark;
  @apply border-b border-corporate-light-gray dark:border-mckinsey-navy-light;
}

.horizontal-nav-inner {
  @apply relative flex items-center justify-center gap-8 md:gap-12 py-4;
}

/* Horizontal Connecting Line */
.horizontal-nav-line {
  @apply absolute h-px;
  @apply bg-corporate-light-gray dark:bg-mckinsey-navy-light;
  @apply left-1/2 -translate-x-1/2;
  top: calc(1rem + 1rem); /* py-4 padding + half of circle height */
  width: 9rem; /* spans between first and last circle centers */
}

@media (min-width: 768px) {
  .horizontal-nav-line {
    width: 13rem; /* spans between first and last circle centers */
  }
}

.horizontal-nav-item {
  @apply relative flex flex-col items-center gap-2 cursor-pointer;
  @apply transition-all duration-200;
}

.horizontal-nav-number {
  @apply relative z-10 w-8 h-8 flex items-center justify-center;
  @apply text-xs font-bold rounded-full;
  @apply bg-white dark:bg-mckinsey-navy-dark;
  @apply border-2 border-corporate-light-gray dark:border-mckinsey-navy-light;
  @apply text-corporate-mid-gray;
  @apply group-hover:border-mckinsey-teal group-hover:text-mckinsey-teal;
  @apply transition-all duration-200;
}

.horizontal-nav-item.active .horizontal-nav-number {
  @apply bg-mckinsey-teal border-mckinsey-teal text-white;
}

.horizontal-nav-label {
  @apply text-xs font-medium uppercase tracking-wider;
  @apply text-corporate-mid-gray;
  @apply group-hover:text-mckinsey-navy dark:group-hover:text-white;
  @apply transition-all duration-200;
}

.horizontal-nav-item.active .horizontal-nav-label {
  @apply text-mckinsey-navy dark:text-white font-semibold;
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
