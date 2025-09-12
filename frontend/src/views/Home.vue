<template>
  <div>
    <h2 class="mdui-typo-display-2">欢迎</h2>
    <p>本平台聚焦计算机基础、Linux、Python 入门与逻辑思维训练，提供个性化学习推荐与实时反馈。</p>
    <div class="mdui-row-xs-2 mdui-row-md-3 mdui-m-t-3">
      <div class="mdui-col">
        <FeatureCard title="学习计划选择" subtitle="根据你的兴趣选择学习路径" img="https://picsum.photos/seed/learn/800/300">
          <template #actions>
            <router-link to="/favor" class="mdui-btn mdui-ripple">选择计划</router-link>
          </template>
        </FeatureCard>
      </div>

      <div class="mdui-col">
        <FeatureCard title="教师空间" subtitle="发布练习并查看学生成绩" img="https://picsum.photos/seed/teacher/800/300">
          <template #actions>
            <router-link to="/teacher" class="mdui-btn mdui-ripple">教师入口</router-link>
          </template>
        </FeatureCard>
      </div>

      <div class="mdui-col">
        <FeatureCard title="学生空间" subtitle="练习、提交与实时反馈" img="https://picsum.photos/seed/student/800/300">
          <template #actions>
            <router-link to="/student" class="mdui-btn mdui-ripple">学生入口</router-link>
          </template>
        </FeatureCard>
      </div>
    </div>
    <div class="mdui-m-t-3">
      <FeatureCard title="课程中心" subtitle="浏览与添加课程，按标签筛选推荐" img="https://picsum.photos/seed/courses/800/300">
        <template #actions>
          <router-link to="/courses" class="mdui-btn mdui-ripple">进入课程中心</router-link>
        </template>
      </FeatureCard>
    </div>
  </div>
</template>

<script>
import FeatureCard from '../components/FeatureCard.vue'

export default { name: 'Home', components: { FeatureCard } }
</script>
