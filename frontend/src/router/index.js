import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import LinkCollection from '@/components/LinkCollection'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    {
      path: '/LinkCollection',
      name: 'LinkCollection',
      component: LinkCollection
    }
  ]
})
