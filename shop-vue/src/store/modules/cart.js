const state = {
  cart: {},
};

const mutations = {
  saveItemsMut(state, payload) {
    state.allCategories = payload;
  },
};

const actions = {
  saveItems({ commit }, payload) {
    commit("saveItemsMut", payload);
  },
};

const getters = {
  GETALLITEMS(state) {
    return state.cart;
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
