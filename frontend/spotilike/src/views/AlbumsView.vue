<template>
  <div>
    <h2>Albums</h2>
    <ul>
      <li v-for="album in albums" :key="album.album_id">
        <router-link :to="'/albums/' + album.album_id">{{ album.title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { getAlbums } from '../api';

export default {
  data() {
    return {
      albums: [],
    };
  },
  created() {
    getAlbums()
      .then(response => {
        this.albums = response.data;
      })
      .catch(error => {
        console.error("Il y a eu une erreur lors de la récupération des albums:", error);
      });
  },
};
</script>
