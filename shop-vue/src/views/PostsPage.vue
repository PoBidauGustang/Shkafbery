<template>
  <section class="blog_page_area">
    <h1 class="blog_page_title">Блог</h1>
    <the-select
      class="blog_page_select"
      :selected="selected"
      :options="categories"
      @select="sortByCategories"
    />
    <ul class="blog_page_item_list">
      <li class="blog_page_item" v-for="post in filteredPosts" :key="post.id">
        <ThePostView :post_data="post.attributes" />
      </li>
    </ul>
  </section>
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
.blog_page_area {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  padding-left: 24px;
  padding-top: 48px;
  padding-right: 24px;
  padding-bottom: 48px;
}

.blog_page_title {
  grid-column: span 12;
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 64px;
  line-height: 72px;
  text-transform: uppercase;
  text-align: center;
  color: var(--on-surface-light);
  margin-bottom: 48px;
}

.blog_page_select {
  grid-column: span 3;
  grid-row: 2;
  margin: 16px;
}

.blog_page_item_list {
  grid-column: span 12;
  grid-row: 3;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  list-style: none;
}

.blog_page_item {
  grid-column: span 4;
  border-right: 1px solid var(--outline-light);
  border-bottom: 1px solid var(--outline-light);
}

.blog_page_item > div {
  height: 100%;
}

.blog_page_item:first-child {
  margin-left: -24px;
}

.blog_page_item:first-child > div {
  padding-left: 24px;
}

.blog_page_item:nth-child(-n + 3) {
  border-top: 1px solid var(--outline-light);
}

.blog_page_item:nth-child(3n) {
  border-right: 0px;
  margin-right: -24px;
}

.blog_page_item:nth-child(3n) > div {
  padding-right: 24px;
}

.blog_page_item:nth-child(3n + 1) {
  margin-left: -24px;
}

.blog_page_item:nth-child(3n + 1) > div {
  padding-left: 24px;
}
</style>
