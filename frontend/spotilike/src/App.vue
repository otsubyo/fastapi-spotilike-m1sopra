<template>
  <v-app>
    <!-- Barre de navigation -->
    <v-app-bar app color="black">
      <v-container class="d-flex align-center">
        <v-btn text to="/" class="text-white">Accueil</v-btn>
        <v-btn text to="/albums" class="text-white">Liste des albums</v-btn>
        <v-btn text to="/artists" class="text-white">Liste des artistes</v-btn>

        <!-- Espaceur pour pousser le logo à droite -->
        <v-spacer></v-spacer>

        <!-- Logo en haut à droite -->
        <v-img src="/logo.png" alt="Logo Spotilike" max-height="50" max-width="50" class="mr-4"></v-img>
      </v-container>
    </v-app-bar>

    <!-- Contenu dynamique selon la route -->
    <v-main class="main-content">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<style>
.main-content {
  background: linear-gradient(to bottom, #1db954, #000);
  min-height: 100vh;
}
</style>
