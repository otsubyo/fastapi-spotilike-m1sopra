<template>
  <v-container>
    <h2 class="text-center text-white title-spacing">Liste des artistes</h2>
    <v-row v-if="artists.length > 0">
      <v-col v-for="artist in artists" :key="artist.artist_id" cols="12" sm="6" md="4" lg="3">
        <v-card class="mx-auto" max-width="344">
          <!-- Image de l'artiste -->
          <img :src="`${artist.avatar}`" alt="Artist Avatar" height="200px" style="width:100%; object-fit: cover;">
          
          <v-card-title>{{ artist.name }}</v-card-title>
          <v-card-subtitle>{{ artist.biography }}</v-card-subtitle>

          <v-card-actions>
            <v-btn color="primary" :to="'/artists/' + artist.artist_id">Voir les détails de l'artiste</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <p v-else class="text-center text-white">Aucun artiste trouvé.</p>
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue';
import { getArtists } from '@/api';

export default {
  setup() {
    const artists = ref([]);

    onMounted(async () => {
      try {
        const response = await getArtists();

        // EXTRACTION DU TABLEAU `data`
        if (response.data && Array.isArray(response.data)) {
          artists.value = response.data;
        } else {
          console.warn("L'API a retourné un format inattendu :", response);
          artists.value = []; // Évite une erreur si la donnée est incorrecte
        }
      } catch (error) {
        console.error("Erreur lors du chargement des artistes :", error);
        artists.value = []; // Évite que Vue essaie de mapper sur `undefined`
      }
    });

    return { artists };
  }
};
</script>

<style scoped>
.title-spacing {
  margin-bottom: 100px; /* Augmente l'espace sous le titre */
}

.v-row {
  row-gap: 30px; /* Espace entre les cartes */
}
</style>
