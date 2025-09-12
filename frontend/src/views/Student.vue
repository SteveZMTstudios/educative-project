<template>
  <div>
    <h2>学生面板</h2>
    <div>
      <button class="mdui-btn mdui-ripple mdui-color-theme" @click="loadRecommendations">加载推荐</button>
    </div>
    <div class="mdui-list mdui-m-t-2">
      <div v-if="loading">加载中...</div>
      <div v-else>
        <a class="mdui-list-item" v-for="r in recommendations" :key="r.id">
          <div class="mdui-list-item-content">
            <div class="mdui-list-item-title">{{ r.title }}</div>
            <div class="mdui-list-item-text">标签: {{ r.tag || r.score }}</div>
          </div>
        </a>
        <div v-if="recommendations.length===0" class="mdui-typo-caption">暂无推荐</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Student',
  data(){ return { recommendations: [], loading: false } },
  methods:{
    loadRecommendations(){
      this.loading = true
      fetch('/api/recommend', { headers: { 'Authorization': 'Bearer ' + (localStorage.getItem('edu_token')||'') } })
        .then(r=>r.json()).then(d=>{ this.recommendations = d.recommendations || [] })
        .catch(()=>{ this.recommendations = [] })
        .finally(()=>{ this.loading = false })
    }
  }
}
</script>
