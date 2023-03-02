<template>

  <div class="fillcontain">

    <div class="el-table-links">
      <el-table
        :data="links"
        border
        highlight-current-row:true
        style="width: 100%">
        <el-table-column
          align="center"
          prop="linkUrl"
          label="链接地址"
          width="180">
        </el-table-column>
        <el-table-column
          align="center"
          prop="linkDescription"
          label="链接描述"
          width="180">
        </el-table-column>
        <el-table-column
          align="center"
          prop="userName"
          label="姓名"
          width="180">
        </el-table-column>
        <el-table-column
          prop="passWord"
          align="center"
          width="180"
          label="地址">
        </el-table-column>
        <el-table-column align="center"
                         width="300" label="操作">
          <template slot-scope="scope">
            <el-row>
              <el-button @click="showUpdateDialog(scope.row)" type="primary" round style="width: 100px">编辑</el-button>
              <el-button @click="showDeleteConfirmDialog(scope.row.linkId)" type="danger" round style="width: 100px">
                删除
              </el-button>
            </el-row>
          </template>

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
    ///页码改变回调
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    ///当前页码改变
    handleCurrentChange(val) {
      this.currentPage = val;
      this.getAllLinks()
    },
    ///显示更改弹窗
    showUpdateDialog(targetOne) {

    },
    ///显示删除确认弹窗
    showDeleteConfirmDialog(targetOne) {

    }
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


</style>
