const state = {
    backendShopUrl: "http://localhost:8000/api/shop",
    backendBlogUrl: "http://localhost:8000/api/blog",

}
const getters = {
    getServerShopUrl: state => {
        return state.backendShopUrl
    },
    getServerBlogUrl: state => {
        return state.backendBlogUrl
    }
}

export default {
    state,
    getters,
}