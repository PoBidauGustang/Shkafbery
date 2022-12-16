<template>
  <div id="app">
    <header>
      <TheHeader />
    </header>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
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

<style></style>
