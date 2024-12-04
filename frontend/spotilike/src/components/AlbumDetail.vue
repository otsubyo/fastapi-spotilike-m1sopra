<template>
  <div v-if="album">
    <div class="flex flex-col md:flex-row gap-8">
      <img :src="album.cover" :alt="album.title" class="w-full md:w-1/3 rounded-lg shadow-lg">
      <div>
        <h1 class="text-4xl font-bold mb-4">{{ album.title }}</h1>
        <p class="text-xl mb-2">Artist: {{ album.artist.name }}</p>
        <p class="text-gray-400">Release Date: {{ album.release_date }}</p>
        <h2 class="text-2xl font-semibold mt-6 mb-4">Tracks</h2>
        <ul class="space-y-2">
          <li v-for="track in album.tracks" :key="track.id" class="flex justify-between items-center bg-gray-800 p-3 rounded">
            <span>{{ track.title }}</span>
            <span class="text-gray-400">{{ formatDuration(track.duration) }}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const album = ref(null)

onMounted(async () => {
  // Fetch album details from your API
  const response = await fetch(`http://your-api-url/api/albums/${route.params.id}`)
  album.value = await response.json()
})

const formatDuration = (duration) => {
  // Implement duration formatting logic here
  return duration
}
</script>