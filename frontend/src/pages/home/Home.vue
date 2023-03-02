<template>
  <div class="manage_page fillcontain">
    <el-row style="height: 100%;">
      <el-col :span="4" style="min-height: 100%; background-color: #324057;">
        <div id="slogan_body">
          <el-avatar :src="nikiLogo"></el-avatar>
          <span id="slogan-style">Niki</span>
        </div>
        <el-menu :default-active="defaultActive" style="min-height: 100%;" theme="dark" router>
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-c-scale-to-original"></i>营销管理</template>
            <el-menu-item index="sales1">营销管理一</el-menu-item>
            <el-menu-item index="shopList">营销管理二</el-menu-item>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-plus"></i>Linkie管理</template>
            <el-menu-item index="addShop">添加商铺</el-menu-item>
            <el-menu-item index="addGoods">添加商品</el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title"><i class="el-icon-share"></i>链接管理</template>
            <el-menu-item index="links">链接列表</el-menu-item>
            <el-menu-item index="addGoods">添加链接</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-col>
      <el-col :span="20" style="height: 100%;overflow: auto; ">
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import nikiLogo from "../../../src/assets/niki_logo.png";

export default {

  data() {
    return {
      nikiLogo: nikiLogo,
    }
  },
  computed: {
    defaultActive: function () {
      return this.$route.path.replace('/', '');
    }
  },
  methods: {

  },
}
</script>


<style lang="less" scoped>
@import '../../style/mixin';

.manage_page {

}


#slogan_body {
  height: 88px;
  display: flex;
  align-items: center;
  justify-content: start;
  margin-left: 4%;
}

#slogan-style {
  margin-left: 12px;
  color: indianred;
  font-size: 40px;
  font-family: Woodine;
}
</style>
