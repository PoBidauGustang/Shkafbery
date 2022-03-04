<template>
  <div>here is step stepcontainer</div>
  <p>{{ GETCURRENTSTEP }}</p>
  <button @click="switchToPreviousStep">Previous</button>
  <button @click="switchToNextStep">Next</button>
  <FirstStep v-if="GETCURRENTSTEP == 1" />
  <SecondStep v-if="GETCURRENTSTEP == 2" />
  <ThirdStep v-if="GETCURRENTSTEP == 3" />
  <FourthStep v-if="GETCURRENTSTEP == 4" />
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import FirstStep from "./FirstStep.vue";
import SecondStep from "./SecondStep.vue";
import ThirdStep from "./ThirdStep.vue";
import FourthStep from "./FourthStep.vue";

export default {
  name: "stepcontainer",
  components: {
    FirstStep,
    SecondStep,
    ThirdStep,
    FourthStep,
  },
  props: ["currentStep"],
  computed: {
    ...mapGetters("closet_configurator", ["GETCURRENTSTEP"]),
  },
  methods: {
    ...mapActions("closet_configurator", [
      "switchToNextStep",
      "switchToPreviousStep",
    ]),
  },
};
</script>

<style></style>
