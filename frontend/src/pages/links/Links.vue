<template>

  <div>
    <Header_top></Header_top>
    <el-col>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item v-for="(value) in envList" :key="value['index']" :index="value['index']">
          <span>{{ value['name'] }}</span>
        </el-menu-item>
      </el-menu>
      <keep-alive>
        <LinkTables v-for="(value) in envList" :env="value" v-if="activeIndex===value['index']"
                    :key="value['index']">
        </LinkTables>
      </keep-alive>
    </el-col>
  </div>
</template>


<script>
import LinkTables from "./link_table/LinkTables.vue";
import Header_top from "../../components/header_top/header_top.vue";

export default {
  name: "Links",
  data() {
    return {
      activeIndex: "test",
      envList: [
        {"name": "测试环境", "key": "0", index: "test"},
        {"name": "集成环境", "key": "1", index: "release"},
        {"name": "生产环境", "key": "2", index: "product"},
      ]
    }
  },
  components: {Header_top, LinkTables},
  methods: {
    handleSelect(key, keyPath) {
      this.activeIndex = keyPath[0];
    }
  }
}
</script>

<style scoped>

</style>
