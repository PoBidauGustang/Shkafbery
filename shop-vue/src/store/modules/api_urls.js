const state = {
<<<<<<< HEAD
  // backendShopUrl: "http://localhost:8000/api/shop",
  // backendBlogUrl: "http://localhost:8000/api/blog",
  // backendClosetUrl: "http://localhost:8000/api/closet",
  // backendInformationUrl: "http://localhost:8000/api/information",
  // backendAuthUrl: "http://localhost:8000/auth/token",
=======
  // backendShopUrl: "http://127.0.0.1:8000/api/shop",
  // backendBlogUrl: "http://127.0.0.1:8000/api/blog",
  // backendClosetUrl: "http://127.0.0.1:8000/api/closet",
  // backendInformationUrl: "http://127.0.0.1:8000/api/information",
  // backendAuthUrl: "http://127.0.0.1:8000/api/auth",
  // backendOrdersUrl: "http://127.0.0.1:8000/api/orders",
>>>>>>> 639568eed9f04c9434a5ff701f0540c029242ff2
  backendShopUrl: "http://194.67.119.7/api/shop",
  backendBlogUrl: "http://194.67.119.7/api/blog",
  backendClosetUrl: "http://194.67.119.7/api/closet",
  backendInformationUrl: "http://194.67.119.7/api/information",
<<<<<<< HEAD
  backendAuthUrl: "http://194.67.119.7/api/auth/token",
=======
  backendAuthUrl: "http://194.67.119.7/api/auth",
  backendOrdersUrl: "http://194.67.119.7/api/orders",
>>>>>>> 639568eed9f04c9434a5ff701f0540c029242ff2
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
