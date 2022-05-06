<template>
  <div>
    <p v-html="company_text"></p>
  </div>
</template>

<script>
export default {
  name: "TheAboutCompany",
  props: {
    // company_title: {
    //   type: String,
    //   default() {
    //     return "";
    //   },
    // },
    company_text: {
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
