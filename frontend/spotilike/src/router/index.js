import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import AlbumsView from '../views/AlbumsView.vue';
import AlbumsDetails from '../views/AlbumsDetails.vue';
import ArtistsView from '../views/ArtistsView.vue';
import ArtistDetails from '../views/ArtistDetails.vue';

const routes = [
  { path: '/', component: HomeView },
  { path: '/albums', component: AlbumsView },
  { path: '/albums/:id', component: AlbumsDetails, props: true },
  { path: '/artists', component: ArtistsView },
  { path: '/artists/:id', component: ArtistDetails, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
