const state = {
  backendShopUrl: "http://localhost:8000/api/shop",
  backendBlogUrl: "http://localhost:8000/api/blog",
  backendClosetUrl: "http://localhost:8000/api/closet",
};
const getters = {
  getServerShopUrl: (state) => {
    return state.backendShopUrl;
  },
  getServerBlogUrl: (state) => {
    return state.backendBlogUrl;
  },
  getServerClosetUrl: (state) => {
    return state.backendClosetUrl;
  },
};

export default {
  state,
  getters,
};
