<template>
  <v-container class="bg-gradient-to-b from-green-700 to-black text-white min-h-screen">
    <h1 class="text-3xl font-bold text-center mb-6">Liste des albums</h1>
    <v-row>
      <v-col v-for="album in albums" :key="album.album_id" cols="12" sm="6" md="3">
        <v-card @click="$router.push(`/albums/${album.album_id}`)" class="cursor-pointer">
          <v-img :src="album.cover" height="200px"></v-img>
          <v-card-title>{{ album.title }}</v-card-title>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { getAlbums } from '../api';

export default {
  data() {
    return { albums: [] };
  },
  async created() {
    try {
      const response = await getAlbums();
      this.albums = response.data;
    } catch (error) {
      console.error("Erreur :", error);
    }
  },
};
</script>
