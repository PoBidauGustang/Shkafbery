import axios from "axios";
// let allCategoriesVar = localStorage.getItem("allCategories");
// let childCategoriesVar = localStorage.getItem("childCategories");
// let mainCategoriesVar = localStorage.getItem("mainCategories");

const state = {
  status: "",
  token: localStorage.getItem("token") || "",
  user: {},
};

const mutations = {
  // saveItemMut(state, payload) {
  //   let item = state.cart[payload.id];
  //   if (item) {
  //     state.cart[payload.id] = {
  //       item: payload,
  //       quantity: state.cart[payload.id].quantity + 1,
  //     };
  //   } else {
  //     state.cart[payload.id] = {
  //       item: payload,
  //       quantity: 1,
  //     };
  //   }
  // },
  // saveItemMut(state, payload) {
  //   state.allCategories = payload;
  // },
  // saveAllCategoriesMut(state, payload) {
  //   state.allCategories = payload;
  //   localStorage.setItem("allCategories", JSON.stringify(state.allCategories));
  // },
  // saveChildCategoriesMut(state, payload) {
  //   state.childCategories = payload;
  //   localStorage.setItem(
  //     "childCategories",
  //     JSON.stringify(state.childCategories)
  //   );
  // },
  // saveMainCategoriesMut(state, payload) {
  //   state.mainCategories = payload;
  //   localStorage.setItem(
  //     "mainCategories",
  //     JSON.stringify(state.mainCategories)
  //   );
  // },
  authRequestMut(state) {
    state.status = "loading";
  },
  authSuccessMut(state, token, user) {
    state.status = "success";
    state.token = token;
    state.user = user;
  },
  authErrorMut(state) {
    state.status = "error";
  },
  logoutMut(state) {
    state.status = "";
    state.token = "";
  },
};

const actions = {
  loginUser({ commit }, user) {
    return new Promise((resolve, reject) => {
      commit("authRequestMut");
      const options = {
        headers: {
          "Content-Type": "application/json",
        },
      };
      // console.log(user)
      // axios.post('http://127.0.0.1:8000/api/auth/token/login/', options, user)
      axios
        .post(`http://127.0.0.1:8000/api/auth/token/login/`, user, options)
        .then((resp) => {
          // const token = resp.data.token
          const token = resp.data.data.attributes.auth_token;
          const user = resp.data.data;
          localStorage.setItem("token", token);
          console.log(user);
          axios.defaults.headers.common["Authorization"] = token;
          commit("authSuccessMut", token, user);
          resolve(resp);
        })
        .catch((err) => {
          commit("authErrorMut");
          localStorage.removeItem("token");
          reject(err);
        });
    });
  },
  registerUser({ commit }, user) {
    return new Promise((resolve, reject) => {
      commit("authRequestMut");
      const options = {
        headers: {
          "Content-Type": "application/json",
        },
      };
      axios
        .post("http://127.0.0.1:8000/api/auth/users/", user, options)
        .then((resp) => {
          const token = resp.data.token;
          const user = resp.data.user;
          localStorage.setItem("token", token);
          axios.defaults.headers.common["Authorization"] = token;
          commit("authSuccessMut", token, user);
          resolve(resp);
        })
        .catch((err) => {
          commit("authErrorMut", err);
          localStorage.removeItem("token");
          reject(err);
        });
    });
  },
  logoutUser({ commit }) {
    return new Promise((resolve) => {
      commit("logoutMut");
      localStorage.removeItem("token");
      delete axios.defaults.headers.common["Authorization"];
      resolve();
    });
  },
  // saveMainCategories({ commit }, payload) {
  //   commit("saveMainCategoriesMut", payload);
  // },
};

const getters = {
  ISLOGGEDIN: (state) => !!state.token,
  AUTHSTATUS: (state) => state.status,
  // GETALLCATEGORIES(state) {
  //   return state.allCategories;
  // },
  // GETCHILDCATEGORIES(state) {
  //   return state.childCategories;
  // },
  // GETMAINCATEGORIES(state) {
  //   return state.mainCategories;
  // },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
