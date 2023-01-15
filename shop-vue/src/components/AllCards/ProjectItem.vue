<template>
  <div class="project_item_wrapper">
    <article class="project_item">
      <h3 class="project_item_title">
        {{ projectItem.attributes.name }}
      </h3>
      <div class="project_item_meta_wrapper">
        <dl class="project_item_price" v-if="projectItem.attributes.price">
          <dt>Стоимость</dt>
          <dd>{{ projectItem.attributes.price }} ₽</dd>
        </dl>
        <ul class="project_item_tag_list">
          <li>
            <BaseTag :BaseTagTitile="projectItem.attributes.category" />
          </li>
        </ul>
      </div>
      <div class="project_item_img_wrapper">
        <img
          v-if="projectItem.attributes.example_photo[0]"
          class=""
          :src="projectItem.attributes.example_photo[0].image"
          :alt="projectItem.attributes.example_photo[0].alt_text"
        />
        <!-- <img
          src="https://images.unsplash.com/photo-1567016546367-c27a0d56712e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
          alt=""
        /> -->
      </div>
    </article>
  </div>
</template>

<script>
import BaseTag from "../AllButtons/BaseTag.vue";

export default {
  name: "Project Item",
  components: {
    BaseTag,
  },
  props: ["projectItem"],
};
</script>

<style scoped>
.project_item_wrapper {
  display: flex;
  list-style: none;
}
.project_item_wrapper:hover {
  background-color: var(--palette-neutral-variant95);
}

.project_item {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-column-gap: 32px;
  padding: 16px;
}

.project_item_title {
  grid-column: span 3;
  grid-row: 1;
  font-weight: 500;
  font-size: 28px;
  line-height: 36px;
  margin-bottom: 32px;
  color: var(--on-surface-light);
}

.project_item_wrapper:hover .project_item_title {
  text-decoration: underline;
  text-decoration-color: var(--primary-light);
}

.project_item_meta_wrapper {
  grid-column: span 3;
  grid-row: 2;
  align-self: end;
  display: flex;
  flex-direction: column;
  row-gap: 16px;
}

.project_item_price {
  display: flex;
  flex-direction: column;
}
.project_item_price dt {
  font-size: 12px;
  line-height: 16px;
  color: var(--on-surface-variant-light);
}
.project_item_price dd {
  font-size: 12px;
  line-height: 16px;
  color: var(--on-surface-light);
}

.project_item_tag_list {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  column-gap: 8px;
  row-gap: 8px;
}

.project_item_img_wrapper {
  grid-column: 4 / span 3;
  grid-row: span 2;
  overflow: hidden;
  aspect-ratio: 1 / 1;
  border-radius: 12px;
}

.project_item_img_wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
