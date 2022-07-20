<template>
  <div>
    <h2>Корзина</h2>
    <div>{{ GETALLITEMS }}</div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "TheCart",
  components: {},
  data() {
    return {
      // aboutCompany: [],
    };
  },
  created() {
    // this.loadAboutCompany();
  },
  computed: {
    ...mapGetters("cart", ["GETALLITEMS"]),
  },
  methods: {
    // loadAboutCompany() {
    //   this.axios
    //     .get(`${this.getServerInformationUrl}/about_company`)
    //     .then((response) => {
    //       this.aboutCompany = response.data.data;
    //     })
    //     .catch(function (error) {
    //       console.error(error);
    //     });
    // },
  },
};
</script>

<style></style>
