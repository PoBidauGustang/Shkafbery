<template>
  <div>
    <router-link
      class="Product_Listing_Item_Input"
      :to="'/product/' + product.id"
    >
      <div class="Product_Input_Wrapper">
        <div class="Product_Input_Img_Wrapper">
          <img
            src="https://images.unsplash.com/photo-1567016546367-c27a0d56712e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
            alt=""
          />
        </div>
        <div class="Product_Input_Meta_Wrapper">
          <div class="Product_Input_Meta">
            <span class="Product_Input_Meta_Name">{{
              product.attributes.title
            }}</span>
            <span
              class="Product_Input_Meta_Description"
              v-if="product.attributes.dimensions_value.length"
            >
              Вариантов размeров:
              {{ product.attributes.dimensions_value.length }}
            </span>
            <span
              class="Product_Input_Meta_Description"
              v-if="product.attributes.color_price.length"
            >
              Вариантов цветов: {{ product.attributes.color_price.length }}
            </span>
          </div>
          <span class="Product_Input_Meta_Price">{{
            product.attributes.regular_price
          }}</span>
        </div>
        <!-- <li v-for="line in product.attributes" :key="line">
        {{ line }}
      </li> -->
      </div>
    </router-link>
    <!-- <div v-if="category.child_free === true">
      <router-link
        class="bottom_menu_link"
        :to="'/category/' + category.attributes.slug"
        >{{ category.attributes.name }}
      </router-link>
    </div> -->
  </div>
</template>

<script>
// import { mapActions, mapGetters } from "vuex";
export default {
  name: "ProductView",
  components: {},
  data() {
    return {};
  },
  props: {
    product: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  methods: {},
};
</script>

<style>
.Product_Input_Wrapper {
  display: flex;
  flex-direction: column;
  padding: 16px;
}

.Product_Input_Img_Wrapper {
  overflow: hidden;
  aspect-ratio: 1 / 1;
  margin-bottom: 16px;
}

.Product_Input_Img_Wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.Product_Input_Meta_Wrapper {
  display: flex;
  justify-content: space-between;
  color: black;
}

.Product_Input_Meta {
  display: flex;
  flex-direction: column;
  margin-right: 16px;
}

.Product_Input_Meta_Name {
  font-size: 18px;
  line-height: 28px;
  font-weight: 700;
  padding-bottom: 4px;
}

.Product_Input_Meta_Description {
  font-size: 16px;
  line-height: 24px;
  font-weight: 400;
}

.Product_Input_Meta_Price {
  font-size: 18px;
  line-height: 28px;
  font-weight: 500;
}
</style>
