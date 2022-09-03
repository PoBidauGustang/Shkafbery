let cartVar = localStorage.getItem("cart");

const state = {
  cart: cartVar ? JSON.parse(cartVar) : {},
};

const mutations = {
  saveItemMut(state, payload) {
    let item = state.cart[payload.id];
    if (item) {
      state.cart[payload.id] = {
        item: payload,
        quantity: state.cart[payload.id].quantity + 1,
      };
    } else {
      state.cart[payload.id] = {
        item: payload,
        quantity: 1,
      };
    }
  },
  saveDataMut(state) {
    localStorage.setItem("cart", JSON.stringify(state.cart));
  },
};

const actions = {
  saveItem({ commit }, payload) {
    commit("saveItemMut", payload);
    commit("saveDataMut");
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
  actions,
  mutations,
  getters,
};
