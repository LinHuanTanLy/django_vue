import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const home = () => import("../pages/home/Home.vue")


const routers = [
  {
    path: "/",
    component: home
  }
]

export default new Router({
  routes: routers,
  strict: process.env.NODE_ENV !== 'production',
})
