<template>
  <div>
    <router-link :to="'/product/' + product.id">
      <p>{{ product.attributes.title }}</p>
      <li v-for="line in product.attributes" :key="line">
        {{ line }}
      </li>
    </router-link>
    <!-- <div v-if="category.child_free === true">
      <router-link
        class="bottom_menu_link"
        :to="'/category/' + category.attributes.slug"
        >{{ category.attributes.name }}
      </router-link>
    </div> -->
  </div>
</template>

<script>
// import { mapActions, mapGetters } from "vuex";
export default {
  name: "ProductView",
  components: {},
  data() {
    return {};
  },
  props: {
    product: {
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
