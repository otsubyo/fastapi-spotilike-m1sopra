<template>
  <div id="app">
    <Navbar />
    <router-view />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';

export default {
  name: 'App',
  components: {
    Navbar,
  },
};
</script>

<style>
#app {
  font-family: Arial, Helvetica, sans-serif;
  background-color: #f5f5f5;
  padding: 20px;
}

nav {
  margin-bottom: 20px;
}

h1 {
  font-size: 2em;
  color: #333;
}
</style>
