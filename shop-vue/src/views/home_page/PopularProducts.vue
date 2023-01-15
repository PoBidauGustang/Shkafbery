<template>
  <section class="main_base_section">
    <div class="main_product_title">
      <h2 class="main_small_title">Популярные товары</h2>
    </div>
    <ul class="main_product_list">
      <li
        class="main_product_list_item"
        v-for="product in popularProducts"
        :key="product.id"
      >
        <ProductView :product="product" />
      </li>
    </ul>
  </section>
</template>

<script>
import ProductView from "../products/ProductView.vue";
export default {
  name: "PopularProducts",
  components: {
    ProductView,
  },
  props: {
    popularProducts: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  data() {
    return {};
  },
  computed: {},
  methods: {},
};
</script>

<style>
.Product_Listing_Wrapper {
  grid-column: 4 / span 9;
  grid-row: 2;
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  list-style: none;
  grid-auto-rows: max-content;
}

.Product_Listing_Item {
  grid-column: span 3;
  border-right: 1px solid;
  border-bottom: 1px solid;
}
</style>
