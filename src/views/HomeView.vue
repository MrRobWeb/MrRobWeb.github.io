<template>
  <section class="section">
    <div class="container-corporate">
      <!-- Hero Section -->
      <div class="max-w-3xl mx-auto text-center py-16 md:py-24">
        <!-- Profile Image - subtle, professional -->
        <img
          src="../assets/imgs/profile.jpg"
          alt="Robert Weber"
          class="w-40 h-40 md:w-48 md:h-48 mx-auto rounded-full border-4 border-corporate-light-gray dark:border-mckinsey-navy-light mb-8 opacity-0 animate-fade-in"
        >

        <!-- Name - strong typographic hierarchy -->
        <h1
          class="text-hero text-mckinsey-navy dark:text-white mb-4 opacity-0 animate-fade-in"
          style="animation-delay: 0.1s"
        >
          Robert Weber
        </h1>

        <!-- Divider - McKinsey style -->
        <div
          class="w-16 h-1 bg-mckinsey-teal mx-auto mb-6 opacity-0 animate-fade-in"
          style="animation-delay: 0.2s"
        ></div>

        <!-- Role - static, professional -->
        <p
          class="text-heading-3 text-corporate-mid-gray dark:text-corporate-light-gray mb-8 opacity-0 animate-fade-in"
          style="animation-delay: 0.3s"
        >
          Data Engineering Manager
        </p>

        <!-- Value Proposition - concise, impactful -->
        <p
          class="text-body-lg text-corporate-dark-gray dark:text-corporate-light-gray max-w-xl mx-auto mb-10 opacity-0 animate-fade-in"
          style="animation-delay: 0.4s"
        >
          Enabling enterprise transformation through Agentic AI solutions, scalable cloud architecture,
          engineering leadership, and strategic technical advisory.
        </p>

        <!-- CTAs - McKinsey button style -->
        <div
          class="flex flex-col sm:flex-row items-center justify-center gap-4 opacity-0 animate-fade-in"
          style="animation-delay: 0.5s"
        >
          <RouterLink to="/about" class="btn-primary">
            View Experience
          </RouterLink>
          <RouterLink to="/contact" class="btn-secondary">
            Get in Touch
          </RouterLink>
        </div>

        <!-- Divider -->
        <p
          class="text-sm text-corporate-mid-gray mt-6 opacity-0 animate-fade-in"
          style="animation-delay: 0.6s"
        >
          or
        </p>

        <!-- Digital Twin CTA -->
        <div
          class="mt-4 opacity-0 animate-fade-in"
          style="animation-delay: 0.7s"
        >
          <RouterLink to="/digital-twin" class="btn-secondary">
            <font-awesome-icon :icon="['fas', 'robot']" class="mr-2" />
            Chat with my Digital Twin
          </RouterLink>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from 'vue';

onMounted(() => {
  window.scrollTo({ top: 0 });
});
</script>
