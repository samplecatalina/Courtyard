<template>
  <el-footer>
    <el-divider></el-divider>
    <p>
      <el-link type="primary">关于我们</el-link>
      <el-divider direction="vertical"></el-divider>
      <el-link type="primary">联系我们</el-link>
      <el-divider direction="vertical"></el-divider>
      <el-link type="primary">加入我们</el-link>
      <el-divider direction="vertical"></el-divider>
      <el-link type="primary">友情链接</el-link>
    </p>
    <p>© 2024 The Regents of the University of Michigan 2281 Bonisteel, Ann Arbor, MI 48105 USA</p>
    <p>Contact us +1 (734) 936-3191</p>
  </el-footer>
</template>
<script>
export default {
  name: "Footer"
};
</script>
<style scoped>
.el-footer {
  background-color: white;
  text-align: center;
  font-size: smaller;
}
.el-divider {
  margin: 0;
  padding: 0;
}
.el-link {
  margin: 0.25em 0.5em;
}
</style>