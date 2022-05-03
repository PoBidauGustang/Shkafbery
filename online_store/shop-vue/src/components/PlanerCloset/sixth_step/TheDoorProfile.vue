<template>
  <div>
    <p>
      ----------------------------------------------------------------------------------------------
    </p>

    <input
      type="radio"
      name="test_id"
      @change="onChange($event)"
      :value="profile_name"
    />
    <label></label>
    <p>Дверной профиль: {{ profile_name }}</p>
    <!-- <p v-html="profile_description"></p> -->
    <!-- <br /> -->
    <p>в сторе: {{ GETDOORSPROFILE }}</p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TheDoorProfile",
  props: {
    profile_name: {
      type: String,
      default() {
        return "ывааыв";
      },
    },
    profile_description: {
      type: String,
      default() {
        return "ывааыв";
      },
    },
  },
  computed: {
    ...mapGetters("closet_configurator", ["GETDOORSPROFILE"]),
  },
  methods: {
    ...mapActions("closet_configurator", ["chooseDoorsProfile"]),
    onChange(event) {
      this.chooseDoorsProfile(event.target.value);
    },
  },
};
</script>

<style></style>
