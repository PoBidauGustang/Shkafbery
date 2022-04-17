<template>
  <div>
    <h1>Выберите схему наполнения</h1>
    <p>все размеры: {{ GETDIMENSIONSDATA }}</p>
    <p>выбранные размеры: {{ GETDIMENSIONS }}</p>
    <p>подходящие схемы наполнения: {{ GETSUITABLEFILLINGSCHEMES }}</p>
    <p>подходящие по заанным размерам схемы: {{ filterSchemesByDimensions }}</p>
    <p>{{ GETDIMENSIONS.width.value }}</p>
    <p>Why?{{ GETDIMENSIONSDATA[0].attributes.min_width }}</p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "third_step",
  // data() {
  //   return {
  //     filteredSchemesByDimensions: [],
  //   };
  // },
  computed: {
    ...mapGetters("closet_configurator", [
      "GETDIMENSIONSDATA",
      "GETDIMENSIONS",
      "GETSUITABLEFILLINGSCHEMES",
    ]),
    filterSchemesByDimensions() {
      let filteredSchemesByDimensions = [];
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
              filteredSchemesByDimensions.push(
                this.GETDIMENSIONSDATA[scheme].attributes.filling_scheme
              );
            }
          }
        }
      }
      return filteredSchemesByDimensions;
    },
  },
  methods: {
    ...mapActions("closet_configurator", ["chooseDimensionsWidth"]),
    // filterSchemesByDimensions() {
    //   this.filteredSchemesByDimensions = 1
    //   for (let scheme in this.GETDIMENSIONSDATA) {
    //     if (
    //       this.GETDIMENSIONSDATA[scheme].attributes.type.type ==
    //       this.GETDOORSAMOUNT
    //     ) {
    //       this.filteredFillingSchemesListID.push(
    //         this.fillingSchemesList.data[scheme].id
    //       );
    //       this.filteredFillingSchemesList.push(
    //         this.fillingSchemesList.data[scheme]
    //       );
    //     }
    //   }
    //   this.saveSuitableFillingSchemes(this.filteredFillingSchemesList)
    // },
  },
};
</script>

<style></style>
