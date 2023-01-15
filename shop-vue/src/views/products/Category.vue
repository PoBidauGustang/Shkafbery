<template>
  <div v-if="Object.keys(this.currentCategory).length">
    <div class="product_page_meta_wrapper">
      <div class="product_page_headline_container">
        <h1 class="product_page_headline">
          {{ currentCategory.attributes.name }}
        </h1>
      </div>
    </div>
    <div class="product_page_variants_warpper">
      <div class="product_page_tabs_wrapper">
        <button
          class="product_page_varians_tab current_product_tab"
          @click="viewVisability['Готовые'] = !viewVisability['Готовые']"
        >
          <span class="material-symbols-outlined">shopping_cart</span>
          <span class="product_page_varians_tab_name">Готовые</span>
        </button>
        <button
          class="product_page_varians_tab"
          @click="viewVisability['На заказ'] = !viewVisability['На заказ']"
        >
          <span class="material-symbols-outlined">handyman</span>
          <span class="product_page_varians_tab_name">На заказ</span>
        </button>
        <button
          class="product_page_varians_tab"
          @click="
            viewVisability['Планировщик'] = !viewVisability['Планировщик']
          "
        >
          <span class="material-symbols-outlined">edit</span>
          <span class="product_page_varians_tab_name">Планировщик</span>
        </button>
      </div>
    </div>
    <div>
      <CategoryInfo
        v-if="viewVisability['На заказ']"
        :category="currentCategory"
      />
    </div>
    <div>
      <CategoryWorkExample
        v-if="viewVisability['На заказ']"
        :category="currentCategory"
      />
    </div>
    <div v-if="productsList.length">
      <Products
        v-if="viewVisability['Готовые']"
        :categoryName="currentCategory.attributes.name"
        :productsList="productsList"
      />
    </div>
    <!-- <div>{{ productsList }}</div> -->
    <!-- <div>{{ wardrobes }}</div> -->
    <!-- <div v-for="categ in GETMAINCATEGORIES" :key="categ.id">
      {{ categ }}
    </div> -->
    <!-- <div>{{ GETMAINCATEGORIES }}</div> -->
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
      viewVisability: {
        Готовые: true,
        "На заказ": false,
        Планировщик: false,
      },
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

<style>
.product_page_meta_wrapper {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  padding-left: 24px;
  padding-right: 24px;
  margin-top: 32px;
  margin-bottom: 32px;
}

.product_page_headline_container {
  grid-column: span 12;
  grid-row: 1;
  padding-left: 16px;
  padding-right: 16px;
}

.product_page_headline {
  font-family: "Akrobat", sans-serif;
  font-size: 64px;
  line-height: 72px;
  font-weight: 800;
  text-align: center;
  text-transform: uppercase;
  margin: 0px;
}

.product_page_variants_warpper {
  grid-row: 2;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  padding-left: 24px;
  padding-right: 24px;
  margin-bottom: 64px;
}

.product_page_tabs_wrapper {
  grid-column: 4 / span 6;
  display: flex;
  border-radius: 24px;
  overflow: hidden;
  padding: 8px;
  background-color: #f0f0f0;
}

.product_page_varians_tab {
  display: flex;
  flex: 1;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding-top: 16px;
  padding-bottom: 16px;
  padding-left: 0px;
  padding-right: 0px;
}

.product_page_varians_tab_name {
  font-family: Golos ui, sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 500;
  text-align: center;
  padding-left: 8px;
}

.current_product_tab {
  background-color: #ffffff;
  border-radius: 16px;
  color: #000000;
}
</style>
