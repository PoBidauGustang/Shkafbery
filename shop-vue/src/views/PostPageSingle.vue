<template>
  <div class="blog_page">
    <div class="post_wrapper">
      <div v-if="listPosts.data">
        <h2>{{ listPosts.data.attributes.title }}</h2>
        <p v-html="listPosts.data.attributes.body"></p>
        <img
          :src="require('../assets/images/2.jpeg')"
          alt="img"
          class="Post_Image"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Article",
  components: {},
  props: {},
  data() {
    return {
      listPosts: [],
    };
  },
  created() {
    this.loadListPosts();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerBlogUrl"]),
  },
  methods: {
    async loadListPosts() {
      this.listPosts = await fetch(
        `${this.getServerBlogUrl}/post/${this.$route.params.slug}`
      ).then((response) => response.json());
    },
  },
};
</script>

<style>
.blog_page {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-column-gap: 24px;
  padding-left: 48px;
  padding-right: 48px;
}

.post_wrapper {
  grid-column: 4 / span 6;
}

.post_wrapper img {
  width: 100%;
  height: 100%;
}
</style>
