<template>
  <div>
    <ul class="bottom_menu">
      <!-- <div @click="close">BUTTON</div>
        <div>Test</div> -->
      <!-- <div>{{ GETMAINCATEGORIES }}</div> -->
      <!-- <div>{{ filteredMainMenuCategories }}</div> -->
      <li class="bottom_menu_input">
        <MenuCatalog />
      </li>
      <li
        class="bottom_menu_input"
        v-for="category in filteredMainMenuCategories"
        :key="category.id"
      >
        <span v-if="category.attributes.for_main_menu == true">
          <MainMenu :category="category" />
        </span>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
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
    ...mapActions("test", ["increment"]),
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
.bottom_menu {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  list-style: none;
  margin: 0px;
  background-color: #ffffff;
  padding-left: 24px;
  padding-right: 24px;
  height: 60px;
  /* position: sticky; */
  top: 80px;
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
}
</style>
