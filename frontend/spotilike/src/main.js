import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createVuetify } from 'vuetify';

// ✅ Importation des styles de Vuetify
import 'vuetify/styles';
import '@mdi/font/css/materialdesignicons.css';

// ✅ Importation des composants et directives de Vuetify
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

// ✅ Configuration de Vuetify
const vuetify = createVuetify({
  components,
  directives,
});

// ✅ Création de l'application Vue
const app = createApp(App);

// ✅ Ajout du routeur et de Vuetify
app.use(router);
app.use(vuetify);

// ✅ Gestionnaire global d'erreurs pour capturer les erreurs non traitées
app.config.errorHandler = (err, instance, info) => {
  console.error("💥 Une erreur est survenue :", err, info);
};

// ✅ Montage de l'application
app.mount('#app');
