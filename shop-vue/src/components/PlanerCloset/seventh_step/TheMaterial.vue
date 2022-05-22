<template>
  <div>
    <p>
      ----------------------------------------------------------------------------------------------
    </p>
    <input
      type="radio"
      name="section_num"
      @change="onChange($event)"
      :value="result"
    />
    <label></label>
    <p>Материал: {{ material_name }}</p>
    <p>в сторе: {{ GETDOORMATERIALS }}</p>
    <p></p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TheMaterial",
  data() {
    return {
      result: "",
    };
  },
  props: {
    material_name: {
      type: String,
      default() {
        return "";
      },
    },
    section_num: {
      type: Number,
      default() {
        return 0;
      },
    },
    doors_num: {
      type: Number,
      default() {
        return 0;
      },
    },
  },
  created() {
    this.makeMaterials();
  },
  computed: {
    ...mapGetters("closet_configurator", [
      "GETDOORMATERIALS",
      "GETDOORSSYSTEM",
    ]),
  },
  methods: {
    ...mapActions("closet_configurator", ["chooseDoorMaterials"]),
    onChange(event) {
      this.chooseDoorMaterials(event.target.value);
    },
    makeMaterials() {
      this.result =
        this.doors_num + "," + this.section_num + "," + this.material_name;
    },
  },
};
</script>

<style></style>
