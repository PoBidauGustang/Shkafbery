<template>
  <div class="base_item_wrapper">
    <a class="base_item">
      <div class="base_item_img_wrapper">
        <img
          src="https://images.unsplash.com/photo-1567016546367-c27a0d56712e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
          alt=""
        />
      </div>
      <div class="base_item_meta_wrapper">
        <h2 class="base_item_title">
          {{ BaseItemTitile }}
        </h2>
        <p class="base_item_description">
          {{ BaseItemDescription }}
        </p>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  name: "BasetItem",
  props: ["BaseItemTitile", "BaseItemDescription"],
};
</script>

<style scoped>
.base_item {
  display: flex;
  flex-direction: column;
  row-gap: 16px;
}

.base_item_img_wrapper {
  overflow: hidden;
  aspect-ratio: 4 / 2;
  border-radius: 12px;
}
.base_item_img_wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.base_item_meta_wrapper {
  display: flex;
  flex-direction: column;
  row-gap: 4px;
}

.base_item_title {
  font-weight: 700;
  font-size: 18px;
  line-height: 28px;
  color: var(--on-surface-light);
  text-decoration: underline;
  text-decoration-color: var(--primary-light);
}
.base_item:hover .base_item_title {
  color: var(--primary-light);
  text-decoration: none;
}

.base_item_description {
  font-size: 16px;
  line-height: 24px;
  color: var(--on-surface-variant-light);
}
.base_item_description:empty {
  display: none;
}

/* small text */

.base_item_wrapper.small_text .base_item_title {
  font-size: 16px;
  line-height: 24px;
}

.base_item_wrapper.small_text .base_item_description {
  font-size: 14px;
  line-height: 20px;
}

@media (max-width: 1240px) {
  .base_item_title {
    font-size: 16px;
    line-height: 24px;
  }
  .base_item_description {
    font-size: 14px;
    line-height: 20px;
  }
}
</style>
