const state = {
  test: JSON.parse(localStorage.getItem("testvalue")),
};

const mutations = {
  incrementMut(state) {
    let testvalue = localStorage.getItem("testvalue");
    if (testvalue) {
      state.test = JSON.parse(testvalue);
    }
    state.test++;
    localStorage.setItem("testvalue", JSON.stringify(state.test));
  },
};

const actions = {
  increment({ commit }) {
    commit("incrementMut");
  },
};

const getters = {
  TEST(state) {
    return state.test;
  },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters,
};
