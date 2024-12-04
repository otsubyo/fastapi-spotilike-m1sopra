<template>
    <div>
      <h2>{{ album.title }}</h2>
      <p>{{ album.release_date }}</p>
      <h3>Songs</h3>
      <ul>
        <li v-for="song in songs" :key="song.track_id">{{ song.title }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import { getAlbum } from '../api';
  import { getAlbumSongs } from '../api';
  
  export default {
    data() {
      return {
        album: {},
        songs: [],
      };
    },
    created() {
      const albumId = this.$route.params.id;
      getAlbum(albumId)
        .then(response => {
          this.album = response.data;
        })
        .catch(error => {
          console.error("Erreur lors de la récupération de l'album:", error);
        });
  
      getAlbumSongs(albumId)
        .then(response => {
          this.songs = response.data;
        })
        .catch(error => {
          console.error("Erreur lors de la récupération des chansons:", error);
        });
    },
  };
  </script>
  