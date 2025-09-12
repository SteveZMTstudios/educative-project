<template>
  <div>
    <header class="mdui-appbar mdui-appbar-fixed">
      <div class="mdui-toolbar mdui-color-theme">
        <a class="mdui-typo-title" href="#/">智能个性化学习平台</a>
        <div class="mdui-toolbar-spacer"></div>
        <router-link to="/login" class="mdui-btn mdui-btn-icon"><i class="mdui-icon material-icons">login</i></router-link>
      </div>
    </header>
    <main class="mdui-container mdui-m-t-6">
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body { padding-top: 56px; }
.mdui-container { max-width: 960px; margin: 0 auto; }
</style>
