<template>
  <section class="main_base_section">
    <div class="main_faq_title">
      <h2 class="main_small_title">Часто задаваемые вопросы</h2>
      <a class="main_base_link">
        <span class="main_base_link_1">Смотреть </span
        ><span class="main_base_link_2">все</span>
      </a>
    </div>
    <div class="main_faq_wrapper" v-for="question in faq" :key="question.id">
      <DetailsItem
        :detailsName="question.attributes.question"
        :detailsText="question.attributes.answer"
      />
    </div>
  </section>
</template>

<script>
import DetailsItem from "../../components/AllCards/DetailsItem.vue";

export default {
  name: "TheFAQ",
  components: {
    DetailsItem,
  },
  props: {
    faq: {
      type: Array,
      default() {
        return [];
      },
    },
  },
};
</script>

<style></style>
