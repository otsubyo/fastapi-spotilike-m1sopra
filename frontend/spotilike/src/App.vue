<template>
  <v-app>
    <!-- 🔹 Barre de navigation -->
    <v-app-bar app color="black" dark>
      <v-container class="d-flex align-center">
        <!-- Logo -->
        <v-img src="/assets/logo.png" max-width="40" class="mr-3"></v-img>

        <!-- Navigation -->
        <v-btn text to="/">Accueil</v-btn>
        <v-btn text to="/albums">Liste des albums</v-btn>
        <v-btn text to="/artists">Liste des artistes</v-btn>

        <v-spacer></v-spacer>
      </v-container>
    </v-app-bar>

    <!-- 🔹 Contenu principal -->
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>
