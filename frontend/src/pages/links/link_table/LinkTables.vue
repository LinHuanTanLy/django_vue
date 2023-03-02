<template>
  <el-button @click="getAllLinks">{{ env }}</el-button>
</template>

<script>
import {linkAll} from "../../../utils/net/api";

export default {
  name: "LinkTables",
  props: ['env'],
  links: [],


  mounted() {
    this.getAllLinks()
  },

  methods: {
    // 获取全部链接
    getAllLinks() {
      linkAll({
        "page": 1,
      }).then(value => {
        alert(value)
      })
    },
  }
}
</script>

<style scoped>

</style>
