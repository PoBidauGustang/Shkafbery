const uuidv4 = require("uuid/v4");

const state = {
  config: {
    id: uuidv4(),
    doorsAmount: "",
    doorDimensions: {
      width: { name: "ширина", value: "" },
      height: { name: "высота", value: "" },
      depth: { name: "глубина", value: "" },
    },
    fillingScheme: "",
    bodyСolor: "",
    doorsSystem: "",
    doorProfile: "",
    doorConfig: "",
    bodyComplectation: "",
    additionalElements: "",
  },
  // steps: {
  //   1: {
  //     active: true,
  //     filled: false,
  //   },
  //   2: {
  //     active: false,
  //     filled: false,
  //   },
  //   3: {
  //     active: false,
  //     filled: false,
  //   },
  //   4: {
  //     active: false,
  //     filled: false,
  //   },
  //   5: {
  //     active: false,
  //     filled: false,
  //   },
  //   6: {
  //     active: false,
  //     filled: false,
  //   },
  //   7: {
  //     active: false,
  //     filled: false,
  //   },
  //   8: {
  //     active: false,
  //     filled: false,
  //   },
  //   9: {
  //     active: false,
  //     filled: false,
  //   },
  // },
  currentStep: 1,
  filledSteps: [],
  count: 5,
};

const mutations = {
  incrementMut(state) {
    state.count++;
  },
  // switchStepVisabilityMut(state) {
  //   for (let step in state.steps) {
  //     // if (state.steps[state.currentStep].active == false) {
  //     if (step.active == false) {
  //       continue;
  //     } else {
  //       console.log("after", state.currentStep, step);
  //       state.steps[state.currentStep].active = false;
  //       if (state.currentStep == 9) {
  //         break;
  //       }
  //       state.currentStep += 1;
  //       state.steps[state.currentStep].active = true;
  //       console.log("after", state.currentStep, step);
  //       break;
  //     }
  //   }
  // },
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
  },
  chooseDoorsDimensionsWidthMut(state, payload) {
    state.config.doorDimensions.width.value = payload;
  },
  chooseDoorsDimensionsHeightMut(state, payload) {
    state.config.doorDimensions.height.value = payload;
  },
  chooseDoorsDimensionsDepthMut(state, payload) {
    state.config.doorDimensions.depth.value = payload;
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
  chooseDoorsDimensionsWidth({ commit }, payload) {
    commit("chooseDoorsDimensionsWidthMut", payload);
  },
  chooseDoorsDimensionsHeight({ commit }, payload) {
    commit("chooseDoorsDimensionsHeightMut", payload);
  },
  chooseDoorsDimensionsDepth({ commit }, payload) {
    commit("chooseDoorsDimensionsDepthMut", payload);
  },
};

const getters = {
  GETCURRENTSTEP(state) {
    return state.currentStep;
  },
  GETDOORSAMOUNT(state) {
    return state.config.doorsAmount;
  },
  GETDOORSDIMENSIONS(state) {
    return state.config.doorDimensions;
  },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters,
};
