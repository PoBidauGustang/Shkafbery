<template>
  <div>
    <div v-if="listPosts.data">
      <h1>{{ listPosts.data.attributes.title }}</h1>
      <p v-html="listPosts.data.attributes.body"></p>
      <img :src=" require('../assets/images/2.jpeg') " alt="img" class="Post_Image">
    </div>
  </div>
</template>

<script>
  export default {
    name: "Article",
    components: {},
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
          `${this.$store.getters.getServerBlogUrl}/post/${this.$route.params.slug}`
        ).then(response => response.json())
      }
    }
  };
</script>

<style scoped>
</style>