<template>
  <div class="men_wrapper_catalog">
    <button class="men_catalog" @click="switchSideMenuVisability">
      <!-- <span class="">Каталог</span><span class="">
          <span @click="closeSideMenuVisability">Закрыть</span>
        </span> -->
      <span class="material-symbols-outlined">widgets</span
      ><span class="men_catalog_text">Каталог</span>
    </button>
    <!-- <teleport to="body"> -->
    <!-- <div class="all_products_wrapper" v-if="sideMenuVisability"> -->
    <div class="all_products_list_wrapper" v-if="sideMenuVisability">
      <div class="all_products_list_header">
        <span>Каталог</span>
        <div class="icon_button_close">
          <span
            class="material-symbols-outlined"
            @click="closeSideMenuVisability"
            >close</span
          >
        </div>
      </div>
      <ul class="all_products_list">
        <li
          class="all_pruducts_list_item_wrapper"
          v-for="category in GETMAINCATEGORIES"
          :key="category.id"
        >
          <!-- <span > -->
          <CatalogSideMenu
            v-if="category.attributes.for_side_menu == true"
            :category="category"
            @switchSideMenuVisability="switchSideMenuVisability"
          />
          <!-- </span> -->
        </li>
      </ul>
    </div>
    <!-- </div> -->
    <!-- </teleport> -->
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
.men_catalog {
  /* grid-column: span 2; */
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  padding-top: 20px;
  padding-bottom: 19px;
  padding-left: 24px;
  padding-right: 0px;
  border-right: 1px solid;
  width: 100%;
}

.men_catalog_text {
  font-family: "Golos Ui", sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 500;
}

.men_wrapper_catalog {
  grid-column: span 2;
  display: flex;
  margin-left: -24px;
}

/* .all_products_wrapper {
  position: fixed;
  right: 0;
  left: 0;
  top: 0;
  z-index: 999;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  height: 100vh;
  padding-left: 24px;
  padding-right: 24px;
} */

.all_products_list_wrapper {
  position: fixed;
  left: 0;
  top: 0;
  z-index: 3;
  display: grid;
  grid-template-rows: 64px 1fr;
  list-style: none;
  background-color: #ffffff;
  border-right: 1px solid;
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
  margin-left: -24px;
  padding-bottom: 64px;
  width: 360px;
}

.all_products_list_header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  background-color: #ffffff;
  padding-left: 40px;
  padding-top: 12px;
  padding-right: 8px;
  padding-bottom: 12px;
  border-bottom: 1px solid;
}

.icon_button_close {
  display: flex;
  padding: 8px;
  border-radius: 100px;
}

.all_products_list {
  display: grid;
  grid-auto-rows: minmax(72px, max-content);
  list-style: none;
}

.all_pruducts_list_item_wrapper {
  border-bottom: 1px solid;
}

.all_pruducts_list_item {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  padding-left: 40px;
  padding-top: 8px;
  padding-right: 16px;
  padding-bottom: 8px;
}

.all_pruducts_list_item_image_meta {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.all_pruducts_list_item_image {
  overflow: hidden;
  width: 56px;
  aspect-ratio: 1 / 1;
  margin-right: 16px;
  border-radius: 8px;
}

.all_pruducts_list_item_image img {
  height: 100%;
  object-fit: cover;
}

/* .all_products_wrapper {
  position: fixed;
  right: 0;
  left: 0;
  top: 0;
  z-index: 2;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  height: 100vh;
  padding-left: 24px;
  padding-right: 24px;
} */

/* body {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  height: 100vh;
  padding-left: 24px;
  padding-right: 24px;
} */

/* .all_products_list_wrapper {
  grid-column: span 3;
  position: sticky;
  left: 0;
  top: 0;
  z-index: 3;
  display: grid;
  grid-template-rows: 64px 1fr;
  list-style: none;
  border-right: 1px solid;
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
  margin-left: -24px;
  padding-bottom: 64px;
  background-color: #ffffff;
}

.all_products_list_header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  background-color: #ffffff;
  padding-left: 40px;
  padding-top: 12px;
  padding-right: 8px;
  padding-bottom: 12px;
  border-bottom: 1px solid;
}

.icon_button_close {
  display: flex;
  padding: 8px;
  border-radius: 100px;
}

.all_products_list {
  display: grid;
  grid-auto-rows: minmax(72px, max-content);
  list-style: none;
}

.all_pruducts_list_item_wrapper {
  border-bottom: 1px solid;
}

.all_pruducts_list_item {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  padding-left: 40px;
  padding-top: 8px;
  padding-right: 16px;
  padding-bottom: 8px;
}

.all_pruducts_list_item_image_meta {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.all_pruducts_list_item_image {
  overflow: hidden;
  width: 56px;
  aspect-ratio: 1 / 1;
  margin-right: 16px;
  border-radius: 8px;
}

.all_pruducts_list_item_image img {
  height: 100%;
  object-fit: cover;
} */

/* .catalog {
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
} */
</style>
