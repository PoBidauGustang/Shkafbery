<template>
  <div>
    <p>
      ----------------------------------------------------------------------------------------------
    </p>

    <input
      type="radio"
      name="handle"
      @change="onChange($event)"
      :value="handle_name"
    />
    <label></label>
    <p>Дверная ручка: {{ handle_name }}</p>
    <!-- <p v-html="handle_description"></p> -->
    <!-- <br /> -->
    <p>в сторе: {{ GETDOORHANDLE }}</p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TheDoorHandle.vue",
  props: {
    handle_name: {
      type: String,
      default() {
        return "ывааыв";
      },
    },
    handle_description: {
      type: String,
      default() {
        return "ывааыв";
      },
    },
  },
  computed: {
    ...mapGetters("closet_configurator", ["GETDOORHANDLE"]),
  },
  methods: {
    ...mapActions("closet_configurator", ["chooseDoorHandle"]),
    onChange(event) {
      this.chooseDoorHandle(event.target.value);
    },
  },
};
</script>

<style></style>
