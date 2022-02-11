<template>
  <div class='posts-page'>
    <h2>Все посты</h2>
    <div class="v-catalog__list">
      <ThePostView
        v-for="post in listPosts.data"
        :key="post.id"
        :post_data="post.attributes"
      />
    </div>
  </div>
</template>

<script>
  // import {mapActions, mapGetters} from 'vuex'
  import ThePostView from '../components/ThePostView.vue'
  export default {
    name: "posts-page",
    components: {
      ThePostView
    },
    props: {},
    data() {
      return {
        listPosts: []
      }
    },
    created() {
      this.loadListPosts()
    },
    methods: {
      async loadListPosts() {
        this.listPosts = await fetch(
          `${this.$store.getters.getServerBlogUrl}/posts`
        ).then(response => response.json())
      }
    }
  };
</script>

<style>
</style>