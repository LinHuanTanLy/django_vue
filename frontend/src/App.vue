<template>
  <el-container>
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
      <el-menu>
        <el-submenu index="1">
          <template slot="title"><i class="el-icon-message"></i>营销</template>
          <el-menu-item-group>
            <template slot="title">商品模块</template>
            <el-menu-item index="1-1" @click="goto('/sales')">商品模块</el-menu-item>
            <el-menu-item index="1-2">选项2</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="分组2">
            <el-menu-item index="1-3">选项3</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="1-4">
            <template slot="title">选项4</template>
            <el-menu-item index="1-4-1">选项4-1</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title"><i class="el-icon-menu"></i>sales</template>
          <el-menu-item-group>
            <template slot="title">分组一</template>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="分组2">
            <el-menu-item index="2-3">选项3</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="2-4">
            <template slot="title">选项4</template>
            <el-menu-item index="2-4-1">选项4-1</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title"><i class="el-icon-setting"></i>links</template>
          <el-menu-item-group>
            <template slot="title">分组一</template>
            <el-menu-item index="3-1" @click="goto('/link')">我的收藏夹</el-menu-item>
            <el-menu-item index="3-2">选项2</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="分组2">
            <el-menu-item index="3-3">选项3</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="3-4">
            <template slot="title">选项4</template>
            <el-menu-item index="3-4-1">选项4-1</el-menu-item>
          </el-submenu>
        </el-submenu>
      </el-menu>
    </el-aside>

    <el-container>
      <el-header style="text-align: right; font-size: 12px;">
        <el-avatar class="title_avatar" :src="nikiLogo" size="small">汤圆</el-avatar>
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
  background-color: #B3C0D1;
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
import nikiLogo from '../src/assets/niki_logo.png'

export default {
  data() {
    return {
      nikiLogo: nikiLogo
    }
  },

  methods: {
    goto(path) {
      this.$router.replace(path)
    }
  }
};
</script>
