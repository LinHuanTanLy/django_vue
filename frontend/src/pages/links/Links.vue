<template>
  <el-col>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item v-for="(value) in envList" :key="value['index']" :index="value['index']">
        <span>{{ value['name'] }}</span>
      </el-menu-item>
    </el-menu>
    <LinkTables v-for="(value) in envList" :env="value['index']" v-if="activeIndex===value['index']"
                :key="value['index']">

    </LinkTables>
  </el-col>
</template>


<script>
import EnvEnum from '../../conf/config.env'

import LinkTables from "./link_table/LinkTables.vue";

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
  components: {
    LinkTables,
  },
  methods: {
    handleSelect(key, keyPath) {
      this.activeIndex = keyPath[0];
    }
  }
}
</script>

<style scoped>

</style>
