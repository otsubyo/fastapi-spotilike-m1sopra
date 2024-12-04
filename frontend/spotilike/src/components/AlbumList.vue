<template>
  <div>
    <h1 class="text-3xl font-bold mb-6">All Albums</h1>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      <div v-for="album in albums" :key="album.id" class="bg-gray-800 rounded-lg overflow-hidden shadow-lg hover:shadow-2xl transition-shadow duration-300">
        <img :src="album.cover" :alt="album.title" class="w-full h-48 object-cover">
        <div class="p-4">
          <h2 class="text-xl font-semibold mb-2">{{ album.title }}</h2>
          <router-link :to="`/albums/${album.id}`" class="text-green-400 hover:text-green-300">View Details</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const albums = ref([])

onMounted(async () => {
  // Fetch albums from your API
  const response = await fetch('http://your-api-url/api/albums')
  albums.value = await response.json()
})
</script>