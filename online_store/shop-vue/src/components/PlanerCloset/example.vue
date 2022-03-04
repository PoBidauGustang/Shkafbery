<template>
  <div>
    <!-- <button @click="gotPrice">hey {{currentStep}}</button> -->
    <!-- <button @click="StepVisibility">hey {{ currentStep }}</button>
    <div>{{ currentStep }}</div> -->
  </div>
</template>

<script>
export default {
  name: "example",
  model: {
    prop: "currentStep",
    event: "StepVisibility",
  },
  props: ["currentStep", "newcurrentStep"],
  methods: {
    StepVisibility(e) {
      // this.switchStepVisibility
      this.$emit("StepVisibility", e.target.value);
    },
  },
};
</script>

<style></style>
