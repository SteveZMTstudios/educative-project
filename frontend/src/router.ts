import { createRouter, createWebHistory } from 'vue-router';
import Landing from './views/Landing.vue';
import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import TagSelect from './views/TagSelect.vue';
import TeacherRegister from './views/TeacherRegister.vue';

const routes = [
  { path: '/', name: 'Landing', component: Landing },
  { path: '/home', name: 'Home', component: Home },
  { path: '/tags', name: 'TagSelect', component: TagSelect },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/teacher-register', name: 'TeacherRegister', component: TeacherRegister },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

import type { NavigationGuardNext, RouteLocationNormalized } from 'vue-router';

router.beforeEach((to: RouteLocationNormalized, from: RouteLocationNormalized, next: NavigationGuardNext) => {
  const token = localStorage.getItem('auth_token');
  if (token && to.path === '/') {
    next('/home');
  } else if (!token && to.path === '/home') {
    next('/');
  } else {
    next();
  }
});

export default router;
