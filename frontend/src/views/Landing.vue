<template>
  <div class="landing">
    <section class="hero">
      <div class="hero-content">
        <h1 class="gradient">让学习与协作更高效</h1>
        <p class="tagline">Educative Project 汇聚练习、匹配与个性化学习路径，并为教学和协作带来前所未有的体验。</p>
        <n-space :size="16">
          <n-button type="primary" size="large" @click="goRegister">免费注册</n-button>
          <n-button tertiary size="large" @click="goLogin">已有账户? 登录</n-button>
        </n-space>
        <p class="mini-hint">注册后即可创建练习、参与匹配、跟踪成长轨迹。</p>
      </div>
      <div class="hero-visual">
        <n-card size="small" class="code-card" embedded>
<pre><code>// Match Engine
async function match(user){
  const pool = await fetchCandidates();
  return pool.filter(p => overlap(p.skills, user.target));
}</code></pre>
        </n-card>
      </div>
    </section>

    <section class="features">
      <n-grid :x-gap="24" :y-gap="24" :cols="isMobile ? 1 : 3">
        <n-gi v-for="f in features" :key="f.title">
          <n-card :title="f.title" size="small" class="feature-card">
            <p>{{ f.desc }}</p>
          </n-card>
        </n-gi>
      </n-grid>
    </section>

    <section class="github-like">
      <n-card size="small" title="项目概览" class="repo-card">
        <n-space vertical :size="8">
          <div class="stat-line">
            <n-tag type="info" size="small">Alpha</n-tag>
            <span>开源演示 · FastAPI + Vue 3 + Naive UI</span>
          </div>
          <n-space :size="24">
            <div class="metric"><strong>{{ stars }}</strong><span>Stars</span></div>
            <div class="metric"><strong>{{ activeUsers }}</strong><span>活跃用户</span></div>
            <div class="metric"><strong>{{ exercises }}</strong><span>示例练习</span></div>
          </n-space>
          <n-divider />
          <p class="repo-desc">后端使用 FastAPI + SQLite，前端采用 Vite + Vue3 Composition API，并集成 Naive UI 主题切换与响应式设计。</p>
          <n-space>
            <n-button size="small" tertiary tag="a" href="https://github.com" target="_blank">GitHub 仓库</n-button>
            <n-button size="small" quaternary @click="goRegister">立即试用</n-button>
          </n-space>
        </n-space>
      </n-card>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { NButton, NSpace, NCard, NGrid, NGi, NTag, NDivider } from 'naive-ui';

const router = useRouter();
function goRegister(){ router.push('/register'); }
function goLogin(){ router.push('/login'); }

const stars = ref(128);
const activeUsers = ref(42);
const exercises = ref(12);

const features = [
  { title: '自适应匹配', desc: '基于标签 & 技能的用户匹配示例，展示协作式学习可能性。' },
  { title: '安全认证', desc: '演示注册 / 登录 / Token 校验流程，可扩展 OAuth。' },
  { title: '可扩展架构', desc: '清晰分层：API / Service / Schema，便于继续添加练习与讨论模块。' },
  { title: '主题与暗色模式', desc: '内置 Naive UI 主题切换，夜间学习更舒适。' },
  { title: '前后端分离', desc: 'FastAPI 提供 JSON API，前端 Vue3 + Vite 快速开发。' },
  { title: '示例工程实践', desc: '可作为入门脚手架：账号、路由、布局、组件化模式。' }
];

const isMobile = computed(() => window.innerWidth < 860);
onMounted(() => {
  window.addEventListener('resize', () => {});
});
</script>

<style scoped>
.landing { display:flex; flex-direction:column; gap:64px; }
.hero { display:grid; gap:48px; grid-template-columns:repeat(auto-fit,minmax(320px,1fr)); align-items:center; }
.hero-content { display:flex; flex-direction:column; gap:24px; }
.gradient { font-size:clamp(2.2rem,6vw,3.4rem); line-height:1.1; background:linear-gradient(90deg,#6366f1,#8b5cf6,#ec4899); -webkit-background-clip:text; background-clip:text; color:transparent; font-weight:700; }
.tagline { font-size:1.125rem; max-width:46ch; color:var(--n-text-color-2); }
.mini-hint { font-size:.75rem; opacity:.7; }
.hero-visual { position:relative; }
.code-card { font-family:ui-monospace, SFMono-Regular, Menlo, monospace; }
pre { margin:0; font-size:.75rem; line-height:1.4; }
.feature-card { height:100%; }
.repo-card .metric { display:flex; flex-direction:column; font-size:.75rem; gap:2px; }
.repo-card .metric strong { font-size:1.1rem; }
.stat-line { display:flex; align-items:center; gap:12px; font-size:.8rem; }
@media (max-width: 860px){
  .hero { grid-template-columns:1fr; }
  .hero-visual { order:-1; }
}
</style>
