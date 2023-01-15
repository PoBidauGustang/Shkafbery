<template>
  <section class="faq_page">
    <h1 class="faq_title">Часто задаваемые вопросы</h1>
    <div class="faq_wrapper" v-for="question in faq" :key="question.id">
      <DetailsItem
        :detailsName="question.attributes.question"
        :detailsText="question.attributes.answer"
      />
    </div>
  </section>
</template>

<script>
import DetailsItem from "../components/AllCards/DetailsItem.vue";
import { mapGetters } from "vuex";
export default {
  name: "FaqPage",
  components: {
    DetailsItem,
  },
  data() {
    return {
      faq: [],
    };
  },
  created() {
    this.loadFaq();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerInformationUrl"]),
  },
  methods: {
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
  },
};
</script>

<style>
.faq_page {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  padding-top: 48px;
  padding-left: 24px;
  padding-right: 24px;
  padding-bottom: 48px;
}

.faq_title {
  grid-column: 2 / span 10;
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 32px;
  line-height: 40px;
  text-transform: uppercase;
  color: var(--on-surface-light);
  padding-left: 16px;
  padding-right: 16px;
  margin-bottom: 32px;
}

.faq_wrapper {
  grid-column: 2 / span 10;
}
</style>
