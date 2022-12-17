import axios from "axios";


const state = {
  status: "",
  token: localStorage.getItem("token") || "",
  userData: localStorage.getItem("user_data") || {},
  username: localStorage.getItem("username") || "",
};

const mutations = {
  authRequestMut(state) {
    state.status = "loading";
  },
  authSuccessMut(state, token, aa) {
    state.status = "success";
    state.token = token;
    // localStorage.setItem("user_data", user)
    // state.userData = user;
    console.log("!!!!!!!", aa["username"])
    localStorage.setItem("username", aa["username"])
    state.username = aa["username"];
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
      axios
        .post(`http://127.0.0.1:8000/api/auth/token/login/`, user, options)
        .then((resp) => {
          const token = resp.data.data.attributes.auth_token;
          // const user = resp.data.data.attributes;
          localStorage.setItem("token", token);
          // console.log("!!!", user);
          axios.defaults.headers.common["Authorization"] = token;
          console.log(user.username);
          let aa = user["username"];
          commit("authSuccessMut", token, aa);
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
    return new Promise((resolve, reject) => {
      let token = localStorage.getItem("token");
      const options = {
        headers: {
          "Authorization": "Token " + token,
        },
      };
      axios
        .post("http://127.0.0.1:8000/api/auth/token/logout", {}, options)
        .then((resp) => {
          localStorage.removeItem("token");
          axios.defaults.headers.common["Authorization"] = null;
          commit("logoutMut");
          resolve(resp);
        })
        .catch((err) => {
          reject(err);
        });
    });
  },
};

const getters = {
  // ISLOGGEDIN: (state) => !!state.token,
  AUTHSTATUS: (state) => state.status,
  ISLOGGEDIN(state) {
    return !!state.token;
  },
  GETUSER(state) {
    return state.user;
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
