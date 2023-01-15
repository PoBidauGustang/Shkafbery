<template>
  <div>
    <div v-for="item in news" :key="item">
      <div v-if="activeNews == item.id">
        <div>
          {{ item.id }}
          {{ item.attributes.title }}
          {{ item.attributes.slug }}
          <router-link :to="'/post/' + item.attributes.slug">{{ item.attributes.carousel_link_text }}</router-link>
          <img
            class=""
            :src="item.attributes.image"
            :alt="item.attributes.alt_text"
          />
        </div>
        <div>
          <button @click="prevNews(item.id)">предыдущая</button>
          <button @click="nextNews(item.id)">следующая</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TheFAQ",
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

<style></style>
