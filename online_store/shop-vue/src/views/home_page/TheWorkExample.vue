<template>
  <div>
    <h4>{{ example_name }}</h4>
    <p v-html="example_description"></p>
    <!-- <p>{{ imagesList }}</p> -->
    <div>
      <TheExampleImage
        v-for="image in filteredImagesList"
        :key="image"
        :image_name="image.attributes.name"
        :image="image.attributes.image"
        :image_alt_text="image.attributes.alt_text"
      />
    </div>
  </div>
</template>

<script>
import TheExampleImage from "./TheExampleImage.vue";
import { mapGetters } from "vuex";
export default {
  name: "TheWorkExample",
  components: {
    TheExampleImage,
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

<style></style>
