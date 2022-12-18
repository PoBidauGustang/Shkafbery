const state = {
  backendShopUrl: "http://127.0.0.1:8000/api/shop",
  backendBlogUrl: "http://127.0.0.1:8000/api/blog",
  backendClosetUrl: "http://127.0.0.1:8000/api/closet",
  backendInformationUrl: "http://127.0.0.1:8000/api/information",
  backendAuthUrl: "http://127.0.0.1:8000/api/auth",
  backendOrdersUrl: "http://127.0.0.1:8000/api/orders",
  // backendShopUrl: "http://185.46.11.192/api/shop",
  // backendBlogUrl: "http://185.46.11.192/api/blog",
  // backendClosetUrl: "http://185.46.11.192/api/closet",
  // backendInformationUrl: "http://185.46.11.192/api/information",
  // backendAuthUrl: "http://185.46.11.192/api/auth",
  // backendOrdersUrl: "http://185.46.11.192/api/orders",
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
  getServerOrdersUrl(state) {
    return state.backendOrdersUrl;
  },
};

export default {
  namespaced: true,
  state,
  getters,
};
