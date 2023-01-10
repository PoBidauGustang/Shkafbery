<template>
  <div>
    <!-- <p>{{company_title}}</p>
    <p v-html="company_text"></p> -->
    <div>
      <div class="category_img_wrapper">
        <img
          class="category_img"
          src="https://images.unsplash.com/photo-1634712282287-14ed57b9cc89?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1206&q=80"
          alt=""
        />
      </div>
      <div class="catalog_headline_wrapper">
        <h3 class="headline">{{ category_title }}</h3>
      </div>
      <ul class="catalog_link_wrapper">
        <li class="catalog_link_container">
          <a
            class="catalog_link"
            href="/page1"
            v-html="category_data.attributes.name"
          ></a>
        </li>
        <li class="catalog_link_container">
          <a class="catalog_link" href="/page1">Отдельностоящие шкафы-купе</a>
        </li>
        <li class="catalog_link_container">
          <a class="catalog_link" href="/page3">Гардеробные</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "TheAboutCompany",
  props: {
    category_title: {
      type: String,
      default() {
        return "";
      },
    },
    category_data: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  computed: {},
  methods: {},
};
</script>

<style>
.category_img_wrapper {
  aspect-ratio: 16 / 9;
  overflow: hidden;
  border-radius: 12px;
  margin-bottom: 24px;
}

.category_img {
  width: 100%;
  object-fit: cover;
}

.catalog_headline_wrapper {
  margin-bottom: 24px;
}

.catalog_link_wrapper {
  list-style: none;
  padding-left: 0px;
  margin: 0px;
}

.catalog_link_container {
  padding-bottom: 12px;
}

.catalog_link:last-child {
  padding-bottom: 0px;
}

.catalog_link {
  font-family: "PT Root UI", sans-serif;
  font-size: 18px;
  line-height: 28px;
  font-weight: 500;
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 4px;
  text-decoration-color: #95a6fd;
  color: #000000;
}
</style>
