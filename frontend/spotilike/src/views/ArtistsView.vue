<template>
  <div class="artists-view">
    <h1>Artists</h1>
    <ArtistList />
  </div>
</template>

<script>
import ArtistList from "../components/ArtistList.vue";

export default {
  name: "ArtistsView",
  components: {
    ArtistList,
  },
};
</script>

<style scoped>
.artists-view {
  padding: 20px;
}
</style>
