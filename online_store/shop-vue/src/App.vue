<template>
  <div id="app">
    <the-header />
    <router-view/>
  </div>
</template>

<script>
  import TheHeader from './components/TheHeader.vue';
  export default {
    components: {
      TheHeader,
    },
    data() {
      return {}
    },
    methods: {}
  }
</script>

<style>
  @import "assets/css/reset.css";
  @import "assets/css/index.css";
</style>
