<template>
  <v-container>
    <h2 class="text-h4 text-white text-center mb-5">Liste des albums</h2>
    <v-row>
      <v-col v-for="album in albums" :key="album.id" cols="12" sm="6" md="3">
        <v-card @click="$router.push(`/albums/${album.id}`)">
          <v-img :src="album.image" height="200px" cover></v-img>
          <v-card-title>{{ album.name }}</v-card-title>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue';
import { getAlbums } from '../api'; // API backend

export default {
  setup() {
    const albums = ref([]);

    onMounted(async () => {
      const response = await getAlbums();
      albums.value = response.data;
    });

    return { albums };
  },
};
</script>
