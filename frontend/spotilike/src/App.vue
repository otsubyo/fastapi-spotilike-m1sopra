<template>
  <div class="min-h-screen bg-black text-white">
    <nav class="bg-green-900 p-4">
      <div class="container mx-auto flex justify-between items-center">
        <router-link to="/" class="text-2xl font-bold">MusicApp</router-link>
        <div class="space-x-4">
          <router-link to="/albums" class="hover:text-green-400">Albums</router-link>
          <router-link to="/artists" class="hover:text-green-400">Artists</router-link>
        </div>
      </div>
    </nav>

    <main class="container mx-auto p-4">
      <router-view></router-view>
    </main>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style>
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
</style>