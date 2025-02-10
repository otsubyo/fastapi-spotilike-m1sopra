<template>
  <v-container class="artist-container">
    <v-btn color="primary" to="/artists" class="mb-3">⬅ Retour à la liste des artistes</v-btn>

    <v-row>
      <v-col cols="12" md="4">
        <!-- Image de l'artiste -->
        <img :src="artist.avatar" alt="Artist Avatar" class="artist-avatar">
      </v-col>

      <v-col cols="12" md="8">
        <!-- Informations de l'artiste -->
        <h1 class="text-h4 font-weight-bold text-white">{{ artist.name }}</h1>
        <p class="text-body-1 text-white">{{ artist.biography }}</p>
      </v-col>
    </v-row>

    <!-- Liste des albums -->
    <h2 class="text-h5 mt-5 text-white">Albums de l'artiste</h2>
    <v-row v-if="albums.length > 0">
      <v-col v-for="album in albums" :key="album.album_id" cols="12" sm="6" md="4">
        <v-card class="album-card">
          <v-img :src="album.cover" height="200px" contain></v-img>
          <v-card-title class="text-white">{{ album.title }}</v-card-title>
          <v-card-subtitle class="text-white">Sorti le {{ album.release_date }}</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
    <p v-else class="text-body-2 text-white">Aucun album trouvé.</p>

    <!-- Liste des morceaux -->
    <h2 class="text-h5 mt-5 text-white">Morceaux de l'artiste</h2>
    <v-row v-if="tracks.length > 0">
      <v-col v-for="track in tracks" :key="track.track_id" cols="12" sm="6" md="4">
        <v-card class="track-card">
          <v-card-title class="text-white">{{ track.title }}</v-card-title>
          <v-card-subtitle class="text-white">{{ formatDuration(track.duration) }}</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
    <p v-else class="text-body-2 text-white">Aucun morceau trouvé.</p>
  </v-container>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { getArtist, getArtistSongs, getArtistAlbums } from "@/api"; // Ajout de `getArtistAlbums`

export default {
  setup() {
    const route = useRoute();
    const artist = ref({});
    const albums = ref([]); // 🔹 Liste des albums
    const tracks = ref([]);

    onMounted(async () => {
      const artistId = route.params.id;
      try {
        // ✅ Récupère les infos de l'artiste
        const response = await getArtist(artistId);
        artist.value = response.data;

        // ✅ Récupère les albums de l'artiste
        const albumsResponse = await getArtistAlbums(artistId);
        albums.value = albumsResponse.data || [];

        // ✅ Récupère les morceaux de l'artiste
        const tracksResponse = await getArtistSongs(artistId);
        tracks.value = tracksResponse.data || [];
      } catch (error) {
        console.error("Erreur lors du chargement des détails de l'artiste :", error);
      }
    });

    const formatDuration = (duration) => {
      if (!duration) return "Durée inconnue";
      const minutes = Math.floor(duration / 60);
      const seconds = duration % 60;
      return `${minutes} min ${seconds.toString().padStart(2, "0")} sec`;
    };

    return { artist, albums, tracks, formatDuration };
  }
};
</script>

<style scoped>
.artist-container {
  padding: 20px;
}

.artist-avatar {
  border-radius: 8px;
  width: 100%; /* Ajuste à la largeur du conteneur */
  max-width: 250px; /* Taille maximale */
  height: 250px; /* Fixe la hauteur pour uniformiser */
  object-fit: cover; /* Assure que l’image remplit bien le cadre */
  display: block;
  margin: 0 auto; /* Centre l'image horizontalement */
}

.album-card, .track-card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 10px;
}

.artist-container {
  padding: 20px;
  max-width: 1200px;
  margin: auto;
}

/* Image de l'artiste */
.artist-avatar {
  border-radius: 8px;
  width: 100%;
  max-width: 250px;
  height: 250px;
  object-fit: cover;
  display: block;
  margin: 0 auto;
}

/* Centrage des infos de l'artiste */
.artist-info {
  text-align: center;
}

/* Section albums et morceaux */
.album-list,
.track-list {
  margin-top: 30px;
}

/* Cartes des albums et morceaux */
.album-card,
.track-card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 15px;
  text-align: center;
}

/* Image des albums */
.album-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
}

/* Organisation des morceaux */
.track-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  justify-content: center;
}

.track-card {
  width: 300px;
  padding: 10px;
}

/* Titres en blanc */
.text-white {
  color: white;
}

</style>
