import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createVuetify } from 'vuetify';
import 'vuetify/styles'; // 🔥 Importation des styles de Vuetify
import '@mdi/font/css/materialdesignicons.css'; // 🔥 Icônes Material Design
import * as components from 'vuetify/components'; // 🔥 Forcer tous les composants
import * as directives from 'vuetify/directives'; // 🔥 Activer les directives (ex: v-ripple)

// ✅ Activation complète de Vuetify
const vuetify = createVuetify({
  components,
  directives,
});

const app = createApp(App);
app.use(router);
app.use(vuetify);
app.mount('#app');
