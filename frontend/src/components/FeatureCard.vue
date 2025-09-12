<template>
  <div class="mdui-card">
    <div v-if="img" class="mdui-card-media">
      <img :src="img" style="width:100%" />
    </div>
    <div class="mdui-card-primary">
      <div class="mdui-card-primary-title">{{ title }}</div>
      <div class="mdui-card-primary-subtitle">{{ subtitle }}</div>
    </div>
    <div class="mdui-card-actions">
      <slot name="actions"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FeatureCard',
  props: { title: String, subtitle: String, img: String }
}
</script>
