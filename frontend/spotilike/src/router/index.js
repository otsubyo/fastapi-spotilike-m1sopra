import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import AlbumsView from '../views/AlbumsView.vue';
import ArtistsView from '../views/ArtistsView.vue';
import AlbumDetails from '../views/AlbumDetails.vue';
import ArtistDetails from '../views/ArtistDetails.vue';

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/albums', name: 'albums', component: AlbumsView },
  { path: '/artists', name: 'artists', component: ArtistsView },
  { path: '/albums/:id', name: 'album-details', component: AlbumDetails, props: true },
  { path: '/artists/:id', name: 'artist-details', component: ArtistDetails, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
