<template>
  <div>
    <h4 v-html="category.attributes.description"></h4>
  </div>
</template>

<script>
// import { mapActions, mapGetters } from "vuex";
export default {
  name: "CategoryInfo",
  components: {},
  data() {
    return {};
  },
  props: {
    category: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  methods: {},
};
</script>

<style></style>
