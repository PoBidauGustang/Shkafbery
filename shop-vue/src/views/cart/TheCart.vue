<template>
  <div>
    <h2>Корзина</h2>
    <div>
      <h3>Оформление заказа</h3>
      <div>
        <span>Ваши данные</span>
        <label for="name">Ваше имя</label>
        <input
          type="text"
          id="name"
          name="name"
          required
          v-model="name"
          placeholder="Ваше имя"
        />
        <div>{{ name }}</div>
        <label for="phone">Телефон</label>
        <span>+7 </span>
        <input
          type="tel"
          id="phone"
          name="phone"
          pattern="[0-9]{3}[0-9]{3}[0-9]{2}[0-9]{2}"
          required
          v-model="phone"
          placeholder="Ваш телефон"
        />
        <div>{{ phone }}</div>
        <label for="email">E-mail</label>
        <input
          type="email"
          id="email"
          name="email"
          required
          v-model="email"
          placeholder="Ваша почта"
        />
        <div>{{ email }}</div>
      </div>
      <div>
        <span>Способ доставки</span>
        <div>
          Доставка осуществляется по Санкт-Петербургу и некоторым населенным
          пунктам Ленинградской области. Узнать подробную информацию о зонах и
          условиях доставки можно в разделе доставка
        </div>
        <input type="radio" value="Доставка" id="delivery" v-model="delivery" />
        <label for="delivery">Доставка</label>
        <input
          type="radio"
          value="Самовывоз"
          id="delivery"
          v-model="delivery"
        />
        <label for="delivery">Самовывоз</label>
        <div>выбранный способ доставки: {{ delivery }}</div>
      </div>
      <div>
        <span>Адрес доставки</span>
        <label for="street">Улица</label>
        <input
          type="text"
          id="street"
          name="street"
          required
          v-model="street"
          placeholder="Улица"
        />
        <div>{{ street }}</div>
        <label for="building">Строение</label>
        <input
          type="number"
          id="building"
          name="building"
          required
          v-model="building"
          placeholder="Строение"
        />
        <div>{{ building }}</div>
        <label for="appartment">Квартира / офис</label>
        <input
          type="number"
          id="appartment"
          name="appartment"
          required
          v-model="appartment"
          placeholder="квартира/офис"
        />
        <div>{{ appartment }}</div>
        <input type="submit" value="Перейти к оплате" />
      </div>
    </div>
    <div v-if="isLocalStorage && cartIsReady">
      <h3>Ваш заказ</h3>
      <div>Товаров: {{ Object.keys(GETALLITEMS).length }}</div>
      <div v-for="item in GETALLITEMS" :key="item.id">
        <CartItem :itemData="item" />
      </div>

      <button @click="removeCart">Удалить все</button>
    </div>
    <div v-else>Корзина пуста</div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import CartItem from "./CartItem.vue";
export default {
  name: "TheCart",
  components: {
    CartItem,
  },
  data() {
    return {
      name: "",
      phone: "",
      email: "",
      street: "",
      building: 0,
      appartment: 0,
      delivery: "",
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
