<template>
  <div>
    <h2>Корзина</h2>
    <div v-if="isLocalStorage && cartIsReady">{{ GETALLITEMS }}</div>
    <div v-else>Корзина пуста</div>
    <button @click="removeCart">Очистить корзину</button>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TheCart",
  components: {},
  data() {
    return {
      cartIsReady: true,
      isLocalStorage: localStorage.getItem("cart"),
    };
  },
  mounted() {},
  computed: {
    ...mapGetters("cart", ["GETALLITEMS"]),
  },
  methods: {
    ...mapActions("cart", ["clearCart"]),
    removeCart() {
      this.clearCart();
      this.cartIsReady = false;
    },
  },
};
</script>

<style></style>
