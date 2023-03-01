# frontend

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

# note
其中使用了less，需要执行以下安装：
```angular2html
npm install less-loader
```
如果发现有报错了
1. vue 报错 !!vue-style-loader!css-loader?{“sourceMap“:true}!.
解决方案为：
 * npm uninstall less-loader
 * npm install less-loader@5.0.0
