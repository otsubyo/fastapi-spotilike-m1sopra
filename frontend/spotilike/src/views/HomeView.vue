<template>
    <div class="home">
      <h1>Welcome to Spotilike</h1>
      <p>Explore our collection of music albums and artists.</p>
      <router-link to="/albums" class="btn">View Albums</router-link>
      <router-link to="/artists" class="btn">View Artists</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: "HomeView",
  };
  </script>
  
  <style scoped>
  .btn {
    margin: 10px;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 5px;
  }
  </style>
  