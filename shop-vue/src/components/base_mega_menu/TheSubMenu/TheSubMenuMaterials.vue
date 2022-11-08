<template>
  <div
    class="all_product_category_open_wrapper"
    ref="all_product_category_open_wrapper"
  >
    <div class="all_product_category_open_header">Материалы</div>
    <ul class="all_product_category_open_list">
      <li
        class="all_product_category_open_list_item"
        v-for="link in linksList"
        :key="link.id"
        @click="closeSubMenu"
      >
        <router-link class="bottom_menu_link" :to="link.route">
          <span>{{ dataList[link.id].attributes.name }}</span>
          <span>{{ dataList[link.id].attributes.slug }}</span>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "TheSubMenuCloset",
  props: {
    linksList: {
      type: Object,
      default() {
        return {};
      },
    },
    dataList: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  data() {
    return {};
  },
  methods: {
    closeSubMenu() {
      this.$emit("closeSubMenu");
    },
  },
  mounted() {
    let vm = this;
    document.addEventListener("click", function (item) {
      if (item.target === vm.$refs["all_product_category_open_wrapper"]) {
        vm.closeSubMenu();
      }
    });
  },
};
</script>

<style>
.all_product_category_open_wrapper {
  grid-column: 4 / span 9;
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  grid-template-rows: minmax(60px, max-content) 1fr;
}

.all_product_category_open_header {
  grid-row: 1;
  grid-column: span 9;
  display: flex;
  align-items: center;
  width: 100%;
  padding: 16px;
  border-bottom: 1px solid;
}

.all_product_category_open_list {
  grid-row: 2;
  grid-column: span 9;
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  grid-column-gap: 32px;
  list-style: none;
  padding-top: 16px;
  padding-right: 16px;
  padding-left: 16px;
}

.all_product_category_open_list_item {
  grid-column: span 3;
  aspect-ratio: 1 / 1;
  background-color: tomato;
}
</style>
