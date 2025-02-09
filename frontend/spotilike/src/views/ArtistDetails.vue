<template>
    <v-container class="bg-gradient-to-b from-green-700 to-black text-white min-h-screen">
      <v-row>
        <v-col cols="12" md="4">
          <v-img :src="artist.avatar" height="300px"></v-img>
        </v-col>
        <v-col cols="12" md="8">
          <h1 class="text-3xl font-bold">{{ artist.name }}</h1>
          <p>{{ artist.biography }}</p>
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
  import { getArtist, getArtistSongs } from '../api';
  
  export default {
    data() {
      return { artist: {}, tracks: [] };
    },
    async created() {
      const artistId = this.$route.params.id;
      try {
        const artistRes = await getArtist(artistId);
        const tracksRes = await getArtistSongs(artistId);
        this.artist = artistRes.data;
        this.tracks = tracksRes.data;
      } catch (error) {
        console.error("Erreur :", error);
      }
    },
  };
  </script>
  