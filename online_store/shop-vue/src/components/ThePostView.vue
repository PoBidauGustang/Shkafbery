<template>
    <div class="Post_Card">
        <router-link :to=" '/post/' + post_data.slug ">
            <img :src=" require('../assets/images/1.jpeg') " alt="img" class="Post_Image">
            <div class="Post_Tag_Wrapper">
                <span class="Post_Tag">Категория: {{ post_data.category[0].name }}</span>
            </div>
            <a class="Post_Headline">{{ post_data.title }}</a>
        </router-link>
    </div>
</template>

<script>
export default {
    name: "the-post-view",
    props: {
        post_data: {
            type: Object,
            default() {
                return {}
            }
        }
    }
}
</script>

<style>
.Post_Card {
  grid-column: span 4;
  display: flex;
  flex-direction: column;
  border-radius: 24px;
  overflow: hidden;
  background: #FFFFFF;
  margin-bottom: 24px;
}

.Post_Card:hover {
  box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.3), 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
}

.Post_Image {
  aspect-ratio: 16 / 9;
  object-fit: cover;
  padding-bottom: 16px;
  width: 100%;
  /* height: 100%; */
}

.Post_Tag_Wrapper {
  display: flex;
  padding-left: 16px;
  padding-right: 16px;
  padding-bottom: 16px;
}

.Post_Tag {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 6px 16px;
  background-color: #9E4300;
  color: #FFFFFF;
  border-radius: 100px;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  text-align: center;
}

.Post_Headline {
  padding-left: 16px;
  padding-right: 16px;
  padding-bottom: 24px;
  font-size: 28px;
  font-weight: 500;
  line-height: 36px;
  color: #1E1B16;
  text-decoration: none;
}
</style>