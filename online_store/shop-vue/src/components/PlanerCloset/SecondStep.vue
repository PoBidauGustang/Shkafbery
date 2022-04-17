<template>
  <div>
    <p>Укажите размеры</p>
    <p>выбрнный тип шкафа: {{ GETDOORSAMOUNT }} двери</p>
    <p>{{ fillingSchemesList.data }}</p>
    <p>ID подходящих схем наполнения: {{ filteredFillingSchemesListID }}</p>
    <p>подходящие схемы наполнения: {{ filteredFillingSchemesList }}</p>
    <p>все размеры: {{ dimensionsData }}</p>
    <!-- <p>сортированный список текущих размеров: {{ currentDimensions }}</p>
    <p>
      минимальная ширина, максимальная ширина: {{ minWidth }} - {{ maxWidth }}
    </p>
    <p>
      минимальная высота, максимальная высота: {{ minHeight }} - {{ maxHeight }}
    </p>
    <p>
      минимальная глубина, максимальная глубина: {{ minDepth }} - {{ maxDepth }}
    </p> -->
    <!-- <label for="new-todo">Add width</label> -->
    <div>
      ширина: {{ minWidth }}
      <input
        v-model="widthValue"
        id="new-todo"
        placeholder="0"
        @change="onChangeWidth($event)"
      />
      {{ maxWidth }}
    </div>
    <!-- <button @click="filteredWidth(widthValue)">Обновить</button> -->
    <div>
      высота: {{ minHeight }}
      <input
        v-model="heightValue"
        id="new-todo"
        placeholder="0"
        @change="onChangeHeight($event)"
      />
      {{ maxHeight }}
    </div>
    <div>
      глубина: {{ minDepth }}
      <input
        v-model="deepthValue"
        id="new-todo"
        placeholder="0"
        @change="onChangeDepth($event)"
      />
      {{ maxDepth }}
    </div>
    <p>выбранные размеры: {{ GETDIMENSIONS }}</p>
    <div v-show="visible">
      <p>{{ dimensionsData }}</p>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "second_step",
  components: {},
  data() {
    return {
      filteredFillingSchemesListID: [],
      filteredFillingSchemesList: [],
      dimensionsData: {},
      currentDimensions: [],
      widthValue: "",
      heightValue: "",
      deepthValue: "",
      minWidth: "",
      maxWidth: "",
      minHeight: "",
      maxHeight: "",
      minDepth: "",
      maxDepth: "",
    };
  },
  // watch: {
  //   widthValue() {
  //     this.minWidth = this.widthValue
  //     this.filteredWidth(this.widthValue)
  //     this.getWidth(this.filteredWidth(this.widthValue));
  //     this.getWidth();
  //     this.getHeight();
  //     this.getDepth();
  //   },
  // },
  props: {
    fillingSchemesList: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  created() {
    this.filterSchemes();
    this.loadDimensionsData();
    this.getSchemesParams();
  },
  beforeUpdate() {
    // this.getWidth(this.dimensionsData);
    this.getWidth();
    this.getHeight();
    this.getDepth();
  },
  computed: {
    ...mapGetters("closet_configurator", ["GETDOORSAMOUNT", "GETDIMENSIONS"]),
    ...mapGetters("api_urls", ["getServerClosetUrl"]),
  },
  methods: {
    ...mapActions("closet_configurator", [
      "chooseDimensionsWidth",
      "chooseDimensionsHeight",
      "chooseDimensionsDepth",
      "saveDimensionsData",
      "saveSuitableFillingSchemes",
    ]),
    getSchemesParams() {
      var schemes = new URLSearchParams();
      for (let i in this.filteredFillingSchemesListID) {
        schemes.append("scheme", this.filteredFillingSchemesListID[i]);
      }
      var request = {
        params: schemes,
      };
      return request;
    },
    filterSchemes() {
      for (let scheme in this.fillingSchemesList.data) {
        if (
          this.fillingSchemesList.data[scheme].attributes.type.type ==
          this.GETDOORSAMOUNT
        ) {
          this.filteredFillingSchemesListID.push(
            this.fillingSchemesList.data[scheme].id
          );
          this.filteredFillingSchemesList.push(
            this.fillingSchemesList.data[scheme]
          );
        }
      }
      this.saveSuitableFillingSchemes(this.filteredFillingSchemesList);
    },
    loadDimensionsData() {
      this.axios
        .get(`${this.getServerClosetUrl}/step_two`, this.getSchemesParams())
        .then((response) => {
          this.dimensionsData = response.data.data;
          this.saveDimensionsData(this.dimensionsData);
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    // getWidth(dimensionsData) {
    getWidth() {
      this.currentDimensions = [];
      for (let dimension in this.dimensionsData) {
        this.currentDimensions.push(
          this.dimensionsData[dimension].attributes.min_width
        );
        this.currentDimensions.push(
          this.dimensionsData[dimension].attributes.max_width
        );
      }
      this.currentDimensions.sort(function (a, b) {
        return a - b;
      });
      this.minWidth = this.currentDimensions[0];
      this.maxWidth = this.currentDimensions[this.currentDimensions.length - 1];
    },
    getHeight() {
      this.currentDimensions = [];
      for (let dimension in this.dimensionsData) {
        this.currentDimensions.push(
          this.dimensionsData[dimension].attributes.min_height
        );
        this.currentDimensions.push(
          this.dimensionsData[dimension].attributes.max_height
        );
      }
      this.currentDimensions.sort(function (a, b) {
        return a - b;
      });
      this.minHeight = this.currentDimensions[0];
      this.maxHeight =
        this.currentDimensions[this.currentDimensions.length - 1];
    },
    getDepth() {
      this.currentDimensions = [];
      for (let dimension in this.dimensionsData) {
        this.currentDimensions.push(
          this.dimensionsData[dimension].attributes.min_depth
        );
        this.currentDimensions.push(
          this.dimensionsData[dimension].attributes.max_depth
        );
      }
      this.currentDimensions.sort(function (a, b) {
        return a - b;
      });
      this.minDepth = this.currentDimensions[0];
      this.maxDepth = this.currentDimensions[this.currentDimensions.length - 1];
    },
    filteredWidth(widthValue) {
      let result = [];
      for (let num in this.dimensionsData) {
        if (
          this.dimensionsData[num].attributes.min_width < widthValue &&
          this.dimensionsData[num].attributes.max_width > widthValue
        ) {
          // console.log(a[num].attributes.min_width);
          result.push(this.dimensionsData[num]);
        }
      }
      this.dimensionsData = result;
      // return result
    },
    onChangeWidth(event) {
      this.chooseDimensionsWidth(event.target.value);
    },
    onChangeHeight(event) {
      this.chooseDimensionsHeight(event.target.value);
    },
    onChangeDepth(event) {
      this.chooseDimensionsDepth(event.target.value);
    },
  },
};
</script>

<style></style>
