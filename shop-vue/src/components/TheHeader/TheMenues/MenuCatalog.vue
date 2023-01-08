<template>
  <div class="men_wrapper_catalog">
    <button class="men_catalog">
      <!-- <span class="">Каталог</span><span class="">
          <span @click="closeSideMenuVisability">Закрыть</span>
        </span> -->
      <span class="material-symbols-outlined">widgets</span
      ><span class="men_catalog_text">Каталог</span>
    </button>
    <!-- <teleport to="body"> -->
    <!-- <div class="all_products_wrapper" v-if="sideMenuVisability"> -->
    <div
      class="all_products_list_backdrop"
      v-if="GETCATALOGSUBMENUVISABILITY"
      @click="closeSideSubMenu"
      @click.stop
    >
      <div class="all_products_list_wrapper" @click.stop>
        <div class="all_products_list_header">
          <div class="icon_button_close">
            <span class="material-symbols-outlined" @click="closeSideSubMenu"
              >close</span
            >
          </div>
          <span class="all_products_list_title">Каталог</span>
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
              @click="
                switchCatalogSubSideMenuVisability(category.attributes.name)
              "
            />
            <!-- </span> -->
          </li>
        </ul>
      </div>
    </div>
    <!-- </div> -->
    <!-- </teleport> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import CatalogSideMenu from "./CatalogSideMenu.vue";
export default {
  name: "MenuCatalog",
  components: {
    CatalogSideMenu,
  },
  data() {
    return {
      // sideMenuVisability: false,
    };
  },
  watch: {},
  computed: {
    ...mapGetters("data", [
      "GETCHILDCATEGORIES",
      "GETMAINCATEGORIES",
      "GETCATALOGSUBMENUVISABILITY",
    ]),
  },
  methods: {
    ...mapActions("data", [
      "switchCatalogSubSideMenuVisability",
      "closeSideSubMenu",
    ]),
    // switchSideMenuVisability() {
    //   this.sideMenuVisability = !this.sideMenuVisability;
    // },
    // closeSideMenuVisability() {
    //   this.sideMenuVisability = false;
    // },
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

.all_products_list_backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 100;
  background-color: rgba(0, 0, 0, 0.8);
}

.all_products_list_wrapper {
  z-index: 101;
  width: 380px;
  display: grid;
  grid-template-rows: 64px 1fr;
  list-style: none;
  background-color: #ffffff;
  border-right: 1px solid;
  height: 100%;
}

.all_products_list_header {
  display: flex;
  flex-direction: row;
  align-items: center;
  column-gap: 8px;
  position: sticky;
  top: 0;
  background-color: #ffffff;
  padding-left: 32px;
  padding-top: 12px;
  padding-right: 8px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--outline-light);
}

.all_products_list_title {
  font-weight: 500;
  font-size: 22px;
  line-height: 28px;
  color: var(--on-surface-light);
}

.icon_button_close {
  display: flex;
  padding: 8px;
  border-radius: 100px;
  color: var(--on-surface-light);
}

.all_products_list {
  display: grid;
  grid-auto-rows: minmax(72px, max-content);
  list-style: none;
  padding-bottom: 24px;
  overflow-y: auto;
  overflow-x: hidden;
}

.all_pruducts_list_item_wrapper {
  border-bottom: 1px solid var(--outline-light);
}

.all_pruducts_list_item {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  color: var(--on-surface-light);
  padding-left: 40px;
  padding-top: 8px;
  padding-right: 16px;
  padding-bottom: 8px;
}

.all_pruducts_list_item_name {
  font-weight: 500;
  font-size: 16px;
  line-height: 24px;
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

@media (max-width: 1239px) {
  .all_products_wrapper {
    bottom: 73px;
  }

  .all_products_list_header {
    padding-left: 24px;
  }

  .all_pruducts_list_item {
    padding-left: 32px;
  }
}

@media (max-width: 904px) {
  .all_products_list_wrapper {
    width: 100vw;
  }

  .all_products_list_header {
    padding-left: 16px;
  }

  .all_pruducts_list_item {
    padding-left: 16px;
  }
}
</style>
