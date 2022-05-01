<template>
  <div>
    <p>
      ----------------------------------------------------------------------------------------------
    </p>

    <input
      type="radio"
      name="test_id"
      @change="onChange($event)"
      :value="colour_name"
    />
    <label></label>
    <p>Цвет: {{ colour_name }}</p>
    <img
      :src="
        'https://www.proplan.ru/sites/owners.proplan.ru/files/2020-11/neperenosimost-komponentov.' +
        'jpg'
      "
      alt=""
    />
    <!-- <p v-html="scheme_description"></p> -->
    <!-- <br /> -->
    <p>в сторе: {{ GETBODYCOLOR }}</p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TheBodyColour",
  props: {
    colour: {
      type: String,
      default() {
        return "ывааыв";
      },
    },
    colour_name: {
      type: String,
      default() {
        return "ывааыв";
      },
    },
  },
  computed: {
    ...mapGetters("closet_configurator", ["GETBODYCOLOR"]),
  },
  methods: {
    ...mapActions("closet_configurator", ["chooseBodyColor"]),
    onChange(event) {
      this.chooseBodyColor(event.target.value);
    },
  },
};
</script>

<style></style>
