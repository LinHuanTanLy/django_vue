import Vue from 'vue'
import Router from 'vue-router'
import LinkCollection from '@/components/LinkCollection'
// import Index from "@/components/index/index.vue";

import sales from '../components/sales/sales.vue';
import linkiee from '../components/linkiee/linkiee.vue';
import link from '../components/link/link.vue';
import linkContainer from '../components/link/link_container.vue';
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/LinkCollection',
      name: 'LinkCollection',
      component: LinkCollection
    },
    {
      path: '/sales',
      name: 'sales',
      component: sales
    },
    {
      path: '/linkiee',
      name: 'linkiee',
      component: linkiee
    },
    {
      path: '/link',
      name: 'link',
      component: link
    },
    {
      path: '/linkContainer',
      name: "linkContaienr",
      component: linkContainer
    }
  ]
})
