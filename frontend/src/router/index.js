import Vue from 'vue'
import Router from 'vue-router'
import * as path from "path";

Vue.use(Router)

const home = () => import("../pages/home/Home.vue",)
const links = () => import("../pages/links/Links.vue")
const linkTables = () => import("../pages/links/link_table/LinkTables.vue")


const routers = [
  {
    path: "/",
    component: home,
    children: [
      {
        path: "/links",
        component: links,
        meta: ['链接管理', '链接列表'],
        children: [
          {
            path: "/link_tables",
            component: linkTables,
          }

        ]
      }
    ]
  },

]

export default new Router({
  routes: routers,
  strict: process.env.NODE_ENV !== 'production',
})
