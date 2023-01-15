<template>
  <div>
    <!-- <div
    v-for="product in popularProducts"
    :key="product.id"
    >
      <router-link :to="'/product/' + product.id">
        <ul>
          <li>{{ product.attributes.title }}</li>
          <li>
            <img v-if="product.attributes.product_image[0]"
              class=""
              :src="product.attributes.product_image[0].image"
            />
          </li>
        </ul>
      </router-link>
    </div> -->
    <h2>Популярные товары</h2>
    <ul class="Product_Listing_Wrapper">
      <li
        class="Product_Listing_Item"
        v-for="product in popularProducts"
        :key="product.id"
      >
        <ProductView :product="product" />
      </li>
    </ul>
  </div>
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
