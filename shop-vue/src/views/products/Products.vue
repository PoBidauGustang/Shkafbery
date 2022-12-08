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
      <div v-if="productsList[0].attributes.color_price.length">
        <p>цвета</p>
        <div>choosed colors: {{ choosedColors }}</div>
        <input
          type="checkbox"
          @click="checkAllColors()"
          v-model="isCheckAllColors"
        />
        Check All
        <ul>
          <li v-for="color in getColors" :key="color.id">
            <input
              type="checkbox"
              :value="color"
              :id="color"
              v-model="choosedColors"
              @change="updateCheckallColors()"
            />
            <label :for="color">{{ color }}</label>
          </li>
        </ul>
        <!-- <input type="checkbox" id="jack" value="Jack" v-model="checkedNames"> -->

        <!-- <input type="checkbox" value="color 2" v-model="choosedColors" /> -->
        <!-- <label for="color1">color 1</label> -->
        <!-- <input type="number" v-model="maxInputPrice" placeholder="0" /> -->
      </div>
    </div>

    <!-- {{filteredProducts}} -->
    <ul v-if="filteredProducts.length">
      <li v-for="product in filteredProducts" :key="product.id">
        <ProductView :product="product" />
      </li>
    </ul>
    <!-- <ul v-else>
      
      <li v-for="product in productsList" :key="product.id">
        <ProductView :product="product" />
      </li>
    </ul> -->
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
      choosedColors: [],
      isCheckAllColors: false,
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
    this.checkAllColors();
    // this.filteredProducts;
  },
  // mounted() {
  //   // this.loadProducts();
  //   this.checkAllColors();
  //   // this.filteredProducts;
  // },
  computed: {
    ...mapGetters("cart", ["GETALLITEMS"]),
    ...mapGetters("api_urls", ["getServerShopUrl"]),
    getColors() {
      let colorsList = [];
      for (let item in this.productsList) {
        if (this.productsList[item].attributes.color_price) {
          for (let colorData in this.productsList[item].attributes
            .color_price) {
            if (
              !colorsList.includes(
                this.productsList[item].attributes.color_price[colorData].color
                  .name
              )
            ) {
              colorsList.push(
                this.productsList[item].attributes.color_price[colorData].color
                  .name
              );
            }
          }
        }
      }
      return colorsList;
    },
    filteredProducts() {
      console.log(1);
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
      if (this.choosedColors.length) {
        tempProducts = tempProducts.filter((item) => {
          let switcher = false;
          for (let colorDict in item.attributes.color_price) {
            if (
              this.choosedColors.includes(
                item.attributes.color_price[colorDict].color.name
              )
            ) {
              switcher = true;
              break;
            }
          }
          return switcher;
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
    checkAllColors() {
      this.isCheckAllColors = !this.isCheckAllColors;
      this.choosedColors = [];
      if (this.isCheckAllColors) {
        for (let key in this.getColors) {
          this.choosedColors.push(this.getColors[key]);
        }
      }
    },
    updateCheckallColors() {
      if (this.choosedColors.length == this.getColors.length) {
        this.isCheckAllColors = true;
      } else {
        this.isCheckAllColors = false;
      }
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
