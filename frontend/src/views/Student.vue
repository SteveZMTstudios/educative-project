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
      // try backend recommend first, fallback to client-side tag matcher
      fetch('/api/recommend', { headers: { 'Authorization': 'Bearer ' + (localStorage.getItem('edu_token')||'') } })
        .then(r=>{
          if(!r.ok) throw new Error('backend fail')
          return r.json()
        }).then(d=>{ this.recommendations = d.recommendations || [] })
        .catch(()=>{ this.recommendations = this.clientRecommend() })
        .finally(()=>{ this.loading = false })
    }
    ,
    clientRecommend(){
      // load user tags and courses, score courses by tag intersection
      const tags = JSON.parse(localStorage.getItem('edu_user_prefer_tags')||'[]')
      const courses = JSON.parse(localStorage.getItem('edu_courses')||'[]')
      if(courses.length===0) return []
      if(!tags || tags.length===0) return courses.slice(0,5)
      const scored = courses.map(c=>{
        const score = c.tags.reduce((s,t)=> s + (tags.includes(t)?1:0), 0)
        return Object.assign({score}, c)
      }).filter(c=>c.score>0).sort((a,b)=>b.score-a.score)
      return scored.slice(0,10)
    }
  }
}
</script>
