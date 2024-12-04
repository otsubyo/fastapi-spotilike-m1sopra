<template>
  <div>
    <h1>Albums</h1>
    <ul>
      <li v-for="album in albums" :key="album.id">
        <router-link :to="{ name: 'album-details', params: { id: album.id } }">
          {{ album.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      albums: []
    };
  },
  mounted() {
    axios.get('/api/albums').then((response) => {
      this.albums = response.data;
    });
  }
};
</script>
