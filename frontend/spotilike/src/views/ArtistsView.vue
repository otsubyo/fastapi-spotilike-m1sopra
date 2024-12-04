<template>
    <div>
      <h2>Artists</h2>
      <ul>
        <li v-for="artist in artists" :key="artist.artist_id">
          <router-link :to="'/artists/' + artist.artist_id">{{ artist.name }}</router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { getArtists } from '../api';
  
  export default {
    data() {
      return {
        artists: [],
      };
    },
    created() {
      getArtists()
        .then(response => {
          this.artists = response.data;
        })
        .catch(error => {
          console.error("Erreur lors de la récupération des artistes:", error);
        });
    },
  };
  </script>
  