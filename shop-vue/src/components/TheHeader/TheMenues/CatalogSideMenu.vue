<template>
  <div
    class="all_product_category_open_wrapper"
    ref="all_product_category_open_wrapper"
  >
    <div v-if="category.child_free === true">
      <router-link
        class="bottom_menu_link"
        :to="'/category/' + category.attributes.slug"
        >{{ category.attributes.name }}</router-link
      >
    </div>
    <div v-else @click="switchSideSubMenuVisability">
      <a class="bottom_menu_link">
        <span class="btm_link">{{ category.attributes.name }}</span>
        <span class="icon_wrapper">
          <span class="material-icons-outlined md-18">expand_more</span>
        </span>
      </a>
    </div>
    <div v-if="sideSubMenuVisability">
      <ul class="all_product_category_open_list">
        <li
          class="MegaMenu_Category"
          v-for="cat in subCategoriesList"
          :key="cat.id"
        >
          <CatalogSubSideMenu
            :categoryData="cat"
            @switchSideSubMenuVisability="switchSideSubMenuVisability"
          />
        </li>
        <li
          v-if="category.id == 6"
          @click="switchSideSubMenuVisability"
          class="Mega_Menu_Conf"
        >
          <router-link class="bottom_menu_link" to="/closet_planner">
            <span class="MegaMenu_input">Планировщик шкафа</span>
            <div class="Mega_Menu_Image_Wrapper">
              <img
                :src="require('../../../assets/images/2.jpeg')"
                alt="img"
                class="MegaMenu_Image"
              />
            </div>
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
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
    ...mapGetters("data", ["GETCHILDCATEGORIES"]),
  },
  methods: {
    switchSideSubMenuVisability() {
      this.sideSubMenuVisability = !this.sideSubMenuVisability;
    },
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
.all_product_category_open_wrapper {
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
}
</style>
