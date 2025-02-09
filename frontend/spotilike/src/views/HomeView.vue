<template>
  <v-container class="d-flex flex-column align-center justify-center fill-height">
    <!-- Logo -->
    <v-img src="../assets/logo.png" max-width="40" class="mr-3"></v-img>

    <!-- Titre -->
    <h1 class="text-h4 font-weight-bold">Bienvenue sur Spotilike</h1>

    <!-- 🔹 Boutons bien visibles -->
    <v-btn to="/albums" color="primary" class="mt-4" size="large">Liste des albums</v-btn>
    <v-btn to="/artists" color="secondary" class="mt-4" size="large">Liste des artistes</v-btn>

    <!-- Crédit -->
    <p class="mt-6">Fait par BELLER Willy et PREMI Carl</p>
  </v-container>
</template>
