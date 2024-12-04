<template>
    <div class="artist-details" v-if="artist">
      <h2>{{ artist.name }}</h2>
      <img :src="artist.avatar" alt="Artist Avatar" />
      <p><strong>Biography:</strong> {{ artist.biography }}</p>
  
      <h3>Songs</h3>
      <ul>
        <li v-for="song in songs" :key="song.track_id">{{ song.title }} - {{ song.duration }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import { getArtistSongs } from '../api/api';
  
  export default {
    data() {
      return {
        artist: null,
        songs: [],
      };
    },
    mounted() {
      const artistId = this.$route.params.id;
      this.fetchArtist(artistId);
      this.fetchSongs(artistId);
    },
    methods: {
      async fetchArtist(id) {
        try {
          const response = await getArtistSongs(id);
          this.artist = response.data;
        } catch (error) {
          console.error("Error fetching artist details:", error);
        }
      },
      async fetchSongs(id) {
        try {
          const response = await getArtistSongs(id);
          this.songs = response.data;
        } catch (error) {
          console.error("Error fetching songs:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .artist-details {
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
  