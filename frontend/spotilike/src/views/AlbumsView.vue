<template>
  <div class="albums-view">
    <h1>Albums</h1>
    <AlbumList />
  </div>
</template>

<script>
import AlbumList from "../components/AlbumList.vue";

export default {
  name: "AlbumsView",
  components: {
    AlbumList,
  },
};
</script>

<style scoped>
.albums-view {
  padding: 20px;
}
</style>
