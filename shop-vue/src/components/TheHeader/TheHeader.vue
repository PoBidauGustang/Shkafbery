<template>
  <div>
    <TheUpperMenu />
    <TheMiddleMenu />
    <TheBottomMenu />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import TheUpperMenu from "./TheUpperMenu.vue";
import TheMiddleMenu from "./TheMiddleMenu.vue";
import TheBottomMenu from "./TheBottomMenu.vue";
export default {
  name: "THeheader",
  components: {
    TheUpperMenu,
    TheMiddleMenu,
    TheBottomMenu,
  },
  created() {
    this.loadCategoriesList();
  },
  props: {},
  data() {
    return {
      categoriesList: [],
      mainCategories: [],
      allCategoriesDict: {},
    };
  },
  watch: {
    categoriesList() {
      this.getMainCategories();
      this.filterAllCategoriesDict();
    },
  },
  computed: {
    ...mapGetters("api_urls", ["getServerShopUrl"]),
  },
  methods: {
    ...mapActions("data", ["saveAllCategories", "saveMainCategories"]),
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
    filterAllCategoriesDict() {
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
  },
};
</script>

<style></style>
