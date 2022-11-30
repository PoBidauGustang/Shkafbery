<template>
  <div>
    <h1>{{ currentCategory.attributes.name }}</h1>
    <div>
      <CategoryInfo :category="currentCategory" />
    </div>
    <div>
      <CategoryWorkExample :category="currentCategory" />
    </div>
    <div>
      <Products :productsList="productsList" />
    </div>
    <!-- <div>{{ productsList }}</div> -->
    <!-- <div>{{ wardrobes }}</div> -->
    <!-- <div v-for="categ in GETMAINCATEGORIES" :key="categ.id">
      {{ categ }}
    </div> -->
    <!-- <div>{{ GETALLITEMS }}</div> -->
    <!-- <button @click="increment">Добавить в корзину</button> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import CategoryInfo from "./CategoryInfo.vue";
import CategoryWorkExample from "./CategoryWorkExample.vue";
import Products from "./Products.vue";
export default {
  name: "Category",
  components: {
    CategoryInfo,
    CategoryWorkExample,
    Products,
  },
  data() {
    return {
      productsList: [],
      currentCategory: "",
    };
  },
  watch: {
    currentCategory() {
      this.loadProducts();
    },
  },
  created() {
    this.getCurrentCategory();
  },
  updated() {
    this.getCurrentCategory();
  },
  computed: {
    ...mapGetters("cart", ["GETALLITEMS"]),
    ...mapGetters("api_urls", ["getServerShopUrl"]),
    ...mapGetters("data", [
      "GETALLCATEGORIES",
      "GETCHILDCATEGORIES",
      "GETMAINCATEGORIES",
    ]),
  },
  methods: {
    ...mapActions("cart", ["saveItem", "loadCart"]),
    getCurrentCategory() {
      for (let category in this.GETALLCATEGORIES) {
        if (
          this.GETALLCATEGORIES[category].attributes.slug ===
          this.$route.params.slug
        ) {
          this.currentCategory = this.GETALLCATEGORIES[category];
          break;
        }
      }
    },
    loadProducts() {
      this.axios
        .get(`${this.getServerShopUrl}/products/${this.currentCategory.id}`)
        .then((response) => {
          this.productsList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
  },
};
</script>

<style></style>
