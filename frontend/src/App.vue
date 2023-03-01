<template>
  <el-container>
    <el-aside width="200px">
      <el-menu>
        <el-submenu index="1">
          <template slot="title"><i class="el-icon-message"></i>营销</template>
          <el-menu-item-group>
            <el-menu-item index="1-1" @click="goto('/sales')"
              >商品模块</el-menu-item
            >
            <el-menu-item index="1-2">选项2</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title"><i class="el-icon-menu"></i>sales</template>
          <el-menu-item index="2-1">sales模块</el-menu-item>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title"><i class="el-icon-setting"></i>links</template>
          <el-menu-item index="3-1" @click="goto('/link')"
            >我的收藏夹</el-menu-item
          >
          <el-menu-item index="3-2" @click="goto('/linkContainer')"
            >我的收藏夹模板测试</el-menu-item
          >
        </el-submenu>
      </el-menu>
    </el-aside>

    <el-container>
      <el-header style="text-align: right; font-size: 12px">
        <el-avatar class="title_avatar" :src="nikiLogo" size="small"
          >汤圆</el-avatar
        >
        <span class="title_name">汤圆</span>
      </el-header>

      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>
<style>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}

.title_avatar {
  border: none;
  vertical-align: middle;
  margin-left: 10px;
  margin-right: 6px;
}

.title_name {
  font-family: "Roboto", "Lucida Grande", Verdana, Arial, sans-serif;
  font-size: 14px;
  color: #3c3c3c;
}
</style>

<script>
import nikiLogo from "../src/assets/niki_logo.png";

export default {
  data() {
    return {
      nikiLogo: nikiLogo,
    };
  },
  onLaunch: function (option) {
    console.log("sdfsfsdfsdfsdfsdf" + option.path);
  },
  onLoad: function (option) {
    console.log("sdfsfsdfsdfsdfsdf" + option.path);
  },
  methods: {
    goto(path) {
      if (this.$router.currentRoute.path !== path) {
        this.$router.replace(path);
      }
    },
  },
};
</script>
