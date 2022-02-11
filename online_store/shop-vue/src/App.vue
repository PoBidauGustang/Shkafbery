<template>
  <div id="app">
    <TheHeader />
    <router-view/>
  </div>
</template>

<script>
  import TheHeader from './components/TheHeader.vue';
  export default {
    components: {TheHeader}
  }
</script>

<style>
  @import "assets/css/reset.css";
  @import "assets/css/index.css";
</style>
