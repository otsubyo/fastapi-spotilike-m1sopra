<template>
  <v-app>
    <!-- Barre de navigation -->
    <v-app-bar app color="black">
      <v-container class="d-flex align-center justify-end">
        <!-- Logo cliquable à gauche du texte -->
        <router-link to="/">
          <img src="/logo.png" alt="Logo Spotilike" class="logo clickable">
        </router-link>

        <!-- Nom du site SPOTILIKE (à droite du logo) -->
        <span class="spotilike-text">SPOTILIKE</span>

        <!-- Espacement pour séparer le logo + texte du menu -->
        <v-spacer></v-spacer>

        <!-- Menu de navigation aligné à droite -->
        <div class="d-flex">
          <v-btn variant="text" to="/" class="text-white">Accueil</v-btn>
          <v-btn variant="text" to="/albums" class="text-white">Liste des albums</v-btn>
          <v-btn variant="text" to="/artists" class="text-white">Liste des artistes</v-btn>
        </div>
      </v-container>
    </v-app-bar>

    <!-- Contenu dynamique selon la route -->
    <v-main class="main-content">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>




<style scoped>
/* 🌟 Fond dégradé de la page */
.main-content {
  background: linear-gradient(to bottom, #1db954, #000);
  min-height: 100vh;
}

/* 🎨 Style du texte "SPOTILIKE" */
.spotilike-text {
  color: white;
  font-size: 20px;
  font-weight: bold;
  text-transform: uppercase;
}

/* 🎯 Style du logo */
.logo {
  width: 40px;  /* 📏 Taille fixe */
  height: 40px;
  object-fit: contain;  /* 🔄 Garde les proportions sans déformation */
  margin-right: 15px; /* 🚀 Ajoute de l'espace entre le logo et le texte */
}

/* 🖱️ Rendre le logo cliquable */
.clickable {
  cursor: pointer;
}

</style>
