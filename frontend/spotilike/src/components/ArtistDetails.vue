<template>
    <div>
      <h1>{{ artist.name }}</h1>
      <img :src="artist.avatar" alt="Artist Avatar">
      <p>{{ artist.biography }}</p>
      <h2>Songs:</h2>
      <ul>
        <li v-for="song in songs" :key="song.id">{{ song.title }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        artist: {},
        songs: []
      };
    },
    mounted() {
      const artistId = this.$route.params.id;
      axios.get(`/api/artists/${artistId}`).then((response) => {
        this.artist = response.data;
      });
      axios.get(`/api/artists/${artistId}/songs`).then((response) => {
        this.songs = response.data;
      });
    }
  };
  </script>
  