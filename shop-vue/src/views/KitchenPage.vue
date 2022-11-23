<template>
  <div>
    <h1>Кухни</h1>
    <!-- <div v-if="TEST">{{ TEST }}</div>
    <div v-else>0</div>
    <button @click="increment">Добавить в тест</button> -->
    <div @click="close">BUTTON</div>
    <div>Test</div>
    <li
      v-for="category in filteredMainMenuCategories"
      :key="category.id"
    >
      <span v-if="category.attributes.for_main_menu==true">
        <TheMenu
          :data="category"
          @click="close"
        />
      </span>
    </li>
  </div>
</template>

<script>
import TheMenu from "../components/base_mega_menu/TheMenu.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Kitchen",
  components: {
    TheMenu,
  },
  data() {
    return {
      visible: false,
      filteredMainMenuCategories: {},
    };
  },
  mounted() {
    this.filterMainMenuCategories();
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
          this.filteredMainMenuCategories[category] = this.GETMAINCATEGORIES[category];
        }
      }
    },
  },
};
</script>
