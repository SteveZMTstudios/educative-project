<template>
  <div>
    <h2>课程中心</h2>

    <div class="mdui-m-b-2">
      <input v-model="filterTag" placeholder="筛选标签 (例如: python, linux)" class="mdui-textfield-input" />
      <button class="mdui-btn mdui-color-theme mdui-ripple" @click="applyFilter">筛选</button>
      <button class="mdui-btn" @click="clearFilter">清除</button>
    </div>

    <div class="mdui-row-xs-1 mdui-row-md-2">
      <div class="mdui-col" v-for="c in filteredCourses" :key="c.id">
        <FeatureCard :title="c.title" :subtitle="c.description" :img="c.img">
          <template #actions>
            <button class="mdui-btn" @click="enroll(c)">添加到我的课程</button>
            <router-link :to="`/courses/${c.id}`" class="mdui-btn mdui-ml-1">查看课程</router-link>
          </template>
        </FeatureCard>
        <div class="mdui-typo-caption">标签: {{ c.tags.join(', ') }}</div>
      </div>
    </div>

    <hr />
    <h3>教师：添加新课程</h3>
    <div>
      <input v-model="newCourse.title" placeholder="课程标题" class="mdui-textfield-input mdui-m-b-1" />
      <input v-model="newCourse.description" placeholder="一句话描述" class="mdui-textfield-input mdui-m-b-1" />
      <input v-model="newCourse.tagsInput" placeholder="标签，逗号分隔" class="mdui-textfield-input mdui-m-b-1" />
      <input v-model="newCourse.img" placeholder="封面图片 URL (可选)" class="mdui-textfield-input mdui-m-b-1" />
      <button class="mdui-btn mdui-color-theme" @click="addCourse">添加课程</button>
    </div>
  </div>
</template>

<script>
import FeatureCard from '../components/FeatureCard.vue'

const STORAGE_KEY = 'edu_courses'

export default {
  name: 'Courses',
  components: { FeatureCard },
  data(){
    return {
      courses: [],
      filterTag: '',
      newCourse: { title:'', description:'', tagsInput:'', img:'' }
    }
  },
  computed: {
    filteredCourses(){
      if(!this.filterTag) return this.courses
      const t = this.filterTag.trim().toLowerCase()
      return this.courses.filter(c=> c.tags.some(tag=> tag.toLowerCase().includes(t)))
    }
  },
  created(){
    try{ this.courses = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]') }
    catch(e){ this.courses = [] }
    if(this.courses.length===0){
      // seed some example courses
      this.courses = [
        { id: 'c1', title: 'Python 入门', description: '0->1 的 Python 学习路径', tags: ['python','beginner'], img: 'https://picsum.photos/seed/python/800/300' },
        { id: 'c2', title: 'Linux 基础', description: '命令行与系统基础', tags: ['linux','system'], img: 'https://picsum.photos/seed/linux/800/300' },
        { id: 'c3', title: '算法思维', description: '逻辑与算法练习', tags: ['logic','algorithms'], img: 'https://picsum.photos/seed/logic/800/300' },
        { id: 'c_linux_shell', title: 'Linux Shell 基础（示例）', description: '从终端命令到简单脚本的入门课程', tags: ['linux','shell','bash','beginner'], img: 'https://picsum.photos/seed/linuxshell/800/300' }
      ]
      localStorage.setItem(STORAGE_KEY, JSON.stringify(this.courses))
    }
  },
  methods:{
    applyFilter(){ /* reactive via computed */ },
    clearFilter(){ this.filterTag=''} ,
    addCourse(){
      const tags = this.newCourse.tagsInput.split(',').map(s=>s.trim()).filter(Boolean)
      const c = { id: 'c'+Date.now(), title: this.newCourse.title || '未命名', description: this.newCourse.description||'', tags, img: this.newCourse.img||('https://picsum.photos/seed/'+encodeURIComponent(this.newCourse.title)+ '/800/300') }
      this.courses.unshift(c)
      localStorage.setItem(STORAGE_KEY, JSON.stringify(this.courses))
      this.newCourse = { title:'', description:'', tagsInput:'', img:'' }
    },
    enroll(course){
      const mineKey = 'edu_my_courses'
      const mine = JSON.parse(localStorage.getItem(mineKey) || '[]')
      if(!mine.find(m=>m.id===course.id)){
        mine.push(course)
        localStorage.setItem(mineKey, JSON.stringify(mine))
        alert('已添加到我的课程')
      } else alert('你已选择该课程')
    }
  }
}
</script>

<style>
.mdui-m-b-2{margin-bottom:16px}
</style>
