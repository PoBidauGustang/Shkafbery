<template>
  <details class="details_item">
    <summary>{{ detailsName }}</summary>
    <p class="details_text">{{ detailsText }}</p>
  </details>
</template>

<script>
export default {
  name: "DetailsItem",
  props: {
    detailsName: {
      type: String,
      default() {
        return "";
      },
    },
    detailsText: {
      type: String,
      default() {
        return "";
      },
    },
  },
};
</script>

<style scoped>
.details_item {
  background-color: var(--palette-neutral95);
  border-bottom: 1px solid var(--outline-light);
}
.details_item[open] {
  background-color: var(--palette-neutral-variant95);
  padding-bottom: 24px;
}
.details_item:last-child {
  border-bottom: 0px;
}

.details_item summary {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  font-size: 28px;
  line-height: 36px;
  font-weight: 500;
  padding-top: 24px;
  padding-left: 16px;
  padding-right: 16px;
  padding-bottom: 24px;
  color: var(--on-surface-light);
  cursor: pointer;
}
.details_item[open] summary {
  padding-bottom: 16px;
}
.details_item summary::after {
  font-size: 40px;
  font-variation-settings: "OPSZ" 40;
  color: var(--on-surface-light);
  font-family: "Material Symbols Outlined";
  content: "expand_more";
}
.details_item[open] summary::after {
  font-size: 40px;
  font-variation-settings: "OPSZ" 40;
  color: var(--on-surface-light);
  font-family: "Material Symbols Outlined";
  content: "expand_less";
}

.details_text {
  font-size: 18px;
  line-height: 28px;
  color: var(--on-surface-light);
  margin-left: 16px;
  margin-right: 16px;
}
</style>
