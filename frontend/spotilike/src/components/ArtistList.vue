<template>
  <div>
    <h1 class="text-3xl font-bold mb-6">All Artists</h1>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      <div v-for="artist in artists" :key="artist.id" class="bg-gray-800 rounded-lg overflow-hidden shadow-lg hover:shadow-2xl transition-shadow duration-300">
        <img :src="artist.avatar" :alt="artist.name" class="w-full h-48 object-cover">
        <div class="p-4">
          <h2 class="text-xl font-semibold mb-2">{{ artist.name }}</h2>
          <router-link :to="`/artists/${artist.id}`" class="text-green-400 hover:text-green-300">View Details</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const artists = ref([])

onMounted(async () => {
  // Fetch artists from your API
  const response = await fetch('http://your-api-url/api/artists')
  artists.value = await response.json()
})
</script>