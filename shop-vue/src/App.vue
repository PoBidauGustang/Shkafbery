<template>
  <div id="app">
    <header>
      <TheHeader />
    </header>
    <main>
      <router-view />
    </main>
    <footer>
      <TheFooter />
    </footer>
  </div>
</template>

<script>
import TheHeader from "./components/TheHeader/TheHeader.vue";
import TheFooter from "./components/TheFooter.vue";
export default {
  components: {
    TheHeader,
    TheFooter,
  },
  data() {
    return {};
  },
  methods: {},
};
</script>

<style></style>
