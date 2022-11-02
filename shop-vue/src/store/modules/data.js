const state = {
  allCategories: {},
  mainCategories: [],
};

const mutations = {
  saveAllCategoriesMut(state, payload) {
    state.allCategories = payload;
  },
  saveMainCategoriesMut(state, payload) {
    state.mainCategories = payload;
  },
};

const actions = {
  saveAllCategories({ commit }, payload) {
    commit("saveAllCategoriesMut", payload);
  },
  saveMainCategories({ commit }, payload) {
    commit("saveMainCategoriesMut", payload);
  },
};

const getters = {
  GETALLCATEGORIES(state) {
    return state.allCategories;
  },
  GETMAINCATEGORIES(state) {
    return state.mainCategories;
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
