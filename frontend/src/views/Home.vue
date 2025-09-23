<template>
  <div class="home-page">
    <n-grid :cols="isMobile ? 1 : 3" :x-gap="24" :y-gap="24">
      <n-gi :span="isMobile ? 1 : 2">
        <n-card title="欢迎" size="small">
          <h3 style="margin-top:0">Hi, {{ username }}</h3>
          <p>继续你的学习旅程，或开始新的练习匹配。</p>
          <n-space>
            <n-button type="primary" size="small">开始练习</n-button>
            <n-button size="small" @click="logout">登出</n-button>
          </n-space>
        </n-card>
        <n-card title="动态" size="small" style="margin-top:24px">
          <ul class="activity">
            <li v-for="a in activity" :key="a.id">{{ a.text }}</li>
          </ul>
        </n-card>
      </n-gi>
      <n-gi>
        <n-card title="项目简介" size="small" class="about">
          <p>Educative Demo 展示账号认证、匹配与练习模块的基础骨架。后续可扩展讨论区、成就体系、排行榜等。</p>
          <n-divider />
          <n-space vertical size="small">
            <n-progress type="line" :percentage="42" indicator-placement="inside" processing />
            <small>示例进度：Learning Path Alpha</small>
          </n-space>
        </n-card>
      </n-gi>
    </n-grid>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { NCard, NButton, NSpace, NGrid, NGi, NDivider, NProgress } from 'naive-ui';

const username = ref('用户');
const router = useRouter();
const activity = ref<Array<{id:number; text:string}>>([
  { id:1, text:'你创建了匹配请求 #24' },
  { id:2, text:'系统为你推荐 3 位协作学习者' },
  { id:3, text:'完成示例练习「SQL 入门」' }
]);
const isMobile = computed(() => window.innerWidth < 860);

onMounted(async () => {
  const token = localStorage.getItem('auth_token');
  if (!token) {
    router.push('/');
    return;
  }
  try {
    const r = await axios.get('/api/auth/me', { params: { token } });
    username.value = r.data.username;
    // if user has default/newuser tags, redirect to tag selection
    const tags = r.data.interest_tags || '';
    if (!tags || tags === '#newuser' || tags === 'None') {
      router.push('/tags');
      return;
    }
  } catch (e) {
    console.error(e);
    router.push('/');
  }
});

function logout() {
  localStorage.removeItem('auth_token');
  router.push('/');
}
</script>

<style scoped>
.activity { list-style:none; padding:0; margin:0; font-size:.85rem; display:flex; flex-direction:column; gap:6px; }
.activity li { padding:4px 0; border-bottom:1px solid rgba(0,0,0,.06); }
html.dark .activity li { border-color:rgba(255,255,255,.08); }
.about small { opacity:.7; }
</style>
