<template>
  <div>
    <div v-if="category.child_free === true">
      <router-link
        class="bottom_menu_link"
        :to="'/category/' + category.attributes.slug"
        >{{ category.attributes.name }}</router-link
      >
    </div>
    <div v-else @click="switchMainSubMenuVisability">
      <!-- <a class="bottom_menu_link" @click="showMegaMenuCloset"> -->
      <a class="bottom_menu_link">
        <span class="btm_link">{{ category.attributes.name }}</span>
        <span class="icon_wrapper">
          <span class="material-icons-outlined md-18">expand_more</span>
        </span>
      </a>
    </div>
    <div class="MegaMenu_wrapper" v-if="mainSubMenuVisible">
      <div class="MegaMenu">
        <ul class="MegaMenu_List">
          <li class="MegaMenu_Category" v-for="cat in dataList" :key="cat.id">
            <MainSubMenu
              :categoryData="cat"
              @switchMainSubMenuVisability="switchMainSubMenuVisability"
            />
          </li>
          <li
            v-if="category.id == 6"
            @click="switchMainSubMenuVisability"
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
    <!-- <div v-if="category.attributes.id == '6'" class="Mega_Menu_Conf">
      <router-link
        class="bottom_menu_link"
        to="/closet_planner"
      >
        <span class="MegaMenu_input">Планировщик шкафа</span>
        <div class="Mega_Menu_Image_Wrapper">
          <img
            :src="require('../../../assets/images/2.jpeg')"
            alt="img"
            class="MegaMenu_Image"
          />
        </div>
      </router-link>
    </div> -->
    <!-- <div>{{ dataList[0] }}</div>  -->
    <!-- <ul class="MegaMenu_List">
        <li
          class="MegaMenu_Category"
          v-for="link in linksList"
          :key="link.id"
          @click="closeMegaMenu"
        >
          <router-link class="bottom_menu_link" :to="link.route">
            <span class="MegaMenu_input">{{ link.title }}</span>
            <span class="MegaMenu_input">{{
              closetList[link.id].attributes.name
            }}</span>
            <div class="Mega_Menu_Image_Wrapper">
              <img
                :src="require('../../assets/images/2.jpeg')"
                alt="img"
                class="MegaMenu_Image"
              />
            </div>
          </router-link>
        </li>
      </ul>
      <div class="Mega_Menu_Conf">
        <router-link
          @click="closeMegaMenu"
          class="bottom_menu_link"
          to="/closet_planner"
        >
          <span class="MegaMenu_input">Планировщик шкафа</span>
          <div class="Mega_Menu_Image_Wrapper">
            <img
              :src="require('../../assets/images/2.jpeg')"
              alt="img"
              class="MegaMenu_Image"
            />
          </div>
        </router-link>
      </div> -->
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
    // closetList: {
    //   type: Array,
    //   default() {
    //     return [];
    //   },
    // },
  },
  data() {
    return {
      dataList: [],
      mainSubMenuVisible: false,
    };
  },
  computed: {
    ...mapGetters("data", ["GETCHILDCATEGORIES"]),
  },
  methods: {
    makeDataList() {
      this.dataList = this.GETCHILDCATEGORIES[this.category.attributes.name];
      this.dataList.sort(function (a, b) {
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
    this.makeDataList();
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
</style>
