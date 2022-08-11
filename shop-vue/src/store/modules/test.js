const state = {
  test: 1
};

const mutations = {
  incrementMut(state) {
    state.test++;
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
