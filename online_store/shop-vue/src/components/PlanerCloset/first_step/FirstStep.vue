<template>
  <div>
    <p>first step</p>
    <div>
      <TheDoor
        v-for="doorsNumber in doorsNumberList.data"
        :key="doorsNumber.id"
        :doors_data="doorsNumber.attributes.type"
      />
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import TheDoor from "./TheDoor.vue";
export default {
  name: "first_step",
  components: {
    TheDoor,
  },
  data() {
    return {
      doorsNumberList: [],
    };
  },
  created() {
    this.loadDoorsNumberList();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerClosetUrl"]),
  },
  methods: {
    ...mapActions("closet_configurator", ["chooseDoorsAmount"]),
    onChange(event) {
      this.chooseDoorsAmount(event.target.value);
    },
    async loadDoorsNumberList() {
      this.doorsNumberList = await fetch(
        `${this.getServerClosetUrl}/step_one`
      ).then((response) => response.json());
    },
  },
};
</script>

<style></style>
