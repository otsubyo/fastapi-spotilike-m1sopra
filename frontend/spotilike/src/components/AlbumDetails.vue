<template>
    <div>
      <h1>{{ album.title }}</h1>
      <img :src="album.cover" alt="Album Cover">
      <p>Release Date: {{ album.release_date }}</p>
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
        album: {},
        songs: []
      };
    },
    mounted() {
      const albumId = this.$route.params.id;
      axios.get(`/api/albums/${albumId}`).then((response) => {
        this.album = response.data;
      });
      axios.get(`/api/albums/${albumId}/songs`).then((response) => {
        this.songs = response.data;
      });
    }
  };
  </script>
  