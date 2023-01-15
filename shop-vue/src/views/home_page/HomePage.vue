<template>
  <div>
    <div v-if="mainPageHeader.attributes">
      <h2>{{ mainPageHeader.attributes.title }}</h2>
      <span>{{ mainPageHeader.attributes.text }}</span>
      <a class="blog_link" href="#/about">
        <button>Узнать больше</button>
      </a>
    </div>
    <NewsCarousel :news="newsCarousel" />
    <TheCatalog />
    <PopularProducts :popularProducts="popularProductsList" />
    <div v-if="planner.attributes">
      <h2>{{ planner.attributes.title }}</h2>
      <span>{{ planner.attributes.text }}</span>
      <img
        v-if="planner.attributes.image"
        class=""
        :src="planner.attributes.image"
        :alt="planner.attributes.alt_text"
      />
      <a class="blog_link" href="#/closet_planner">
        <button>Начать планирование</button>
      </a>
    </div>
    <TheWorkExample class="portfolio" :workExamplesList="workExamplesList" />
    <TheServices :servicesList="servicesList" />
    <ThePostView
      class="Post_Page"
      v-for="post in newsList"
      :key="post.id"
      :post_data="post.attributes"
    />
    <!-- <TheAboutCompany
      v-for="company in aboutCompany"
      :key="company"
      :company_title="company.attributes.title"
      :company_text="company.attributes.text"
    /> -->
    <div>
      <TheFAQ
        v-for="question in faq"
        :key="question"
        :question_name="question.attributes.name"
        :question="question.attributes.question"
        :question_answer="question.attributes.answer"
      />
    </div>
  </div>
</template>

<script>
// import TheAboutCompany from "./TheAboutCompany.vue";
import TheWorkExample from "./TheWorkExample.vue";
// import TheCategory from "./TheCategory.vue";
import TheFAQ from "./TheFAQ.vue";
import NewsCarousel from "./NewsCarousel.vue";
import TheCatalog from "./TheCatalog.vue";
import PopularProducts from "./PopularProducts.vue";
import TheServices from "./TheServices.vue";
import ThePostView from "../../components/ThePostView.vue";
import { mapGetters } from "vuex";
export default {
  name: "HomePage",
  components: {
    // TheAboutCompany,
    TheWorkExample,
    TheFAQ,
    // TheCategory,
    NewsCarousel,
    TheCatalog,
    PopularProducts,
    TheServices,
    ThePostView,
  },
  data() {
    return {
      // aboutCompany: [],
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
    // this.loadAboutCompany();
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
    // loadAboutCompany() {
    //   this.axios
    //     .get(`${this.getServerInformationUrl}/about_company`)
    //     .then((response) => {
    //       this.aboutCompany = response.data.data;
    //     })
    //     .catch(function (error) {
    //       console.error(error);
    //     });
    // },
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
.catalog {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-column-gap: 32px;
  padding-left: 40px;
  padding-right: 40px;
}

.category {
  grid-column: span 4;
  display: flex;
  flex-direction: column;
  margin-bottom: 64px;
}

.products {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-column-gap: 32px;
  padding-left: 40px;
  padding-right: 40px;
  margin-bottom: 120px;
}

.banner {
  grid-column: span 12;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-column-gap: 32px;
  background-color: #f0eef1;
  color: #000000;
  border-radius: 12px;
}

.banner_img_wrapper {
  grid-column: span 6;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  border-radius: 12px;
}

.banner_img {
  width: 100%;
  object-fit: cover;
}

.banner_info {
  grid-column: span 6;
  display: grid;
  grid-auto-rows: max-content max-content 1fr;
  padding-top: 32px;
  padding-right: 16px;
  padding-bottom: 16px;
}

.banner_title {
  grid-row: 1;
  padding-bottom: 24px;
}

.banner_text {
  grid-row: 2;
  padding-bottom: 32px;
}

.banner_btn {
  grid-row: 3;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  place-self: end;
}

.button_filled_li {
  align-self: flex-end;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 10px 24px 10px 16px;
  font-family: "PT Root UI", sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 500;
  font-variation-settings: "wght" 400;
  color: #000000;
  background: #f0eef1;
  border-radius: 100px;
  border: 1px solid #000000;
}

.li_btn_text {
  padding-left: 8px;
}

@media (any-hover: hover) {
  .button_filled_li:hover {
    background-color: #303030;
    transition: background-color 0.1s linear;
    font-weight: 700;
    font-variation-settings: "wght" 600;
  }
}

.button_filled_li:active {
  background-color: #1d1d1d;
  transition: background-color 0.1s linear;
  font-weight: 700;
}

.button_filled_li:first-child {
  margin-right: 8px;
}

.portfolio {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-column-gap: 32px;
  padding-left: 40px;
  padding-right: 40px;
  margin-bottom: 120px;
}

.display_work_wrapper {
  grid-column: span 12;
  margin-bottom: 48px;
  text-align: center;
}

.work {
  grid-column: span 3;
  grid-row: 2;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background-color: #1c1c1c;
  color: #ffffff;
  padding-bottom: 16px;
  border-radius: 12px;
  margin-bottom: 64px;
}

.Post_Page {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-column-gap: 24px;
  background: #f6f3f3;
  padding-left: 48px;
  padding-right: 48px;
  padding-top: 48px;
}
</style>
