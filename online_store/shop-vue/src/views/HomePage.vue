<template>
  <div>
    <h2>какая-то информация</h2>
    <div v-for="product in listProducts.data" :key="product.id">
      {{ product.attributes.name }}
    </div>
  </div>
</template>

<script>
  export default {
    name: "HomePage",
    data() {
      return {
        listProducts: []
      }
    },
    components: {},
    created() {
      this.loadListProducts()
    },
    methods: {
      async loadListProducts() {
        this.listProducts = await fetch(
          `${this.$store.getters.getServerShopUrl}/productcategories`
        ).then(response => response.json())
      }
    }
  };
</script>

<style scoped>
</style>
