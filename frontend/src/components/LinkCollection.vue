<template>
  <el-button @click="getLink()">点击</el-button>
</template>

<script>
export default {
  name: 'LinkCollection',
  methods: {
    // 获取所有链接
    getLink () {
      console.log('sdfsdfs')
      this.$http.get('http://localhost:8000/api/queryAllLinks')
      // this.$http.get('http://localhost:8000/api/queryAllLinks').then((resp) => {
      //
      // })
    }
  }
}

</script>

<style scoped>

</style>
