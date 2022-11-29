const state = {
  allCategories: {},
  childCategories: {},
  mainCategories: [],
};

const mutations = {
  saveChildCategoriesMut(state, payload) {
    state.childCategories = payload;
  },
  saveMainCategoriesMut(state, payload) {
    state.mainCategories = payload;
  },
};

const actions = {
  saveChildCategories({ commit }, payload) {
    commit("saveChildCategoriesMut", payload);
  },
  saveMainCategories({ commit }, payload) {
    commit("saveMainCategoriesMut", payload);
  },
};

const getters = {
  GETCHILDCATEGORIES(state) {
    return state.childCategories;
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
