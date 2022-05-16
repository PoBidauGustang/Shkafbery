const state = {
  allCategories: {},
};

const mutations = {
  saveAllCategoriesMut(state, payload) {
    state.allCategories = payload;
  },
};

const actions = {
  saveAllCategories({ commit }, payload) {
    commit("saveAllCategoriesMut", payload);
  },
};

const getters = {
  GETALLCATEGORIES(state) {
    return state.allCategories;
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
