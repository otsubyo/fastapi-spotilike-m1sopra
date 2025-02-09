import axios from 'axios';

const API_URL = 'http://localhost:8000/api'; // Assure-toi que le backend est bien lancé !

export const getAlbums = () => axios.get(`${API_URL}/albums/`);
export const getAlbum = (id) => axios.get(`${API_URL}/albums/${id}`);
export const getArtists = () => axios.get(`${API_URL}/artists/`);
export const getArtist = (id) => axios.get(`${API_URL}/artists/${id}`);
export const getAlbumSongs = (albumId) => axios.get(`${API_URL}/albums/${albumId}/songs`);
export const getArtistSongs = (artistId) => axios.get(`${API_URL}/artists/${artistId}/songs`);