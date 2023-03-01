<template>
  <div class="manage_page fillcontain">
    <el-row style="height: 100%;">
      <el-col :span="4" style="min-height: 100%; background-color: #324057;">
        <el-menu :default-active="defaultActive" style="min-height: 100%;" theme="dark" router>
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-c-scale-to-original"></i>营销管理</template>
            <el-menu-item index="links"
            >我的收藏夹
            </el-menu-item
            >
            <el-menu-item index="links" @click="replaceRouter('/links')">营销管理一</el-menu-item>
            <el-menu-item index="shopList">营销管理二</el-menu-item>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-plus"></i>Linkie管理</template>
            <el-menu-item index="addShop">添加商铺</el-menu-item>
            <el-menu-item index="addGoods">添加商品</el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title"><i class="el-icon-plus"></i>链接管理</template>
            <el-menu-item index="addShop">添加商铺</el-menu-item>
            <el-menu-item index="addGoods">添加商品</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-col>
      <el-col :span="20" style="height: 100%;overflow: auto; width: 800px; background-color: red">
        <keep-alive>
          <el-main>
            <router-view></router-view>
          </el-main>
        </keep-alive>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  computed: {
    defaultActive: function () {
      return this.$route.path.replace('/', '');
    }
  },
  methods: {
    replaceRouter: function (router) {
      this.$router.replace(router);
    }
  },
}
</script>


<style lang="less" scoped>
@import '../../style/mixin';

.manage_page {

}
</style>
