<template>
  <v-container class="bg-gradient-to-b from-green-700 to-black text-white min-h-screen py-10">
    <v-row>
      <v-col cols="12" md="4">
        <v-img 
          :src="album.cover" 
          alt="Album Cover"
          height="300px"
          contain
          class="album-cover"
        ></v-img>
      </v-col>
      <v-col cols="12" md="8">
        <h1 class="text-3xl font-bold mb-4">{{ album.title }}</h1>
        <p class="text-lg">🗓 Date de sortie : {{ album.release_date }}</p>
        
        <h2 class="text-xl mt-6 mb-3 font-semibold">Morceaux :</h2>
        <v-list class="track-list">
          <v-list-item 
            v-for="track in tracks" 
            :key="track.track_id"
            class="track-item"
          >
            <v-list-item-content>
              <v-list-item-title class="text-lg font-medium">{{ track.title }}</v-list-item-title>
              <v-list-item-subtitle class="text-sm">Durée : {{ track.duration }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { getAlbum, getAlbumSongs } from "../api";

export default {
  data() {
    return { album: {}, tracks: [] };
  },
  async created() {
    const albumId = this.$route.params.id;
    try {
      const albumRes = await getAlbum(albumId);
      const tracksRes = await getAlbumSongs(albumId);

      // Vérifier si le chemin de l'image est correct
      const baseURL = "http://localhost:8000";
      this.album = {
        ...albumRes.data,
        cover: albumRes.data.cover.startsWith("/static/")
          ? `${baseURL}${albumRes.data.cover}`
          : `${baseURL}/static${albumRes.data.cover}`
      };

      this.tracks = tracksRes.data;
    } catch (error) {
      console.error("Erreur :", error);
    }
  },
};
</script>


<style scoped>
.album-cover {
  border-radius: 12px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
}

.track-list {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 10px;
}

.track-item {
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.track-item:last-child {
  border-bottom: none;
}
</style>
