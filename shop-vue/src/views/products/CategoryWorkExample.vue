<template>
  <div>
    <h2>примеры работ</h2>
    <h4>id категории: {{ category.id }}</h4>
    <h4>здесь будут примеры работ</h4>
  </div>
</template>

<script>
// import { mapActions, mapGetters } from "vuex";
export default {
  name: "CategoryWorkExample",
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
