const state = {
  cart: {},
};

const mutations = {
  saveItemMut(state, payload) {
    let itemLocalStorage = localStorage.getItem(payload.id);
    if (itemLocalStorage) {
      state.cart[payload.id] = {
        item: payload,
        quantity: JSON.parse(itemLocalStorage) + 1,
      };
    } else {
      state.cart[payload.id] = {
        item: payload,
        quantity: 1,
      };
    }
    localStorage.setItem(
      payload.id,
      JSON.stringify(state.cart[payload.id].quantity)
    );
  },
  loadCartMut(state) {
    let itemsLocalStorage = JSON.stringify(localStorage);
    if (itemsLocalStorage) {
      state.cart = itemsLocalStorage;
    }
  },
};

const actions = {
  saveItem({ commit }, payload) {
    commit("saveItemMut", payload);
  },
  loadCart({ commit }) {
    commit("loadCartMut");
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
