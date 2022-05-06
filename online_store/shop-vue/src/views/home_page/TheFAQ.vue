<template>
  <div>
    <h4>{{ question_name }}</h4>
    <p v-html="question"></p>
    <p v-html="question_answer"></p>
  </div>
</template>

<script>
export default {
  name: "TheFAQ",
  props: {
    question_name: {
      type: String,
      default() {
        return "";
      },
    },
    question: {
      type: String,
      default() {
        return "";
      },
    },
    question_answer: {
      type: String,
      default() {
        return "";
      },
    },
  },
  computed: {},
  methods: {},
};
</script>

<style></style>
