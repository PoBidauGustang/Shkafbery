const state = {
  cart: 1,
};

const mutations = {
  saveItemsMut(state) {
    // state.cart.push(payload);
    state.cart++;

  },
};

const actions = {
  saveItems({ commit }) {
    commit("saveItemsMut");
  },
};

const getters = {
  GETALLITEMS(state) {
    return (state.cart);
  },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters,
};
