<template>
  <section class="main_base_section">
    <div class="main_catalog_title">
      <h2 class="main_title">Каталог</h2>
    </div>
    <ul class="main_catalog_list">
      <li
        class="main_catalog_list_item"
        v-for="category in GETMAINCATEGORIES"
        :key="category.id"
      >
        <div class="base_item_wrapper">
          <router-link
            class="base_item"
            :to="'/category/' + category.attributes.slug"
          >
            <div class="base_item_img_wrapper">
              <img :src="category.attributes.image" />
            </div>
            <div class="base_item_meta_wrapper">
              <h3 class="base_item_title">{{ category.attributes.name }}</h3>
            </div>
          </router-link>
        </div>
      </li>
    </ul>
  </section>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "TheCatalog",
  props: {
    news: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters("data", ["GETMAINCATEGORIES"]),
  },
  methods: {},
};
</script>

<style>
.base_item {
  display: flex;
  flex-direction: column;
  row-gap: 16px;
}

.base_item_img_wrapper {
  overflow: hidden;
  aspect-ratio: 4 / 2;
  border-radius: 12px;
}
.base_item_img_wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.base_item_meta_wrapper {
  display: flex;
  flex-direction: column;
  row-gap: 4px;
}

.base_item_title {
  font-weight: 700;
  font-size: 18px;
  line-height: 28px;
  color: var(--on-surface-light);
  text-decoration: underline;
  text-decoration-color: var(--primary-light);
}
.base_item:hover .base_item_title {
  color: var(--primary-light);
  text-decoration: none;
}

.base_item_description {
  font-size: 16px;
  line-height: 24px;
  color: var(--on-surface-variant-light);
}
.base_item_description:empty {
  display: none;
}

/* small text */

.base_item_wrapper.small_text .base_item_title {
  font-size: 16px;
  line-height: 24px;
}

.base_item_wrapper.small_text .base_item_description {
  font-size: 14px;
  line-height: 20px;
}

@media (max-width: 1240px) {
  .base_item_title {
    font-size: 16px;
    line-height: 24px;
  }
  .base_item_description {
    font-size: 14px;
    line-height: 20px;
  }
}
</style>
