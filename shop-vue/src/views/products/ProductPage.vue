<template>
  <div v-if="isProductFetched">
    <h2>{{ productData.attributes.title }}</h2>
    <span v-html="productData.attributes.description"></span>
    <span>, {{ productData.attributes.dimensions_value[0].value }}</span>
    <div>{{ productData.attributes.regular_price }} ₽</div>
    <div>Описание</div>
    <div>Характеристики</div>
    <span
      >Вариантов размeров: {{ productData.attributes.dimensions_value.length }},
      вариантов цветов: {{ productData.attributes.color_price.length }}</span
    >
    <div>
    <!-- <div> -->
      <span @click="dimensionsVisability=!dimensionsVisability"
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
              :value="dimension.value"
              :id="dimension"
              v-model="choosedDimesion"
            />
            <label :for="dimension">{{ dimension.value }}</label>
          </li>
        </ul>
      </div>
      <div v-if="choosedDimesion.length" @click="dimensionsVisability=!dimensionsVisability">{{ choosedDimesion }} мм</div>
      <div v-else @click="dimensionsVisability=!dimensionsVisability">
        {{ productData.attributes.dimensions_value[0].value }} мм
      </div>
    </div>
    <p v-for="(value, key) in productData.attributes" :key="value">
      {{ key }}: {{ value }}
    </p>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "ProductPage",
  components: {},
  data() {
    return {
      productData: [],
      dimensionsVisability: true,
      choosedDimesion: "",
      isProductFetched: false,
    };
  },
  created() {
    this.loadProduct();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerShopUrl"]),
  },
  methods: {
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
  },
};
</script>

<style></style>
