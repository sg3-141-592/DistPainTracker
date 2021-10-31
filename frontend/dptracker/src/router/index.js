import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CreatePain from '../views/CreatePain.vue'
import ViewPain from '../views/ViewPain.vue'
import ViewLabel from '../views/ViewLabel.vue'
import Login from '../views/Login.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/create-pain',
    name: 'create-pain',
    component: CreatePain
  },
  {
    path: '/view-pain/:id',
    name: 'view-pain',
    component: ViewPain,
  },
  {
    path: '/view-label/:id',
    name: 'view-label',
    component: ViewLabel,
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  linkActiveClass: 'is-active',
  routes
})

export default router
