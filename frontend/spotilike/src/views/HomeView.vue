<template>
  <v-container class="d-flex flex-column align-center justify-center text-center home-container">
    <img src="/logo.png" alt="Logo Spotilike" width="120" class="mb-5 logo">
    <h1 class="text-h4 text-white">Bienvenue sur Spotilike</h1>
    <div class="mt-5">
      <v-btn color="primary" class="mr-3" to="/albums">Liste des albums</v-btn>
      <v-btn color="secondary" to="/artists">Liste des artistes</v-btn>
    </div>
    <p class="text-white mt-10">Fait par BELLER Willy et PREMI Carl</p>
  </v-container>
</template>

<style scoped>
.home-container {
  min-height: 50vh;
  display: flex;
  justify-content: flex-start;
  padding-top: 4vh;
}
</style>