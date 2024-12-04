<template>
  <div>
    <h1>Artists</h1>
    <ul>
      <li v-for="artist in artists" :key="artist.id">
        <router-link :to="{ name: 'artist-details', params: { id: artist.id } }">
          {{ artist.name }}
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
      artists: []
    };
  },
  mounted() {
    axios.get('/api/artists').then((response) => {
      this.artists = response.data;
    });
  }
};
</script>
