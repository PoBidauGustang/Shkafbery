<template>
  <div>
    <h2>какая-то информация</h2>
    <div v-for="product in listProducts.data" :key="product.id">
      {{ product.attributes.name }}
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "HomePage",
  data() {
    return {
      listProducts: [],
    };
  },
  components: {},
  created() {
    this.loadListProducts();
  },
  computed: {
    ...mapGetters({ getServerShopUrl: "getServerShopUrl" }),
  },
  methods: {
    async loadListProducts() {
      this.listProducts = await fetch(
        `${this.getServerShopUrl}/productcategories`
      ).then((response) => response.json());
    },
  },
};
</script>

<style scoped></style>
