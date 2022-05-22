<template>
  <div>
    <p>
      ----------------------------------------------------------------------------------------------
    </p>

    <input
      type="radio"
      name="test_id"
      @change="onChange($event)"
      :value="system_name"
    />
    <label></label>
    <p>Система: {{ system_name }}</p>
    <!-- <p v-html="scheme_description"></p> -->
    <!-- <br /> -->
    <p>в сторе: {{ GETDOORSSYSTEM }}</p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TheDoorsSystem",
  props: {
    system_name: {
      type: String,
      default() {
        return "ывааыв";
      },
    },
    system_description: {
      type: String,
      default() {
        return "ывааыв";
      },
    },
  },
  computed: {
    ...mapGetters("closet_configurator", ["GETDOORSSYSTEM"]),
  },
  methods: {
    ...mapActions("closet_configurator", ["chooseDoorsSystem"]),
    onChange(event) {
      this.chooseDoorsSystem(event.target.value);
    },
  },
};
</script>

<style></style>
