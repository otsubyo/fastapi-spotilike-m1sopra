<template>
  <div id="app">
    <!-- Navbar component for navigation -->
    <Navbar />
    
    <!-- Main Content Area, where the routed views are injected -->
    <router-view></router-view>
  </div>
</template>

<script>
// Import the global Navbar component
import Navbar from './components/Navbar.vue';

export default {
  name: 'App',
  components: {
    Navbar, // Registering Navbar as a child component of App
  },
};
</script>

<style>
/* Global Styles for the App */

#app {
  font-family: 'Arial', sans-serif;
  text-align: center;
  background-color: #f8f8f8;
  padding-top: 20px;
}

/* Navbar specific styling */
nav {
  background-color: #333;
  padding: 15px;
}

router-link {
  color: white;
  margin: 0 20px;
  text-decoration: none;
}

router-link:hover {
  background-color: #555;
  padding: 10px;
  border-radius: 5px;
}

#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  max-width: 1200px;
}
</style>
