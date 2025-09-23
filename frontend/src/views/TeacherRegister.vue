<template>
  <n-space vertical align="center" class="teacher-register">
    <n-card title="教师注册 (占位)">
      <p>这里将来用于教师课程与班级信息录入。</p>
      <n-button type="primary" @click="goBack">返回</n-button>
    </n-card>
  </n-space>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { NSpace, NCard, NButton } from 'naive-ui';
const router = useRouter();
function goBack(){ router.push('/tags'); }
</script>

<style scoped>
.teacher-register { max-width:640px; margin:2rem auto; }
</style>