<template>
  <div class="btm_link">
    <div>
      <div @click="close">BUTTON</div>
      <div>Test</div>
      <!-- <div>{{ GETMAINCATEGORIES }}</div> -->
      <!-- <div>{{ filteredMainMenuCategories }}</div> -->
      <ul
        class="bottom_menu_input"
        v-for="category in filteredMainMenuCategories"
        :key="category.id"
      >
        <span class="btm_link" v-if="category.attributes.for_main_menu == true">
          <MainMenu :data="category" @click="close" />
        </span>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import MainMenu from "./TheMenues/MainMenu.vue";
export default {
  name: "BottomMenu",
  components: {
    MainMenu,
  },
  data() {
    return {
      visible: false,
      filteredMainMenuCategories: {},
    };
  },
  watch: {
    GETMAINCATEGORIES() {
      this.filterMainMenuCategories();
    },
  },
  computed: {
    ...mapGetters("test", ["TEST"]),
    ...mapGetters("data", ["GETMAINCATEGORIES"]),
  },
  methods: {
    ...mapActions("test", ["increment"]),
    close() {
      this.visible = !this.visible;
    },
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
</style>
