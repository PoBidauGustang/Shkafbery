<template>
  <div id="app">
    <the-header class="the_header" />
    <router-view />
  </div>
</template>

<script>
// import TheHeader from "./components/TheHeader.vue";
import TheHeader from "./components/TheHeader/TheHeader.vue";
export default {
  components: {
    TheHeader,
  },
  data() {
    return {};
  },
  methods: {},
};
</script>

<style>
@import "assets/css/index.css";
.the_header {
  position: sticky;
  top: 0;
}
</style>
