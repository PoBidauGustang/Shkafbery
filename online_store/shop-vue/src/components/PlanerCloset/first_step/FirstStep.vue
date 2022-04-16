<template>
  <div>
    <p>Выберите количество дверей</p>
    <div>
      <TheDoor
        v-for="doorsNumber in doorsNumberListJson.data"
        :key="doorsNumber.id"
        :doors_data="doorsNumber.attributes.type"
        :doors_description="doorsNumber.attributes.description"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import TheDoor from "./TheDoor.vue";
export default {
  name: "first_step",
  components: {
    TheDoor,
  },
  data() {
    return {
      doorsNumberListJson: [],
    };
  },
  created() {
    this.loadDoorsNumberList();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerClosetUrl"]),
  },
  methods: {
    async loadDoorsNumberList() {
      this.doorsNumberListJson = await fetch(
        `${this.getServerClosetUrl}/step_one`
      ).then((response) => response.json());
    },
  },
};
</script>

<style></style>
