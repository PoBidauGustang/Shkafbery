<template>
  <div>
    <h1>Товары</h1>
    <div class="Product_Page">
      <TheProductView
        v-for="product in products"
        :key="product.id"
        :product_title="product.attributes.title"
        :product_regular_price="product.attributes.regular_price"
        :product_data="product"
        @addToCart="addToCart"
      />
    </div>
    <div>{{ GETALLITEMS }}</div>
    <!-- <button @click="increment">Добавить в корзину</button> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import TheProductView from "../../components/TheProductView.vue";
export default {
  name: "ProductsPage",
  components: {
    TheProductView,
  },
  data() {
    return {
      products: [],
      b: 111,
    };
  },
  created() {
    this.loadProducts();
  },
  computed: {
    ...mapGetters("cart", ["GETALLITEMS"]),
    ...mapGetters("api_urls", ["getServerShopUrl"]),
  },
  methods: {
    ...mapActions("cart", ["saveItem", "loadCart"]),
    addToCart(b) {
      this.saveItem(b);
    },
    loadProducts() {
      this.axios
        .get(`${this.getServerShopUrl}/products`)
        .then((response) => {
          this.products = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
  },
};
</script>

<style></style>
