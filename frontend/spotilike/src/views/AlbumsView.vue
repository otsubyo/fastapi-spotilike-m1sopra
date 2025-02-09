<template>
  <v-container>
    <h2 class="text-center text-white">Liste des albums</h2>
    <v-row v-if="albums.length > 0">
      <v-col v-for="album in albums" :key="album.id" cols="12" sm="6" md="4" lg="3">
        <v-card class="mx-auto" max-width="344">
          <img :src="album.image" alt="Album cover" height="200px" style="width:100%; object-fit: cover;">
          <v-card-title>{{ album.title }}</v-card-title>
          <v-card-subtitle>{{ album.artist }}</v-card-subtitle>
          <v-card-actions>
            <v-btn color="primary" :to="'/albums/' + album.id">Voir Détails</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <p v-else class="text-center text-white">Aucun album trouvé.</p>
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue';
import { getAlbums } from '@/api';

export default {
  setup() {
    const albums = ref([]);
    const baseURL = "http://localhost:8000"; // Base de l'API
    const defaultImage = "/static/default.jpg"; // Image par défaut

    onMounted(async () => {
      albums.value = await getAlbums();

      // Assurer que chaque album a bien une image avec `/static/`
      albums.value = albums.value.map(album => ({
        ...album,
        image: album.cover ? `${baseURL}${album.cover}` : `${baseURL}${defaultImage}`
      }));
    });

    return { albums };
  }
};
</script>
