const uuidv4 = require("uuid/v4");

const state = {
  config: {
    id: uuidv4(),
    doorsAmount: "",
    dimensions: {
      width: { name: "ширина", value: "" },
      height: { name: "высота", value: "" },
      depth: { name: "глубина", value: "" },
    },
    fillingScheme: "",
    bodyСolor: "",
    doorsSystem: "",
    doorProfile: "",
    doorHandle: "",
    doorMaterials: {},
    doorConfig: "",
    bodyComplectation: "",
    additionalElements: "",
  },
  currentStep: 1,
  filledSteps: [],
  count: 5,
  dimensionsData: [],
  suitableFillingSchemes: [],
};

const mutations = {
  incrementMut(state) {
    state.count++;
  },
  switchToNextStepMut(state) {
    for (; state.currentStep < 9; ) {
      state.currentStep += 1;
      break;
    }
  },
  switchToPreviousStepMut(state) {
    for (; state.currentStep > 1; ) {
      state.currentStep -= 1;
      break;
    }
  },
  chooseDoorsAmountMut(state, payload) {
    state.config.doorsAmount = payload;
    let num = 0;
    if (payload === "Две") {
      num = 2;
    }
    if (payload === "Три") {
      num = 3;
    }
    if (payload === "Четыре") {
      num = 4;
    }
    if (payload === "Пять") {
      num = 5;
    }
    for (let i = 1; i <= num; i++) {
      state.config.doorMaterials[i] = {};
    }
  },
  chooseDimensionsWidthMut(state, payload) {
    state.config.dimensions.width.value = payload;
  },
  chooseDimensionsHeightMut(state, payload) {
    state.config.dimensions.height.value = payload;
  },
  chooseDimensionsDepthMut(state, payload) {
    state.config.dimensions.depth.value = payload;
  },
  saveDimensionsDataMut(state, payload) {
    state.dimensionsData = payload;
  },
  saveSuitableFillingSchemesMut(state, payload) {
    state.suitableFillingSchemes = payload;
  },
  chooseSchemaMut(state, payload) {
    state.config.fillingScheme = payload;
  },
  chooseBodyColorMut(state, payload) {
    state.config.bodyColor = payload;
  },
  chooseDoorsSystemMut(state, payload) {
    state.config.doorsSystem = payload;
  },
  chooseDoorsProfileMut(state, payload) {
    state.config.doorProfile = payload;
  },
  chooseDoorHandleMut(state, payload) {
    state.config.doorHandle = payload;
  },
  chooseDoorSectionMut(state, payload) {
    let listPayload = payload.split(",");
    let doorNum = listPayload[0];
    let sectionNum = listPayload[1];
    state.config.doorMaterials[doorNum] = {};
    for (let i = 1; i <= sectionNum; i++) {
      state.config.doorMaterials[doorNum][i] = "";
    }
  },
  chooseDoorMaterialsMut(state, payload) {
    let listPayload = payload.split(",");
    let doorNum = listPayload[0];
    let sectionNum = listPayload[1];
    let material = listPayload[2];
    state.config.doorMaterials[doorNum][sectionNum] = material;
  },
};

const actions = {
  increment({ commit }) {
    commit("incrementMut");
  },
  // switchStepVisability({ commit }) {
  //   commit("switchStepVisabilityMut");
  // },
  switchToNextStep({ commit }) {
    commit("switchToNextStepMut");
  },
  switchToPreviousStep({ commit }) {
    commit("switchToPreviousStepMut");
  },
  chooseDoorsAmount({ commit }, payload) {
    commit("chooseDoorsAmountMut", payload);
  },
  chooseDimensionsWidth({ commit }, payload) {
    commit("chooseDimensionsWidthMut", payload);
  },
  chooseDimensionsHeight({ commit }, payload) {
    commit("chooseDimensionsHeightMut", payload);
  },
  chooseDimensionsDepth({ commit }, payload) {
    commit("chooseDimensionsDepthMut", payload);
  },
  saveDimensionsData({ commit }, payload) {
    commit("saveDimensionsDataMut", payload);
  },
  saveSuitableFillingSchemes({ commit }, payload) {
    commit("saveSuitableFillingSchemesMut", payload);
  },
  chooseSchema({ commit }, payload) {
    commit("chooseSchemaMut", payload);
  },
  chooseBodyColor({ commit }, payload) {
    commit("chooseBodyColorMut", payload);
  },
  chooseDoorsSystem({ commit }, payload) {
    commit("chooseDoorsSystemMut", payload);
  },
  chooseDoorsProfile({ commit }, payload) {
    commit("chooseDoorsProfileMut", payload);
  },
  chooseDoorHandle({ commit }, payload) {
    commit("chooseDoorHandleMut", payload);
  },
  chooseDoorSection({ commit }, payload) {
    commit("chooseDoorSectionMut", payload);
  },
  chooseDoorMaterials({ commit }, payload) {
    commit("chooseDoorMaterialsMut", payload);
  },
};

const getters = {
  GETCURRENTSTEP(state) {
    return state.currentStep;
  },
  GETDOORSAMOUNT(state) {
    return state.config.doorsAmount;
  },
  GETDIMENSIONS(state) {
    return state.config.dimensions;
  },
  GETDIMENSIONSDATA(state) {
    return state.dimensionsData;
  },
  GETSUITABLEFILLINGSCHEMES(state) {
    return state.suitableFillingSchemes;
  },
  GETFILLINGSCHEME(state) {
    return state.config.fillingScheme;
  },
  GETBODYCOLOR(state) {
    return state.config.bodyColor;
  },
  GETDOORSSYSTEM(state) {
    return state.config.doorsSystem;
  },
  GETDOORSPROFILE(state) {
    return state.config.doorProfile;
  },
  GETDOORHANDLE(state) {
    return state.config.doorHandle;
  },
  GETDOORMATERIALS(state) {
    return state.config.doorMaterials;
  },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters,
};

// function addNumOfDoorsToMaterials() {

//   return aa = 2;
// };
