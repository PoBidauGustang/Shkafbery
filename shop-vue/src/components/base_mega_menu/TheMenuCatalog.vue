<template>
  <div class="all_products_wrapper" ref="all_products_wrapper">
    <TheSubMenuCloset
      v-if="isSubMenuVisibleCloset"
      :linksList="linksClosetList"
      :dataList="closetList"
      @closeSubMenu="closeSubMenu"
    />
    <TheSubMenuDoors
      v-if="isSubMenuVisibleDoors"
      :linksList="linksDoorsList"
      :dataList="doorsList"
      @closeSubMenu="closeSubMenu"
    />
    <TheSubMenuMaterials
      v-if="isSubMenuVisibleMaterials"
      :linksList="linksMaterialsList"
      :dataList="materialsList"
      @closeSubMenu="closeSubMenu"
    />
    <TheSubMenuServices
      v-if="isSubMenuVisibleServices"
      :linksList="linksServicesList"
      :dataList="servicesList"
      @closeSubMenu="closeSubMenu"
    />
    <TheSubMenuAccessories
      v-if="isSubMenuVisibleAccessories"
      :linksList="linksAccessoriesList"
      :dataList="accessoriesList"
      @closeSubMenu="closeSubMenu"
    />
    <ul class="all_products_list">
      <li class="all_pruducts_list_item">
        <div>Каталог</div>
        <div @click="closeMegaMenu">Закрыть</div>
      </li>
      <li class="all_pruducts_list_item">
        <a @click="showSubMenuCloset">
          <span>{{ linksList[0].title }}</span>
        </a>
      </li>
      <li class="all_pruducts_list_item">
        <router-link :to="linksList[1].route">
          <span @click="closeMegaMenu">{{ linksList[1].title }}</span>
        </router-link>
      </li>
      <li class="all_pruducts_list_item">
        <a @click="showSubMenuDoors">
          <span>{{ linksList[2].title }}</span>
        </a>
      </li>
      <li class="all_pruducts_list_item">
        <a @click="showSubMenuMaterials">
          <span>{{ linksList[3].title }}</span>
        </a>
      </li>
      <li class="all_pruducts_list_item">
        <a @click="showSubMenuAccessories">
          <span>{{ linksList[4].title }}</span>
        </a>
      </li>
      <li class="all_pruducts_list_item">
        <a @click="showSubMenuServices">
          <span>{{ linksList[5].title }}</span>
        </a>
      </li>
      <li class="all_pruducts_list_item">
        <router-link :to="linksList[6].route">
          <span @click="closeMegaMenu">{{ linksList[6].title }}</span>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import TheSubMenuCloset from "./TheSubMenu/TheSubMenuCloset.vue";
import TheSubMenuDoors from "./TheSubMenu/TheSubMenuDoors.vue";
import TheSubMenuMaterials from "./TheSubMenu/TheSubMenuMaterials.vue";
import TheSubMenuServices from "./TheSubMenu/TheSubMenuServices.vue";
import TheSubMenuAccessories from "./TheSubMenu/TheSubMenuAccessories.vue";
export default {
  name: "TheMenuCatalog",
  components: {
    TheSubMenuCloset,
    TheSubMenuDoors,
    TheSubMenuMaterials,
    TheSubMenuServices,
    TheSubMenuAccessories,
  },
  props: {
    linksList: {
      type: Object,
      default() {
        return {};
      },
    },
    catalogDict: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      isSubMenuVisibleCloset: false,
      isSubMenuVisibleDoors: false,
      isSubMenuVisibleMaterials: false,
      isSubMenuVisibleServices: false,
      isSubMenuVisibleAccessories: false,
      closetList: [],
      doorsList: [],
      materialsList: [],
      servicesList: [],
      accessoriesList: [],
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
      linksAccessoriesList: [
        { id: "0", title: "Полки", route: "/shelfs" },
        { id: "1", title: "Ящики", route: "/box" },
      ],
    };
  },
  watch: {
    isSubMenuVisibleCloset() {
      this.makeClosetList();
    },
    isSubMenuVisibleDoors() {
      this.makeDoorsList();
    },
    isSubMenuVisibleMaterials() {
      this.makeMaterialsList();
    },
    isSubMenuVisibleServices() {
      this.makeServicesList();
    },
    isSubMenuVisibleAccessories() {
      this.makeAccessoriesList();
    },
  },
  computed: {
    ...mapGetters("data", ["GETALLCATEGORIES", "GETMAINCATEGORIES"]),
  },
  methods: {
    closeMegaMenu() {
      this.$emit("closeMegaMenu");
    },
    makeClosetList() {
      this.closetList = this.GETALLCATEGORIES["Шкаф-купе"];
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
      this.doorsList = this.GETALLCATEGORIES["Двери-купе"];
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
      this.materialsList = this.GETALLCATEGORIES["Материалы"];
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
      this.servicesList = this.GETALLCATEGORIES["Услуги"];
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
    makeAccessoriesList() {
      this.accessoriesList = this.GETALLCATEGORIES["Фурнитура"];
      this.accessoriesList.sort(function (a, b) {
        if (a.attributes.position > b.attributes.position) {
          return 1;
        }
        if (a.attributes.position < b.attributes.position) {
          return -1;
        }
        return 0;
      });
    },
    showSubMenuCloset() {
      this.isSubMenuVisibleServices = false;
      this.isSubMenuVisibleDoors = false;
      this.isSubMenuVisibleMaterials = false;
      this.isSubMenuVisibleCloset = true;
      this.isSubMenuVisibleAccessories = false;
    },
    showSubMenuDoors() {
      this.isSubMenuVisibleServices = false;
      this.isSubMenuVisibleDoors = true;
      this.isSubMenuVisibleMaterials = false;
      this.isSubMenuVisibleCloset = false;
      this.isSubMenuVisibleAccessories = false;
    },
    showSubMenuMaterials() {
      this.isSubMenuVisibleServices = false;
      this.isSubMenuVisibleDoors = false;
      this.isSubMenuVisibleMaterials = true;
      this.isSubMenuVisibleCloset = false;
      this.isSubMenuVisibleAccessories = false;
    },
    showSubMenuServices() {
      this.isSubMenuVisibleServices = true;
      this.isSubMenuVisibleDoors = false;
      this.isSubMenuVisibleMaterials = false;
      this.isSubMenuVisibleCloset = false;
      this.isSubMenuVisibleAccessories = false;
    },
    showSubMenuAccessories() {
      this.isSubMenuVisibleServices = false;
      this.isSubMenuVisibleDoors = false;
      this.isSubMenuVisibleMaterials = false;
      this.isSubMenuVisibleCloset = false;
      this.isSubMenuVisibleAccessories = true;
    },
    closeSubMenu() {
      this.closeMegaMenu();
      this.isSubMenuVisibleServices = false;
      this.isSubMenuVisibleDoors = false;
      this.isSubMenuVisibleMaterials = false;
      this.isSubMenuVisibleCloset = false;
      this.isSubMenuVisibleAccessories = false;
    },
  },
  mounted() {
    let vm = this;
    document.addEventListener("click", function (item) {
      if (item.target === vm.$refs["all_products_wrapper"]) {
        vm.closeMegaMenu();
      }
    });
  },
};
</script>

<style>
.all_products_wrapper {
  position: fixed;
  right: 0;
  left: 0;
  top: 120px;
  bottom: 30px;
  width: 80vw;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  margin-right: 24px;
  margin-left: 24px;
  background: rgba(64, 64, 64, 0.4);
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
