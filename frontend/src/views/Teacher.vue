<template>
  <div>
    <h2>教师面板</h2>
    <p>教师可以发布作业、查看学生提交、打分和推送练习（占位）。</p>
    <div class="mdui-card mdui-p-a-2 mdui-m-t-2">
      <h3>发布作业</h3>
      <div class="mdui-textfield mdui-textfield-floating-label">
        <label class="mdui-textfield-label">标题</label>
        <input class="mdui-textfield-input" v-model="title" />
      </div>
      <div class="mdui-textfield mdui-textfield-floating-label mdui-m-t-2">
        <label class="mdui-textfield-label">描述</label>
        <textarea class="mdui-textfield-input" v-model="description"></textarea>
      </div>
      <div class="mdui-m-t-2">
        <button class="mdui-btn mdui-color-theme" @click="publish">发布</button>
      </div>
    </div>
    <div class="mdui-m-t-2">
      <h3>已发布作业</h3>
      <ul>
        <li v-for="a in assignments" :key="a.id">#{{a.id}} - {{a.title}} by {{a.author}}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Teacher',
  data(){ return { title:'', description:'', assignments: [] } },
  created(){ this.fetchAssignments() },
  methods:{
    authHeader(){ const t = localStorage.getItem('edu_token'); return t? { Authorization: 'Bearer '+t } : {} },
    fetchAssignments(){ import('../utils/safeJson').then(mod=>{ fetch('/api/assignments', { headers: this.authHeader() }).then(async r=>{ const d = await mod.safeJson(r); if (!r.ok) throw new Error(d.error||'获取作业失败'); this.assignments = d.assignments || [] }).catch(()=>{}) }) },
    publish(){ import('../utils/safeJson').then(mod=>{ fetch('/api/assignments', { method:'POST', headers: Object.assign({'Content-Type':'application/json'}, this.authHeader()), body: JSON.stringify({ title:this.title, description:this.description }) })
      .then(async r=>{ const d = await mod.safeJson(r); if (!r.ok) throw new Error(d.error||'发布失败'); return d })
      .then(()=>{ this.title=''; this.description=''; this.fetchAssignments(); alert('发布成功') })
      .catch(e=>alert(e.message)) }) }
  }
}
</script>
