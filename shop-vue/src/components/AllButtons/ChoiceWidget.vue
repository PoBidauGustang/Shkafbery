<template>
  <button class="choice_widget">
    <div class="choice_widget_meta_wrapper">
      <div class="choice_widget_img_wrapper">
        <img
          src="https://images.unsplash.com/photo-1567016546367-c27a0d56712e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
          alt=""
        />
      </div>
      <div class="choice_widget_meta">
        <span class="choice_widget_title">Выберете размер (6)</span>
        <span class="choice_widget_value">800×500×760 мм</span>
      </div>
    </div>
    <span class="material-symbols-outlined">chevron_right</span>
  </button>
</template>

<script>
export default {
  name: "ChoiceWidget",
};
</script>

<style scoped>
.choice_widget {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--on-surface-light);
  background-color: var(--palette-neutral95);
  min-height: 72px;
  padding-top: 8px;
  padding-left: 16px;
  padding-right: 16px;
  padding-bottom: 8px;
  border-radius: 16px;
}

.choice_widget_meta_wrapper {
  display: flex;
  align-items: center;
  column-gap: 16px;
}

.choice_widget_img_wrapper {
  overflow: hidden;
  width: 56px;
  height: 56px;
  border-radius: 100%;
}
.choice_widget_img_wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.choice_widget_img_wrapper:empty {
  display: none;
}

.choice_widget_meta {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.choice_widget_title {
  font-weight: 700;
  font-size: 16px;
  line-height: 24px;
}

.choice_widget_value {
  font-size: 14px;
  line-height: 20px;
  color: var(--on-surface-variant-light);
}
</style>
