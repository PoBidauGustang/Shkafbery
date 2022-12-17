<template>
  <div class="Product_Area_Wrapper">
    <div class="product_variant_header_wrapper">
      <div class="product_sub_header_wrapper">
        <h4 class="product_sub_header">{{ categoryName }} готовыe</h4>
      </div>
      <div class="Product_Amount_Warpper">
        <span class="Product_Amount">Товаров: {{ productsList.length }}</span>
      </div>
    </div>

    <div class="Filter_area_wrapper">
      <div class="Product_Filters_Wrapper">
        <div class="Products_Filters_Header">
          <h3 class="Products_Filters_Header_Name">Фильтры</h3>
          <div v-if="productsList[0].attributes.regular_price.length">
            <button v-on:click="ascending = !ascending">
              <div v-if="ascending">
                По возрастанию цены
                <span class="material-symbols-outlined size_20"
                  >arrow_upward</span
                >
              </div>
              <div v-else>
                По убыванию цены
                <span class="material-symbols-outlined size_20"
                  >arrow_downward</span
                >
              </div>
            </button>
          </div>
        </div>
        <ul class="Product_Filters_List">
          <li
            class="Product_Filters_List_Item"
            v-if="productsList[0].attributes.regular_price.length"
          >
            <button
              @click="priceFilterVisability = !priceFilterVisability"
              class="Product_Filters_List_Item_Head"
            >
              <div class="Product_Filters_List_Item_Head_Meta">
                <span class="Product_Filters_List_Item_Head_Name">Цена</span>
              </div>
            </button>
            <div
              class="Product_Filters_List_Input_Area"
              v-if="priceFilterVisability"
            >
              <label class="Product_Filters_List_Label_Price">
                <span>От</span>
                <input
                  class="Product_Filters_List_Label_Price_Input"
                  type="number"
                  v-model="minInputPrice"
                  placeholder="0"
                />
              </label>
              <label class="Product_Filters_List_Label_Price">
                <span>До</span>
                <input
                  class="Product_Filters_List_Label_Price_Input"
                  type="number"
                  v-model="maxInputPrice"
                  placeholder="0"
                />
              </label>
            </div>
          </li>
        </ul>
        <ul
          class="Product_Filters_List"
          v-if="productsList[0].attributes.dimensions_value.length"
        >
          <li
            class="Product_Filters_List_Item"
            v-if="
              productsList[0].attributes.dimensions_value[0].dimension[0] == 'Ш'
            "
          >
            <button
              @click="widthFilterVisability = !widthFilterVisability"
              class="Product_Filters_List_Item_Head"
            >
              <div class="Product_Filters_List_Item_Head_Meta">
                <span class="Product_Filters_List_Item_Head_Name">Ширина</span>
              </div>
            </button>
            <div
              class="Product_Filters_List_Input_Area"
              v-if="widthFilterVisability"
            >
              <label class="Product_Filters_List_Label_Price">
                <span>От</span>
                <input
                  class="Product_Filters_List_Label_Price_Input"
                  type="number"
                  v-model="minInputWidth"
                  placeholder="0"
                />
              </label>
              <label class="Product_Filters_List_Label_Price">
                <span>До</span>
                <input
                  class="Product_Filters_List_Label_Price_Input"
                  type="number"
                  v-model="maxInputWidth"
                  placeholder="0"
                />
              </label>
            </div>
          </li>
          <li
            v-if="
              productsList[0].attributes.dimensions_value[0].dimension[1] == 'Г'
            "
          >
            <button
              @click="depthFilterVisability = !depthFilterVisability"
              class="Product_Filters_List_Item_Head"
            >
              <div class="Product_Filters_List_Item_Head_Meta">
                <span class="Product_Filters_List_Item_Head_Name">Глубина</span>
              </div>
            </button>
            <div
              class="Product_Filters_List_Input_Area"
              v-if="depthFilterVisability"
            >
              <label class="Product_Filters_List_Label_Price">
                <span>От</span>
                <input
                  class="Product_Filters_List_Label_Price_Input"
                  type="number"
                  v-model="minInputDepth"
                  placeholder="0"
                />
              </label>
              <label class="Product_Filters_List_Label_Price">
                <span>До</span>
                <input
                  class="Product_Filters_List_Label_Price_Input"
                  type="number"
                  v-model="maxInputDepth"
                  placeholder="0"
                />
              </label>
            </div>
          </li>
          <li
            v-if="
              productsList[0].attributes.dimensions_value[0].dimension[2] == 'В'
            "
          >
            <button
              @click="heightFilterVisability = !heightFilterVisability"
              class="Product_Filters_List_Item_Head"
            >
              <div class="Product_Filters_List_Item_Head_Meta">
                <span class="Product_Filters_List_Item_Head_Name">Высота</span>
              </div>
            </button>
            <div
              class="Product_Filters_List_Input_Area"
              v-if="heightFilterVisability"
            >
              <label class="Product_Filters_List_Label_Price">
                <span>От</span>
                <input
                  class="Product_Filters_List_Label_Price_Input"
                  type="number"
                  v-model="minInputHeight"
                  placeholder="0"
                />
              </label>
              <label class="Product_Filters_List_Label_Price">
                <span>До</span>
                <input
                  class="Product_Filters_List_Label_Price_Input"
                  type="number"
                  v-model="maxInputHeight"
                  placeholder="0"
                />
              </label>
            </div>
          </li>
          <li
            v-if="
              productsList[0].attributes.dimensions_value[0].dimension == 'п.м.'
            "
          >
            <button
              @click="pmFilterVisability = !pmFilterVisability"
              class="Product_Filters_List_Item_Head"
            >
              <div class="Product_Filters_List_Item_Head_Meta">
                <span class="Product_Filters_List_Item_Head_Name"
                  >Ширина п.м.</span
                >
              </div>
            </button>
            <div
              class="Product_Filters_List_Input_Area"
              v-if="pmFilterVisability"
            >
              <label class="Product_Filters_List_Label_Price">
                <span>От</span>
                <input
                  class="Product_Filters_List_Label_Price_Input"
                  type="number"
                  v-model="minInputPM"
                  placeholder="0"
                />
              </label>
              <label class="Product_Filters_List_Label_Price">
                <span>До</span>
                <input
                  class="Product_Filters_List_Label_Price_Input"
                  type="number"
                  v-model="maxInputPM"
                  placeholder="0"
                />
              </label>
            </div>
          </li>
        </ul>
        <div
          class="Product_Filters_List"
          v-if="productsList[0].attributes.color_price.length"
        >
          <div class="Product_Filters_List_Item">
            <button
              @click="colorFilterVisability = !colorFilterVisability"
              class="Product_Filters_List_Item_Head"
            >
              <div class="Product_Filters_List_Item_Head_Meta">
                <span class="Product_Filters_List_Item_Head_Name">Цвет</span>
                <span v-if="choosedColors.length">{{ choosedColors }}</span>
              </div>
            </button>
          </div>
          <div v-if="colorFilterVisability">
            <button @click="resetAllColors()">Сбросить выбранные цвета</button>
            <ul>
              <li v-for="color in getColors" :key="color.id">
                <label class="Product_Filters_Check_Area">
                  <input
                    class="check_input"
                    type="checkbox"
                    :value="color"
                    v-model="choosedColors"
                    @change="updateCheckallColors()"
                  />
                  <span class="check_label" :for="color">{{ color }}</span>
                </label>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <ul v-if="filteredProducts.length">
      <li v-for="product in filteredProducts" :key="product.id">
        <ProductView :product="product" />
      </li>
    </ul>
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
      priceFilterVisability: false,
      minInputPrice: null,
      maxInputPrice: null,
      widthFilterVisability: false,
      minInputWidth: null,
      maxInputWidth: null,
      depthFilterVisability: false,
      minInputDepth: null,
      maxInputDepth: null,
      heightFilterVisability: false,
      minInputHeight: null,
      maxInputHeight: null,
      pmFilterVisability: false,
      minInputPM: null,
      maxInputPM: null,
      colorFilterVisability: false,
      choosedColors: [],
      isCheckAllColors: false,
      ascending: true,
    };
  },
  props: {
    productsList: {
      type: Array,
      default() {
        return [];
      },
    },
    categoryName: {
      type: String,
      default() {
        return "";
      },
    },
  },
  created() {},
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
      this.resetAllColors();
      return colorsList;
    },
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
      if (this.ascending) {
        tempProducts = tempProducts.sort((a, b) => {
          return a.attributes.regular_price - b.attributes.regular_price;
        });
      }
      if (!this.ascending) {
        tempProducts = tempProducts.sort((a, b) => {
          return b.attributes.regular_price - a.attributes.regular_price;
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
    resetAllColors() {
      this.isCheckAllColors = false;
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
  },
};
</script>

<style>
.Product_Area_Wrapper {
  grid-column: span 12;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  padding-left: 24px;
  padding-right: 24px;
}

.product_variant_header_wrapper {
  grid-column: span 12;
  grid-row: 1;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 32px;
}

.product_sub_header_wrapper {
  padding-left: 16px;
}

.product_sub_header {
  font-family: Akrobat, sans-serif;
  font-size: 32px;
  line-height: 40px;
  font-weight: 800;
  text-transform: uppercase;
  margin: 0px;
}

.Product_Amount_Warpper {
  display: flex;
  flex-direction: row-reverse;
  padding-right: 16px;
}

.Product_Amount {
  font-size: 14px;
  line-height: 20px;
  text-align: right;
}

.Filter_area_wrapper {
  grid-column: span 3;
  grid-row: 2;
  position: sticky;
  left: 0;
  top: -1px;
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
  border-right: 1px solid;
  border-top: 1px solid;
  margin-left: -24px;
  background-color: #ffffff;
}

.Product_Listing_Wrapper {
  grid-column: 4 / span 9;
  grid-row: 2;
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  list-style: none;
}

.Product_Listing_Item {
  grid-column: span 3;
  border-right: 1px solid;
  border-bottom: 1px solid;
}

.Product_Listing_Item:nth-child(-n + 3) {
  border-top: 1px solid;
}

.Product_Listing_Item:nth-child(3n) {
  border-right: 0px;
  margin-right: -24px;
}

.Product_Listing_Item:nth-child(3n) a {
  padding-right: 24px;
}

.Product_Listing_Item_Input {
  display: flex;
  text-decoration: none;
}

.Product_Listing_Item_Input:hover {
  background-color: #f6f3f3;
}

.Product_Filters_Wrapper {
  display: flex;
  flex-direction: column;
}

.Products_Filters_Header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding-left: 40px;
  padding-right: 16px;
  padding-top: 12px;
  padding-bottom: 12px;
  border-bottom: 1px solid;
  width: 100%;
  min-height: 65px;
}

.Products_Filters_Header_Name {
  font-size: 20px;
  line-height: 28px;
  font-weight: 500;
}

.products_filter_select {
  font-family: "Golos Ui", sans-serif;
  font-size: 14px;
  line-height: 20px;
  font-weight: 500;
  border: 0;
}

.Product_Filters_List {
  display: flex;
  flex-direction: column;
  list-style: none;
  width: 100%;
}

.Product_Filters_List_Item {
  border-bottom: 1px solid;
}

.Product_Filters_List_Item_Head {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding-left: 40px;
  padding-right: 16px;
  padding-top: 16px;
  padding-bottom: 16px;
}

.Product_Filters_List_Item_Head_Meta {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.Product_Filters_List_Item_Head_Name {
  font-family: "Golos Ui", sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 500;
  padding-top: 4px;
  padding-bottom: 4px;
}

.Product_Filters_List_Input_Area {
  display: flex;
  flex-direction: column;
  margin-top: 8px;
  padding-bottom: 28px;
}

.Product_Filters_Check_Area {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding-left: 40px;
  padding-right: 16px;
  padding-top: 12px;
  padding-bottom: 12px;
}

.check_input {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  margin: 0px;
  width: 24px;
  height: 24px;
}

.check_input::before {
  font-family: "Material Symbols Outlined";
  content: "check_box_outline_blank";
  font-variation-settings: "wght" 400, "opsz" 24;
  font-size: 24px;
  line-height: 1;
}

.check_input:hover::before {
  font-variation-settings: "wght" 700;
}

.check_input:checked::before {
  font-family: "Material Symbols Outlined";
  font-variation-settings: "FILL" 1;
  content: "check_box";
  font-size: 24px;
  line-height: 1;
}

.check_input:checked:hover::before {
  font-variation-settings: "wght" 700, "FILL" 1;
}

.check_label {
  font-size: 16px;
  line-height: 24px;
  padding-left: 16px;
}

.Product_Filters_List_Label_Price {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-top: 16px;
  padding-right: 16px;
  padding-left: 40px;
  padding-bottom: 12px;
}

.Product_Filters_List_Label_Price_Input {
  padding: 12px;
  border-radius: 8px;
}
</style>
