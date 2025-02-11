import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

/* ===========================
   GESTION DES ALBUMS
=========================== */

// Récupérer tous les albums
export const getAlbums = async () => {
  try {
    const response = await axios.get(`${API_URL}/albums/`);
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la récupération des albums :", error);
    return []; // Renvoie un tableau vide en cas d'erreur
  }
};

// Récupérer un album spécifique par son ID
export const getAlbum = (id) => {
  return axios.get(`${API_URL}/albums/${id}`);
};

// Récupérer les morceaux d'un album spécifique
export const getAlbumSongs = (albumId) => {
  return axios.get(`${API_URL}/albums/${albumId}/songs`);
};

// Récupérer les détails d'un album (genres, artistes, feats...)
export const getAlbumDetails = (albumId) => {
  return axios.get(`${API_URL}/albums/${albumId}/details`);
};

/* ===========================
   GESTION DES ARTISTES
=========================== */

// Récupérer tous les artistes
export const getArtists = () => {
  return axios.get(`${API_URL}/artists/`);
};

// Récupérer un artiste spécifique par son ID
export const getArtist = (id) => {
  return axios.get(`${API_URL}/artists/${id}`);
};

// Récupérer les albums d'un artiste
export const getArtistAlbums = (artistId) => {
  return axios.get(`${API_URL}/artists/${artistId}/albums`);
};

// Récupérer les morceaux d'un artiste
export const getArtistSongs = (id) => {
  return axios.get(`${API_URL}/artists/${id}/songs`);
};
