<template>
  <div>
    <h1>Выберите схему наполнения</h1>
    <!-- <p>все размеры: {{ GETDIMENSIONSDATA }}</p>
    <p>выбранные размеры: {{ GETDIMENSIONS }}</p>
    <p>подходящие схемы наполнения: {{ GETSUITABLEFILLINGSCHEMES }}</p>
    <p>подходящие по заданным размерам схемы: {{ filteredSchemesByDimensions }}</p>
    <p>данные подходящих по заданным размерам схем: {{ filteredSchemesData }}</p> -->
    <div>
      <TheFillingScheme
        v-for="scheme in filteredSchemesData"
        :key="scheme.id"
        :scheme_name="scheme.attributes.name"
      />
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import TheFillingScheme from "./TheFillingScheme.vue";
export default {
  name: "third_step",
  components: {
    TheFillingScheme,
  },
  data() {
    return {
      filteredSchemesByDimensions: [],
      filteredSchemesData: [],
    };
  },
  created() {
    this.filterSchemesByDimensions();
  },
  beforeupdate() {
    this.filterSchemesData();
  },
  computed: {
    ...mapGetters("closet_configurator", [
      "GETDIMENSIONSDATA",
      "GETDIMENSIONS",
      "GETSUITABLEFILLINGSCHEMES",
    ]),
  },
  methods: {
    ...mapActions("closet_configurator", ["chooseDimensionsWidth"]),
    filterSchemesData() {
      for (let i in this.filteredSchemesByDimensions) {
        for (let scheme in this.GETSUITABLEFILLINGSCHEMES) {
          if (
            Number(this.GETSUITABLEFILLINGSCHEMES[scheme].id) ===
            this.filteredSchemesByDimensions[i]
          )
            this.filteredSchemesData.push(
              this.GETSUITABLEFILLINGSCHEMES[scheme]
            );
        }
      }
    },
    filterSchemesByDimensions() {
      this.filteredSchemesByDimensions = [];
      for (let scheme in this.GETDIMENSIONSDATA) {
        if (
          this.GETDIMENSIONSDATA[scheme].attributes.min_width <=
            this.GETDIMENSIONS.width.value &&
          this.GETDIMENSIONSDATA[scheme].attributes.max_width >=
            this.GETDIMENSIONS.width.value
        ) {
          if (
            this.GETDIMENSIONSDATA[scheme].attributes.min_height <=
              this.GETDIMENSIONS.height.value &&
            this.GETDIMENSIONSDATA[scheme].attributes.max_height >=
              this.GETDIMENSIONS.height.value
          ) {
            if (
              this.GETDIMENSIONSDATA[scheme].attributes.min_depth <=
                this.GETDIMENSIONS.depth.value &&
              this.GETDIMENSIONSDATA[scheme].attributes.max_depth >=
                this.GETDIMENSIONS.depth.value
            ) {
              this.filteredSchemesByDimensions.push(
                this.GETDIMENSIONSDATA[scheme].attributes.filling_scheme.id
              );
            }
          }
        }
      }
      // return filteredSchemesByDimensions;
      this.filterSchemesData();
    },
  },
};
</script>

<style></style>
