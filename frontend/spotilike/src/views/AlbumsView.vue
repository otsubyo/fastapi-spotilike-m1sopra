<template>
  <v-container>
    <h2 class="text-center text-white title-spacing">Liste des albums</h2>

    <v-row v-if="albums.length > 0">
      <v-col v-for="album in albums" :key="album.id" cols="12" sm="6" md="4" lg="3">
        <v-card class="mx-auto" max-width="344">
          <!-- Chargement des images depuis le dossier public -->
          <img :src="album.cover" alt="Album cover" height="200px" style="width:100%; object-fit: cover;">
          
          <v-card-title>{{ album.title }}</v-card-title>
          <v-card-subtitle>{{ album.artist }}</v-card-subtitle>
          <v-card-actions>
            <v-btn color="primary" :to="'/albums/' + album.album_id">Voir Les détails de l'album</v-btn>
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
    const defaultImage = "/images/albums/default.jpg"; // Image par défaut dans /public/images/albums/

    onMounted(async () => {
      albums.value = await getAlbums();

      // Charger les images locales depuis /public/images/albums/
      albums.value = albums.value.map(album => ({
        ...album,
        image: album.cover ? `/images/albums/${album.cover}` : defaultImage
      }));
    });

    return { albums };
  }
};
</script>

<style scoped>
/* Espacement sous le titre */
.title-spacing {
  margin-bottom: 100px;
}

/* Espace entre les cartes */
.v-row {
  row-gap: 30px;
}
</style>
