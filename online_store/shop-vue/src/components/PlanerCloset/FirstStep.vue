<template>
  <div>
    <p>first step</p>
    <div>
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
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "first_step",
  methods: {
    ...mapActions("closet_configurator", ["chooseDoorsAmount"]),
    onChange(event) {
      this.chooseDoorsAmount(event.target.value);
    },
  },
};
</script>

<style></style>
