import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Student from '../views/Student.vue'
import Teacher from '../views/Teacher.vue'
import Favor from '../views/Favor.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/student', component: Student },
  { path: '/teacher', component: Teacher },
  { path: '/favor', component: Favor }
]

const router = createRouter({ history: createWebHashHistory(), routes })
export default router
