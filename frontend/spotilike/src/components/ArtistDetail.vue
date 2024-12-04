<template>
  <div v-if="artist">
    <div class="flex flex-col md:flex-row gap-8">
      <img :src="artist.avatar" :alt="artist.name" class="w-full md:w-1/3 rounded-lg shadow-lg">
      <div>
        <h1 class="text-4xl font-bold mb-4">{{ artist.name }}</h1>
        <p class="text-gray-400 mb-6">{{ artist.biography }}</p>
        <h2 class="text-2xl font-semibold mb-4">Albums</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
          <div v-for="album in artist.albums" :key="album.id" class="bg-gray-800 rounded-lg overflow-hidden shadow-lg">
            <img :src="album.cover" :alt="album.title" class="w-full h-32 object-cover">
            <div class="p-3">
              <h3 class="font-semibold">{{ album.title }}</h3>
              <p class="text-gray-400 text-sm">{{ album.release_date }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const artist = ref(null)

onMounted(async () => {
  // Fetch artist details from your API
  const response = await fetch(`http://your-api-url/api/artists/${route.params.id}`)
  artist.value = await response.json()
})
</script>