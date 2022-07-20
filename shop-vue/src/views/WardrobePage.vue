<template>
  <div>
    <h1>Гардеробная</h1>
    <div>{{ wardrobes }}</div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "WardrobePage",
  components: {},
  data() {
    return {
      wardrobes: [],
    };
  },
  created() {
    this.loadWardrobes();
  },
  computed: {
    ...mapGetters("cart", ["GETALLITEMS"]),
    ...mapGetters("api_urls", ["getServerShopUrl"]),
  },
  methods: {
    loadWardrobes() {
      this.axios
        .get(`${this.getServerShopUrl}/products/16`)
        .then((response) => {
          this.wardrobes = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
  },
};
</script>

<style></style>
