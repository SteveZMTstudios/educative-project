<template>
  <div>
    <h2>登录</h2>
    <div class="mdui-textfield mdui-textfield-floating-label">
      <label class="mdui-textfield-label">用户名</label>
      <input class="mdui-textfield-input" v-model="username" />
    </div>
    <div class="mdui-textfield mdui-textfield-floating-label mdui-m-t-2">
      <label class="mdui-textfield-label">密码</label>
      <input type="password" class="mdui-textfield-input" v-model="password" />
    </div>
    <div class="mdui-m-t-2">
  <button class="mdui-btn mdui-color-theme mdui-ripple" @click="login">登录</button>
  <router-link to="/register" class="mdui-btn mdui-ml-2">注册</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data(){ return { username: '', password: '' } },
  methods:{
    login(){
      import('../utils/safeJson').then(mod=>{
        fetch('/api/auth/login', { method: 'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ username: this.username, password: this.password }) })
          .then(async r=>{
            const d = await mod.safeJson(r)
            if (!r.ok) throw new Error(d.error || '登录失败')
            return d
          })
          .then(d=>{ if (d.token){ localStorage.setItem('edu_token', d.token); this.$router.push('/favor') } })
          .catch(e=>alert(e.message || '网络错误'))
      })
    }
  }
}
</script>
