import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'
import router from './router'

import { library } from '@fortawesome/fontawesome-svg-core'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faChartColumn, faEnvelope, faGears, faImage, faMoon, faServer, faSun, faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { faFacebook, faGithub, faGitlab, faInstagram, faLinkedin, faMixcloud, faTwitter } from '@fortawesome/free-brands-svg-icons'

library.add(faUserSecret,faFacebook,faLinkedin,faInstagram,faGithub,faTwitter, faMoon, faSun, faEnvelope, faGitlab, faChartColumn, faImage, faServer, faGears)

const pinia = createPinia()
createApp(App)
.use(pinia)
.use(router)
.component('font-awesome-icon', FontAwesomeIcon)
.mount('#app');

