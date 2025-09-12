<template>
  <div>
    <h2>登录</h2>
    <div class="mdui-textfield mdui-textfield-floating-label">
      <label class="mdui-textfield-label">用户名</label>
      <input class="mdui-textfield-input" v-model="username" />
    </div>
    <div class="mdui-m-t-2">
      <button class="mdui-btn mdui-color-theme mdui-ripple" @click="login">登录</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data(){ return { username: '' } },
  methods:{
    login(){
      fetch('/api/login', { method: 'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ username: this.username }) })
        .then(r=>r.json()).then(d=>{
          if (d.token){ localStorage.setItem('edu_token', d.token); this.$router.push('/favor') }
          else { alert('登录失败') }
        }).catch(()=>alert('网络错误'))
    }
  }
}
</script>
