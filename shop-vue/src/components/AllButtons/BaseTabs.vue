<template>
  <div>
    <!-- <a class="tab_item">
        <span class="material-symbols-outlined">{{ TabIcon }}</span>
        <span class="tab_name">{{ TabName }}</span>
    </a> -->
    <button
      class="tab_item"
      v-for="tab in tabs"
      :key="tab"
      :class="['tab_item', { current: currentTab === tab }]"
      @click="currentTab = tab"
    >
      <span class="material-symbols-outlined">{{ TabIcon }}</span>
      <span class="tab_name">{{ tab }}</span>
    </button>
  </div>
</template>

<script>
export default {
  name: "BaseTabs",
  data() {
    return {
      currentTab: "Готовые",
      tabs: ["Готовые", "На заказ", "Планировщик"],
    };
  },
};
</script>

<style scoped>
.tab_item {
  flex: 1;
  display: flex;
  flex-direction: row;
  column-gap: 8px;
  align-items: center;
  justify-content: center;
  color: var(--on-surface-variant-light);
  background-color: transparent;
  padding-top: 20px;
  padding-bottom: 20px;
  border-radius: 16px;
  cursor: pointer;
}

.tab_item:last-child {
  border-right: 0;
}

.tab_name {
  font-size: 16px;
  line-height: 24px;
}

.tab_item .material-symbols-outlined {
  transition: font-weight 0.5s ease, font-variation-settings 0.5s ease,
    transform 0.5s ease;
}

.tab_item .tab_name {
  transition: font-weight 0.5s ease;
}

/* hover */
.tab_item:hover {
  background-color: var(--palette-neutral95);
  transition: background-color 0.1s;
}

.tab_item:hover .material-symbols-outlined {
  font-weight: 700;
  font-variation-settings: "WGHT" 700;
  transition: font-weight 0.2s ease, font-variation-settings 0.2s ease;
}

.tab_item:hover .tab_name {
  font-weight: 700;
  transition: font-weight 0.2s ease;
}

/* focus */
.tab_item:focus-visible {
  background-color: var(--palette-neutral95);
  transition: background-color 0.1s;
}

.tab_item:focus-visible .material-symbols-outlined {
  font-weight: 700;
  font-variation-settings: "WGHT" 700;
  transition: font-weight 0.2s ease, font-variation-settings 0.2s ease;
}

.tab_item:focus-visible .tab_name {
  font-weight: 700;
  transition: font-weight 0.2s ease;
}

/* active */
.tab_item:active {
  background-color: var(--palette-neutral90);
  transition: background-color 0.1s;
}

.tab_item:active .material-symbols-outlined {
  transform: scale(0.92);
  transition: transform 0.2s ease;
}

/* current */
.tab_item.current {
  color: var(--on-primary-container-light);
  background-color: var(--primary-container-light);
  box-shadow: 0px 0px 0px 1px var(--outline-light);
  transition: box-shadow 0.1s ease;
  z-index: 2;
}

.tab_item.current .material-symbols-outlined {
  font-variation-settings: "FILL" 1;
}

.tab_item.current .tab_name {
  font-weight: 700;
}
</style>
