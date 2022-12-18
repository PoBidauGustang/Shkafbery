let cartVar = localStorage.getItem("cart");
let currentOrderVar = localStorage.getItem("orderedItems");

const state = {
  cart: cartVar ? JSON.parse(cartVar) : {},
  currentOrder: currentOrderVar ? JSON.parse(currentOrderVar) : {},
  orderPrice: localStorage.getItem("orderedPrice") || 0,
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
    state.currentOrder = {};
    localStorage.removeItem("cart");
    localStorage.removeItem("orderedItems");
    localStorage.removeItem("orderedPrice");
  },
  saveCurrentOrderMut(state, payload) {
    console.log("+++++++", payload.uuid, payload.price);
    for (let item in state.cart) {
      if (state.cart[item].item.uuid == payload.uuid) {
        console.log(
          "!!",
          state.cart[item].item.uuid,
          state.cart[item].item.title,
          payload.price
        );
        state.currentOrder[item] = [
          state.cart[item].item.uuid,
          state.cart[item].item.title,
          payload.price,
        ];
      }
    }
    localStorage.setItem("orderedItems", JSON.stringify(state.currentOrder));
  },
  calcOrderPriceMut(state) {
    let price = 0;
    for (let item in state.currentOrder) {
      price += Number(state.currentOrder[item][2]);
    }
    state.orderPrice = price;
    localStorage.setItem("orderedPrice", state.orderPrice);
  },
};

const actions = {
  saveItem({ commit }, payload) {
    console.log("price in cart", payload.price);
    commit("saveItemMut", payload.item);
    commit("saveDataMut");
    commit("saveCurrentOrderMut", {
      uuid: payload.item.uuid,
      price: payload.price,
    });
    commit("calcOrderPriceMut");
  },
  removeItem({ commit }, payload) {
    commit("removeItemMut", payload.item);
    commit("saveDataMut");
    commit("saveCurrentOrderMut", {
      uuid: payload.item.uuid,
      price: payload.price,
    });
    commit("calcOrderPriceMut");
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
  GETALLPRICE(state) {
    // let price = 0;
    // for (let item in state.currentOrder) {
    //   console.log(state.currentOrder[item])
    //   price += state.currentOrder[item].price
    // }
    return state.orderPrice;
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
