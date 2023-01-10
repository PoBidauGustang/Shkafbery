<template>
  <div @click="switchMainSubMenuVisability">
    <router-link
      class="all_product_category_open_list_product"
      :to="'/category/' + categoryData.attributes.slug"
    >
      <div class="all_product_category_open_list_image">
        <img :src="require('../../../assets/images/2.jpeg')" alt="img" />
      </div>
      <span>{{ categoryData.attributes.name }}</span>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "CatalogSubSideMenu",
  props: {
    categoryData: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {};
  },
  methods: {
    switchMainSubMenuVisability() {
      this.$emit("switchSideSubMenuVisability");
    },
  },
};
</script>

<style>
/* .all_product_category_open_list_item {
  grid-column: span 3;
} */

.all_product_category_open_list_product {
  display: flex;
  flex-direction: column;
}

.all_product_category_open_list_image {
  overflow: hidden;
  aspect-ratio: 4 / 2;
  margin-bottom: 16px;
}

.all_product_category_open_list_image img {
  width: 100%;
  object-fit: cover;
}

/* .MegaMenu_input {
  color: #1e1b16;
  font-size: 16px;
  font-weight: 700;
  line-height: 24px;
}

.Mega_Menu_Image_Wrapper {
  aspect-ratio: 16 / 9;
  min-height: 0;
  padding-bottom: 16px;
}

.MegaMenu_Image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.Mega_Menu_Conf {
  grid-column: 10 / span 3;
  display: flex;
  flex-direction: column;
  padding-top: 12px;
  padding-bottom: 16px;
  padding-left: 16px;
  padding-right: 16px;
  background-color: #ffffff;
  border-radius: 12px;
} */
</style>
