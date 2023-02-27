<template>
  <el-col>

    <el-table
      :data="this.links"
      :header-cell-style="{
    'background-color': '#E5EEFF'
    }"
      border
      style="width: 100%">
      <el-table-column
        class="normal-table-column"
        prop="linkDescription"
        align="center"
        label="链接描述">
      </el-table-column>
      <el-table-column
        prop="linkUrl"
        align="center"
        label="网页地址"
        class="normal-table-column">
      </el-table-column>
      <el-table-column
        align="center"
        prop="linkRemark"
        label="网页备注"
        class="normal-table-column">
      </el-table-column>
      <el-table-column
        align="center"
        prop="userName"
        class="normal-table-column"
        label="账户名">
      </el-table-column>
      <el-table-column
        class="normal-table-column"
        prop="passWord"
        align="center"
        label="账户密码">
      </el-table-column>
      <el-table-column align="center"
                       width="180">
        <template slot-scope="scope">
          <el-button @click="showUpdateDialog(scope.row)">编辑</el-button>
          <el-button @click="showDeleteConfirmDialog(scope.row.linkId)">删除</el-button>
        </template>

      </el-table-column>
    </el-table>

    <el-button class="button-add" @click="addLinkVisible = true">新增链接</el-button>

    <el-dialog title="新增链接" :visible.sync="addLinkVisible">
      <el-form :model="addForm">
        <el-form-item label="链接描述" :label-width="formLabelWidth">
          <el-input v-model="addForm.linkDescription" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="链接地址" :label-width="formLabelWidth">
          <el-input v-model="addForm.linkUrl" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="链接备注" :label-width="formLabelWidth">
          <el-input v-model="addForm.linkRemark" autocomplete="off"></el-input>
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

    <el-dialog title="编辑" :visible.sync="modifyLinkVisible">
      <el-form :model="updateForm">
        <el-form-item label="链接描述" :label-width="formLabelWidth">
          <el-input v-model="updateForm.linkDescription" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="链接地址" :label-width="formLabelWidth">
          <el-input v-model="updateForm.linkUrl" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="链接备注" :label-width="formLabelWidth">
          <el-input v-model="updateForm.linkRemark" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="对应账号" :label-width="formLabelWidth">
          <el-input v-model="updateForm.userName" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="对应密码" :label-width="formLabelWidth">
          <el-input v-model="updateForm.passWord" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="modifyLinkVisible = false">取 消</el-button>
        <el-button type="primary" @click="updateLInkById">确 定</el-button>
      </div>
    </el-dialog>
  </el-col>
</template>

<script>
import axios from "axios";

export default {
  name: "link",
  created() {
  },
  mounted() {
    this.getAllLinks();
  },
  data() {
    return {
      links: [],
      addLinkVisible: false,
      modifyLinkVisible: false,
      addForm: {
        "linkDescription": "",
        "linkUrl": "",
        "linkRemark": "",
        "userName": "",
        "passWord": "",
      },
      updateForm: {
        "linkDescription": "",
        "linkUrl": "",
        "linkRemark": "",
        "userName": "",
        "passWord": "",
      },
      tempUpdateForm: {},

      formLabelWidth: '120px'

    }
  },
  methods: {
    // 获取全部链接
    getAllLinks() {
      axios.get('http://localhost:8000/api/queryAllLinks').then(value => {
        console.log(value)
        if (value.status === 200) {
          console.log(value.data['list'])
          this.links = (value.data['list']);
        }
      })
    },
    // 删除对应链接
    showDeleteConfirmDialog(id) {
      this.$confirm('此操作将永久删除该链接, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.deleteLinkById(id)
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
    },
    // 根据id去删除link
    deleteLinkById(id) {
      axios({
        method: "post",
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        },
        data: {"linkId": id},
        url: "http://localhost:8000/api/deleteLink"
      }).then(res => {
        if (res.status === 200) {
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
          this.getAllLinks();
        }
        console.log(res)
      })
    },
    // 增加链接
    addLink() {
      this.addLinkVisible = false;
      axios({
        method: "post",
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        },
        data: this.addForm,
        url: "http://localhost:8000/api/addLink"
      }).then(res => {
        if (res.status === 200) {
          this.getAllLinks();
        }
        console.log(res)
      })
    },

    showUpdateDialog(targetOne) {
      this.modifyLinkVisible = true
      this.updateForm = {
        linkUrl: targetOne.linkUrl,
        linkDescription: targetOne.linkDescription,
        linkRemark: targetOne.linkRemark,
        linkId: targetOne.linkId,
        userName: targetOne.userName,
        passWord: targetOne.passWord
      };
      console.log(targetOne)
    },
    // 根据id去更新
    updateLInkById() {
      this.modifyLinkVisible = false;
      axios({
        method: "post",
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        },
        data: this.updateForm,
        url: "http://localhost:8000/api/updateLink"
      }).then(res => {
        if (res.status === 200) {
          this.getAllLinks();
        }
        console.log(res)
      })
    }
  },
}
</script>

<style scoped>
.normal-table-column {
  width: 20%;
}

.button-add {
  margin-top: 24px;
  float: right;
}
</style>
