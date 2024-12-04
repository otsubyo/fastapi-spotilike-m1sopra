<template>
    <div class="album-details" v-if="album">
      <h2>{{ album.title }}</h2>
      <img :src="album.cover" alt="Album Cover" />
      <p><strong>Release Date:</strong> {{ album.release_date }}</p>
  
      <h3>Songs</h3>
      <ul>
        <li v-for="song in songs" :key="song.track_id">{{ song.title }} - {{ song.duration }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import { getAlbum, getAlbumSongs } from '../api/api';
  
  export default {
    data() {
      return {
        album: null,
        songs: [],
      };
    },
    mounted() {
      const albumId = this.$route.params.id;
      this.fetchAlbum(albumId);
      this.fetchSongs(albumId);
    },
    methods: {
      async fetchAlbum(id) {
        try {
          const response = await getAlbum(id);
          this.album = response.data;
        } catch (error) {
          console.error("Error fetching album details:", error);
        }
      },
      async fetchSongs(id) {
        try {
          const response = await getAlbumSongs(id);
          this.songs = response.data;
        } catch (error) {
          console.error("Error fetching songs:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .album-details {
    padding: 20px;
  }
  
  img {
    width: 200px;
    height: 200px;
    object-fit: cover;
  }
  
  h2 {
    font-size: 2em;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 10px;
  }
  </style>
  