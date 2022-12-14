let cartVar = localStorage.getItem("cart");

const state = {
  cart: cartVar ? JSON.parse(cartVar) : {},
};

const mutations = {
  saveItemMut(state, payload) {
    let item = state.cart[payload.uuid];
    if (item) {
      state.cart[payload.uuid] = {
        item: payload,
        quantity: state.cart[payload.uuid].quantity + 1,
      };
    } else {
      state.cart[payload.uuid] = {
        item: payload,
        quantity: 1,
      };
    }
  },
  removeItemMut(state, payload) {
    let item = state.cart[payload.uuid];
    if (item && state.cart[payload.uuid].quantity > 1) {
      state.cart[payload.uuid] = {
        item: payload,
        quantity: state.cart[payload.uuid].quantity - 1,
      };
    }
  },
  saveDataMut(state) {
    localStorage.setItem("cart", JSON.stringify(state.cart));
  },
  clearCartMut(state) {
    state.cart = {};
    localStorage.removeItem("cart");
  },
};

const actions = {
  saveItem({ commit }, payload) {
    commit("saveItemMut", payload);
    commit("saveDataMut");
  },
  removeItem({ commit }, payload) {
    commit("removeItemMut", payload);
    commit("saveDataMut");
  },
  clearCart({ commit }) {
    commit("clearCartMut");
  },
};

const getters = {
  GETALLITEMS(state) {
    // if (state.cart.length) {
    //   console.log(1)
    return state.cart;
  },
  // else {
  //   console.log(JSON.parse(cartVar))
  //   return JSON.parse(localStorage.getItem("cart"))
  // }

  // },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters,
};
