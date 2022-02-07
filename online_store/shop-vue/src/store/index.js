import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from "/src/App.vue";

const store = createStore({
    state: {
        // backendUrl: "http://127.0.0.1:8000/api/v1"
        backendUrl: "http://localhost:8000/api/v1"
    },
    mutations: {},
    actions: {},
    modules: {},
    getters: {
        getServerUrl: state => {
            return state.backendUrl
        }
    }
})

const app = createApp({ App })

app.use(store)

export default store