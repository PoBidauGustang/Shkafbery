<template>
  <div>
    <section class="main_first">
      <div class="main_first_title_wrapper" v-if="mainPageHeader.attributes">
        <h1 class="main_title left">{{ mainPageHeader.attributes.title }}</h1>
        <p class="main_first_description">
          {{ mainPageHeader.attributes.text }}
          <a class="main_first_link" href="#/about">Подробнее о нас</a>
        </p>
      </div>
      <article class="main_first_slider">
        <NewsCarousel :news="newsCarousel" />
      </article>
    </section>
    <TheCatalog />
    <PopularProducts :popularProducts="popularProductsList" />
    <div class="main_large_card" v-if="planner.attributes">
      <article class="large_card">
        <div class="large_card_img_wrapper">
          <img
            v-if="planner.attributes.image"
            class=""
            :src="planner.attributes.image"
            :alt="planner.attributes.alt_text"
          />
        </div>
        <div class="large_card_meta_wrapper">
          <div class="large_card_meta">
            <h2 class="large_card_title">{{ planner.attributes.title }}</h2>
            <p class="large_card_description">{{ planner.attributes.text }}</p>
          </div>
          <a class="large_card_actions" href="#/closet_planner">
            <BaseIconButton
              class="primary"
              ButtonIcon="create"
              ButtonMeta="Начать планирование"
            />
          </a>
        </div>
      </article>
    </div>
    <TheWorkExample :workExamplesList="workExamplesList" />
    <TheServices :servicesList="servicesList" />
    <section class="main_base_section">
      <div class="main_blog_title">
        <h2 class="main_title">Новости</h2>
        <a class="main_base_link" href="#/posts">
          <span class="main_base_link_1">Смотреть </span>
          <span class="main_base_link_2">все</span>
        </a>
      </div>
      <ul class="main_blog_list">
        <li class="main_blog_list_item" v-for="post in newsList" :key="post.id">
          <ThePostView :post_data="post.attributes" />
        </li>
      </ul>
    </section>
    <TheFAQ :faq="faq" />
  </div>
</template>

<script>
import TheWorkExample from "./TheWorkExample.vue";
import TheFAQ from "./TheFAQ.vue";
import NewsCarousel from "./NewsCarousel.vue";
import TheCatalog from "./TheCatalog.vue";
import PopularProducts from "./PopularProducts.vue";
import TheServices from "./TheServices.vue";
import ThePostView from "../../components/ThePostView.vue";
import BaseIconButton from "../../components/AllButtons/BaseIconButton.vue";
import { mapGetters } from "vuex";
export default {
  name: "HomePage",
  components: {
    TheWorkExample,
    TheFAQ,
    NewsCarousel,
    TheCatalog,
    PopularProducts,
    TheServices,
    ThePostView,
    BaseIconButton,
  },
  data() {
    return {
      workExamplesList: [],
      faq: [],
      mainPageHeader: [],
      newsCarousel: [],
      popularProductsList: [],
      planner: [],
      servicesList: [],
      newsList: [],
    };
  },
  created() {
    this.loadWorkExamplesList();
    this.loadFaq();
    this.loadMainPageHeader();
    this.loadNewsCarousel();
    this.loadPopularProductsList();
    this.loadPlanner();
    this.loadServicesList();
    this.loadNewsList();
  },
  computed: {
    ...mapGetters("api_urls", [
      "getServerBlogUrl",
      "getServerShopUrl",
      "getServerInformationUrl",
    ]),
    ...mapGetters("data", ["GETMAINCATEGORIES"]),
  },
  methods: {
    loadWorkExamplesList() {
      this.axios
        .get(`${this.getServerInformationUrl}/work_examples_main`)
        .then((response) => {
          this.workExamplesList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    loadFaq() {
      this.axios
        .get(`${this.getServerInformationUrl}/FAQ`)
        .then((response) => {
          this.faq = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    loadMainPageHeader() {
      this.axios
        .get(`${this.getServerInformationUrl}/main_page_header`)
        .then((response) => {
          this.mainPageHeader = response.data.data[0];
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    loadNewsCarousel() {
      this.axios
        .get(`${this.getServerBlogUrl}/news_carousel`)
        .then((response) => {
          this.newsCarousel = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    loadPopularProductsList() {
      this.axios
        .get(`${this.getServerShopUrl}/popular_products`)
        .then((response) => {
          this.popularProductsList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    loadPlanner() {
      this.axios
        .get(`${this.getServerInformationUrl}/planner`)
        .then((response) => {
          this.planner = response.data.data[0];
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    loadServicesList() {
      this.axios
        .get(`${this.getServerInformationUrl}/services`)
        .then((response) => {
          this.servicesList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    loadNewsList() {
      this.axios
        .get(`${this.getServerBlogUrl}/posts`)
        .then((response) => {
          this.newsList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
  },
};
</script>

<style>
.main_base_section {
  display: grid;
  grid-column: span 12;
  grid-template-columns: repeat(12, 1fr);
  padding-left: 24px;
  padding-right: 24px;
  margin-bottom: 64px;
}
.main_base_section.main_large_margin {
  margin-bottom: 80px;
}

.main_title {
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 64px;
  line-height: 72px;
  text-transform: uppercase;
  text-align: center;
  color: var(--on-surface-light);
  margin-bottom: 48px;
}
.main_title.left {
  text-align: left;
  margin-bottom: 24px;
}

.main_small_title {
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 32px;
  line-height: 40px;
  text-transform: uppercase;
  color: var(--on-surface-light);
  margin-bottom: 32px;
}

.main_base_link {
  font-weight: 500;
  font-size: 16px;
  line-height: 24px;
  color: var(--primary-light);
  text-decoration: none;
}
.main_base_link:hover {
  font-weight: 700;
  text-decoration: underline;
}

/* first screen */

.main_first {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin-bottom: 80px;
}

.main_first_title_wrapper {
  grid-column: 1;
  background-color: var(--palette-neutral98);
  padding-left: 40px;
  padding-top: 48px;
  padding-right: 16px;
  padding-bottom: 16px;
  border-right: 1px solid var(--outline-light);
}

.main_first_description {
  font-size: 24px;
  line-height: 32px;
  color: var(--on-surface-variant-light);
  margin-bottom: 16px;
}

.main_first_link {
  font-weight: 500;
  color: var(--primary-light);
  text-decoration: none;
}
.main_first_link:hover {
  font-weight: 700;
  text-decoration: underline;
}

.main_first_slider {
  grid-column: 2;
  display: flex;
  flex-direction: column;
  background-color: var(--surface-variant-light);
  padding-left: 16px;
  padding-top: 16px;
  padding-right: 40px;
  padding-bottom: 16px;
}

.main_first_slider_img_wrapper {
  overflow: hidden;
  aspect-ratio: 4 / 2;
  border-radius: 12px;
  margin-bottom: 16px;
}

.main_first_slider_img_wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.main_first_meta_wrapper {
  display: flex;
  flex-direction: column;
  row-gap: 4px;
  margin-bottom: 32px;
}

.main_first_slider_title {
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 32px;
  line-height: 40px;
  text-transform: uppercase;
  color: var(--on-surface-light);
}

.main_first_slider_description {
  font-size: 18px;
  line-height: 28px;
  color: var(--on-surface-variant-light);
}

.main_first_slider_description:empty {
  display: none;
}

.main_first_slider_controls {
  display: flex;
  align-items: center;
  column-gap: 24px;
}

/* catalog */

.main_catalog_title {
  grid-column: 2 / span 10;
  padding-left: 16px;
  padding-right: 16px;
}

.main_catalog_list {
  grid-column: 2 / span 10;
  display: grid;
  grid-template-columns: repeat(10, 1fr);
  grid-column-gap: 32px;
  grid-row-gap: 32px;
  list-style: none;
  padding-left: 16px;
  padding-right: 16px;
}

.main_catalog_list_item {
  grid-column: span 2;
}

/* product */

.main_product_title {
  grid-column: span 12;
  padding-left: 16px;
  padding-right: 16px;
}

.main_product_list {
  grid-column: span 12;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  list-style: none;
  margin-bottom: 32px;
}

.main_product_list_item {
  grid-column: span 3;
  border-right: 1px solid var(--outline-light);
  border-bottom: 1px solid var(--outline-light);
}

.main_product_list_item > div {
  height: 100%;
}

.main_product_list_item:first-child {
  margin-left: -24px;
}
.main_product_list_item:first-child > div {
  padding-left: 24px;
}

.main_product_list_item:nth-child(-n + 4) {
  border-top: 1px solid var(--outline-light);
}

.main_product_list_item:nth-child(4n) {
  border-right: 0px;
  margin-right: -24px;
}
.main_product_list_item:nth-child(4n) > div {
  padding-right: 24px;
}

.main_product_list_item:nth-child(4n + 1) {
  margin-left: -24px;
}
.main_product_list_item:nth-child(4n + 1) > div {
  padding-left: 24px;
}

.main_product_button_wrapper {
  grid-column: span 12;
  display: flex;
  justify-content: center;
}

/* card */

.main_large_card {
  margin-left: 40px;
  margin-right: 40px;
  margin-bottom: 64px;
}

/* projects */

.main_project_title {
  grid-column: span 12;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  column-gap: 8px;
  padding-left: 16px;
  padding-right: 16px;
}

.main_project_list {
  grid-column: span 12;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  list-style: none;
}

.main_project_list_item {
  grid-column: span 6;
  border-right: 1px solid var(--outline-light);
  border-bottom: 1px solid var(--outline-light);
}

.main_project_list_item > div {
  height: 100%;
}

.main_project_list_item:first-child {
  margin-left: -24px;
}
.main_project_list_item:first-child > div {
  padding-left: 24px;
}

.main_project_list_item:nth-child(-n + 2) {
  border-top: 1px solid var(--outline-light);
}

.main_project_list_item:nth-child(2n) {
  border-right: 0px;
  margin-right: -24px;
}
.main_project_list_item:nth-child(2n) > div {
  padding-right: 24px;
}

.main_project_list_item:nth-child(2n + 1) {
  margin-left: -24px;
}
.main_project_list_item:nth-child(2n + 1) > div {
  padding-left: 24px;
}

/* services */

.main_services_title {
  grid-column: 2 / span 10;
  padding-left: 16px;
  padding-right: 16px;
}

.main_services_description {
  grid-row: 2;
  grid-column: 2 / span 4;
  font-size: 24px;
  line-height: 32px;
  color: var(--on-surface-light);
  padding-left: 16px;
  padding-right: 16px;
}

.main_services_list {
  grid-row: 2;
  grid-column: 6 / span 6;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-column-gap: 32px;
  grid-row-gap: 32px;
  list-style: none;
  padding-left: 16px;
  padding-right: 16px;
}

.main_services_list_item {
  grid-column: span 3;
}

/* blog */

.main_blog_title {
  grid-column: span 12;
  position: relative;
  padding-left: 16px;
  padding-right: 16px;
}

.main_blog_title > a {
  position: absolute;
  right: 16px;
  top: 38px;
}

.main_blog_list {
  grid-column: span 12;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  list-style: none;
}

.main_blog_list_item {
  grid-column: span 4;
  border-right: 1px solid var(--outline-light);
  border-bottom: 1px solid var(--outline-light);
}
.main_blog_list_item > div {
  height: 100%;
}

.main_blog_list_item:first-child {
  margin-left: -24px;
}
.main_blog_list_item:first-child > div {
  padding-left: 24px;
}

.main_blog_list_item:nth-child(-n + 3) {
  border-top: 1px solid var(--outline-light);
}

.main_blog_list_item:nth-child(3n) {
  border-right: 0px;
  margin-right: -24px;
}
.main_blog_list_item:nth-child(3n) > div {
  padding-right: 24px;
}

.main_blog_list_item:nth-child(3n + 1) {
  margin-left: -24px;
}
.main_blog_list_item:nth-child(3n + 1) > div {
  padding-left: 24px;
}

/* faq */

.main_faq_title {
  grid-column: 2 / span 10;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  column-gap: 8px;
  padding-left: 16px;
  padding-right: 16px;
}

.main_faq_wrapper {
  grid-column: 2 / span 10;
}

/* planner */

.large_card {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  background-color: var(--surface-dark);
  overflow: hidden;
  border-radius: 24px;
}

.large_card_img_wrapper {
  grid-column: 1;
  overflow: hidden;
  aspect-ratio: 4 / 2;
  width: 100%;
}

.large_card_img_wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.large_card_meta_wrapper {
  grid-column: 2;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 16px;
}

.large_card_meta {
  display: flex;
  flex-direction: column;
  row-gap: 16px;
}

.large_card_title {
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 64px;
  line-height: 72px;
  text-transform: uppercase;
  color: var(--on-surface-dark);
}

.large_card_description {
  font-size: 24px;
  line-height: 32px;
  color: var(--on-surface-variant-dark);
}

.large_card_actions {
  display: flex;
  justify-content: end;
  align-self: end;
  column-gap: 8px;
}
</style>
