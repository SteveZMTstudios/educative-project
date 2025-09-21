import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Student from '../views/Student.vue'
import Teacher from '../views/Teacher.vue'
import Favor from '../views/Favor.vue'
import Courses from '../views/Courses.vue'
import CourseDetail from '../views/CourseDetail.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/student', component: Student },
  { path: '/teacher', component: Teacher },
  { path: '/favor', component: Favor },
  { path: '/courses', component: Courses }
  ,{ path: '/courses/:id', component: CourseDetail }
]

const router = createRouter({ history: createWebHashHistory(), routes })
export default router
