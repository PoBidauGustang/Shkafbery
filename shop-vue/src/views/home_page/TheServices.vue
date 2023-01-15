<template>
  <section class="main_base_section main_large_margin">
    <div class="main_services_title">
      <h2 class="main_title">Услуги</h2>
    </div>
    <p class="main_services_description">
      Опытный персонал и современное оборудование гарантируют самое высокое
      качество работ
    </p>
    <ul class="main_services_list">
      <li
        class="main_services_list_item"
        v-for="service in servicesList"
        :key="service.id"
      >
        <div class="base_item_wrapper">
          <router-link
            class="base_item"
            :to="'/category/' + service.attributes.slug"
          >
            <div class="base_item_img_wrapper">
              <img :src="service.attributes.image" />
            </div>
            <div class="base_item_meta_wrapper">
              <h3 class="base_item_title">{{ service.attributes.name }}</h3>
            </div>
          </router-link>
        </div>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: "TheCatalog",
  props: {
    servicesList: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  data() {
    return {};
  },
};
</script>

<style></style>
