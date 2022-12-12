<template>
  <div v-if="isProductFetched">
    <h2>{{ productData.attributes.title }}</h2>
    <span
      v-if="productData.attributes.description"
      v-html="productData.attributes.description"
    ></span>
    <span v-if="productData.attributes.description">, </span>
    <span v-if="choosedDimesion">{{ choosedDimesion.value }}, </span>
    <span v-else>
      {{ productData.attributes.dimensions_value[0].value }},
    </span>
    <span v-if="choosedColor">{{ choosedColor.color.name }}</span>
    <span v-else>
      {{ productData.attributes.color_price[0].color.name }}
    </span>
    <div v-if="productData.attributes.regular_price">{{ updatedPrice }} ₽</div>
    <div>Описание</div>
    <div>Характеристики</div>
    <span v-if="productData.attributes.dimensions_value.length"
      >Вариантов размeров:
      {{ productData.attributes.dimensions_value.length }}</span
    >
    <span v-if="productData.attributes.color_price.length"
      >, вариантов цветов: {{ productData.attributes.color_price.length }}</span
    >
    <div>
      <span @click="dimensionsVisability = !dimensionsVisability"
        >Выберите размер ({{
          productData.attributes.dimensions_value.length
        }})</span
      >
      <div v-if="dimensionsVisability">
        <ul>
          <li
            v-for="dimension in productData.attributes.dimensions_value"
            :key="dimension.id"
          >
            <input
              type="radio"
              :value="dimension"
              :id="dimension"
              v-model="choosedDimesion"
            />
            <label :for="dimension">{{ dimension.value }}</label>
          </li>
        </ul>
      </div>
      <div
        v-if="choosedDimesion"
        @click="dimensionsVisability = !dimensionsVisability"
      >
        {{ choosedDimesion.value }}
      </div>
      <div v-else @click="dimensionsVisability = !dimensionsVisability">
        {{ productData.attributes.dimensions_value[0].value }}
      </div>
      <p></p>
      <span @click="colorsVisability = !colorsVisability"
        >Выберите цвет ({{ productData.attributes.color_price.length }})</span
      >
      <div v-if="colorsVisability">
        <ul>
          <li
            v-for="color in productData.attributes.color_price"
            :key="color.id"
          >
            <input
              type="radio"
              :value="color"
              :id="color"
              v-model="choosedColor"
            />
            <label :for="color">{{ color.color.name }}</label>
          </li>
        </ul>
      </div>
      <div v-if="choosedColor" @click="colorsVisability = !colorsVisability">
        {{ choosedColor.color.name }}
      </div>
      <div v-else @click="colorsVisability = !colorsVisability">
        {{ productData.attributes.color_price[0].color.name }}
      </div>
    </div>
    <button v-if="choosedColor && choosedDimesion" @click="addToCart(cartData)">
      Добавить в корзину
    </button>
    <div v-if="productData.attributes.description">
      {{ productData.attributes.description }}
    </div>
    <div v-if="productData.attributes.product_specification_value.length">
      <div
        v-for="value in productData.attributes.product_specification_value"
        :key="value"
      >
        {{ value.specification }}: {{ value.value }}
      </div>
    </div>
    <div v-if="choosedColor && choosedDimesion">
      {{ cartData }}
      <!-- <div v-for="(key, value) in cartData" :key="value">{{ key }}: {{ value }}</div> -->
    </div>
    <p>{{ productData }}</p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "ProductPage",
  components: {},
  data() {
    return {
      productData: [],
      dimensionsVisability: false,
      colorsVisability: false,
      choosedDimesion: null,
      choosedColor: null,
      isProductFetched: false,
    };
  },
  created() {
    this.loadProduct();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerShopUrl"]),
    updatedPrice() {
      let price = Number(
        Number(this.productData.attributes.regular_price).toFixed()
      );
      if (this.choosedDimesion) {
        price = Number(price) + this.choosedDimesion.price_change;
      }
      if (this.choosedColor) {
        price = Number(price) * (1 + this.choosedColor.price_percent * 0.01);
      }
      return Number(price.toFixed());
    },
    cartData() {
      let result = {};
      let uuid =
        String(this.productData.id) +
        String(this.choosedColor.id) +
        String(this.choosedDimesion.id);
      result["uuid"] = uuid;
      result["id"] = this.productData.id;
      result["title"] = this.productData.attributes.title;
      result["category"] = this.productData.attributes.category;
      result["color"] = this.choosedColor;
      result["dimensions"] = this.choosedDimesion;
      result["product_specification"] =
        this.productData.attributes.product_specification_value;
      result["price"] = this.updatedPrice;
      return result;
    },
  },
  methods: {
    ...mapActions("cart", ["saveItem"]),
    async loadProduct() {
      await this.axios
        .get(`${this.getServerShopUrl}/product/${this.$route.params.id}`)
        .then((response) => {
          this.productData = response.data.data;
        })
        .catch((error) => {
          console.error(error);
        });
      this.isProductFetched = true;
    },
    addToCart(payload) {
      this.saveItem(payload);
    },
  },
};
</script>

<style></style>
