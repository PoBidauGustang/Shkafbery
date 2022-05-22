<template>
  <div class="about">
    <p>{{ this.$store.state.closet_configurator.count }}</p>
    <button @click="this.$store.dispatch('closet_configurator/increment')">
      {{ count }}
    </button>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  name: "about",
  components: {},
  computed: {
    ...mapState("closet_configurator", ["count"]),
  },
  methods: {
    ...mapActions("closet_configurator", ["increment"]),
  },
};
</script>
