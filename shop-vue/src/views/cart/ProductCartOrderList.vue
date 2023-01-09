<template>
  <div class="product_cart_order_list_wrapper">
    <h3 class="product_cart_order_list_title">Сумма заказа</h3>
    <dl class="product_cart_order_list">
      <div class="product_cart_order_list_meta">
        <dt class="product_cart_order_list_key">Стоимость товаров</dt>
        <dd class="product_cart_order_list_value">{{ GETALLPRICE }} ₽</dd>
      </div>
      <div class="product_cart_order_list_meta">
        <dt class="product_cart_order_list_key">Доставка</dt>
        <dd class="product_cart_order_list_value">1000 ₽</dd>
      </div>
    </dl>
    <dl>
      <output class="product_cart_order_list_total_price">
        <dt class="product_cart_order_list_total_key">Итого</dt>
        <dd class="product_cart_order_list_total_value">
          {{ Number(GETALLPRICE) + 1000 }} ₽
        </dd>
      </output>
    </dl>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Product-Cart-Order-List",
  computed: {
    ...mapGetters("cart", ["GETALLPRICE"]),
  },
};
</script>

<style>
.product_cart_order_list_wrapper {
  padding-left: 16px;
  padding-right: 16px;
}

.product_cart_order_list_title {
  font-weight: 700;
  font-size: 16px;
  line-height: 24px;
  color: var(--on-surface-light);
  margin-bottom: 16px;
}

.product_cart_order_list {
  display: flex;
  flex-direction: column;
  row-gap: 12px;
  margin-bottom: 32px;
}

.product_cart_order_list_meta {
  display: flex;
  justify-content: space-between;
}

.product_cart_order_list_key {
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--on-surface-variant-light);
}

.product_cart_order_list_value {
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  text-align: right;
  color: var(--on-surface-light);
}

.product_cart_order_list_total_price {
  display: flex;
  justify-content: space-between;
  padding-top: 16px;
  border-top: 1px solid var(--outline-light);
}

.product_cart_order_list_total_key {
  font-weight: 500;
  font-size: 24px;
  line-height: 32px;
  color: var(--on-surface-light);
}

.product_cart_order_list_total_value {
  font-weight: 500;
  font-size: 24px;
  line-height: 32px;
  text-align: right;
  color: var(--on-surface-light);
}
</style>
