<template>
  <div>
    <h3>Товары:</h3>
    <div>
      Фильтры:
      <div v-if="productsList[0].attributes.regular_price.length">
        <p>цена</p>
        <input type="number" v-model="minInputPrice" placeholder="0" />
        <input type="number" v-model="maxInputPrice" placeholder="0" />
      </div>
      <div v-if="productsList[0].attributes.dimensions_value.length">
        <div
          v-if="
            productsList[0].attributes.dimensions_value[0].dimension[0] == 'Ш'
          "
        >
          <!-- <div> -->
          <p>ширина</p>
          <input type="number" v-model="minInputWidth" placeholder="0" />
          <input type="number" v-model="maxInputWidth" placeholder="0" />
        </div>
        <div
          v-if="
            productsList[0].attributes.dimensions_value[0].dimension[1] == 'Г'
          "
        >
          <p>глубина</p>
          <input type="number" v-model="minInputDepth" placeholder="0" />
          <input type="number" v-model="maxInputDepth" placeholder="0" />
        </div>
        <div
          v-if="
            productsList[0].attributes.dimensions_value[0].dimension[2] == 'В'
          "
        >
          <p>высота</p>
          <input type="number" v-model="minInputHeight" placeholder="0" />
          <input type="number" v-model="maxInputHeight" placeholder="0" />
        </div>
        <div
          v-if="
            productsList[0].attributes.dimensions_value[0].dimension == 'п.м.'
          "
        >
          <p>ширина п.м.</p>
          <input type="number" v-model="minInputPM" placeholder="0" />
          <input type="number" v-model="maxInputPM" placeholder="0" />
        </div>
      </div>
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
      minInputDepth: null,
      maxInputDepth: null,
      minInputHeight: null,
      maxInputHeight: null,
      minInputPM: null,
      maxInputPM: null,
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
        tempProducts = tempProducts.filter((item) => {
          return item.attributes.regular_price >= this.minInputPrice;
        });
      }
      if (this.maxInputPrice) {
        tempProducts = tempProducts.filter((item) => {
          return item.attributes.regular_price <= this.maxInputPrice;
        });
      }
      if (this.minInputWidth) {
        tempProducts = tempProducts.filter((item) => {
          let switcher = false;
          for (let dimension_dict in item.attributes.dimensions_value) {
            if (
              Number(
                item.attributes.dimensions_value[dimension_dict].value.split(
                  "-"
                )[0]
              ) >= this.minInputWidth
            ) {
              switcher = true;
              break;
            }
          }
          return switcher;
        });
      }
      if (this.maxInputWidth) {
        tempProducts = tempProducts.filter((item) => {
          let switcher = false;
          for (let dimension_dict in item.attributes.dimensions_value) {
            if (
              Number(
                item.attributes.dimensions_value[dimension_dict].value.split(
                  "-"
                )[0]
              ) <= this.maxInputWidth
            ) {
              switcher = true;
              break;
            }
          }
          return switcher;
        });
      }
      if (this.minInputDepth) {
        tempProducts = tempProducts.filter((item) => {
          let switcher = false;
          for (let dimension_dict in item.attributes.dimensions_value) {
            if (
              Number(
                item.attributes.dimensions_value[dimension_dict].value.split(
                  "-"
                )[1]
              ) >= this.minInputDepth
            ) {
              switcher = true;
              break;
            }
          }
          return switcher;
        });
      }
      if (this.maxInputDepth) {
        tempProducts = tempProducts.filter((item) => {
          let switcher = false;
          for (let dimension_dict in item.attributes.dimensions_value) {
            if (
              Number(
                item.attributes.dimensions_value[dimension_dict].value.split(
                  "-"
                )[1]
              ) <= this.maxInputDepth
            ) {
              switcher = true;
              break;
            }
          }
          return switcher;
        });
      }
      if (this.minInputHeight) {
        tempProducts = tempProducts.filter((item) => {
          let switcher = false;
          for (let dimension_dict in item.attributes.dimensions_value) {
            if (
              Number(
                item.attributes.dimensions_value[dimension_dict].value.split(
                  "-"
                )[2]
              ) >= this.minInputHeight
            ) {
              switcher = true;
              break;
            }
          }
          return switcher;
        });
      }
      if (this.maxInputHeight) {
        tempProducts = tempProducts.filter((item) => {
          let switcher = false;
          for (let dimension_dict in item.attributes.dimensions_value) {
            if (
              Number(
                item.attributes.dimensions_value[dimension_dict].value.split(
                  "-"
                )[2]
              ) <= this.maxInputHeight
            ) {
              switcher = true;
              break;
            }
          }
          return switcher;
        });
      }
      if (this.minInputPM) {
        tempProducts = tempProducts.filter((item) => {
          let switcher = false;
          for (let dimension_dict in item.attributes.dimensions_value) {
            if (
              Number(item.attributes.dimensions_value[dimension_dict].value) >=
              this.minInputPM
            ) {
              switcher = true;
              break;
            }
          }
          return switcher;
        });
      }
      if (this.maxInputPM) {
        tempProducts = tempProducts.filter((item) => {
          let switcher = false;
          for (let dimension_dict in item.attributes.dimensions_value) {
            if (
              Number(item.attributes.dimensions_value[dimension_dict].value) <=
              this.maxInputPM
            ) {
              switcher = true;
              break;
            }
          }
          return switcher;
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
