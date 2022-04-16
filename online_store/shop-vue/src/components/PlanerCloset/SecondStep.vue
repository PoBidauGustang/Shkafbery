<template>
  <div>
    <p>Укажите размеры</p>
    <!-- <p>выбрнный тип шкафа: {{ GETDOORSAMOUNT }} двери</p> -->
    <!-- <p>{{ fillingSchemesList.data }}</p> -->
    <!-- <p>подходящие схемы наполнения: {{ filteredFillingSchemesList }}</p>
    <p>все размеры: {{ doorsDimensionsData }}</p>
    <p>сортированный список текущих размеров: {{ currentDimensions }}</p>
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
    <p>выбранные размеры: {{ GETDOORSDIMENSIONS }}</p>
    <div v-show="visible">
      <p>{{ doorsDimensionsData }}</p>
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
      filteredFillingSchemesList: [],
      doorsDimensionsData: {},
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
    this.filterPosts();
    this.loadDoorsDimensionsData();
    this.getSchemesParams();
  },
  beforeUpdate() {
    // this.getWidth(this.doorsDimensionsData);
    this.getWidth();
    this.getHeight();
    this.getDepth();
  },
  computed: {
    ...mapGetters("closet_configurator", [
      "GETDOORSAMOUNT",
      "GETDOORSDIMENSIONS",
    ]),
    ...mapGetters("api_urls", ["getServerClosetUrl"]),
  },
  methods: {
    ...mapActions("closet_configurator", [
      "chooseDoorsDimensionsWidth",
      "chooseDoorsDimensionsHeight",
      "chooseDoorsDimensionsDepth",
    ]),
    getSchemesParams() {
      var schemes = new URLSearchParams();
      for (let i in this.filteredFillingSchemesList) {
        schemes.append("scheme", this.filteredFillingSchemesList[i]);
      }
      var request = {
        params: schemes,
      };
      return request;
    },
    filterPosts() {
      for (let scheme in this.fillingSchemesList.data) {
        if (
          this.fillingSchemesList.data[scheme].attributes.type.type ==
          this.GETDOORSAMOUNT
        ) {
          this.filteredFillingSchemesList.push(
            this.fillingSchemesList.data[scheme].id
          );
        }
      }
    },
    loadDoorsDimensionsData() {
      this.axios
        .get(`${this.getServerClosetUrl}/step_two`, this.getSchemesParams())
        .then((response) => {
          this.doorsDimensionsData = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    // getWidth(doorsDimensionsData) {
    getWidth() {
      this.currentDimensions = [];
      for (let dimension in this.doorsDimensionsData) {
        this.currentDimensions.push(
          this.doorsDimensionsData[dimension].attributes.min_width
        );
        this.currentDimensions.push(
          this.doorsDimensionsData[dimension].attributes.max_width
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
      for (let dimension in this.doorsDimensionsData) {
        this.currentDimensions.push(
          this.doorsDimensionsData[dimension].attributes.min_height
        );
        this.currentDimensions.push(
          this.doorsDimensionsData[dimension].attributes.max_height
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
      for (let dimension in this.doorsDimensionsData) {
        this.currentDimensions.push(
          this.doorsDimensionsData[dimension].attributes.min_depth
        );
        this.currentDimensions.push(
          this.doorsDimensionsData[dimension].attributes.max_depth
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
      for (let num in this.doorsDimensionsData) {
        if (
          this.doorsDimensionsData[num].attributes.min_width < widthValue &&
          this.doorsDimensionsData[num].attributes.max_width > widthValue
        ) {
          // console.log(a[num].attributes.min_width);
          result.push(this.doorsDimensionsData[num]);
        }
      }
      this.doorsDimensionsData = result;
      // return result
    },
    onChangeWidth(event) {
      this.chooseDoorsDimensionsWidth(event.target.value);
    },
    onChangeHeight(event) {
      this.chooseDoorsDimensionsHeight(event.target.value);
    },
    onChangeDepth(event) {
      this.chooseDoorsDimensionsDepth(event.target.value);
    },
  },
};
</script>

<style></style>
