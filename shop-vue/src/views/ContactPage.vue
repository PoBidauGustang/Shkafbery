<template>
  <section class="base_page">
    <h1 class="base_page_title">Контакты</h1>
    <div class="base_page_meta_wrapper">
      <p class="base_page_description">Контакты компании</p>
      <div class="base_page_img_wrapper">
        <img
          src="https://images.unsplash.com/photo-1567016546367-c27a0d56712e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
          alt=""
        />
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "BasePage",
};
</script>

<style>
.base_page {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  padding-left: 24px;
  padding-top: 48px;
  padding-right: 24px;
  padding-bottom: 48px;
}

.base_page_title {
  grid-column: span 12;
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 64px;
  line-height: 72px;
  text-transform: uppercase;
  text-align: center;
  color: var(--on-surface-light);
  padding-left: 16px;
  padding-right: 16px;
  margin-bottom: 48px;
}

.base_page_meta_wrapper {
  grid-column: span 12;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  column-gap: 32px;
  padding-left: 16px;
  padding-right: 16px;
}

.base_page_description {
  grid-column: span 6;
  font-size: 18px;
  line-height: 28px;
  color: var(--on-surface-light);
}

.base_page_img_wrapper {
  grid-column: 7 / span 6;
  overflow: hidden;
  aspect-ratio: 3 / 2;
}

.base_page_img_wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
