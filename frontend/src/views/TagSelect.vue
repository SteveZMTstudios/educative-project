<template>
  <n-space vertical align="center" class="tag-select">
    <n-card title="个性化学习计划选择">
      <n-steps :current="currentStep" :status="stepStatus">
        <n-step title="优先目标" />
        <n-step title="聚焦内容" />
        <n-step title="编程熟练程度" />
        <n-step title="学习目标" />
        <n-step title="准备就绪" />
      </n-steps>
      <n-divider />
      <div v-if="currentStep === 0">
        <h3>你的优先目标是？</h3>
        <n-radio-group v-model:value="selections[0]">
          <n-space vertical>
            <n-radio value="future-ready" label="专业技能提升（为未来做好准备）" />
            <n-radio value="beginner" label="基础知识学习" />
            <n-radio value="new-tech" label="学习新技术" />
            <n-radio value="course-work" label="完成课程作业" />
            <n-radio value="time-killer" label="打发时间（利用碎片时间）" />
            <n-radio value="mystery" label="其他（神秘）" />
          </n-space>
        </n-radio-group>
        <div v-if="selections[0] === 'course-work'">
          <p>当选择“完成课程作业”时，询问是否目前在学校跟随课程学习或是否应教师要求注册</p>
          <n-radio-group v-model:value="subSelection">
            <n-space vertical>
              <n-radio value="student" label="是" />
              <n-radio value="no" label="否" />
              <n-radio value="teacher" label="我是教师" />
            </n-space>
          </n-radio-group>
          <div v-if="subSelection === 'student'" style="margin-top:12px">
            <n-input v-model:value="classCode" placeholder="请输入教师提供的班级号或邀请码" />
          </div>
        </div>
      </div>
      <div v-else-if="currentStep === 1">
        <h3>你希望聚焦于哪些内容？</h3>
        <n-radio-group v-model:value="selections[1]">
          <n-space vertical>
            <n-radio value="basic-skills" label="学习基本技能" />
            <n-radio value="programming" label="学习编程" />
            <n-radio value="operating-systems" label="学习操作系统" />
            <n-radio value="curiosity" label="好奇看看" />
            <n-radio value="review" label="复习我的知识" />
            <n-radio value="other" label="别的" />
          </n-space>
        </n-radio-group>
      </div>
      <div v-else-if="currentStep === 2">
        <h3>你的编程熟练程度怎么样？</h3>
        <n-radio-group v-model:value="selections[2]">
          <n-space vertical>
            <n-radio value="noob" label='print("hello world") # 初学者' />
            <n-radio value="rookie" label="if b>a: print b # 新手" />
            <n-radio value="experienced" label="for i in range(5): #入门者" />
            <n-radio value="newbie" label="def circle(size): # 有经验" />
          </n-space>
        </n-radio-group>
      </div>
      <div v-else-if="currentStep === 3">
        <h3>你的日常学习目标是什么？</h3>
        <n-radio-group v-model:value="selections[3]">
          <n-space vertical>
            <n-radio value="fastfood" label="5分钟" />
            <n-radio value="quick-study" label="10分钟" />
            <n-radio value="lessonly" label="30分钟" />
            <n-radio value="full-course" label="1小时" />
          </n-space>
        </n-radio-group>
      </div>
      <div v-else-if="currentStep === 4">
        <h3>你已经准备就绪</h3>
        <n-radio-group v-model:value="selections[4]">
          <n-space vertical>
            <n-radio value="create-account" label="创建账户" />
            <n-radio value="try-interactive" label="先尝试一次交互式学习" />
          </n-space>
        </n-radio-group>
        <p v-if="selections[4]">太棒了！让我们开始你的个性化学习之旅吧！</p>
      </div>
      <n-space justify="space-between" style="margin-top:24px">
        <n-button v-if="currentStep > 0" @click="prevStep">上一步</n-button>
        <n-button v-if="currentStep < 4" :disabled="!selections[currentStep]" @click="nextStep">下一步</n-button>
        <n-button v-if="currentStep === 4" type="primary" :disabled="!selections[4]" @click="save">完成</n-button>
      </n-space>
    </n-card>
  </n-space>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { NRadio, NRadioGroup, NButton, NCard, NSpace, NSteps, NStep, NDivider, NInput } from 'naive-ui';

const selections = ref<string[]>(['', '', '', '', '']);
const subSelection = ref<string>('');
const classCode = ref<string>('');
const currentStep = ref(0);
const router = useRouter();

const stepStatus = computed(() => {
  if (currentStep.value === 4 && selections.value[4]) return 'finish';
  return 'process';
});

function nextStep() {
  if (currentStep.value < 4) {
    currentStep.value++;
  }
}

function prevStep() {
  if (currentStep.value > 0) {
    currentStep.value--;
  }
}

function getToken() { return localStorage.getItem('auth_token'); }

async function save() {
  const token = getToken();
  if (!token) { router.push('/'); return; }

  // Handle teacher redirect
  if (selections.value[0] === 'course-work' && subSelection.value === 'teacher') {
    router.push('/teacher-register');
    return;
  }

  // Handle no
  if (selections.value[0] === 'course-work' && subSelection.value === 'no') {
    alert('提示用户可以将平台推荐给教师');
    // Still proceed to save tags
  }

  // Collect tags
  const tags: string[] = [];
  selections.value.slice(0, 4).forEach((sel) => {
    if (sel) {
      tags.push('#' + sel);
    }
  });
  let user_type: string | undefined = undefined;
  let class_code: string | undefined = undefined;
  if (selections.value[0] === 'course-work') {
    if (subSelection.value === 'student') {
      tags.push('#student');
      user_type = 'student';
      if (classCode.value) class_code = classCode.value.trim();
    } else if (subSelection.value === 'teacher') {
      user_type = 'teacher';
    }
  }

  // 默认用户类型
  if (!user_type) user_type = 'user';

  try {
    await axios.post('/api/auth/tags', { token, tags, user_type, class_code });
    router.push('/home');
  } catch (e) {
    alert('保存失败');
  }
}
</script>

<style scoped>
.tag-select { max-width:720px; margin:2rem auto; }
</style>
