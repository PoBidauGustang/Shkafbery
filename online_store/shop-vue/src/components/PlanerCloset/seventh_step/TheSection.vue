<template>
  <div>
    <p>
      ----------------------------------------------------------------------------------------------
    </p>
    <p>Секция № {{ section_num }}</p>
    <div>
      <TheMaterial
        v-for="material in doors_materials"
        :key="material"
        :material_name="material.attributes.name"
        :doors_num="this.doors_num"
        :section_num="this.section_num"
      />
    </div>
  </div>
</template>

<script>
import TheMaterial from "./TheMaterial.vue";
export default {
  name: "TheSection",
  components: {
    TheMaterial,
  },
  data() {
    return {
      f: 3,
    };
  },
  props: {
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
    doors_materials: {
      type: Array,
      default() {
        return [];
      },
    },
  },
};
</script>

<style></style>
