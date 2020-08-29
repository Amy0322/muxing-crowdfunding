import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import BootstrapVue from "bootstrap-vue";
import upperFirst from "lodash/upperFirst";
import camelCase from "lodash/camelCase";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import axios from 'axios';

Vue.use(BootstrapVue);
// 讓瀏覽器的全域環境可以使用到 $
import jQuery from "jquery";
window.$ = window.jQuery = jQuery;

Vue.config.productionTip = false;

const requireComponent = require.context(
  "./components",
  false,
  /Base[A-Z]\w+\.(vue|js)$/
);

requireComponent.keys().forEach(fileName => {
  const componentConfig = requireComponent(fileName);

  const componentName = upperFirst(
    camelCase(fileName.replace(/^\.\/(.*)\.\w+$/, "$1"))
  );

  Vue.component(componentName, componentConfig.default || componentConfig);
});

new Vue({
  router,
  store,
  beforeCreate () {
    Vue.prototype.$http = axios
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    axios.defaults.xsrfCookieName = 'csrftoken'
  },
  render: h => h(App)
}).$mount("#app");

// new Vue({
//   el: '#app',
//   beforeCreate () {
//     Vue.prototype.$http = axios
//     axios.defaults.xsrfHeaderName = 'X-CSRFToken'
//     axios.defaults.xsrfCookieName = 'csrftoken'
//   },
//   render: h => h(App)
// })
