<template>
  <div>
    <!-- <ul class="all_products_list">
      <li class="all_pruducts_list_item">
        <div>Каталог</div>
        <div @click="closeMegaMenu">Закрыть</div>
      </li>
    </ul> -->
    <div @click="switchSideMenuVisability">
      <a class="catalog" @click="showMegaMenuCatalog">
        <span class="btm_link">Каталог</span
        ><span class="icon_wrapper">
          <span class="material-icons-outlined md-18">expand_more</span>
          <span @click="closeSideMenuVisability">Закрыть</span>
        </span>
      </a>
    </div>
    <div class="all_products_wrapper" v-if="sideMenuVisability">
      <ul class="all_products_list">
        <li
          class="all_pruducts_list_item"
          v-for="category in GETMAINCATEGORIES"
          :key="category.id"
        >
          <span v-if="category.attributes.for_side_menu == true">
            <CatalogSideMenu :category="category" />
          </span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import CatalogSideMenu from "./CatalogSideMenu.vue";
export default {
  name: "MenuCatalog",
  components: {
    CatalogSideMenu,
  },
  data() {
    return {
      sideMenuVisability: false,
    };
  },
  watch: {},
  computed: {
    ...mapGetters("data", ["GETCHILDCATEGORIES", "GETMAINCATEGORIES"]),
  },
  methods: {
    switchSideMenuVisability() {
      this.sideMenuVisability = !this.sideMenuVisability;
    },
    closeSideMenuVisability() {
      this.sideMenuVisability = false;
    },
  },
};
</script>

<style>
.catalog {
  grid-column: span 2;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "PT Root UI", sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 400;
  padding-top: 20px;
  padding-bottom: 19px;
  padding-left: 24px;
  padding-right: 0px;
  border-right: 1px solid;
}

.bottom_menu_link {
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  color: #000000;
  font-size: 16px;
  font-weight: 500;
  line-height: 24px;
  text-align: center;
}

.bottom_menu_link:hover {
  background: #f0eef1;
}

.btm_link {
  padding-left: 4px;
  padding-right: 4px;
}

.MegaMenu_wrapper {
  background: rgba(64, 64, 64, 0.4);
  position: fixed;
  right: 0;
  left: 0;
  top: 180px;
  bottom: 0;
  width: 100vw;
}

.MegaMenu {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  background-color: #f0f0f0;
  grid-column-gap: 24px;
  position: fixed;
  top: 180px;
  padding-top: 32px;
  padding-bottom: 48px;
  padding-left: 48px;
  padding-right: 48px;
  width: 100%;
}

.MegaMenu_List {
  grid-column: span 9;
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  grid-column-gap: 24px;
  grid-auto-rows: max-content;
}

.MegaMenu_Category {
  grid-column: span 3;
  display: flex;
  flex-direction: column-reverse;
  background-color: #ffffff;
  padding: 16px;
  border-radius: 12px;
}

.MegaMenu_input {
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
}

.all_products_wrapper {
  position: fixed;
  right: 0;
  left: 0;
  top: 0;
  z-index: 2;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  height: 100vh;
}

.all_products_list {
  grid-column: span 3;
  display: flex;
  flex-direction: column;
  list-style: none;
  min-height: 100vh;
  border-right: 1px solid;
}

.all_pruducts_list_item {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  min-height: 60px;
  padding-left: 16px;
  padding-top: 12px;
  padding-right: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid;
}
</style>
