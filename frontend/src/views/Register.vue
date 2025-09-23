<template>
  <n-space vertical align="center" class="auth">
    <n-card title="注册">
      <n-form @submit.prevent="submit">
        <n-form-item label="用户名">
          <n-input v-model:value="username" placeholder="用户名" />
        </n-form-item>
        <n-form-item label="邮箱">
          <n-input v-model:value="email" placeholder="邮箱" />
        </n-form-item>
        <n-form-item label="密码">
          <n-input type="password" v-model:value="password" placeholder="密码" />
        </n-form-item>
        <n-form-item>
          <n-button type="primary" @click="submit">注册</n-button>
        </n-form-item>
      </n-form>
      <p><router-link to="/login">去登录</router-link></p>
    </n-card>
  </n-space>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { NInput, NButton, NForm, NFormItem, NCard, NSpace } from 'naive-ui';

const username = ref('');
const password = ref('');
const email = ref('');
const router = useRouter();

async function sha256Hex(message: string) {
  const msgUint8 = new TextEncoder().encode(message);
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgUint8);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

async function submit() {
  try {
    const clientHash = await sha256Hex(password.value);
    await axios.post('/api/auth/register', { username: username.value, password: clientHash, email: email.value });
    router.push('/login');
  } catch (e) {
    alert('注册失败');
  }
}
</script>

<style scoped>
.auth { max-width: 420px; margin: 2rem auto; }
</style>
