<template>
  <div class="product_cart_wrapper">
    <div class="product_cart_headline_wrapper">
      <h1 class="product_cart_headline">Корзина</h1>
    </div>
    <div class="product_cart_form_area">
      <div class="product_cart_form_area_head_wrapper">
        <h2 class="product_cart_form_area_head">Оформление заказа</h2>
      </div>
      <ProductCartForm />
    </div>
    <div class="product_cart_product_area" v-if="isLocalStorage && cartIsReady">
      <div class="product_cart_product_area_header_wrapper">
        <div class="product_cart_product_area_head_wrapper">
          <h2 class="product_cart_product_area_head">Ваш заказ</h2>
          <span class="product_cart_product_area_amount"
            >Товаров: {{ Object.keys(GETALLITEMS).length }}</span
          >
        </div>
        <div>
          <BaseIconButton
            ButtonMeta="Удалить все"
            ButtonIcon="delete"
            @click="removeCart"
          />
        </div>
      </div>
      <ul class="product_cart_products_list_wrapper">
        <li
          class="product_cart_products_list_item"
          v-for="item in GETALLITEMS"
          :key="item.id"
        >
          <CartItem :itemData="item" />
        </li>
      </ul>
      <div>
        <ProductCartOrderList />
      </div>
      <!-- <div>Итого {{ GETALLPRICE }} ₽</div> -->
    </div>
    <div v-else>Корзина пуста</div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import CartItem from "./CartItem.vue";
// import ProductCartInput from './ProductCartInput.vue'
import ProductCartForm from "./ProductCartForm.vue";
import ProductCartOrderList from "./ProductCartOrderList.vue";
import BaseIconButton from "../../components/AllButtons/BaseIconButton.vue";

export default {
  name: "TheCart",
  components: {
    CartItem,
    // ProductCartInput,
    ProductCartForm,
    ProductCartOrderList,
    BaseIconButton,
  },
  data() {
    return {
      orderCompleteVisability: false,
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
    ...mapGetters("cart", ["GETALLITEMS", "GETALLPRICE"]),
    ...mapGetters("auth", ["GETUSER", "GETUSERDATA"]),
    ...mapGetters("api_urls", ["getServerOrdersUrl"]),
  },
  methods: {
    ...mapActions("cart", ["clearCart"]),
    removeCart() {
      this.clearCart();
      this.cartIsReady = false;
    },
    sendOrder() {
      let token = localStorage.getItem("token");
      const options = {
        headers: {
          "Content-Type": "application/json",
          Authorization: "Token " + token,
          Accept: "application/json",
        },
      };
      const data = {
        user: "1",
        full_name: "aaaaaaa aaaaaaaa",
        email: "123ss@sss.com",
        address: "aaaaaaa aaaaaaaa",
        town: "aaaaaaa aaaaaaaa",
        phone: "11111111",
        total_order_price: "11111111",
        payment_option: "наличка",
        billing_status: false,
      };
      this.axios
        .post(`${this.getServerOrdersUrl}/orders_list/`, data, options)
        .then((response) => {
          console.log(response.data.data);
        })
        .catch(function (error) {
          console.error(error);
        });
    },
  },
};
</script>

<style>
.product_cart_wrapper {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  background-color: var(--palette-neutral95);
  padding-left: 24px;
  padding-right: 24px;
  padding-bottom: 64px;
}

.product_cart_headline_wrapper {
  grid-column: span 12;
  grid-row: 1;
  margin-top: 32px;
  margin-bottom: 64px;
}

.product_cart_headline {
  font-family: Akrobat, sans-serif;
  font-size: 64px;
  line-height: 72px;
  font-weight: 800;
  text-align: center;
  text-transform: uppercase;
  color: var(--on-surface-light);
  margin: 0px;
}

.product_cart_form_area {
  grid-row: 2;
  grid-column: span 6;
  display: flex;
  flex-direction: column;
}

.product_cart_form_area_head_wrapper {
  padding-left: 16px;
  padding-right: 16px;
  margin-bottom: 32px;
}

.product_cart_form_area_head {
  font-family: Akrobat, sans-serif;
  font-size: 32px;
  line-height: 40px;
  font-weight: 800;
  text-transform: uppercase;
  color: var(--on-surface-light);
  margin: 0px;
}

.product_cart_product_area {
  grid-row: 2;
  grid-column: 8 / span 5;
  display: flex;
  flex-direction: column;
}

.product_cart_product_area_header_wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-left: 16px;
  padding-right: 4px;
  margin-bottom: 32px;
}

.product_cart_product_area_head_wrapper {
  display: flex;
  align-items: baseline;
}

.product_cart_product_area_head {
  font-family: Akrobat, sans-serif;
  font-size: 32px;
  line-height: 40px;
  font-weight: 800;
  text-transform: uppercase;
  padding-right: 16px;
  color: var(--on-surface-light);
  margin: 0px;
}

.product_cart_product_area_amount {
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--on-surface-variant-light);
}

.product_cart_products_list_wrapper {
  display: flex;
  flex-direction: column;
  list-style: none;
  margin-bottom: 24px;
}

.product_cart_products_list_item {
  border-bottom: 1px solid var(--outline-light);
}

.product_cart_products_list_item:last-child {
  border-bottom: 0px;
}

.product_cart_delete {
  color: var(--on-surface-variant-light);
}

@media (max-width: 1239px) {
  .product_cart_wrapper {
    padding-left: 16px;
    padding-right: 16px;
  }

  .product_cart_headline {
    font-size: 56px;
    line-height: 64px;
  }

  .product_cart_form_area_head {
    font-size: 28px;
    line-height: 36px;
  }

  .product_cart_product_area_head {
    font-size: 28px;
    line-height: 36px;
  }
}

@media (max-width: 904px) {
  .product_cart_wrapper {
    grid-template-columns: repeat(8, 1fr);
  }

  .product_cart_headline {
    grid-column: span 8;
  }

  .product_cart_form_area {
    grid-row: 3;
    grid-column: span 8;
  }

  .product_cart_product_area {
    grid-column: span 8;
    margin-bottom: 64px;
  }
}

@media (max-width: 599px) {
  .product_cart_wrapper {
    grid-template-columns: repeat(4, 1fr);
    padding-left: 0;
    padding-right: 0;
  }

  .product_cart_headline_wrapper {
    margin-bottom: 48px;
  }

  .product_cart_headline {
    grid-column: span 4;
    font-size: 40px;
    line-height: 48px;
  }

  .product_cart_form_area {
    grid-row: 3;
    grid-column: span 4;
  }

  .product_cart_product_area {
    grid-column: span 4;
    margin-bottom: 64px;
  }

  .product_cart_product_area_head_wrapper {
    flex-direction: column;
    row-gap: 4px;
    align-items: flex-start;
  }
}
</style>
