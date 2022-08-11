<template>
  <div>
    <h1>Кухни</h1>
    <div>{{ TEST }}</div>
    <button @click="increment">Добавить в тест</button>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Kitchen",
  components: {
  },
  computed: {
    ...mapGetters("test", ["TEST"]),
  },
  methods: {
    ...mapActions("test", [
      "increment",
    ]),
  },
};
</script>