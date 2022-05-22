<template>
  <div>
    <p>
      ----------------------------------------------------------------------------------------------
    </p>
    <p>Дверь: {{ doors_num }}</p>
    <select v-model="selectedDelimeters">
      <option
        v-for="delimiter in delimiters"
        :key="delimiter"
        :value="delimiter.value"
      >
        {{ delimiter.text }}
      </option>
    </select>
    <span>Выбрано количество разделителей: {{ selectedDelimeters }}</span>
    <div>Выбраные секции: {{ sections }}</div>
    <div>
      <TheSection
        v-for="section in sections"
        :key="section"
        :doors_num="this.doors_num"
        :section_num="section"
        :doors_materials="this.doors_materials"
      />
    </div>
    <p>в сторе: {{ GETDOORMATERIALS }}</p>
    <!-- <p>!!{{ doors_materials }}</p> -->
  </div>
</template>

<script>
import TheSection from "./TheSection.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TheDoor",
  components: {
    TheSection,
  },
  data() {
    return {
      selectedDelimeters: 1,
      sections: [],
    };
  },
  watch: {
    selectedDelimeters() {
      this.makeSections();
    },
    sections() {
      this.onChange();
    },
  },
  props: {
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
    delimiters: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  computed: {
    ...mapGetters("closet_configurator", [
      "GETDOORMATERIALS",
      "GETDOORSSYSTEM",
    ]),
  },
  methods: {
    ...mapActions("closet_configurator", ["chooseDoorSection"]),
    onChange() {
      let section_num = this.sections.length;
      let result = this.doors_num + "," + section_num;
      this.chooseDoorSection(result);
    },
    makeSections() {
      this.sections = [];
      for (let i = 1; i <= this.selectedDelimeters + 1; i++) {
        this.sections.push(i);
      }
    },
  },
};
</script>

<style></style>
