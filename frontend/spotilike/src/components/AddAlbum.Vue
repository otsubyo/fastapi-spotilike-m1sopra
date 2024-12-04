<template>
    <div>
      <h1>Ajouter un album</h1>
      <form @submit.prevent="createAlbum">
        <input v-model="title" placeholder="Titre de l'album" />
        <button type="submit">Ajouter</button>
      </form>
    </div>
  </template>
  
  <script>
  import apiClient from '../api';
  
  export default {
    data() {
      return {
        title: '',
      };
    },
    methods: {
      async createAlbum() {
        try {
          await apiClient.post('/albums/', { title: this.title });
          alert('Album ajouté avec succès !');
        } catch (error) {
          console.error('Error creating album:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Ajoute du style ici si nécessaire */
  </style>
  