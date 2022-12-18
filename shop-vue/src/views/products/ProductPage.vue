<template>
  <div class="product_item_page_area" v-if="isProductFetched">
    <div class="product_item_page_meta_area">
      <div class="product_item_page_meta_gallery_wrapper">
        <div class="product_item_page_meta_gallery_primary_img">
          <img
            src="https://images.unsplash.com/photo-1567016546367-c27a0d56712e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
            alt=""
          />
        </div>
      </div>
    </div>
    <div class="product_page_feature_wrapper">
      <div class="product_feture_wrapper">
        <div
          class="product_feature_description_wrapper"
          v-if="productData.attributes.description"
        >
          <h3 class="product_feature_description_head">Описание</h3>
          <p
            class="product_feature_description_meta"
            v-html="productData.attributes.description"
          ></p>
        </div>
        <div
          class="product_feature_specification_wrapper"
          v-if="productData.attributes.product_specification_value.length"
        >
          <h3 class="product_feature_specification_head">Характеристики</h3>
          <dl
            class="product_feature_specification"
            v-for="value in productData.attributes.product_specification_value"
            :key="value"
          >
            <dt class="product_feature_specification_key">
              {{ value.specification }}
            </dt>
            <dd class="product_feature_specification_value">
              {{ value.value }}
            </dd>
          </dl>
        </div>
      </div>
    </div>
    <div class="product_item_page_product_area_wrapper">
      <div class="product_item_page_product_area">
        <div class="product_item_page_meta_wrapper">
          <div class="product_item_headline_container">
            <h1 class="product_item_headline">
              {{ productData.attributes.title }}
            </h1>
          </div>
          <div class="product_item_description_container">
            <span
              class="product_item_description"
              v-if="productData.attributes.description"
              >{{ productData.attributes.description }}</span
            >
            <span
              class="product_item_description"
              v-if="productData.attributes.description"
              >,
            </span>
            <span class="product_item_description" v-if="choosedDimesion"
              >{{ choosedDimesion.value }},
            </span>
            <span class="product_item_description" v-else>
              {{ productData.attributes.dimensions_value[0].value }},
            </span>
            <span class="product_item_description" v-if="choosedColor">{{
              choosedColor.color.name
            }}</span>
            <span class="product_item_description" v-else>
              {{ productData.attributes.color_price[0].color.name }}
            </span>
          </div>
          <div class="product_item_price_container">
            <span
              class="product_item_price"
              v-if="productData.attributes.regular_price"
              >{{ updatedPrice }} ₽</span
            >
          </div>
          <div class="product_item_controls_wrapper">
            <div class="product_item_controls_links_wrapper">
              <a class="product_item_controls_link">Описание</a>
              <a class="product_item_controls_link">Характеристики</a>
            </div>
            <div class="product_item_controls_buttons_wrapper">
              <button class="product_item_controls_button">
                <div class="product_item_controls_button_icon">
                  <span class="material-symbols-outlined">favorite</span>
                </div>
                <span class="product_item_controls_button_text"
                  >В избранное</span
                >
              </button>
              <button class="product_item_controls_button">
                <div class="product_item_controls_button_icon">
                  <span class="material-symbols-outlined">favorite</span>
                </div>
                <span class="product_item_controls_button_text">Сравнить</span>
              </button>
            </div>
          </div>
        </div>
        <div class="product_item_widgets_wrapper">
          <div class="product_item_widgets_choice_wrapper">
            <div class="product_item_widgets_choice_description_wrapper">
              <span
                class="product_item_widgets_choice_description"
                v-if="productData.attributes.dimensions_value.length"
              >
                Вариантов размeров:
                {{ productData.attributes.dimensions_value.length }}
              </span>
              <span
                class="product_item_widgets_choice_description"
                v-if="productData.attributes.color_price.length"
              >
                , вариантов цветов:
                {{ productData.attributes.color_price.length }}
              </span>
            </div>
            <div class="product_item_widgets_choice_buttons_wrapper">
              <button class="product_item_widgets_choice_button">
                <div class="product_item_widgets_choice_button_meta">
                  <span class="product_item_widgets_choice_button_head" @click="dimensionsVisability = !dimensionsVisability">Выберите размер ({{ productData.attributes.dimensions_value.length }})</span>
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
                  <span
                    class="product_item_widgets_choice_button_value"
                    v-if="choosedDimesion"
                    @click="dimensionsVisability = !dimensionsVisability"
                  >
                    {{ choosedDimesion.value }}
                  </span>
                  <span class="product_item_widgets_choice_button_value" v-else @click="dimensionsVisability = !dimensionsVisability">
                    {{ productData.attributes.dimensions_value[0].value }}
                  </span>
                </div>
                <span class="material-symbols-outlined">chevron_right</span>
              </button>
              <button class="product_item_widgets_choice_button">
                <div class="product_item_widgets_choice_button_meta">
                  <span class="product_item_widgets_choice_button_head" @click="colorsVisability = !colorsVisability">
                    Выберите цвет ({{ productData.attributes.color_price.length }})
                  </span>
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
                  <span class="product_item_widgets_choice_button_value" v-if="choosedColor" @click="colorsVisability = !colorsVisability">
                    {{ choosedColor.color.name }}
                  </span>
                  <span class="product_item_widgets_choice_button_value" v-else @click="colorsVisability = !colorsVisability">
                    {{ productData.attributes.color_price[0].color.name }}
                  </span>
                </div>
                <span class="material-symbols-outlined">chevron_right</span>
              </button>
            </div>
          </div>
          <div class="product_item_widgets_cart_button_wrapper">
            <button class="product_item_widgets_cart_button" v-if="choosedColor && choosedDimesion" @click="addToCart(cartData)">
              <span class="material-symbols-outlined">shopping_cart</span>
              <span class="product_item_widgets_cart_button_text">Добавить в корзину</span>
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- <div> -->
        <!-- <span @click="dimensionsVisability = !dimensionsVisability"
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
        <p></p> -->
        <!-- <span @click="colorsVisability = !colorsVisability"
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
      </div> -->
      <!-- <button
        v-if="choosedColor && choosedDimesion"
        @click="addToCart(cartData)"
      >
        Добавить в корзину
      </button> -->

      <!-- <div v-if="choosedColor && choosedDimesion">
        {{ cartData }}
        <div v-for="(key, value) in cartData" :key="value">{{ key }}: {{ value }}</div>
      </div> -->
      <!-- <p>{{ productData }}</p> -->
    <!-- </div> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "ProductPage",
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

<style>
.product_item_page_area {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  padding-left: 24px;
  padding-right: 24px;
}

.product_item_page_meta_area {
  grid-column: span 8;
  display: grid;
  border-right: 1px solid;
}

.product_item_page_meta_gallery_wrapper {
  grid-row: 1;
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  padding-top: 24px;
  margin-bottom: 64px;
}

.product_item_page_meta_gallery_primary_img {
  grid-column: 3 / span 6;
  overflow: hidden;
  aspect-ratio: 1 / 1;
  margin-right: 16px;
  margin-left: 16px;
}

.product_item_page_meta_gallery_primary_img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product_page_feature_wrapper {
  grid-row: 2;
  padding-left: 16px;
  padding-right: 16px;
}

.product_item_page_product_area_wrapper {
  grid-column: span 4;
  margin-right: -24px;
}

.product_item_page_product_area {
  display: flex;
  flex-direction: column;
  padding-top: 24px;
}

.product_item_page_meta_wrapper {
  display: flex;
  flex-direction: column;
  padding-left: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid;
}

.product_item_headline_container {
  margin-bottom: 4px;
  padding-right: 40px;
}

.product_item_headline {
  font-family: Akrobat, sans-serif;
  font-size: 32px;
  line-height: 40px;
  font-weight: 800;
  text-transform: uppercase;
  margin: 0px;
}

.product_item_description_container {
  display: flex;
  flex-direction: row;
  margin-bottom: 16px;
  padding-right: 40px;
}

.product_item_description {
  font-size: 14px;
  line-height: 20px;
}

.product_item_price_container {
  display: flex;
  flex-direction: row;
  margin-bottom: 32px;
}

.product_item_price {
  font-size: 28px;
  line-height: 36px;
  font-weight: 500;
}

.product_item_controls_wrapper {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  padding-right: 24px;
}

.product_item_controls_links_wrapper {
  grid-column: span 2;
  display: flex;
  flex-direction: column;
}

.product_item_controls_link {
  font-size: 16px;
  line-height: 24px;
  font-weight: 500;
  margin-bottom: 8px;
}

.product_item_controls_buttons_wrapper {
  grid-column: span 2;
  display: flex;
}

.product_item_controls_button {
  display: flex;
  flex: 1;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 0px;
}

.product_item_controls_button_icon {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8px;
  background-color: #f0f0f0;
  border-radius: 100px;
}

.product_item_controls_button_text {
  font-family: Golos ui, sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 16px;
  text-align: center;
  padding-top: 8px;
}

.product_item_widgets_wrapper {
  display: flex;
  flex-direction: column;
  padding-left: 16px;
  padding-top: 16px;
}

.product_item_widgets_choice_wrapper {
  display: flex;
  flex-direction: column;
  padding-right: 40px;
}

.product_item_widgets_choice_description_wrapper {
  display: flex;
  margin-bottom: 16px;
}

.product_item_widgets_choice_description {
  font-size: 14px;
  line-height: 20px;
}

.product_item_widgets_choice_buttons_wrapper {
  display: flex;
  flex-direction: column;
  margin-bottom: 32px;
}

.product_item_widgets_choice_button {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  background-color: #f0f0f0;
  padding-left: 16px;
  padding-right: 16px;
  padding-top: 12px;
  padding-bottom: 12px;
  border-radius: 12px;
  margin-bottom: 16px;
}

.product_item_widgets_choice_button:last-child {
  margin-bottom: 0px;
}

.product_item_widgets_choice_button_meta {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.product_item_widgets_choice_button_head {
  display: flex;
  font-family: "Golos ui", sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 700;
}

.product_item_widgets_choice_button_value {
  font-family: Golos ui, sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 400;
}

.product_item_widgets_cart_button_wrapper {
  display: flex;
  margin-bottom: 32px;
}

.product_item_widgets_cart_button {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 10px 24px 10px 16px;
  font-family: "Golos ui", sans-serif;
  color: #ffffff;
  background: #000000;
  border-radius: 100px;
}

.product_item_widgets_cart_button_text {
  font-size: 16px;
  line-height: 24px;
  font-weight: 500;
  padding-left: 8px;
}

.product_feture_wrapper {
  display: flex;
  flex-direction: column;
}

.product_feature_description_wrapper {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  grid-column-gap: 32px;
  padding-top: 32px;
  padding-bottom: 32px;
  border-top: 1px solid;
  border-bottom: 1px solid;
}

.product_feature_description_head {
  grid-column: span 8;
  grid-row: 1;
  font-family: "Golos UI", sans-serif;
  font-weight: 500;
  font-size: 28px;
  line-height: 36px;
  padding-bottom: 24px;
  margin: 0px;
}

.product_feature_description_meta {
  grid-column: span 8;
  grid-row: 2;
  font-family: "Golos UI", sans-serif;
  font-weight: 400;
  font-size: 24px;
  line-height: 32px;
  margin: 0px;
}

.product_feature_specification_wrapper {
  display: flex;
  flex-direction: column;
  padding-top: 32px;
  padding-bottom: 32px;
  border-bottom: 1px solid;
}

.product_feature_specification_head {
  font-family: "Golos UI", sans-serif;
  font-weight: 500;
  font-size: 28px;
  line-height: 36px;
  padding-bottom: 24px;
  margin: 0px;
}

.product_feature_specification {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  grid-column-gap: 32px;
  margin: 0px;
}

.product_feature_specification_key {
  grid-column: span 3;
  padding-bottom: 12px;
  margin: 0px;
  font-family: "Golos UI", sans-serif;
  font-weight: 400;
  font-size: 18px;
  line-height: 28px;
}

.product_feature_specification_value {
  grid-column: 4 / span 5;
  font-family: "Golos UI", sans-serif;
  font-weight: 400;
  font-size: 18px;
  line-height: 28px;
  margin: 0px;
}
</style>
