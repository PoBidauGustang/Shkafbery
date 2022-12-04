<template>
  <div>
    <h3>Товары:</h3>
    <div>
      Фильтры:
      <input type="number" v-model="minInputPrice" placeholder="0" />
      <input type="number" v-model="maxInputPrice" placeholder="0" />
    </div>
    <ul>
      <li v-for="product in filteredProducts" :key="product.id">
        <ProductView :product="product" />
      </li>
    </ul>
    <!-- <div class="Product_Page">
      <TheProductView
        v-for="product in products"
        :key="product.id"
        :product_title="product.attributes.title"
        :product_regular_price="product.attributes.regular_price"
        :product_data="product"
        @addToCart="addToCart"
      />
    </div> -->
    <!-- <div>{{ GETALLITEMS }}</div> -->
    <!-- <button @click="increment">Добавить в корзину</button> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import ProductView from "./ProductView.vue";
export default {
  name: "Products",
  components: {
    ProductView,
  },
  data() {
    return {
      minInputPrice: null,
      maxInputPrice: null,
      minInputWidth: null,
      maxInputWidth: null,
    };
  },
  props: {
    productsList: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  created() {
    // this.loadProducts();
  },
  computed: {
    ...mapGetters("cart", ["GETALLITEMS"]),
    ...mapGetters("api_urls", ["getServerShopUrl"]),
    filteredProducts() {
      let tempProducts = this.productsList;

      if (this.minInputPrice) {
        console.log(1);
        tempProducts = tempProducts.filter((item) => {
          return item.attributes.regular_price >= this.minInputPrice;
        });
      }

      return tempProducts;
    },
  },
  methods: {
    ...mapActions("cart", ["saveItem", "loadCart"]),
    addToCart(b) {
      this.saveItem(b);
    },
    // onChangeWidth(event) {
    //   this.chooseDimensionsWidth(event.target.value);
    // },
    // loadProducts() {
    //   this.axios
    //     .get(`${this.getServerShopUrl}/products`)
    //     .then((response) => {
    //       this.products = response.data.data;
    //     })
    //     .catch(function (error) {
    //       console.error(error);
    //     });
    // },
  },
};
</script>

<style></style>
