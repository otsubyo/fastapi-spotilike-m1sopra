import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

// Use Pinia and Vue Router
app.use(createPinia())   // Setting up the Pinia store
app.use(router)          // Setting up the router

// Mount the app on the DOM element with the id "app"
app.mount('#app')
