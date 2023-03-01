<template>
  <el-col>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
      <el-menu-item v-for="(value) in envList" :key="value" :index="value['index']">
        <span>{{ value['name'] }}</span>
      </el-menu-item>
    </el-menu>

  </el-col>
</template>


<script>
import EnvEnum from '../../conf/config.env'

export default {
  name: "Links",
  data() {
    return {
      activeIndex: "test",
      envList: [
        {"name": "测试环境", key: EnvEnum.TEST, index: "test"},
        {"name": "集成环境", key: EnvEnum.RELEASE, index: "release"},
        {"name": "生产环境", key: EnvEnum.PRODUCT, index: "product"},
      ]
    }
  },
}
</script>

<style scoped>

</style>
