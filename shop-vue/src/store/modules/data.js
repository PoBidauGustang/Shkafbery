let allCategoriesVar = localStorage.getItem("allCategories");
let childCategoriesVar = localStorage.getItem("childCategories");
let mainCategoriesVar = localStorage.getItem("mainCategories");

const state = {
  allCategories: allCategoriesVar ? JSON.parse(allCategoriesVar) : {},
  childCategories: childCategoriesVar ? JSON.parse(childCategoriesVar) : {},
  mainCategories: mainCategoriesVar ? JSON.parse(mainCategoriesVar) : [],
  // currentSubSideMenuVisability: false,
  mainSubMenuVisability: "",
  // allCategories: {},
  // childCategories: {},
  // mainCategories: [],
};

const mutations = {
  // saveItemMut(state, payload) {
  //   let item = state.cart[payload.id];
  //   if (item) {
  //     state.cart[payload.id] = {
  //       item: payload,
  //       quantity: state.cart[payload.id].quantity + 1,
  //     };
  //   } else {
  //     state.cart[payload.id] = {
  //       item: payload,
  //       quantity: 1,
  //     };
  //   }
  // },
  // saveItemMut(state, payload) {
  //   state.allCategories = payload;
  // },
  saveAllCategoriesMut(state, payload) {
    state.allCategories = payload;
    localStorage.setItem("allCategories", JSON.stringify(state.allCategories));
  },
  saveChildCategoriesMut(state, payload) {
    state.childCategories = payload;
    localStorage.setItem(
      "childCategories",
      JSON.stringify(state.childCategories)
    );
  },
  saveMainCategoriesMut(state, payload) {
    state.mainCategories = payload;
    localStorage.setItem(
      "mainCategories",
      JSON.stringify(state.mainCategories)
    );
  },
  switchMainSubMenuVisabilityMut(state, payload) {
    if (state.mainSubMenuVisability === payload) {
      state.mainSubMenuVisability = ""
    }
    else {
      state.mainSubMenuVisability = payload;
    }
    console.log(state.mainSubMenuVisability);
  },
  closeSubMenuMut(state) {
    state.mainSubMenuVisability = "";
    console.log("closed");
  },
};

const actions = {
  saveAllCategories({ commit }, payload) {
    commit("saveAllCategoriesMut", payload);
  },
  saveChildCategories({ commit }, payload) {
    commit("saveChildCategoriesMut", payload);
  },
  saveMainCategories({ commit }, payload) {
    commit("saveMainCategoriesMut", payload);
  },
  switchMainSubMenuVisability({ commit }, payload) {
    commit("switchMainSubMenuVisabilityMut", payload);
  },
  closeSubMenu({ commit }) {
    commit("closeSubMenuMut");
  },
};

const getters = {
  GETALLCATEGORIES(state) {
    return state.allCategories;
  },
  GETCHILDCATEGORIES(state) {
    return state.childCategories;
  },
  GETMAINCATEGORIES(state) {
    return state.mainCategories;
  },
  GETCMAINSUBMENUVISABILITY(state) {
    return state.mainSubMenuVisability;
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
