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
  try {
    const response = await axios.get(`${API_URL}/albums/${albumId}/songs`);
    return response.data;
  } catch (error) {
    console.error(`Erreur lors de la récupération des chansons de l'album ${albumId}:`, error);
    return []; // Renvoie un tableau vide si l'album n'a pas de chansons
  }
};

export const getAlbum = (id) => axios.get(`${API_URL}/albums/${id}`);
export const getArtists = () => axios.get(`${API_URL}/artists/`);

// Récupérer un artiste par son ID
export const getArtist = (id) => {
  return axios.get(`http://localhost:8000/api/artists/${id}`);
};

// Récupérer les morceaux d'un artiste
export const getArtistSongs = (id) => {
  return axios.get(`${API_URL}/artists/${id}/songs`);
};

