import axios from "axios";

let userDataVar = localStorage.getItem("user_data");

const state = {
  status: "",
  token: localStorage.getItem("token") || "",
  // userData: localStorage.getItem("user_data") || null,
  userData: userDataVar ? JSON.parse(userDataVar) : {},
  username: localStorage.getItem("username") || "",
};

const mutations = {
  authRequestMut(state) {
    state.status = "loading";
  },
  authSuccessMut(state, token) {
    state.status = "success";
    state.token = token;
    // localStorage.setItem("user_data", user)
    // state.userData = user;
    // console.log("!!!!!!!", aa["username"])
    // localStorage.setItem("username", aa["username"])
    // state.username = aa["username"];
  },
  authErrorMut(state) {
    state.status = "error";
  },
  logoutMut(state) {
    state.status = "";
    state.token = "";
    state.userData = {};
    state.username = "";
  },
  setUserMut(state, user) {
    localStorage.setItem("username", user);
    state.username = user;
  },
  setUserDataMut(state, data) {
    console.log(data);
    localStorage.setItem("user_data", JSON.stringify(data));
    state.userData = data;
  },
};

const actions = {
  loginUser({ commit }, user) {
    return new Promise((resolve, reject) => {
      commit("authRequestMut");
      commit("setUserMut", user.username);
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
          // console.log(user.username);
          // let aa = user["username"];
          commit("authSuccessMut", token);
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
          Authorization: "Token " + token,
        },
      };
      axios
        .post("http://127.0.0.1:8000/api/auth/token/logout", {}, options)
        .then((resp) => {
          localStorage.removeItem("token");
          localStorage.removeItem("username");
          localStorage.removeItem("user_data");
          axios.defaults.headers.common["Authorization"] = null;
          commit("logoutMut");
          resolve(resp);
        })
        .catch((err) => {
          reject(err);
        });
    });
  },
  loadUserData({ commit }) {
    return new Promise((resolve, reject) => {
      let token = localStorage.getItem("token");
      const options = {
        headers: {
          Authorization: "Token " + token,
        },
      };
      axios
        .get("http://127.0.0.1:8000/api/auth/users/me", options)
        .then((resp) => {
          // localStorage.removeItem("token");
          // localStorage.removeItem("username");
          // localStorage.removeItem("user_data");
          // axios.defaults.headers.common["Authorization"] = null;
          const data = resp.data.data.attributes;
          console.log("!!!!", data);
          commit("setUserDataMut", data);
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
    return state.username;
  },
  GETUSERDATA(state) {
    return state.userData;
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
