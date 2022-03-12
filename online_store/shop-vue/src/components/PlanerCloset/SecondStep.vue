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
      b: this.getSchemesParams,
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
    this.getSchemesParams();
  },
  computed: {
    ...mapGetters("closet_configurator", ["GETDOORSAMOUNT"]),
    ...mapGetters("api_urls", ["getServerClosetUrl"]),
  },
  methods: {
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
          console.log("we are here", response);
          this.doorsDimensionsData = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
  },
};
</script>

<style></style>
