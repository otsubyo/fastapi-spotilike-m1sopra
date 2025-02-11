<template>
  <v-container>
    <v-btn color="primary" to="/albums" class="mb-4">
  <img src="/iconmonstr-arrow-left-alt-lined-240.png" alt="Retour" class="arrow-icon">
  Retour à la liste des albums
    </v-btn>
    

    <v-row>
      <!-- Image de l'album -->
      <v-col cols="12" md="4">
        <v-img v-if="album.cover" :src="album.cover" alt="Album Cover" height="300px" contain></v-img>
        <v-img v-else src="/static/images/albums/default.jpg" alt="Image par défaut" height="300px" contain></v-img>
      </v-col>

      <!-- Informations de l'album -->
      <v-col cols="12" md="8" class="d-flex flex-column align-start">
        <h1 class="text-h4 font-weight-bold text-white">
          {{ album.title || "Titre non disponible" }}
        </h1>
        <p class="text-white text-subtitle-1">Date de sortie : {{ album.release_date || "Date non disponible" }}</p>
        <p class="text-white text-subtitle-1">Artiste : {{ album.artist || "Inconnu" }}</p>
        <p class="text-white text-subtitle-1">Genre : {{ album.genres ? album.genres.join(", ") : "Aucun" }}</p>

        <h2 class="text-h5 mt-4 text-white">Morceaux :</h2>

        <v-list v-if="album.tracks.length > 0" class="track-list">
          <v-list-item v-for="track in album.tracks" :key="track.track_id">
            <v-list-item-title class="text-white">
              {{ track.title }}
            </v-list-item-title>
            <v-list-item-subtitle class="text-white">
              {{ formatDuration(track.duration) }}
              <span v-if="track.featuring.length > 0"> (feat. {{ track.featuring.join(", ") }})</span>
            </v-list-item-subtitle>
          </v-list-item>
        </v-list>

        <p v-else class="text-white mt-4">Aucun morceau trouvé.</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getAlbumDetails } from '../api';

export default {
  setup() {
    const album = ref({ tracks: [] });
    const route = useRoute();

    onMounted(async () => {
      const albumId = route.params.id;

      try {
        // 🔍 Récupérer les détails de l'album
        const albumRes = await getAlbumDetails(albumId);
        album.value = albumRes.data || {};
      } catch (error) {
        console.error("❌ Erreur lors du chargement des données :", error);
      }
    });

    const formatDuration = (duration) => {
      const [hours, minutes, seconds] = duration.split(":").map(Number);

  if (hours > 0) {
    return `${hours}h ${minutes}m ${seconds.toString().padStart(2, "0")}s`;
  }
  return `${minutes} min ${seconds.toString().padStart(2, "0")} sec`;
  };

  return {
    album,
    formatDuration
  };
}
};
</script>

<style scoped>
.album-details {
  min-height: 100vh;
  padding-top: 20px;
  padding-bottom: 40px;
}

.track-list {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 10px;
}

/* Ajoute un espacement et centre la liste */
.track-container {
  max-width: 600px;
  margin-top: 20px;
  text-align: center;
}

/* Stylisation de la liste des morceaux */
.track-list {
  width: 100%;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}

.album-cover {
  border-radius: 8px;
}

.track-list {
  background: rgba(255, 255, 255, 0.1); /* Fond semi-transparent */
  border-radius: 8px;
  padding: 10px;
  max-width: 400px; /* Ajuster la largeur pour ne pas prendre toute la page */
}

.track-item {
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.track-item:last-child {
  border-bottom: none;
}

.arrow-icon {
  width: 20px;  /* Taille contrôlée pour la flèche */
  height: 20px;
  margin-right: 8px;  /* Ajoute un espace entre l'icône et le texte */
}
</style>
