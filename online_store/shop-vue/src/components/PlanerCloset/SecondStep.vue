<template>
  <div>
    <p>second step</p>
    <p>выбрнный тип шкафа: {{ GETDOORSAMOUNT }} двери</p>
    <!-- <p>{{ fillingSchemesList.data }}</p> -->
    <p>подходящие схемы наполнения: {{ filteredFillingSchemesList }}</p>
    <p>все размеры: {{ doorsDimensionsData }}</p>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "second_step",
  components: {},
  data() {
    return {
      filteredFillingSchemesList: [],
      doorsDimensionsData: {},
    };
  },
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
  },
  computed: {
    ...mapGetters("closet_configurator", ["GETDOORSAMOUNT"]),
    ...mapGetters("api_urls", ["getServerClosetUrl"]),
  },
  methods: {
    filterPosts() {
      for (let scheme in this.fillingSchemesList.data) {
        if (
          this.fillingSchemesList.data[scheme].attributes.type.type ==
          this.GETDOORSAMOUNT
        ) {
          this.filteredFillingSchemesList +=
            this.fillingSchemesList.data[scheme].attributes.name;
        }
      }
    },
    async loadDoorsDimensionsData() {
      this.doorsDimensionsData = await fetch(
        `${this.getServerClosetUrl}/step_two`
      ).then((response) => response.json());
    },
  },
};
</script>

<style></style>
