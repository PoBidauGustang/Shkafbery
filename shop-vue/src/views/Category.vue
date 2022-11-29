<template>
  <div>
    <h1>ТЕКУЩАЯ КАТЕГОРИЯ - {{ $route.params.slug }}</h1>
    <!-- <div>{{ wardrobes }}</div> -->
    <div v-for="categ in GETMAINCATEGORIES" :key="categ.id">
      {{ categ }}
    </div>
    <div class="Product_Page">
      <TheProductView
        v-for="product in wardrobes"
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
import TheProductView from "../components/TheProductView.vue";
export default {
  name: "WardrobePage",
  components: {
    TheProductView,
  },
  data() {
    return {
      wardrobes: [],
      b: 111,
    };
  },
  created() {
    this.loadWardrobes();
    // this.loadCart();
  },
  computed: {
    ...mapGetters("cart", ["GETALLITEMS"]),
    ...mapGetters("api_urls", ["getServerShopUrl"]),
    ...mapGetters("data", ["GETCHILDCATEGORIES", "GETMAINCATEGORIES"]),
  },
  methods: {
    ...mapActions("cart", ["saveItem", "loadCart"]),
    // ...mapActions("test", ["increment"]),
    // ...mapActions("cart", ["saveItems"]),
    // addToCart(product) {
    //   console.log(product);
    //   this.saveItems(product);
    addToCart(b) {
      // console.log(b);
      this.saveItem(b);
    },
    loadWardrobes() {
      this.axios
        .get(`${this.getServerShopUrl}/products/16`)
        .then((response) => {
          this.wardrobes = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
  },
};
</script>

<style></style>
