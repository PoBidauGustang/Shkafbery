const uuidv4 = require("uuid/v4");
const state = {
    products: {
        id: uuidv4(),
    },
    price: 1.5, // base price
};
const actions = {};
const mutations = {};

export default {
    namespaced: true,
    state,
    actions,
    mutations,
};