import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from "/src/App.vue";

const store = createStore({
    state: {
        backendShopUrl: "http://localhost:8000/api/shop",
        backendBlogUrl: "http://localhost:8000/api/blog",
    },
    mutations: {},
    actions: {},
    modules: {},
    getters: {
        getServerShopUrl: state => {
            return state.backendShopUrl
        },
        getServerBlogUrl: state => {
            return state.backendBlogUrl
        }
    }
})

const app = createApp({ App })

app.use(store)

export default store