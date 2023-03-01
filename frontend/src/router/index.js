import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const home = () => import("../pages/home/Home.vue")
const links = () => import("../pages/links/Links.vue")


const routers = [
  {
    path: "/",
    component: home,
    children: [
      {
        path: "/links",
        component: links
      }
    ]
  },

]

export default new Router({
  routes: routers,
  strict: process.env.NODE_ENV !== 'production',
})
