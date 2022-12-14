<template>
  <div>
    <div>
      <li>
        <p>{{ itemData.item.title }}</p>
        <p>{{ itemData.item.dimensions.value }} мм</p>
        <p>{{ itemData.quantity * itemData.item.price }} ₽</p>
      </li>
      <button @click="removeItem(itemData.item)">-----</button>
      <p>{{ itemData.quantity }}</p>
      <button @click="saveItem(itemData.item)">++++++</button>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "CartItem",
  components: {},
  data() {
    return {};
  },
  props: {
    itemData: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  methods: {
    ...mapActions("cart", ["saveItem", "removeItem"]),
  },
};
</script>

<style></style>
