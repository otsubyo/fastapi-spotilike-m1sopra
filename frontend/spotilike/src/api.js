import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const getAlbums = async () => {
  try {
    const response = await axios.get(`${API_URL}/albums/`);
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la récupération des albums :", error);
    return []; // Renvoie un tableau vide en cas d'erreur
  }
};

export const getAlbumSongs = async (albumId) => {
  return axios.get(`http://localhost:8000/api/albums/${albumId}/songs`);
};

export const getAlbum = (id) => axios.get(`${API_URL}/albums/${id}`);
export const getArtists = () => axios.get(`${API_URL}/artists/`);

export const getArtistAlbums = (artistId) => {
  return axios.get(`${API_URL}/artists/${artistId}/albums`);
};

// Récupérer un artiste par son ID
export const getArtist = (id) => {
  return axios.get(`http://localhost:8000/api/artists/${id}`);
};

// Récupérer les morceaux d'un artiste
export const getArtistSongs = (id) => {
  return axios.get(`${API_URL}/artists/${id}/songs`);
};

