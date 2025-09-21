<template>
  <div>
    <h2>注册</h2>
    <div class="mdui-textfield mdui-textfield-floating-label">
      <label class="mdui-textfield-label">用户名</label>
      <input class="mdui-textfield-input" v-model="username" />
    </div>
    <div class="mdui-textfield mdui-textfield-floating-label mdui-m-t-2">
      <label class="mdui-textfield-label">密码</label>
      <input type="password" class="mdui-textfield-input" v-model="password" />
    </div>
    <div class="mdui-textfield mdui-textfield-floating-label mdui-m-t-2">
      <label class="mdui-textfield-label">角色</label>
      <select v-model="role" class="mdui-select">
        <option value="student">学生</option>
        <option value="teacher">教师</option>
      </select>
    </div>
    <div class="mdui-m-t-2">
      <button class="mdui-btn mdui-color-theme" @click="register">创建账号</button>
      <router-link to="/login" class="mdui-btn mdui-ml-2">返回登录</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data(){ return { username:'', password:'', role:'student' } },
  methods:{
    register(){
      import('../utils/safeJson').then(mod=>{
        fetch('/api/auth/register', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ username:this.username, password:this.password, role:this.role }) })
          .then(async r=>{ const d = await mod.safeJson(r); if (!r.ok) throw new Error(d.error||'注册失败'); return d })
          .then(()=>{ alert('注册成功，请登录'); this.$router.push('/login') })
          .catch(e=>alert(e.message || '注册失败'))
      })
    }
  }
}
</script>
