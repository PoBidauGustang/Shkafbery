<template>
  <div>
    <StepContainer />
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import StepContainer from "../components/PlanerCloset/StepContainer.vue";
export default {
  name: "PlannerCloset",
  data() {
    return {};
  },
  components: {
    StepContainer,
  },
  computed: {
    ...mapState("closet_configurator", ["steps", "config"]),
    ...mapGetters("closet_configurator", []),
    showBwithoutgetter() {
      return this.$store.state.closet_configurator.b;
    },
  },
  // methods: {
  //   ...mapActions("closet_configurator", ["switchStepVisability"]),
  // },

  // mounted() {
  //   this.switchStepVisability();
  // },
};
</script>
