<template>
  <div>
    <h1>Выберите цвет корпуса</h1>
    <!-- <p>все размеры: {{ GETDIMENSIONSDATA }}</p>
    <p>выбранные размеры: {{ GETDIMENSIONS }}</p>
    <p>подходящие схемы наполнения: {{ GETSUITABLEFILLINGSCHEMES }}</p>
    <p>подходящие по заданным размерам схемы: {{ filteredSchemesByDimensions }}</p>
    <p>данные подходящих по заданным размерам схем: {{ filteredSchemesData }}</p> -->
    <div>
      <TheBodyColour
        v-for="colour in filteredBodyColourList"
        :key="colour.id"
        :colour_name="colour.attributes.name"
        :colour="colour.attributes.image"
      />
      <div v-show="visible">
        <p>{{ bodyColourList }}</p>
      </div>
      <!-- <p>в сторе: {{ GETFILLINGSCHEME }}</p> -->
      <!-- <p>{{ filteredBodyColourList }}</p> -->
    </div>
  </div>
</template>

<script>
import TheBodyColour from "./TheBodyColour.vue";
import { mapGetters } from "vuex";
export default {
  name: "fourth_step",
  components: {
    TheBodyColour,
  },
  data() {
    return {
      bodyColourList: [],
      filteredBodyColourList: [],
      visible: false,
    };
  },
  created() {
    this.loadBodyColoursList();
  },
  beforeUpdate() {
    this.filterColoursByScheme();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerClosetUrl"]),
    ...mapGetters("closet_configurator", ["GETFILLINGSCHEME"]),
  },
  methods: {
    loadBodyColoursList() {
      this.axios
        .get(`${this.getServerClosetUrl}/step_fourth`)
        .then((response) => {
          this.bodyColourList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    filterColoursByScheme() {
      for (let colour in this.bodyColourList) {
        for (let scheme in this.bodyColourList[Number(colour)].attributes
          .filling_scheme) {
          if (
            this.bodyColourList[Number(colour)].attributes.filling_scheme[
              Number(scheme)
            ].name === this.GETFILLINGSCHEME
          ) {
            this.filteredBodyColourList.push(
              this.bodyColourList[Number(colour)]
            );
          }
        }
      }
      // var uniqueArray = this.filteredBodyColourList.filter((val, ind, arr) => arr.indexOf(val) === ind)
      // this.filteredBodyColourList = uniqueArray
    },
  },
};
</script>

<style></style>
