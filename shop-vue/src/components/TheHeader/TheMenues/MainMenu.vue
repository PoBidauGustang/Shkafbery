<template>
  <div>
    <!-- <div v-if="category.child_free === true"> -->
    <router-link
      class="main_menu_item_link"
      v-if="category.child_free === true"
      :to="'/category/' + category.attributes.slug"
      >{{ category.attributes.name }}
    </router-link>
    <!-- </div> -->
    <!-- <div v-else @click="switchMainSubMenuVisability"> -->
    <!-- <a class="bottom_menu_link" @click="showMegaMenuCloset"> -->
    <a class="main_menu_item_link" v-else @click="switchMainSubMenuVisability">
      <span class="">{{ category.attributes.name }}</span>
      <!-- <span class=""> -->
      <span class="material-symbols-outlined">expand_more</span>
      <!-- </span> -->
    </a>
    <!-- </div> -->
    <div class="" v-if="mainSubMenuVisible">
      <div class="main_sub_menu_wrapper">
        <ul class="main_sub_menu_open_list">
          <li
            class="main_sub_menu_open_list_item"
            v-for="cat in subCategoriesList"
            :key="cat.id"
          >
            <MainSubMenu
              :categoryData="cat"
              @switchMainSubMenuVisability="switchMainSubMenuVisability"
            />
          </li>
          <li
            v-if="category.id == 6"
            @click="switchMainSubMenuVisability"
            class="main_sub_menu_open_list_item"
          >
            <router-link
              class="main_sub_menu_open_list_product"
              to="/closet_planner"
            >
              <div class="main_sub_menu_open_list_image">
                <img
                  :src="require('../../../assets/images/2.jpeg')"
                  alt="img"
                  class=""
                />
              </div>
              <span>Планировщик шкафа</span>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import MainSubMenu from "./MainSubMenu.vue";
export default {
  name: "MainMenu",
  components: {
    MainSubMenu,
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
      mainSubMenuVisible: false,
    };
  },
  computed: {
    ...mapGetters("data", ["GETCHILDCATEGORIES"]),
  },
  methods: {
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
    switchMainSubMenuVisability() {
      this.mainSubMenuVisible = !this.mainSubMenuVisible;
    },
    turnoffAllMainSubMenuVisability() {
      if (this.mainSubMenuVisible) {
        this.mainSubMenuVisible = false;
      }
    },
  },
  mounted() {
    this.makeSubCategoriesList();
    // let vm = this;
    // document.addEventListener("click", function (item) {
    //   if (item.target === vm.$refs["MegaMenu_wrapper"]) {
    //     vm.closeMegaMenu();
    //   }
    // });
  },
};
</script>

<style>
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

.main_sub_menu_wrapper {
  position: absolute;
  right: 0;
  left: 0;
  top: 185;
  z-index: 2;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-auto-rows: max-content;
  background-color: #f0f0f0;
  padding-bottom: 24px;
  padding-top: 24px;
  padding-left: 24px;
  padding-right: 24px;
}

.main_sub_menu_header {
  grid-column: span 12;
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
}

.icon_button_close {
  display: flex;
  padding: 8px;
  border-radius: 100px;
}

.main_sub_menu_open_list {
  grid-column: span 12;
  grid-row: 2;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-column-gap: 32px;
  grid-auto-rows: max-content;
  grid-row-gap: 32px;
  list-style: none;
  margin-right: 16px;
  margin-left: 16px;
}

.main_sub_menu_open_list_item {
  grid-column: span 3;
}

.main_sub_menu_open_list_product {
  display: flex;
  flex-direction: column;
  padding: 0;
}

.main_sub_menu_open_list_image {
  overflow: hidden;
  aspect-ratio: 4 / 2;
  margin-bottom: 16px;
}

.main_sub_menu_open_list_image img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}

.main_sub_menu_open_all {
  grid-row: 3;
  grid-column: 10;
  margin-top: 32px;
}
/* .bottom_menu_link {
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
} */
</style>
