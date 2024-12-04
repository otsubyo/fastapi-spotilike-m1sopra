import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AlbumsView from "../views/AlbumsView.vue";
import ArtistsView from "../views/ArtistsView.vue";
import AlbumDetails from "../components/AlbumDetails.vue";
import ArtistDetails from "../components/ArtistDetails.vue";

const routes = [
  { path: "/", component: HomeView, name: "home" },
  { path: "/albums", component: AlbumsView, name: "albums" },
  { path: "/albums/:id", component: AlbumDetails, name: "album-details" },
  { path: "/artists", component: ArtistsView, name: "artists" },
  { path: "/artists/:id", component: ArtistDetails, name: "artist-details" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
