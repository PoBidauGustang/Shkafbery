<template>
  <a class="blog_item_wrapper">
    <article class="blog_item">
      <h3 class="blog_item_title">
          {{ BlogItemTitile }}
      </h3>
      <div class="blog_item_meta_wrapper">
        <time class="blog_item_time" datetime="2023-05-01">
          05.01.2021
        </time>
        <ul class="blog_item_tag_list">
          <li>
            <BaseTag
              BaseTagTitile="Новости"
            />
          </li>
        </ul>
      </div>
      <div class="blog_item_img_wrapper">
        <img src="https://images.unsplash.com/photo-1567016546367-c27a0d56712e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt="">
      </div>
    </article>
  </a>
</template>
  
<script>
import BaseTag from '../AllButtons/BaseTag.vue';

  export default {
    name: "BlogItem",
    components: {
        BaseTag
    },
    props: ['BlogItemTitile']
}
</script>


<style scoped>

.blog_item_wrapper {
    display: flex;
    list-style: none;
}
.blog_item_wrapper:hover {
    background-color: var(--palette-neutral-variant95);
}

.blog_item {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-column-gap: 32px;
    padding: 16px;
}

.blog_item_title {
    grid-column: span 4;
    font-weight: 500;
    font-size: 28px;
    line-height: 36px;
    margin-bottom: 32px;
    color: var(--on-surface-light);
}

.blog_item_wrapper:hover .blog_item_title {
    text-decoration: underline;
    text-decoration-color: var(--primary-light);
}

.blog_item_meta_wrapper {
    grid-column: span 2;
    grid-row: 2;
    align-self: end;
    display: flex;
    flex-direction: column;
    row-gap: 16px;
}

.blog_item_time {
    font-size: 12px;
    line-height: 16px;
    color: var(--on-surface-variant-light);
}

.blog_item_tag_list {
    display: flex;
    flex-wrap: wrap;
    list-style: none;
    column-gap: 8px;
    row-gap: 8px;
}

.blog_item_img_wrapper {
    grid-column: 3 / span 2;
    grid-row: 2;
    align-self: end;
    overflow: hidden;
    aspect-ratio: 1 / 1;
    border-radius: 12px;
}
  
.blog_item_img_wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
  
</style>