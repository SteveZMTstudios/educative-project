<template>
  <n-config-provider :theme="isDark ? darkTheme : null" :theme-overrides="themeOverrides">
    <n-global-style />
    <n-loading-bar-provider>
      <n-dialog-provider>
        <n-message-provider>
          <div class="app-shell" :class="{ dark: isDark }">
            <header class="app-header">
              <n-space align="center" justify="space-between" style="width:100%">
                <div class="brand" @click="goHome">
                  <n-space align="center">
                    <n-avatar size="small" round>EDU</n-avatar>
                    <h1 class="logo-text">Educative</h1>
                  </n-space>
                </div>
                <n-space align="center" :size="12">
                  <n-input v-model:value="search" placeholder="搜索…" clearable size="small" style="width:200px" />
                  <n-button quaternary size="small" @click="toggleDark">
                    <template #icon>
                      <n-icon>
                        <svg v-if="isDark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3a9 9 0 0 0 0 18 1 1 0 0 1 .117 1.993L12 23A11 11 0 0 1 12 1a1 1 0 0 1 .117 1.993L12 3Z"/></svg>
                        <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 18a6 6 0 1 1 0-12 6 6 0 0 1 0 12Zm0 4a1 1 0 0 1 1 1v1h-2v-1a1 1 0 0 1 1-1Zm8-8a1 1 0 0 1 1 1h1v-2h-1a1 1 0 0 1-1 1ZM4 12a1 1 0 0 1-1-1H2v2h1a1 1 0 0 1 1-1Zm8-8a1 1 0 0 1-1-1V2h2v1a1 1 0 0 1-1 1Z"/></svg>
                      </n-icon>
                    </template>
                  </n-button>
                  <n-dropdown trigger="click" :options="menuOptions" @select="handleMenuSelect">
                    <n-button size="small" tertiary>
                      账户
                    </n-button>
                  </n-dropdown>
                </n-space>
              </n-space>
            </header>
            <main class="app-main">
              <router-view />
            </main>
            <footer class="app-footer">
              <n-space justify="space-between" style="width:100%">
                <span>© 2025 Educative Demo</span>
                <n-space size="small">
                  <a href="https://github.com" target="_blank">GitHub</a>
                  <a href="/" @click.prevent="goLanding">主页</a>
                </n-space>
              </n-space>
            </footer>
          </div>
        </n-message-provider>
      </n-dialog-provider>
    </n-loading-bar-provider>
  </n-config-provider>
</template>

<script setup lang="ts">
import { ref, watchEffect } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import {
  darkTheme,
  NConfigProvider,
  NGlobalStyle,
  NMessageProvider,
  NDialogProvider,
  NLoadingBarProvider,
  NAvatar,
  NIcon,
  NSpace,
  NButton,
  NDropdown,
  NInput
} from 'naive-ui';

const router = useRouter();
const route = useRoute();
const isDark = ref<boolean>(localStorage.getItem('color-scheme') === 'dark');
const search = ref('');

function toggleDark() {
  isDark.value = !isDark.value;
  localStorage.setItem('color-scheme', isDark.value ? 'dark' : 'light');
}

watchEffect(() => {
  document.documentElement.classList.toggle('dark', isDark.value);
});

function goHome() {
  router.push('/home');
}
function goLanding() {
  router.push('/');
}

function handleMenuSelect(key: string) {
  if (key === 'logout') {
    localStorage.removeItem('auth_token');
    router.push('/');
  } else if (key === 'home') {
    router.push('/home');
  } else if (key === 'login') {
    router.push('/login');
  }
}

import type { DropdownOption } from 'naive-ui';
function computeMenu(): DropdownOption[] {
  const authed = !!localStorage.getItem('auth_token');
  const options: DropdownOption[] = [
    { label: '主页', key: 'home' },
    !authed ? { label: '登录', key: 'login' } : { label: '登出', key: 'logout' }
  ];
  return options;
}
const menuOptions = computeMenu();

const themeOverrides = {
  common: {
    primaryColor: '#6366f1',
    primaryColorHover: '#818cf8',
    primaryColorPressed: '#4f46e5'
  }
};
</script>

<style scoped>
.app-shell { min-height:100dvh; display:flex; flex-direction:column; }
.app-header { position:sticky; top:0; z-index:20; backdrop-filter: blur(12px); background:rgba(255,255,255,.75); border-bottom:1px solid rgba(0,0,0,.08); padding:8px 24px; }
.dark .app-header { background:rgba(20,20,24,.75); border-color:rgba(255,255,255,.08); }
.logo-text { font-size:1rem; font-weight:600; letter-spacing:.5px; }
.app-main { flex:1; width:100%; max-width:1180px; margin:0 auto; padding:32px 32px 64px; }
.app-footer { padding:16px 24px; font-size:.875rem; border-top:1px solid rgba(0,0,0,.08); background:rgba(255,255,255,.65); backdrop-filter:blur(10px); }
.dark .app-footer { border-color:rgba(255,255,255,.08); background:rgba(20,20,24,.65); }
:deep(a) { color: var(--primary-color,#6366f1); text-decoration:none; }
:deep(a:hover){ text-decoration:underline; }
</style>
