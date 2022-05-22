<template>
  <div>
    <the-select
      :selected="selected"
      :options="categories"
      @select="sortByCategories"
    />
    <div class="Post_Page">
      <ThePostView
        v-for="post in filteredPosts"
        :key="post.id"
        :post_data="post.attributes"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import ThePostView from "../components/ThePostView.vue";
import TheSelect from "../components/TheSelect.vue";
export default {
  name: "posts-page",
  components: {
    ThePostView,
    TheSelect,
  },
  props: {},
  data() {
    return {
      listPosts: [],
      categories: [
        { name: "Все", value: 1 },
        { name: "Новости", value: 1 },
        { name: "Статьи", value: 2 },
      ],
      selected: "Все",
      sortedPosts: [],
    };
  },
  created() {
    this.loadListPosts();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerBlogUrl"]),
    filteredPosts() {
      if (this.sortedPosts.length) {
        return this.sortedPosts;
      } else {
        return this.listPosts.data;
      }
    },
  },
  methods: {
    sortByCategories(category) {
      this.sortedPosts = [];
      this.listPosts.data.map((post) => {
        if (post.attributes.category[0].name === category.name) {
          console.log(post);
          this.sortedPosts.push(post);
        }
      });
      this.selected = category.name;
    },

    async loadListPosts() {
      this.listPosts = await fetch(`${this.getServerBlogUrl}/posts`).then(
        (response) => response.json()
      );
    },
  },
};
</script>

<style>
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
