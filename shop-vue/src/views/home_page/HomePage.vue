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
    <div>
      <TheAboutCompany
        v-for="company in aboutCompany"
        :key="company"
        :company_title="company.attributes.title"
        :company_text="company.attributes.text"
      />
    </div>
    <div class="catalog">
      <TheCategory
        class="category"
        v-for="category in GETMAINCATEGORIES"
        :key="category"
        :category_title="category.attributes.name"
        :category_data="category"
      />
    </div>
    <section class="products">
      <div class="banner">
        <div class="banner_img_wrapper">
          <img
            class="banner_img"
            src="https://images.unsplash.com/photo-1611486212355-d276af4581c0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
            alt=""
          />
        </div>
        <div class="banner_info">
          <div class="banner_title">
            <h2 class="headline">планировщики шкафа-купе и дверей-купе</h2>
          </div>
          <div class="banner_text">
            <span class="body_large"
              >создайте свой уникальный шкаф-купе или двери-купе, которые будут
              отвечать всем вашим потребностям и идеально впишутся в
              интерьер</span
            >
          </div>
          <div class="banner_btn">
            <router-link to="/closet_planner">
              <button name="button" class="button_filled_li">
                <span class="material-symbols-outlined">edit</span
                ><span class="li_btn_text">Планировать двери</span>
              </button>
            </router-link>
            <router-link to="/closet_planner">
              <button name="button" class="button_filled_li">
                <span class="material-symbols-outlined">edit</span
                ><span class="li_btn_text">Планировать шкаф</span>
              </button>
            </router-link>
          </div>
        </div>
      </div>
    </section>
    <div class="display_work_wrapper">
      <h2 class="display_large">Выполненные работы</h2>
    </div>
    <div class="portfolio">
      <TheWorkExample
        class="work"
        v-for="example in workExamplesList"
        :key="example"
        :example_name="example.attributes.name"
      />
    </div>
    <a class="blog_link" href="/page3"
      ><span class="links_large">Смотреть все работы</span
      ><span class="material-symbols-outlined">arrow_forward</span></a
    >
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
import TheAboutCompany from "./TheAboutCompany.vue";
import TheWorkExample from "./TheWorkExample.vue";
import TheCategory from "./TheCategory.vue";
import TheFAQ from "./TheFAQ.vue";
import NewsCarousel from "./NewsCarousel.vue";
import { mapGetters } from "vuex";
export default {
  name: "HomePage",
  components: {
    TheAboutCompany,
    TheWorkExample,
    TheFAQ,
    TheCategory,
    NewsCarousel,
  },
  data() {
    return {
      aboutCompany: [],
      workExamplesList: [],
      faq: [],
      mainPageHeader: [],
      newsCarousel: [],
    };
  },
  created() {
    this.loadAboutCompany();
    this.loadWorkExamplesList();
    this.loadFaq();
    this.loadMainPageHeader();
    this.loadNewsCarousel();
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
    loadAboutCompany() {
      this.axios
        .get(`${this.getServerInformationUrl}/about_company`)
        .then((response) => {
          this.aboutCompany = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    loadWorkExamplesList() {
      this.axios
        .get(`${this.getServerInformationUrl}/work_examples`)
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
</style>
