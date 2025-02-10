<template>
  <v-container>
    <v-btn color="primary" to="/artists" class="mb-3">⬅ Retour à la liste des artistes</v-btn>

    <v-row>
      <v-col cols="12" md="4">
        <!-- Image de l'artiste -->
        <img :src="artist.avatar" alt="Artist Avatar" width="100%" style="border-radius: 8px;">
      </v-col>

      <v-col cols="12" md="8">
        <!-- ✅ Texte en blanc -->
        <h1 class="text-h4 font-weight-bold text-white">{{ artist.name }}</h1>
        <p class="text-body-1 text-white">{{ artist.biography }}</p>
      </v-col>
    </v-row>

    <h2 class="text-h5 mt-5 text-white">Morceaux de l'artiste</h2>
    <v-row v-if="tracks.length > 0">
      <v-col v-for="track in tracks" :key="track.id" cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>{{ track.title }}</v-card-title>
          <v-card-subtitle>{{ track.duration }} min</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
    <p v-else class="text-body-2 text-white">Aucun morceau trouvé.</p>
  </v-container>
</template>


<script>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { getArtist, getArtistSongs } from "@/api";

export default {
  setup() {
    const route = useRoute();
    const artist = ref({});
    const tracks = ref([]);

    onMounted(async () => {
      const artistId = route.params.id;
      try {
        // ✅ Récupère les infos de l'artiste
        const response = await getArtist(artistId);
        artist.value = response.data;

        // ✅ Récupère les morceaux de l'artiste
        const tracksResponse = await getArtistSongs(artistId);
        tracks.value = tracksResponse.data;
      } catch (error) {
        console.error("Erreur lors du chargement des détails de l'artiste :", error);
      }
    });

    return { artist, tracks };
  }
};
</script>

