<template>
  <v-container class="d-flex flex-column align-center justify-center text-center home-container">
    <!-- Logo -->
    <img src="/logo.png" alt="Logo Spotilike" width="120" class="mb-5 logo">

    <!-- Titre -->
    <h1 class="text-h4 text-white">Bienvenue sur Spotilike</h1>

    <!-- Boutons -->
    <div class="mt-5 button-group">
      <v-btn color="primary" variant="elevated" class="mr-3" to="/albums">Liste des albums</v-btn>
      <v-btn color="secondary" variant="elevated" to="/artists">Liste des artistes</v-btn>
    </div>

    <!-- Signature -->
    <p class="text-white mt-10 signature">Fait par <span class="author">BELLER Willy</span> et <span class="author">PREMI Carl</span></p>
  </v-container>
</template>

<style scoped>
/* Conteneur principal */
.home-container {
  min-height: 60vh;  /* Augmente la hauteur pour un meilleur centrage */
  display: flex;
  justify-content: center;
  padding-top: 15vh;
}

/* Ajustement des boutons */
.button-group {
  display: flex;
  gap: 15px;
}

/* Signature */
.signature {
  font-size: 14px;
  opacity: 0.8;
}

.author {
  font-weight: bold;
  color: #1db954;  /* Met en valeur les noms */
}
</style>
