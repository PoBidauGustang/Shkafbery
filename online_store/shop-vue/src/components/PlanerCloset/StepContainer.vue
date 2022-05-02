<template>
  <div>here is step stepcontainer</div>
  <!-- <p>{{ GETCURRENTSTEP }}</p> -->
  <FirstStep v-if="GETCURRENTSTEP == 1" />
  <SecondStep
    v-if="GETCURRENTSTEP == 2"
    :fillingSchemesList="fillingSchemesList"
  />
  <ThirdStep v-if="GETCURRENTSTEP == 3" />
  <FourthStep v-if="GETCURRENTSTEP == 4" />
  <FifthStep v-if="GETCURRENTSTEP == 5" />
  <button @click="switchToPreviousStep">Previous</button>
  <button @click="switchToNextStep">Next</button>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import FirstStep from "./first_step/FirstStep.vue";
import SecondStep from "./SecondStep.vue";
import ThirdStep from "./third_step/ThirdStep.vue";
import FourthStep from "./fourth_step/FourthStep.vue";
import FifthStep from "./fifth_step/FifthStep.vue";

export default {
  name: "stepcontainer",
  components: {
    FirstStep,
    SecondStep,
    ThirdStep,
    FourthStep,
    FifthStep,
  },
  data() {
    return {
      fillingSchemesList: [],
    };
  },
  created() {
    this.loadFillingSchemesList();
  },
  computed: {
    ...mapGetters("closet_configurator", ["GETCURRENTSTEP"]),
    ...mapGetters("api_urls", ["getServerClosetUrl"]),
  },
  methods: {
    ...mapActions("closet_configurator", [
      "switchToNextStep",
      "switchToPreviousStep",
    ]),
    async loadFillingSchemesList() {
      this.fillingSchemesList = await fetch(
        `${this.getServerClosetUrl}/step_three`
      ).then((response) => response.json());
    },
  },
};
</script>

<style></style>
