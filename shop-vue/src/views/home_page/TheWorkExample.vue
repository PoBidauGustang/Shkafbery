<template>
  <div>
    <!-- <h4>{{ example_name }}</h4> -->
    <!-- <p v-html="example_description"></p> -->
    <!-- <p>{{ imagesList }}</p> -->
    <!-- <div>
      <TheExampleImage
        v-for="image in filteredImagesList"
        :key="image"
        :image_name="image.attributes.name"
        :image="image.attributes.image"
        :image_alt_text="image.attributes.alt_text"
      />
    </div> -->
    <div class="work_img_wrapper">
      <img
        class="work_img"
        src="https://images.unsplash.com/photo-1567016546367-c27a0d56712e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
        alt=""
      />
    </div>
    <div class="work_title">
      <h3 class="title_large">{{ example_name }}</h3>
    </div>
    <div class="work_meta_wrapper">
      <div class="work_meta_tags">
        <div class="work_tag"><span class="promt_large">Двери-купе</span></div>
        <div class="work_tag"><span class="promt_large">Гардеробная</span></div>
      </div>
      <div class="work_price">
        <span class="links_promt_large">118 900 ₽</span>
      </div>
    </div>
  </div>
</template>

<script>
// import TheExampleImage from "./TheExampleImage.vue";
import { mapGetters } from "vuex";
export default {
  name: "TheWorkExample",
  components: {
    // TheExampleImage,
  },
  data() {
    return {
      imagesList: [],
      filteredImagesList: [],
    };
  },
  watch: {
    imagesList() {
      this.filterImageList();
    },
  },
  props: {
    example_name: {
      type: String,
      default() {
        return "";
      },
    },
    example_description: {
      type: String,
      default() {
        return "";
      },
    },
    example_image: {
      type: Number,
      default() {
        return 0;
      },
    },
  },
  created() {
    this.loadImagesList();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerShopUrl", "getServerInformationUrl"]),
  },
  methods: {
    loadImagesList() {
      this.axios
        .get(`${this.getServerInformationUrl}/examples_photos`)
        .then((response) => {
          this.imagesList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    filterImageList() {
      for (let image in this.imagesList) {
        if (
          this.imagesList[Number(image)].attributes.examples[0].name ===
          this.example_name
        ) {
          this.filteredImagesList.push(this.imagesList[Number(image)]);
        }
      }
    },
  },
};
</script>

<style>
.work_img_wrapper {
  aspect-ratio: 3 / 2;
  margin-bottom: 16px;
}

.work_img {
  width: 100%;
  object-fit: cover;
}

.work_title {
  margin-bottom: 32px;
  padding-left: 16px;
  padding-right: 16px;
}

.work_meta_wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  padding-left: 16px;
  padding-right: 16px;
}

.work_meta_tags {
  display: flex;
  flex-direction: column;
  padding-right: 16px;
}

.work_tag {
  padding-bottom: 8px;
}

.work_tag:last-child {
  padding-bottom: 0px;
}

.work_price {
  align-self: end;
}
</style>
