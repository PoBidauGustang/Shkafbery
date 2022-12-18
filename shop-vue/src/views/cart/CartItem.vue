<template>
  <div>
    <div>
      <li>
        <p>{{ itemData.item.title }}</p>
        <p>{{ itemData.item.dimensions.value }} мм</p>
        <p>{{ itemData.quantity * itemData.item.price }} ₽</p>
        <!-- <p>{{ price }} ₽</p> -->
      </li>
      <button @click="removeItem({ item: itemData.item, price: priceMinus })">
        -----
      </button>
      <p>{{ itemData.quantity }}</p>
      <!-- <button @click="getPrice()">++++++</button> -->
      <button @click="saveItem({ item: itemData.item, price: pricePlus })">
        ++++++
      </button>
      <!-- <div>item price: {{ itemPrice }}</div> -->
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "CartItem",
  components: {},
  data() {
    return {
      itemPrice: "",
    };
  },
  props: {
    itemData: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  computed: {
    pricePlus() {
      return (this.itemData.quantity + 1) * this.itemData.item.price;
    },
    priceMinus() {
      let result = 0;
      if (this.itemData.quantity > 1) {
        result = (this.itemData.quantity - 1) * this.itemData.item.price;
      } else {
        result = this.itemData.quantity * this.itemData.item.price;
      }
      return result;
    },
  },
  methods: {
    // getPrice() {
    //   this.itemPrice = this.price
    // },
    ...mapActions("cart", ["saveItem", "removeItem"]),
  },
};
</script>

<style></style>
