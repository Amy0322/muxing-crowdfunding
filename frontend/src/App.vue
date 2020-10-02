<template>
  <div id="app">
    <div
      class="navbar navbar-expand-sm navbar-light bg-light fixed-top navbar-top mx-auto border-bottom"
      id="nav"
    >
      <div class="container">
        <router-link class="router" style="text-decoration: none;" to="/">
          <img src="https://i.imgur.com/RQ7zU1P.png" width="37%" height="" />
          <span class="logo-name">募星</span>
        </router-link>
        <img class="bar" src="https://i.imgur.com/5j5ECcc.png" />
      </div>
    </div>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  height: 60px;
}

#nav a {
  padding: 5px 20px;
  color: #fff;
  cursor: pointer;
}

#nav a.router-link-exact-active {
  padding: 5px 20px;
  color: #42b983;
  font-weight: 550;
  cursor: pointer;
}

.navbar {
  overflow: hidden;
  height: 60px;
  background: -webkit-linear-gradient(left, #281483, #be78d1);
  background: -o-linear-gradient(right, #281483, #be78d1);
  background: -moz-linear-gradient(right, #281483, #be78d1);
  background: linear-gradient(to right, #281483, #be78d1);
}

.bar {
  position: absolute;
  right: 0px;
}

.router {
  left: -20px;
}

.logo-name {
  font-family: "微軟正黑體";
  top: 5px;
  left: 10px;
  color: #fff;
}
</style>

<script>
export default {
  // 使用watch監聽$router的變化，跳頁時移到最上方
  watch: {
    // eslint-disable-next-line no-unused-vars
    $route: function(to, from) {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    }
  }
};
</script>
