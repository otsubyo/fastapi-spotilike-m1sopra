<template>
    <v-container class="bg-gradient-to-b from-green-700 to-black text-white min-h-screen">
      <h1 class="text-3xl font-bold text-center mb-6">Liste des artistes</h1>
      <v-row>
        <v-col v-for="artist in artists" :key="artist.artist_id" cols="12" sm="6" md="3">
          <v-card @click="$router.push(`/artists/${artist.artist_id}`)" class="cursor-pointer">
            <v-img :src="artist.avatar" height="200px"></v-img>
            <v-card-title>{{ artist.name }}</v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import { getArtists } from '../api';
  
  export default {
    data() {
      return { artists: [] };
    },
    async created() {
      try {
        const response = await getArtists();
        this.artists = response.data;
      } catch (error) {
        console.error("Erreur :", error);
      }
    },
  };
  </script>
  