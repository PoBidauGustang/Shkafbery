<template>
  <div>
    <div>{{ faq }}</div>
    <div>
      <TheAboutCompany
        v-for="company in aboutCompany"
        :key="company"
        :company_title="company.attributes.title"
        :company_text="company.attributes.text"
      />
    </div>
    <div>
      <TheWorkExample
        v-for="example in workExamplesList"
        :key="example"
        :example_name="example.attributes.name"
        :example_description="example.attributes.description"
        :example_image="1"
      />
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
import TheFAQ from "./TheFAQ.vue";
import { mapGetters } from "vuex";
export default {
  name: "HomePage",
  components: {
    TheAboutCompany,
    TheWorkExample,
    TheFAQ,
  },
  data() {
    return {
      aboutCompany: [],
      workExamplesList: [],
      faq: [],
    };
  },
  created() {
    this.loadAboutCompany();
    this.loadWorkExamplesList();
    this.loadFaq();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerShopUrl", "getServerInformationUrl"]),
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
  },
};
</script>

<style></style>
