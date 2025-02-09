<template>
    <v-container class="bg-gradient-to-b from-green-700 to-black text-white min-h-screen">
      <v-row>
        <v-col cols="12" md="4">
          <v-img :src="album.cover" height="300px"></v-img>
        </v-col>
        <v-col cols="12" md="8">
          <h1 class="text-3xl font-bold">{{ album.title }}</h1>
          <p>Date de sortie : {{ album.release_date }}</p>
          <h2 class="text-xl mt-4">Morceaux :</h2>
          <v-list>
            <v-list-item v-for="track in tracks" :key="track.track_id">
              {{ track.title }}
            </v-list-item>
          </v-list>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import { getAlbum, getAlbumSongs } from '../api';
  
  export default {
    data() {
      return { album: {}, tracks: [] };
    },
    async created() {
      const albumId = this.$route.params.id;
      try {
        const albumRes = await getAlbum(albumId);
        const tracksRes = await getAlbumSongs(albumId);
        this.album = albumRes.data;
        this.tracks = tracksRes.data;
      } catch (error) {
        console.error("Erreur :", error);
      }
    },
  };
  </script>
  