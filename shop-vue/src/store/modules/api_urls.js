const state = {
  // backendShopUrl: "http://localhost:8000/api/shop",
  // backendBlogUrl: "http://localhost:8000/api/blog",
  // backendClosetUrl: "http://localhost:8000/api/closet",
  // backendInformationUrl: "http://localhost:8000/api/information",
  // backendAuthUrl: "http://localhost:8000/auth/token",
  backendShopUrl: "http://185.46.11.192:8000/api/shop",
  backendBlogUrl: "http://185.46.11.192:8000/api/blog",
  backendClosetUrl: "http://185.46.11.192:8000/api/closet",
  backendInformationUrl: "http://185.46.11.192:8000/api/information",
  backendAuthUrl: "http://185.46.11.192:8000/auth/token",
};
const getters = {
  getServerShopUrl(state) {
    return state.backendShopUrl;
  },
  getServerBlogUrl(state) {
    return state.backendBlogUrl;
  },
  getServerClosetUrl(state) {
    return state.backendClosetUrl;
  },
  getServerInformationUrl(state) {
    return state.backendInformationUrl;
  },
  getServerAuthUrl(state) {
    return state.backendAuthUrl;
  },
};

export default {
  namespaced: true,
  state,
  getters,
};
