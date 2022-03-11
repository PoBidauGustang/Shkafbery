<template>
  <div>
    <p>
      ----------------------------------------------------------------------------------------------
    </p>
    <p>Карточка № {{ doors_data }}</p>
    <input
      type="radio"
      name="test_id"
      @change="onChange($event)"
      :value="doors_data"
    />
    <label>{{ doors_data }}</label>
    <!-- <br /> -->
    <!-- <p>в сторе: {{GETDOORSAMOUNT}}</p> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TheDoor",
  props: {
    doors_data: {
      type: String,
      default() {
        return "";
      },
    },
  },
  computed: {
    ...mapGetters("closet_configurator", ["GETDOORSAMOUNT"]),
  },
  methods: {
    ...mapActions("closet_configurator", ["chooseDoorsAmount"]),
    onChange(event) {
      this.chooseDoorsAmount(event.target.value);
    },
  },
};
</script>

<style></style>
