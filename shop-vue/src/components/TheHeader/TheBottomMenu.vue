<template>
  <div class="the_bottom_menu">
    <MenuCatalog />
    <!-- <button class="catalog_bottom_menu">
      <span class="material-symbols-outlined">widgets</span>
      <span><MenuCatalog /></span>
    </button> -->
    <ul class="main_menu">
      <li
        class="main_menu_item"
        v-for="category in filteredMainMenuCategories"
        :key="category.id"
      >
        <!-- <span > -->
        <MainMenu
          v-if="category.attributes.for_main_menu == true"
          :category="category"
        />
        <!-- </span> -->
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import MainMenu from "./TheMenues/MainMenu.vue";
import MenuCatalog from "./TheMenues/MenuCatalog.vue";
export default {
  name: "BottomMenu",
  components: {
    MainMenu,
    MenuCatalog,
  },
  data() {
    return {
      filteredMainMenuCategories: {},
    };
  },
  watch: {
    GETMAINCATEGORIES() {
      this.filterMainMenuCategories();
    },
  },
  computed: {
    ...mapGetters("data", ["GETMAINCATEGORIES"]),
  },
  methods: {
    filterMainMenuCategories() {
      for (let category in this.GETMAINCATEGORIES) {
        if (this.GETMAINCATEGORIES[category].attributes.for_main_menu == true) {
          this.filteredMainMenuCategories[category] =
            this.GETMAINCATEGORIES[category];
        }
      }
    },
  },
};
</script>

<style>
.the_bottom_menu {
  /* grid-row: 3; */
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  border-bottom: 1px solid;
  padding-left: 24px;
  padding-right: 24px;
}

.catalog_bottom_menu {
  grid-column: span 2;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "Golos Ui", sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 500;
  padding-top: 20px;
  padding-bottom: 19px;
  padding-left: 24px;
  margin-left: -24px;
  padding-right: 0px;
  border-right: 1px solid;
  gap: 8px;
}

.main_menu {
  grid-column: span 10;
  grid-template-columns: repeat(10, 1fr);
  display: grid;
  list-style: none;
}

.main_menu_item {
  grid-column: span 2;
  border-right: 1px solid;
}

.main_menu_item:last-child {
  border-right: 0px;
  margin-right: -24px;
}

.main_menu_item:last-child a {
  padding-right: 24px;
}

.main_menu_item_link {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  font-family: "Golos Ui", sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 500;
  color: black;
  padding-top: 20px;
  padding-bottom: 19px;
}

/* .bottom_menu {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  list-style: none;
  margin: 0px;
  background-color: #ffffff;
  padding-left: 24px;
  padding-right: 24px;
  height: 60px; */
/* position: sticky; */
/* top: 80px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.32);
}

.bottom_menu_input {
  grid-column: span 1;
  display: grid;
  border-right: 1px solid rgba(0, 0, 0, 0.32);
}

.bottom_menu_input:last-child {
  border-right: 0px;
}

.bottom_menu_input:first-child a {
  margin-left: -24px;
  padding-left: 24px;
}

.bottom_menu_input:last-child a {
  margin-right: -24px;
  padding-right: 24px;
} */
</style>
