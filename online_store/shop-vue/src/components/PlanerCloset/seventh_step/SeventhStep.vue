<template>
  <div>
    <h1>Конфигурация дверного полотна</h1>
    <p>{{ GETDOORSAMOUNT }}{{ doorsList }}</p>
    <p>выбранная система дверей: {{ GETDOORSSYSTEM }}</p>
    <p>материалы по системе дверей : {{ filteredMaterialList }}</p>
    <p>{{ delimitersList }}</p>
    <div>
      <div>
        <TheDoor
          v-for="door in doorsList"
          :key="door"
          :doors_num="door"
          :doors_materials="this.filteredMaterialList"
          :delimiters="this.delimitersList"
        />
      </div>
    </div>
  </div>
</template>

<script>
import TheDoor from "./TheDoor.vue";
import { mapGetters } from "vuex";
export default {
  name: "seventh_step",
  components: {
    TheDoor,
  },
  data() {
    return {
      materialList: [],
      filteredMaterialList: [],
      delimitersList: [
        { text: "Один", value: 1 },
        { text: "Два", value: 2 },
        { text: "Три", value: 3 },
        { text: "Четыре", value: 4 },
        { text: "Пять", value: 5 },
        { text: "Шесть", value: 6 },
        { text: "Семь", value: 7 },
        { text: "Восемь", value: 8 },
        { text: "Девять", value: 9 },
      ],
      doorsList: [],
    };
  },
  watch: {
    materialList() {
      this.filterMaterials();
    },
  },
  created() {
    this.loadMaterialList();
    this.makeDoorsList();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerClosetUrl"]),
    ...mapGetters("closet_configurator", ["GETDOORSSYSTEM", "GETDOORSAMOUNT"]),
  },
  methods: {
    loadMaterialList() {
      this.axios
        .get(`${this.getServerClosetUrl}/step_seventh`)
        .then((response) => {
          this.materialList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    filterMaterials() {
      for (let profile in this.materialList) {
        for (let system in this.materialList[Number(profile)].attributes
          .doors_system) {
          if (
            this.materialList[Number(profile)].attributes.doors_system[
              Number(system)
            ].name === this.GETDOORSSYSTEM
          ) {
            this.filteredMaterialList.push(this.materialList[Number(profile)]);
          }
        }
      }
    },
    makeDoorsList() {
      if (this.GETDOORSAMOUNT === "Две") {
        this.doorsList = [1, 2];
      }
      if (this.GETDOORSAMOUNT === "Три") {
        this.doorsList = [1, 2, 3];
      }
      if (this.GETDOORSAMOUNT === "Четыре") {
        this.doorsList = [1, 2, 3, 4];
      }
      if (this.GETDOORSAMOUNT === "Пять") {
        this.doorsList = [1, 2, 3, 4, 5];
      }
    },
  },
};
</script>

<style></style>
