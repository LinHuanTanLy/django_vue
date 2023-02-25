<template>
  <el-col>

    <el-table
      :data="this.links"
      :header-cell-style="{
    'background-color': '#E5EEFF'
    }"
      chan
      border
      style="width: 100%">
      <el-table-column
        class="normal-table-column"
        prop="fields.linkDescription"
        align="center"
        label="链接描述">
      </el-table-column>
      <el-table-column
        prop="fields.linkUrl"
        align="center"
        label="网页地址"
        class="normal-table-column">
      </el-table-column>
      <el-table-column
        align="center"
        prop="fields.linkRemark"
        label="网页备注"
        class="normal-table-column">
      </el-table-column>
      <el-table-column
        align="center"
        prop="fields.userName"
        class="normal-table-column"
        label="账户名">
      </el-table-column>
      <el-table-column
        class="normal-table-column"
        prop="fields.passWord"
        align="center"
        label="账户密码">
      </el-table-column>
      <el-table-column align="center"
                       width="180">
        <template slot-scope="scope">
          <el-button @click="open(scope.row.fields)">编辑</el-button>
          <el-button @click="deleteLink">删除</el-button>
        </template>

      </el-table-column>
    </el-table>

    <el-button class="button-add">新增链接</el-button>
  </el-col>
</template>

<script>
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
    }
  },
  methods: {
    open(id) {
      console.log(id)
      this.$confirm('此操作将永久删除该文件, 是否继续?' + id, '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'success',
          message: '删除成功!'
        });
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
    },
    getAllLinks() {
      this.$http.get('http://localhost:8000/api/queryAllLinks').then(
        value => {
          console.log(value)
          if (value.status === 200) {
            this.links = (value['data']['list']);
          }
        }
      )
    },
    deleteLink(id) {
      this.$confirm('此操作将永久删除该链接, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'success',
          message: '删除成功!'
        });
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
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
