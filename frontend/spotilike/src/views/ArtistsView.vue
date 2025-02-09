<template>
    <v-container>
      <h2 class="text-h4 text-white text-center mb-5">Liste des artistes</h2>
      <v-row>
        <v-col v-for="artist in artists" :key="artist.id" cols="12" sm="6" md="3">
          <v-card @click="$router.push(`/artists/${artist.id}`)">
            <v-img :src="artist.image" height="200px" cover></v-img>
            <v-card-title>{{ artist.name }}</v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { getArtists } from '../api'; // API backend
  
  export default {
    setup() {
      const artists = ref([]);
  
      onMounted(async () => {
        const response = await getArtists();
        artists.value = response.data;
      });
  
      return { artists };
    },
  };
  </script>
  