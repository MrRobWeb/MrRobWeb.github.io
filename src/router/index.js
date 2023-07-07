import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ProjectView from '../views/ProjectView.vue'
import ContactView from '../views/ContactView.vue'
import PrivacyPolicy from '../views/PrivacyPolicy.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'About',
        component: AboutView
    },
    {
        path: '/project',
        name: 'Project',
        component: ProjectView
    },
    {
        path: '/contact',
        name: 'Contact',
        component: ContactView
    },
    {
        path: '/privacyPolicy',
        name: 'PrivacyPolicy',
        component: PrivacyPolicy
    },
    {
        path : '/:catchAll(.*)',
        redirect : '/'
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
  })
  

export default router