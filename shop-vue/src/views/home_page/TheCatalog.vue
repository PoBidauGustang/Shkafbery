<template>
  <div>
    <div
    v-for="category in GETMAINCATEGORIES"
    :key="category.id"
    >
      <router-link :to="'/category/' + category.attributes.slug">
        <ul>
          <li>{{ category.attributes.name }}</li>
          <li>
            <img
              class=""
              :src="category.attributes.image"
            />
          </li>
        </ul>
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "TheFAQ",
  props: {
    news: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
    };
  },
  computed: {
    ...mapGetters("data", ["GETMAINCATEGORIES"]),
  },
  methods: {},
};
</script>

<style></style>
