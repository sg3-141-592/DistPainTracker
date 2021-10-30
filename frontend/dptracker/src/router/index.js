import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Profile from '../views/Profile.vue'
import ViewPain from '../views/ViewPain.vue'
import ViewLabel from '../views/ViewLabel.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile,
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
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  linkActiveClass: 'is-active',
  routes
})

export default router
