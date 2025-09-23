<template>
  <AppLayout />
</template>

<script setup lang="ts">
import AppLayout from './components/AppLayout.vue';
</script>

<style scoped>
/* Global base styles overrides if needed */
html.dark { background:#0f1115; color:#e5e7eb; }
html, body { transition: background-color .35s ease, color .35s ease; }
</style>
