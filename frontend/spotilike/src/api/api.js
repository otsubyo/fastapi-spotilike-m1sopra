import axios from 'axios';

const API_URL = 'http://localhost:8000/api';  // Assure-toi que l'URL est correcte

// Exemple de fonction pour récupérer les albums
export const getAlbums = () => {
  return axios.get(`${API_URL}/albums/`);
};

// Exemple de fonction pour récupérer un album par ID
export const getAlbum = (id) => {
  return axios.get(`${API_URL}/albums/${id}`);
};

// Exemple de fonction pour récupérer les artistes
export const getArtists = () => {
  return axios.get(`${API_URL}/artists/`);
};

// Fonction pour récupérer les chansons d'un album
export const getAlbumSongs = (albumId) => {
  return axios.get(`${API_URL}/albums/${albumId}/songs`);
};

// Fonction pour récupérer les chansons d'un artiste
export const getArtistSongs = (artistId) => {
  return axios.get(`${API_URL}/artists/${artistId}/songs`);  // Modifie cette URL en fonction de l'API backend
};
