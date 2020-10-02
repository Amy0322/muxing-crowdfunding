import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Form from "../views/Form.vue";
import Result from "../views/Result.vue";
import Feedback from "../views/Feedback.vue";
import NotFound from "../views/NotFound.vue";


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/form",
    name: "Form",
    component: Form
  },
  {
    path: "/result",
    name: "Result",
    component: Result
  },
  {
    path: "/feedback/:id",
    name: "Feedback",
    component: Feedback,
    props: true
  },
  { path: "*", component: NotFound }
];

const router = new VueRouter({
  routes,
  mode: "history"
});

export default router;
