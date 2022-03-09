<template>
  <div>
    <p>first step</p>
    <!-- <div>
      <input type="radio" name="test_id" @change="onChange($event)" value="1" />
      <label for="1">1-ый шкаф</label>
      <br />
      <input type="radio" name="test_id" @change="onChange($event)" value="2" />
      <label for="1">2-ый шкаф</label>
      <br />
      <input type="radio" name="test_id" @change="onChange($event)" value="3" />
      <label for="1">3-ый шкаф</label>
      <br />
      <input type="radio" name="test_id" @change="onChange($event)" value="4" />
      <label for="1">4-ый шкаф</label>
      <br />
      <span
        >Выбрано:
        {{ this.$store.state.closet_configurator.config.doorsAmount }}</span
      >
    </div> -->
    <div>
      <TheDoor
        v-for="doorsNumber in doorsNumberList.data"
        :key="doorsNumber.id"
        :doors_data="doorsNumber.attributes.type"
      />
    </div>
    <!-- <p>{{doorsNumberList}}</p> -->
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
    ...mapGetters({ getServerClosetUrl: "getServerClosetUrl" }),
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
