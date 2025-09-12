<template>
  <div>
    <h2>{{ course.title || '课程详情' }}</h2>
    <div class="mdui-typo-caption">标签: {{ course.tags ? course.tags.join(', ') : '' }}</div>
    <p>{{ course.description }}</p>

    <div class="mdui-m-t-2">
      <button class="mdui-btn mdui-color-theme" @click="openShell">打开快速 Shell 环境</button>
      <button class="mdui-btn" @click="$router.back()">返回</button>
    </div>

    <div v-if="showShell" class="mdui-m-t-2">
      <p class="mdui-typo-caption">如果页面未加载，请等待或尝试刷新（嵌入的是 jslinux 的快速示例）。</p>
      <!-- 使用 jslinux 提供的在线 demo iframe（注意：外部站点可能有 iframe 限制） -->
      <iframe :src="jslinuxUrl" style="width:100%;height:600px;border:1px solid #ddd" />
    </div>

  </div>
</template>

<script>
const COURSES_KEY = 'edu_courses'
export default {
  name: 'CourseDetail',
  data(){
    return { course: {}, showShell:false }
  },
  computed:{
    jslinuxUrl(){
      // 使用 jslinux 的 demo url（web 端），这是一个通用的 busybox demo
      return 'https://bellard.org/jslinux/vm.html?arch=x86&mem=64' // 可替换为更合适的页面
    }
  },
  created(){
    const id = this.$route.params.id
    try{ const arr = JSON.parse(localStorage.getItem(COURSES_KEY) || '[]')
      this.course = arr.find(c=>c.id===id) || { id }
    }catch(e){ this.course = { id } }
  },
  methods:{ openShell(){ this.showShell = true } }
}
</script>

<style>
</style>
