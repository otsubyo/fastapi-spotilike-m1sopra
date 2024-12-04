<template>
    <div class="artist-list">
      <h2>Artists</h2>
      <ul>
        <li v-for="artist in artists" :key="artist.artist_id">
          <router-link :to="'/artists/' + artist.artist_id">
            <img :src="artist.avatar" alt="Artist Avatar" />
            <h3>{{ artist.name }}</h3>
          </router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { getArtists } from '../api/api';
  
  export default {
    data() {
      return {
        artists: [],
      };
    },
    mounted() {
      this.fetchArtists();
    },
    methods: {
      async fetchArtists() {
        try {
          const response = await getArtists();
          this.artists = response.data;
        } catch (error) {
          console.error("Error fetching artists:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .artist-list {
    padding: 20px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 20px;
  }
  
  img {
    width: 100px;
    height: 100px;
    object-fit: cover;
  }
  
  h3 {
    font-size: 1.2em;
  }
  </style>
  