<template>
  <div>
    <h1>Выберите систему дверей</h1>
    <!-- <p>все размеры: {{ GETDIMENSIONSDATA }}</p>
    <p>выбранные размеры: {{ GETDIMENSIONS }}</p>
    <p>подходящие схемы наполнения: {{ GETSUITABLEFILLINGSCHEMES }}</p>
    <p>подходящие по заданным размерам схемы: {{ filteredSchemesByDimensions }}</p>
    <p>данные подходящих по заданным размерам схем: {{ filteredSchemesData }}</p> -->
    <p>{{ doorsSystemList }}</p>
    <p>{{ filteredDoorsSystemList }}</p>
    <div>
      <TheDoorsSystem
        v-for="system in filteredDoorsSystemList"
        :key="system.id"
        :system_name="system.attributes.name"
        :system_description="system.attributes.image"
      />
      <div v-show="visible">
        <p>{{ doorsSystemList }}</p>
      </div>
      <!-- <p>в сторе: {{ GETFILLINGSCHEME }}</p> -->
      <!-- <p>{{ filteredBodyColourList }}</p> -->
    </div>
  </div>
</template>

<script>
import TheDoorsSystem from "./TheDoorsSystem.vue";
import { mapGetters } from "vuex";
export default {
  name: "fifth_step",
  components: {
    TheDoorsSystem,
  },
  data() {
    return {
      doorsSystemList: [],
      filteredDoorsSystemList: [],
      visible: false,
    };
  },
  created() {
    this.loadDoorsSystemList();
  },
  beforeUpdate() {
    this.filterDoorsSystemByScheme();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerClosetUrl"]),
    ...mapGetters("closet_configurator", ["GETFILLINGSCHEME"]),
  },
  methods: {
    loadDoorsSystemList() {
      this.axios
        .get(`${this.getServerClosetUrl}/step_fifth`)
        .then((response) => {
          this.doorsSystemList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    filterDoorsSystemByScheme() {
      for (let system in this.doorsSystemList) {
        for (let scheme in this.doorsSystemList[Number(system)].attributes
          .filling_scheme) {
          if (
            this.doorsSystemList[Number(system)].attributes.filling_scheme[
              Number(scheme)
            ].name === this.GETFILLINGSCHEME
          ) {
            this.filteredDoorsSystemList.push(
              this.doorsSystemList[Number(system)]
            );
          }
        }
      }
      this.filteredDoorsSystemList.sort(function (a, b) {
        if (a.attributes.position > b.attributes.position) {
          return 1;
        }
        if (a.attributes.position < b.attributes.position) {
          return -1;
        }
        return 0;
      });
      let numOfNull = 0;
      for (let i in this.filteredDoorsSystemList) {
        if (this.filteredDoorsSystemList[i].attributes.position === null) {
          numOfNull += 1;
        }
      }
      let tempDoorsList = this.filteredDoorsSystemList.slice();
      let temp1DoorsList = tempDoorsList.slice(numOfNull);
      let c = tempDoorsList.slice(0, numOfNull);
      for (let i in c) {
        temp1DoorsList.push(c[i]);
      }
      this.filteredDoorsSystemList = temp1DoorsList;
    },
  },
};
</script>

<style></style>
