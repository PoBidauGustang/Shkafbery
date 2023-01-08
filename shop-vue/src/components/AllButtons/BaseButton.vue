<template>
  <button class="base_button">
    {{ ButtonMeta }}
  </button>
</template>

<script>
export default {
  name: "BaseButton",
  props: ["ButtonMeta"],
};
</script>

<style scoped>
.base_button {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
  color: var(--on-primary-light);
  text-align: center;
  background-color: var(--primary-light);
  padding-top: 10px;
  padding-left: 24px;
  padding-right: 24px;
  padding-bottom: 10px;
  border-radius: 100px;
  cursor: pointer;
  transition: background-color 0.1s, box-shadow 0.5s ease, font-weight 0.5s ease;
}

.base_button:hover {
  font-weight: 700;
  background-color: var(--palette-primary50);
  box-shadow: var(--elevation-light-1);
  transition: background-color 0.1s, box-shadow 0.2s ease, font-weight 0.2s ease;
}

.base_button:focus-visible {
  font-weight: 700;
  background-color: var(--palette-primary50);
  transition: background-color 0.1s, font-weight 0.2s ease;
}

.base_button:active {
  font-weight: 700;
  background-color: var(--palette-primary60);
  transition: background-color 0.1s, font-weight 0.1s ease, box-shadow 0.2s ease;
  box-shadow: none;
}

/* tonal */

.base_button.tonal {
  color: var(--on-primary-container-light);
  background-color: var(--primary-container-light);
}

.base_button.tonal:hover {
  background-color: var(--palette-primary80);
}

.base_button.tonal:focus-visible {
  background-color: var(--palette-primary80);
}

.base_button.tonal:active {
  background-color: var(--palette-primary70);
}

/* elevated */

.base_button.elevated {
  color: var(--primary-light);
  background-color: transparent;
  box-shadow: var(--elevation-light-1);
}

.base_button.elevated:hover {
  background-color: var(--palette-primary90);
  box-shadow: var(--elevation-light-2);
}

.base_button.elevated:focus-visible {
  background-color: var(--palette-primary90);
}

.base_button.elevated:active {
  background-color: var(--palette-primary80);
}

/* text */

.base_button.text {
  color: var(--primary-light);
  background-color: transparent;
  padding-left: 12px;
  padding-right: 12px;
}

.base_button.text:hover {
  background-color: var(--palette-primary90);
}

.base_button.text:focus-visible {
  background-color: var(--palette-primary90);
}

.base_button.text:active {
  background-color: var(--palette-primary80);
}

/* primary */

@media (min-width: 1240px) {
  .primary {
    font-size: 16px;
    line-height: 24px;
    padding-top: 12px;
    padding-bottom: 12px;
  }
}
</style>
