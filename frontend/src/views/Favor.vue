<template>
  <div>
    <h2>选择学习计划</h2>
    <div class="mdui-list">
      <a class="mdui-list-item" @click.prevent="select('python')">Python 入门</a>
      <a class="mdui-list-item" @click.prevent="select('linux')">Linux 基础</a>
      <a class="mdui-list-item" @click.prevent="select('logic')">逻辑思维</a>
    </div>
    <div class="mdui-m-t-2">
      <button class="mdui-btn mdui-color-theme" @click="$router.push('/')">完成</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Favor',
  methods:{ 
    select(p){ 
      // persist preference tags to localStorage for client-side recommender
      const key = 'edu_user_prefer_tags'
      let arr = JSON.parse(localStorage.getItem(key) || '[]')
      if(!arr.includes(p)) arr.push(p)
      localStorage.setItem(key, JSON.stringify(arr))
      alert('已选择：' + p)
    } 
  }
}
</script>
