<template>
  <div>
    <!-- <p>{{company_title}}</p>
    <p v-html="company_text"></p> -->
    <section class="first">
      <div class="first_dislplay_wrapper">
        <h2 class="display_large">{{ company_title }}</h2>
      </div>
      <div class="first_text">
        <span class="head_text_large" v-html="company_text"></span>
      </div>
      <div class="first_img_wrapper">
        <img
          class="first_img"
          src="https://images.unsplash.com/photo-1567016546367-c27a0d56712e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
          alt=""
        />
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "TheAboutCompany",
  props: {
    company_title: {
      type: String,
      default() {
        return "";
      },
    },
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

<style>
.first {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-column-gap: 32px;
  height: calc(100vh - 180px);
  padding-left: 40px;
  padding-right: 40px;
  margin-bottom: 80px;
}

.first_dislplay_wrapper {
  grid-column: span 2;
  text-align: center;
  margin-top: 48px;
  margin-bottom: 48px;
}

.first_text {
  grid-row: 2;
  grid-column: 1;
}

.first_img_wrapper {
  grid-row: 2;
  grid-column: 2;
  overflow: hidden;
  border-radius: 16px;
  margin-bottom: 16px;
}

.first_img {
  width: 100%;
  object-fit: cover;
}
</style>
