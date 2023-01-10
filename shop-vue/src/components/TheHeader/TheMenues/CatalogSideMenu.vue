<template>
  <div>
    <!-- <div class="all_pruducts_list_item" v-if="category.child_free === true"> -->
    <router-link
      class="all_pruducts_list_item"
      v-if="category.child_free === true"
      :to="'/category/' + category.attributes.slug"
      @click.stop
      @click="closeSideSubMenu"
    >
      <div class="all_pruducts_list_item_image_meta">
        <div class="all_pruducts_list_item_image">
          <img :src="require('../../../assets/images/2.jpeg')" alt="img" />
        </div>
        <span>{{ category.attributes.name }}</span>
      </div>
    </router-link>
    <!-- </div> -->
    <!-- <div class="" v-else @click="switchSideSubMenuVisability"> -->
    <a class="all_pruducts_list_item" v-else>
      <!-- <span class=""> -->
      <div class="all_pruducts_list_item_image_meta">
        <div class="all_pruducts_list_item_image">
          <img :src="require('../../../assets/images/2.jpeg')" alt="img" />
        </div>
        <span>{{ category.attributes.name }}</span>
      </div>
      <!-- </span> -->
      <!-- <span class=""> -->
      <span class="material-symbols-outlined">chevron_right</span>
      <!-- </span> -->
    </a>
    <!-- </div> -->
    <teleport to="body">
      <div
        class="all_product_category_open_skr"
        v-if="GETCATALOGSUBSIDEMENUVISABILITY === category.attributes.name"
        @click="closeSideSubMenu"
        @click.stop
      >
        <div class="all_product_category_open_wrapper">
          <div class="all_product_category_open_header">
            {{ category.attributes.name }}
          </div>
          <ul class="all_product_category_open_list">
            <li
              class="all_product_category_open_list_item"
              v-for="cat in subCategoriesList"
              :key="cat.id"
            >
              <CatalogSubSideMenu :categoryData="cat" />
            </li>
            <li
              v-if="category.id == 6"
              @click="switchMenuVisability"
              class="all_product_category_open_list_item"
            >
              <router-link
                class="all_product_category_open_list_product"
                to="/closet_planner"
              >
                <div class="all_product_category_open_list_image">
                  <img
                    :src="require('../../../assets/images/2.jpeg')"
                    alt="img"
                    class=""
                  />
                </div>
                <span class="">Планировщик шкафа</span>
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </teleport>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import CatalogSubSideMenu from "./CatalogSubSideMenu.vue";
export default {
  name: "CatalogSideMenu",
  components: {
    CatalogSubSideMenu,
  },
  props: {
    category: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      subCategoriesList: [],
      sideSubMenuVisability: false,
    };
  },
  computed: {
    ...mapGetters("data", [
      "GETCATALOGSUBSIDEMENUVISABILITY",
      "GETCHILDCATEGORIES",
    ]),
  },
  methods: {
    ...mapActions("data", [
      "closeSideSubMenu",
      "switchCatalogSubSideMenuVisability",
    ]),
    // switchMenuVisability() {
    //   this.$emit("switchSideMenuVisability");
    // },
    // switchSideSubMenuVisability() {
    //   this.sideSubMenuVisability = !this.sideSubMenuVisability;
    // },
    makeSubCategoriesList() {
      this.subCategoriesList =
        this.GETCHILDCATEGORIES[this.category.attributes.name];
      this.subCategoriesList.sort(function (a, b) {
        if (a.attributes.position > b.attributes.position) {
          return 1;
        }
        if (a.attributes.position < b.attributes.position) {
          return -1;
        }
        return 0;
      });
    },
  },
  mounted() {
    this.makeSubCategoriesList();
  },
};
</script>

<style>
.all_product_category_open_skr {
  position: absolute;
  top: 0;
  right: 0;
  left: 380px;
  z-index: 105;
  background-color: #ffffff;
  pointer-events: none;
}

.all_product_category_open_wrapper {
  grid-column: 1;
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  grid-template-rows: minmax(64px, max-content);
  grid-auto-rows: max-content;
  overflow-y: auto;
  overflow-x: hidden;
  pointer-events: auto;
  background-color: #f8f8f8;
  padding-bottom: 64px;
  margin-right: -24px;
}

.all_product_category_open_header {
  grid-row: 1;
  grid-column: span 9;
  position: sticky;
  top: 0;
  display: flex;
  align-items: center;
  background-color: #ffffff;
  padding-left: 16px;
  padding-right: 40px;
  border-bottom: 1px solid;
}

.all_product_category_open_list {
  grid-row: 2;
  grid-column: span 9;
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  grid-column-gap: 32px;
  grid-auto-rows: max-content;
  grid-row-gap: 32px;
  list-style: none;
  padding-top: 16px;
  padding-right: 40px;
  padding-left: 16px;
}

.all_product_category_open_list_item {
  grid-column: span 3;
}

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

/* .all_product_category_open_all {
  grid-row: 3;
  grid-column: 7 / 13;
  margin-top: 32px;
  margin-right: 40px;
} */

/* .all_product_category_open_wrapper {
  grid-column: 4 / span 9;
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  grid-template-rows: minmax(60px, max-content) 1fr;
}

.all_product_category_open_header {
  grid-row: 1;
  grid-column: span 9;
  display: flex;
  align-items: center;
  width: 100%;
  padding: 16px;
  border-bottom: 1px solid;
}

.all_product_category_open_list {
  grid-row: 2;
  grid-column: span 9;
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  grid-column-gap: 32px;
  list-style: none;
  padding-top: 16px;
  padding-right: 16px;
  padding-left: 16px;
}

.all_product_category_open_list_item {
  grid-column: span 3;
  aspect-ratio: 1 / 1;
  background-color: tomato;
} */
</style>
