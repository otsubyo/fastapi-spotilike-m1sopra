import { createRouter, createWebHistory } from 'vue-router'
import AlbumList from '@/components/AlbumList.vue'
import AlbumDetail from '@/components/AlbumDetail.vue'
import ArtistList from '@/components/ArtistList.vue'
import ArtistDetail from '@/components/ArtistDetails.vue'

const routes = [
  { path: '/', redirect: '/albums' },
  { path: '/albums', component: AlbumList },
  { path: '/albums/:id', component: AlbumDetail },
  { path: '/artists', component: ArtistList },
  { path: '/artists/:id', component: ArtistDetail },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router