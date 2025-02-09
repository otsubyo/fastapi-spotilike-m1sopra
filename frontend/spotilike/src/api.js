import axios from 'axios';

const API_URL = 'http://localhost:8000/api'; // Assure-toi que c'est bien l'URL de ton backend

// 🔹 Récupérer tous les albums
export const getAlbums = () => axios.get(`${API_URL}/albums/`);

// 🔹 Récupérer un album par ID
export const getAlbum = (id) => axios.get(`${API_URL}/albums/${id}`);

// 🔹 Récupérer tous les artistes
export const getArtists = () => axios.get(`${API_URL}/artists/`);

// 🔹 Récupérer un artiste par ID
export const getArtist = (id) => axios.get(`${API_URL}/artists/${id}`);

// 🔹 Récupérer les morceaux d’un album
export const getAlbumSongs = (albumId) => axios.get(`${API_URL}/albums/${albumId}/songs`);

// 🔹 Récupérer les morceaux d’un artiste
export const getArtistSongs = (artistId) => axios.get(`${API_URL}/artists/${artistId}/songs`);
