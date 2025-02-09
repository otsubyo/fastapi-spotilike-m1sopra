<template>
  <v-container>
    <h2 class="text-center text-white">Liste des albums</h2>
    <v-row v-if="albums.length > 0">
      <v-col v-for="album in albums" :key="album.id" cols="12" sm="6" md="4" lg="3">
        <v-card class="mx-auto" max-width="344">
          <v-img
            :src="getAlbumImage(album.image)"
            height="200px"
            contain
          ></v-img>
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

    onMounted(async () => {
      albums.value = await getAlbums();
    });

    const getAlbumImage = (imageName) => {
  try {
    return new URL(`@/assets/images/albums/${imageName}`, import.meta.url).href;
  } catch (e) {
    console.error(`Erreur de chargement de l'image : ${e.message}`);
    return new URL(`@/assets/images/albums/default.jpg`, import.meta.url).href;
  }
};




    return { albums, getAlbumImage };
  }
};
</script>