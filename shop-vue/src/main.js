import * as Vue from "vue";
// import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import VueAxios from "vue-axios";

const app = Vue.createApp(App);
const token = localStorage.getItem("token");
if (token) {
  axios.defaults.headers.common["Authorization"] = token;
}
app.use(store).use(router).use(VueAxios, axios).mount("#app");
