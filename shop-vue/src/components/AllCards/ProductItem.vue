<template>
  <a class="product_item_wrapper">
    <article class="product_item">
      <div class="product_item_controls">
        <IconButton class="add_favorite" IconName="favorite" />
      </div>
      <div class="product_item_img_wrapper">
        <img
          src="https://images.unsplash.com/photo-1567016546367-c27a0d56712e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
          alt=""
        />
      </div>
      <div class="product_item_meta_wrapper">
        <div class="product_item_meta">
          <h3 class="product_item_meta_name">Ящик выдвижной прямой</h3>
          <span class="product_item_meta_description"
            >Ещё 6 вариантов размера, 3 варианта цвета</span
          >
        </div>
        <span class="product_item_meta_price">2280&nbsp;₽</span>
      </div>
    </article>
  </a>
</template>

<script>
import IconButton from "../AllButtons/IconButton.vue";

export default {
  name: "ProductItem",
  components: {
    IconButton,
  },
};
</script>

<style scoped>
.product_item_wrapper {
  display: flex;
  list-style: none;
}
.product_item_wrapper:hover {
  background-color: var(--palette-neutral-variant95);
}

.product_item {
  display: flex;
  flex-direction: column;
  padding-left: 16px;
  padding-right: 16px;
  padding-bottom: 16px;
}

.product_item_controls {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-between;
  align-items: center;
  padding-top: 4px;
  padding-bottom: 4px;
}
.product_item_controls:empty {
  height: 16px;
}

.add_favorite {
  position: relative;
  right: -8px;
}

.product_item_img_wrapper {
  overflow: hidden;
  aspect-ratio: 1 / 1;
  margin-bottom: 16px;
  border-radius: 12px;
}

.product_item_img_wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product_item_meta_wrapper {
  display: flex;
  justify-content: space-between;
  column-gap: 16px;
}

.product_item_meta {
  display: flex;
  flex-direction: column;
}

.product_item_meta_name {
  font-size: 18px;
  line-height: 28px;
  font-weight: 700;
  color: var(--on-surface-light);
  padding-bottom: 4px;
}
.product_item_wrapper:hover .product_item_meta_name {
  text-decoration: underline;
  text-decoration-color: var(--primary-light);
}

.product_item_meta_description {
  font-size: 16px;
  line-height: 24px;
  font-weight: 400;
  color: var(--on-surface-variant-light);
}

.product_item_meta_price {
  font-size: 18px;
  line-height: 28px;
  font-weight: 500;
  color: var(--on-surface-light);
}

@media (max-width: 1240px) {
  .product_item_meta_wrapper {
    flex-direction: column;
    justify-content: flex-start;
    row-gap: 16px;
  }

  .product_item_meta_name {
    font-size: 16px;
    line-height: 24px;
  }

  .product_item_meta_description {
    font-size: 14px;
    line-height: 20px;
  }

  .product_item_meta_price {
    font-size: 16px;
    line-height: 24px;
  }
}
</style>
