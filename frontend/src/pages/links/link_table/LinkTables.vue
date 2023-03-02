<template>

  <div class="fillcontain">

    <div class="el-table-links">
      <el-table
        :data="links"
        border
        highlight-current-row:true
        style="width: 100%">
        <el-table-column
          prop="linkUrl"
          label="链接地址"
          width="180">
        </el-table-column>
        <el-table-column
          prop="linkDescription"
          label="链接描述"
          width="180">
        </el-table-column>
        <el-table-column
          prop="userName"
          label="姓名"
          width="180">
        </el-table-column>
        <el-table-column
          prop="passWord"
          label="地址">
        </el-table-column>
      </el-table>
    </div>

    <el-button class="button-add">添加链接</el-button>
    <div class="Pagination" style="text-align: left;margin-top: 60px;">
      <el-pagination
        background
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-size="20"
        layout="total, prev, pager, next"
        :total="count">
      </el-pagination>
    </div>
  </div>
</template>

<script>
import {linkAll} from "../../../utils/net/api";

export default {
  name: "LinkTables",

  props: ['env'],


  data() {
    return {
      links: [],
      currentPage: 1,
      count: 0,
    }
  },

  mounted() {
    this.getAllLinks()
  },

  methods: {
    // 获取全部链接
    getAllLinks() {
      linkAll({
        "page": this.currentPage,
        "env": this.env["key"]
      }).then(value => {
        // this.links.push(...value['resultData']["list"])
        this.links = value["resultData"]["list"]
        this.count = value['resultData']["total"]
      })
    },
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.getAllLinks()
    },
  }
}
</script>
<style lang="less">
@import '../../../style/mixin';

.el-table-links {
  padding: 20px;
}

.button-add {
  margin-right: 24px;
  float: right;
}

el-table-column {
  alignment: center;
}
</style>
