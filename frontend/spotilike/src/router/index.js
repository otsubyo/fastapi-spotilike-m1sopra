import { createRouter, createWebHistory } from 'vue-router';
import AlbumList from '../components/AlbumList.vue';   // Utilisation du composant AlbumList
import AlbumDetails from '../components/AlbumDetails.vue'; // Utilisation du composant AlbumDetails
import ArtistList from '../components/ArtistList.vue';  // Utilisation du composant ArtistList
import ArtistDetails from '../components/ArtistDetails.vue'; // Utilisation du composant ArtistDetails
import Navbar from '../components/Navbar.vue';  // Le composant Navbar que nous avons défini précédemment

const routes = [
  {
    path: '/',
    name: 'home',
    component: AlbumList,  // Accueil avec la liste des albums
  },
  {
    path: '/albums',
    name: 'albums',
    component: AlbumList, // Liste des albums
  },
  {
    path: '/albums/:id',
    name: 'album-details',
    component: AlbumDetails,  // Détails d'un album spécifique
    props: true,  // Permet de passer l'ID comme prop
  },
  {
    path: '/artists',
    name: 'artists',
    component: ArtistList, // Liste des artistes
  },
  {
    path: '/artists/:id',
    name: 'artist-details',
    component: ArtistDetails, // Détails d'un artiste spécifique
    props: true,  // Permet de passer l'ID comme prop
  },
  {
    path: '/navbar',
    name: 'navbar',
    component: Navbar,  // Si tu veux rendre la Navbar accessible directement
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
