<template>
  <div>
    <p>
      ----------------------------------------------------------------------------------------------
    </p>

    <input
      type="radio"
      name="test_id"
      @change="onChange($event)"
      :value="scheme_name"
    />
    <label></label>
    <!-- <label>{{ doors_data }}</label> -->
    <p>Схема: {{ scheme_name }}</p>
    <!-- <p v-html="scheme_description"></p> -->
    <!-- <br /> -->
    <p>в сторе: {{ GETFILLINGSCHEME }}</p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TheFillingScheme",
  props: {
    scheme_name: {
      type: String,
      default() {
        return "ывааыв";
      },
    },
  },
  computed: {
    ...mapGetters("closet_configurator", ["GETFILLINGSCHEME"]),
  },
  methods: {
    ...mapActions("closet_configurator", ["chooseSchema"]),
    onChange(event) {
      this.chooseSchema(event.target.value);
    },
  },
};
</script>

<style></style>
