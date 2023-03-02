<template>

  <div class="fillcontain">

    <!--    展示链接的表格-->
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
          label="密码">
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

    <!--    添加按钮-->
    <el-button class="button-add" @click="addLinkVisible=true">添加链接</el-button>
    <div class="Pagination" style="text-align: left;margin-top: 40px;margin-left: 12px">
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
    <!--  新增链接的弹窗-->
    <el-dialog title="新增链接" :visible.sync="addLinkVisible">
      <el-form :model="addForm">
        <el-form-item label="链接描述" :label-width="formLabelWidth">
          <el-input v-model="addForm.linkDescription" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="链接地址" :label-width="formLabelWidth">
          <el-input v-model="addForm.linkUrl" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="对应账号" :label-width="formLabelWidth">
          <el-input v-model="addForm.userName" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="对应密码" :label-width="formLabelWidth">
          <el-input v-model="addForm.passWord" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="addLinkVisible = false">取 消</el-button>
        <el-button type="primary" @click="addLink">确 定</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
import {linkAll, addLink, deleteLink} from "../../../utils/net/api";

export default {
  name: "LinkTables",
  props: ['env'],
  data() {
    return {
      links: [],
      currentPage: 1,
      count: 0,
      formLabelWidth: '120px',
      addLinkVisible: false,
      addForm: {
        "linkDescription": "",
        "linkUrl": "",
        "userName": "",
        "passWord": "",
      },
    }
  },

  created() {
    this.getAllLinks()
  },

  methods: {
    // 获取全部链接
    async getAllLinks() {
      linkAll({
        "page": this.currentPage,
        "env": this.env["key"]
      }).then(value => {
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
    showDeleteConfirmDialog(targetOneId) {
      this.$confirm('此操作将永久删除该链接, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteLink({
          "linkId": targetOneId,
          "env": this.env["key"]
        }).then(value => {
          if (value["resultCode"] === '0') {
            this.currentPage = 1;
            this.getAllLinks()
          }
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
    },
    ///添加链接
    addLink() {
      this.addLinkVisible = false;
      this.addForm['env'] = this.env['key']
      addLink(this.addForm).then(value => {
        if (value["resultCode"] === '0') {
          this.currentPage = 1;
          this.getAllLinks()
        }
      })
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
