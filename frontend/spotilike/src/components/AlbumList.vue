<template>
    <div class="album-list">
      <h2>Albums</h2>
      <ul>
        <li v-for="album in albums" :key="album.album_id">
          <router-link :to="'/albums/' + album.album_id">
            <img :src="album.cover" alt="Album Cover" />
            <h3>{{ album.title }}</h3>
          </router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { getAlbums } from '../api/api'; // Assure-toi d'importer ton API
  
  export default {
    data() {
      return {
        albums: [],
      };
    },
    mounted() {
      this.fetchAlbums();
    },
    methods: {
      async fetchAlbums() {
        try {
          const response = await getAlbums();
          this.albums = response.data;
        } catch (error) {
          console.error("Error fetching albums:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .album-list {
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
  