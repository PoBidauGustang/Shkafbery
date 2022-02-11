<template>
  <div>
    <h2>Страница статьи: {{ this.$route.params.slug }} </h2>
    <div>
      {{ listPosts.data.attributes }}
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