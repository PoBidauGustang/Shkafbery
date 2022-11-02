<template>
  <div>
    <TheMenuCatalog
      v-if="isMegaMenuVisibleCatalog"
      :linksList="linksCatalogList"
      :catalogDict="catalogDict"
      @closeMegaMenu="closeMegaMenuCloset"
    />
    <TheMenuCloset
      v-if="isMegaMenuVisibleCloset"
      :linksList="linksClosetList"
      :closetList="closetList"
      @closeMegaMenu="closeMegaMenuCloset"
    />
    <TheMenuDoors
      v-if="isMegaMenuVisibleDoors"
      :linksList="linksDoorsList"
      :doorsList="doorsList"
      @closeMegaMenu="closeMegaMenuDoors"
    />
    <TheMenuMaterials
      v-if="isMegaMenuVisibleMaterials"
      :linksList="linksMaterialsList"
      :materialsList="materialsList"
      @closeMegaMenu="closeMegaMenuMaterials"
    />
    <TheMenuServices
      v-if="isMegaMenuVisibleServices"
      :linksList="linksServicesList"
      :servicesList="servicesList"
      @closeMegaMenu="closeMegaMenuServices"
    />
    <!-- <nav class="header"> -->
    <div class="header_top">
      <ul class="top_menu">
        <li class="top_menu_input">
          <router-link class="top_menu_link" to="/about">О нас</router-link>
        </li>
        <li class="top_menu_input">
          <router-link class="top_menu_link" to="/contacts"
            >Контакты</router-link
          >
        </li>
        <li class="top_menu_input">
          <router-link class="top_menu_link" to="/services"
            >Установка</router-link
          >
        </li>
        <li class="top_menu_input">
          <router-link class="top_menu_link" to="/services">Замеры</router-link>
        </li>
        <li class="top_menu_input">
          <router-link class="top_menu_link" to="/partners"
            >Партнерам</router-link
          >
        </li>
        <li class="top_menu_input">
          <router-link class="top_menu_link" to="/photos"
            >Фото работ</router-link
          >
        </li>
        <li class="top_menu_input">
          <router-link class="top_menu_link" to="/posts">Блог</router-link>
        </li>
      </ul>
      <div class="phone">
        <a class="phone_link" href="/">+7 999 987 78 89</a>
        <div class="phone_info">
          <span class="material-icons-outlined md-18">info</span>
        </div>
      </div>
    </div>
    <div class="header_middle">
      <button class="search">
        <span class="material-icons-outlined md-24">search</span>
      </button>
      <div class="logo">
        <svg
          width="216"
          height="48"
          viewBox="0 0 216 48"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M10.001 40H40.5098V8.64003H35.089V34.7584H27.9658V8.64003H22.545V34.7584H15.4218V8.64003H10.001V40ZM60.3775 40H66.6495L56.8831 22.3041L65.3055 8.64003H58.9438L53.7022 17.824L51.8655 21.4977V8.64003H46.4446V40H51.8655V30.2337L53.7919 27.232L60.3775 40ZM82.4461 40H88.1805L80.4749 8.64003H74.5613L66.8557 40H72.5901L73.8445 34.3104H81.1917L82.4461 40ZM74.9645 29.0688L76.2189 23.2449C76.6669 21.0945 77.1597 17.6448 77.4285 15.5392H77.5629C77.8765 17.6448 78.3693 21.0945 78.8173 23.2449L80.0717 29.0688H74.9645ZM100.875 42.9568H106.34V39.4176H106.967C113.105 39.4176 117.809 35.2512 117.809 27.8145V21.0945C117.809 13.5681 113.105 9.22243 106.967 9.22243H106.34V5.90723H100.875V9.22243H100.247C94.1098 9.22243 89.4058 13.5681 89.4058 21.0945V27.8145C89.4058 35.2512 94.1098 39.4176 100.247 39.4176H100.875V42.9568ZM99.9785 34.1313C97.0666 34.1313 94.9162 32.3392 94.9162 27.8145V21.0945C94.9162 16.3905 97.0666 14.5089 99.9785 14.5089H100.875V34.1313H99.9785ZM106.34 34.1313V14.5089H107.191C110.148 14.5089 112.299 16.3905 112.299 21.0945V27.8145C112.299 32.3392 110.148 34.1313 107.191 34.1313H106.34ZM121.782 40H130.787C137.148 40 140.419 36.864 140.419 30.3681C140.419 24.6784 137.148 20.7808 130.787 20.7808H127.293V13.792H138.672V8.64003H121.782V40ZM127.293 34.7584V25.9329H130.384C133.072 25.9329 134.729 27.3664 134.729 30.3681C134.729 33.4144 133.072 34.7584 130.384 34.7584H127.293ZM150.13 34.8033V26.6049H159.538V21.5872H150.13V13.8369H160.39V8.64003H144.619V40H160.837V34.8033H150.13ZM174.136 8.64003H165.444V40H170.956V29.472H174.136C180.453 29.472 184.171 25.6641 184.171 19.0785C184.171 12.4929 180.453 8.64003 174.136 8.64003ZM174.091 24.2752H170.956V13.8816H174.091C177.048 13.8816 178.527 15.6288 178.527 19.0785C178.527 22.528 177.048 24.2752 174.091 24.2752ZM187.888 40H193.354L199.671 25.5297C200.611 23.3793 201.462 20.8704 202.269 18.72L202.403 18.8544C202.045 22.1697 201.821 27.2769 201.821 30.2337V40H207.197V8.64003H201.687L195.011 23.9616C194.16 25.8432 193.398 27.9936 192.726 29.7408L192.592 29.6512C192.995 26.2464 193.264 21.4977 193.264 18.8992V8.64003H187.888V40Z"
            fill="white"
          />
        </svg>
      </div>
      <div class="navbar_wrapper">
        <router-link class="cart" to="/cart"
          ><span class="material-icons-outlined md-24"
            >shopping_cart</span
          ></router-link
        >
        <a class="cart" href="/"
          ><span class="material-icons-outlined md-24">favorite_border</span></a
        >
      </div>
      <router-link class="login" to="/login"
        ><span class="material-icons-outlined md-24">person</span
        ><span class="login_text">Войти</span></router-link
      >
    </div>
    <!-- <div class="bottom_menu"> -->
    <ul class="bottom_menu">
      <li class="bottom_menu_input">
        <a class="bottom_menu_link" @click="showMegaMenuCatalog">
          <span class="btm_link">Каталог</span
          ><span class="icon_wrapper">
            <span class="material-icons-outlined md-18">expand_more</span>
          </span>
        </a>
      </li>
      <li class="bottom_menu_input">
        <!-- <base-mega-menu/> -->
        <a class="bottom_menu_link" @click="showMegaMenuCloset">
          <span class="btm_link">Шкафы-купе</span>
          <span class="icon_wrapper">
            <span class="material-icons-outlined md-18">expand_more</span>
          </span>
        </a>
      </li>
      <li class="bottom_menu_input">
        <router-link class="bottom_menu_link" to="/wardrobe"
          >Гардеробные</router-link
        >
      </li>
      <li class="bottom_menu_input">
        <a class="bottom_menu_link" @click="showMegaMenuDoors">
          <span class="btm_link">Двери-купе</span>
          <span class="icon_wrapper">
            <span class="material-icons-outlined md-18">expand_more</span>
          </span>
        </a>
      </li>
      <li class="bottom_menu_input">
        <a class="bottom_menu_link" @click="showMegaMenuMaterials">
          <span class="btm_link">Материалы</span
          ><span class="icon_wrapper">
            <span class="material-icons-outlined md-18">expand_more</span>
          </span>
        </a>
      </li>
      <li class="bottom_menu_input">
        <a class="bottom_menu_link" @click="showMegaMenuServices">
          <span class="btm_link">Услуги</span
          ><span class="icon_wrapper">
            <span class="material-icons-outlined md-18">expand_more</span>
          </span>
        </a>
      </li>
      <!-- <li class="bottom_menu_input">
        <router-link class="bottom_menu_link" to="/kitchen">Кухни</router-link>
      </li> -->
    </ul>
    <!-- </div> -->
    <!-- </nav> -->
  </div>
</template>

<script>
import TheMenuCatalog from "./base_mega_menu/TheMenuCatalog.vue";
import TheMenuCloset from "./base_mega_menu/TheMenuCloset.vue";
import TheMenuDoors from "./base_mega_menu/TheMenuDoors.vue";
import TheMenuMaterials from "./base_mega_menu/TheMenuMaterials.vue";
import TheMenuServices from "./base_mega_menu/TheMenuServices.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "THeheader",
  components: {
    TheMenuCatalog,
    TheMenuCloset,
    TheMenuDoors,
    TheMenuMaterials,
    TheMenuServices,
  },
  created() {
    this.loadCategoriesList();
  },
  props: {},
  data() {
    return {
      isMegaMenuVisibleCloset: false,
      isMegaMenuVisibleDoors: false,
      isMegaMenuVisibleMaterials: false,
      isMegaMenuVisibleServices: false,
      isMegaMenuVisibleCatalog: false,
      categoriesList: [],
      mainCategories: [],
      catalogDict: {},
      closetList: [],
      doorsList: [],
      materialsList: [],
      servicesList: [],
      allCategoriesDict: {},
      linksCatalogList: [
        { id: "0", title: "Шкафы-купе", route: "/closets" },
        { id: "1", title: "Гардеробная", route: "/wardrobe" },
        { id: "2", title: "Двери-купе", route: "/doors_closet" },
        { id: "3", title: "Материалы", route: "/materials" },
        { id: "4", title: "Фурнитура", route: "/accessories" },
        { id: "5", title: "Услуги", route: "/services" },
        { id: "6", title: "Кухни", route: "/kitchen" },
      ],
      linksClosetList: [
        {
          id: "0",
          title: "Отдельностоящие шкафы",
          route: "/freestanding_closets",
        },
        { id: "1", title: "Встроенные шкафы", route: "/built-in_closets" },
      ],
      linksDoorsList: [
        // { id: "0", title: "В шкаф", route: "/doors_closet" },
        { id: "0", title: "Двери в гардероб", route: "/doors_dressing_room" },
        { id: "1", title: "Двери в нишу", route: "/doors_opening" },
      ],
      linksMaterialsList: [
        { id: "0", title: "ДСП", route: "/chipboard" },
        { id: "1", title: "Зеркала", route: "/mirror" },
        // { id: "2", title: "Другие", route: "/other" },
      ],
      linksServicesList: [
        { id: "0", title: "Замеры", route: "/measurements" },
        { id: "1", title: "Установка", route: "/installation" },
        { id: "2", title: "Распил", route: "/cutting" },
        { id: "3", title: "Кромкование", route: "/cutting" },
      ],
    };
  },
  watch: {
    categoriesList() {
      this.getMainCategories();
      this.filterAllCategories();
      this.makeCatalogDict();
      this.makeClosetList();
      this.makeDoorsList();
      this.makeMaterialsList();
      this.makeServicesList();
    },
  },
  computed: {
    ...mapGetters("api_urls", ["getServerShopUrl"]),
    ...mapGetters("data", ["GETALLCATEGORIES"]),
  },
  methods: {
    ...mapActions("data", ["saveAllCategories", "saveMainCategories"]),
    makeCatalogDict() {
      this.catalogDict = this.allCategoriesDict;
    },
    makeClosetList() {
      this.closetList = this.allCategoriesDict["Шкаф-купе"];
      this.closetList.sort(function (a, b) {
        if (a.attributes.position > b.attributes.position) {
          return 1;
        }
        if (a.attributes.position < b.attributes.position) {
          return -1;
        }
        return 0;
      });
    },
    makeDoorsList() {
      this.doorsList = this.allCategoriesDict["Двери-купе"];
      this.doorsList.sort(function (a, b) {
        if (a.attributes.position > b.attributes.position) {
          return 1;
        }
        if (a.attributes.position < b.attributes.position) {
          return -1;
        }
        return 0;
      });
    },
    makeMaterialsList() {
      this.materialsList = this.allCategoriesDict["Материалы"];
      this.materialsList.sort(function (a, b) {
        if (a.attributes.position > b.attributes.position) {
          return 1;
        }
        if (a.attributes.position < b.attributes.position) {
          return -1;
        }
        return 0;
      });
    },
    makeServicesList() {
      this.servicesList = this.allCategoriesDict["Услуги"];
      this.servicesList.sort(function (a, b) {
        if (a.attributes.position > b.attributes.position) {
          return 1;
        }
        if (a.attributes.position < b.attributes.position) {
          return -1;
        }
        return 0;
      });
    },
    loadCategoriesList() {
      this.axios
        .get(`${this.getServerShopUrl}/product_categories`)
        .then((response) => {
          this.categoriesList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    getMainCategories() {
      let categoriesList = this.categoriesList.slice();
      for (let category in categoriesList) {
        if (categoriesList[category].attributes.parent === null) {
          this.mainCategories.push(categoriesList[category]);
        }
      }
      this.mainCategories.sort(function (a, b) {
        if (a.attributes.position > b.attributes.position) {
          return 1;
        }
        if (a.attributes.position < b.attributes.position) {
          return -1;
        }
        return 0;
      });
      this.saveMainCategories(this.mainCategories);
    },
    filterAllCategories() {
      // this.allCategories = JSON.parse(JSON.stringify(this.mainCategories));
      // for (let maincategory in this.mainCategories) {
      //   this.allCategories[maincategory].subcategories = [];
      // }
      let valuesList = [];
      for (let maincategory in this.mainCategories) {
        valuesList = [];
        for (let category in this.categoriesList) {
          if (this.categoriesList[category].attributes.parent != null) {
            if (
              Number(this.categoriesList[category].attributes.parent.id) ===
              Number(this.mainCategories[maincategory].id)
            ) {
              valuesList.push(this.categoriesList[category]);
            }
          }
          this.allCategoriesDict[
            this.mainCategories[maincategory].attributes.name
          ] = valuesList;
        }
      }
      this.saveAllCategories(this.allCategoriesDict);
    },
    showMegaMenuCatalog() {
      this.isMegaMenuVisibleServices = false;
      this.isMegaMenuVisibleDoors = false;
      this.isMegaMenuVisibleMaterials = false;
      this.isMegaMenuVisibleCloset = false;
      this.isMegaMenuVisibleCatalog = true;
    },
    closeMegaMenuCatalog() {
      this.isMegaMenuVisibleCatalog = false;
    },
    showMegaMenuCloset() {
      this.isMegaMenuVisibleServices = false;
      this.isMegaMenuVisibleDoors = false;
      this.isMegaMenuVisibleMaterials = false;
      this.isMegaMenuVisibleCloset = true;
      this.isMegaMenuVisibleCatalog = false;
    },
    closeMegaMenuCloset() {
      this.isMegaMenuVisibleCloset = false;
    },
    showMegaMenuDoors() {
      this.isMegaMenuVisibleServices = false;
      this.isMegaMenuVisibleMaterials = false;
      this.isMegaMenuVisibleCloset = false;
      this.isMegaMenuVisibleDoors = true;
      this.isMegaMenuVisibleCatalog = false;
    },
    closeMegaMenuDoors() {
      this.isMegaMenuVisibleDoors = false;
    },
    showMegaMenuMaterials() {
      this.isMegaMenuVisibleServices = false;
      this.isMegaMenuVisibleCloset = false;
      this.isMegaMenuVisibleDoors = false;
      this.isMegaMenuVisibleMaterials = true;
      this.isMegaMenuVisibleCatalog = false;
    },
    closeMegaMenuMaterials() {
      this.isMegaMenuVisibleMaterials = false;
    },
    showMegaMenuServices() {
      this.isMegaMenuVisibleCloset = false;
      this.isMegaMenuVisibleDoors = false;
      this.isMegaMenuVisibleMaterials = false;
      this.isMegaMenuVisibleServices = true;
      this.isMegaMenuVisibleCatalog = false;
    },
    closeMegaMenuServices() {
      this.isMegaMenuVisibleServices = false;
    },
  },
};
</script>

<style>
.header_top {
  display: flex;
  justify-content: space-between;
  background: #1c1c1c;
  padding-left: 40px;
  padding-right: 40px;
}

.top_menu {
  display: flex;
  list-style: none;
  padding-top: 4px;
  padding-bottom: 4px;
  margin: 0px;
  padding-left: 0px;
}

.top_menu_input {
  margin-right: 8px;
}

.top_menu_input:last-child {
  margin-right: 0px;
}

.top_menu_link {
  display: flex;
  border-radius: 8px;
  padding-left: 12px;
  padding-right: 12px;
  padding-top: 6px;
  padding-bottom: 6px;
  text-decoration: none;
  color: #ffffff;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  text-align: center;
}

.top_menu_link:hover {
  background-color: #000000;
}

.phone_link {
  text-decoration: none;
  color: #ffffff;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  text-align: right;
}

.phone {
  display: flex;
  justify-content: center;
  align-items: center;
  color: #ffffff;
  padding-top: 4px;
  padding-bottom: 4px;
}

.phone_info {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  font-variation-settings: "wght" 400, "opsz" 20;
  padding: 4px;
  border-radius: 100px;
}

.phone_info:hover {
  background-color: #000000;
}

.header_middle {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-column-gap: 32px;
  background: #1c1c1c;
  padding-left: 40px;
  padding-right: 40px;
  padding-top: 16px;
  padding-bottom: 16px;
  position: sticky;
  top: 0px;
}

.navbar_wrapper {
  grid-column-start: 9;
  grid-column-end: span 2;
  justify-self: end;
  display: flex;
}

.cart {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  border-radius: 100px;
  padding: 11px;
  text-decoration: none;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.32);
}

.cart:last-child {
  margin-left: 16px;
}

.cart:hover {
  background-color: #000000;
}

.login {
  grid-column-start: 11;
  grid-column-end: span 2;
  justify-self: end;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  text-decoration: none;
  color: #ffffff;
  padding: 11px 15px 11px 11px;
  border: 1px solid rgba(255, 255, 255, 0.32);
  border-radius: 16px;
}

.login:hover {
  background-color: #000000;
}

.login_text {
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  padding-left: 8px;
}

.search {
  grid-column-start: 1;
  justify-self: start;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  background-color: #1c1c1c;
  color: #ffffff;
  border: none;
  border-radius: 100px;
  padding: 12px;
}

.search:hover {
  background-color: #000000;
}

.logo {
  grid-column-start: 5;
  grid-column-end: span 4;
  justify-self: center;
  align-self: center;
}

.bottom_menu {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  list-style: none;
  margin: 0px;
  background-color: #ffffff;
  padding-left: 24px;
  padding-right: 24px;
  height: 60px;
  position: sticky;
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
