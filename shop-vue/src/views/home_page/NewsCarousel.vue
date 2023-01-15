<template>
  <div>
    <div v-for="item in news" :key="item">
      <div v-if="activeNews == item.id">
        <div>
          <div class="main_first_slider_img_wrapper">
            <img :src="item.attributes.image" :alt="item.attributes.alt_text" />
          </div>
          <div class="main_first_meta_wrapper">
            <h2 class="main_first_slider_title">{{ item.attributes.title }}</h2>
          </div>
          <div class="main_first_slider_controls">
            <router-link :to="'/post/' + item.attributes.slug">
              <BaseButton
                class="primary"
                :ButtonMeta="item.attributes.carousel_link_text"
              />
            </router-link>
            <div class="main_first_slider_switch">
              <IconButton @click="prevNews(item.id)" IconName="chevron_left" />
              <IconButton @click="nextNews(item.id)" IconName="chevron_right" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BaseButton from "../../components/AllButtons/BaseButton.vue";
import IconButton from "../../components/AllButtons/IconButton.vue";
export default {
  name: "NewsCarousel",
  components: {
    BaseButton,
    IconButton,
  },
  props: {
    news: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      activeNews: 0,
      newsDict: {},
    };
  },
  watch: {
    news() {
      this.makeNewsIdDict();
      this.activeNews = this.newsDict[0];
    },
  },
  methods: {
    makeNewsIdDict() {
      for (let item in this.news) {
        this.newsDict[item] = this.news[item].id;
      }
    },
    nextNews(id) {
      for (let news in this.newsDict) {
        if (id == this.newsDict[news]) {
          if (this.newsDict[Number(news) + 1]) {
            this.activeNews = this.newsDict[Number(news) + 1];
            break;
          } else {
            this.activeNews = this.newsDict[0];
          }
        }
      }
    },
    prevNews(id) {
      for (let news in this.newsDict) {
        if (id == this.newsDict[news]) {
          if (this.newsDict[Number(news) - 1]) {
            this.activeNews = this.newsDict[Number(news) - 1];
          } else {
            this.activeNews =
              this.newsDict[Object.keys(this.newsDict).length - 1];
          }
        }
      }
    },
  },
};
</script>

<style>
.main_first_slider_switch {
  display: flex;
  column-gap: 8px;
}
</style>
