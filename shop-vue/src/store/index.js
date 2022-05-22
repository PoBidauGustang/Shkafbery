import { createApp } from "vue";
import { createStore } from "vuex";
import closet_configurator from "./modules/closet_configurator";
import api_urls from "./modules/api_urls";
import data from "./modules/data";
import App from "/src/App.vue";

const store = createStore({
  modules: {
    closet_configurator,
    api_urls,
    data,
  },
});

const app = createApp({ App });

app.use(store);

export default store;
