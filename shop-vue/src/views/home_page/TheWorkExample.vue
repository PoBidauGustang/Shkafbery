<template>
  <section class="main_base_section main_large_margin">
    <div class="main_project_title">
      <h2 class="main_small_title">Примеры работ</h2>
      <a class="main_base_link" href="#/photos">
        <span class="main_base_link_1">Смотреть </span>
        <span class="main_base_link_2">все</span>
      </a>
    </div>
    <ul class="main_project_list">
      <li
        class="main_project_list_item"
        v-for="example in workExamplesList"
        :key="example.id"
      >
        <ProjectItem :projectItem="example" />
      </li>
    </ul>
  </section>
</template>

<script>
import ProjectItem from "../../components/AllCards/ProjectItem.vue";
import { mapGetters } from "vuex";
export default {
  name: "TheWorkExample",
  components: {
    ProjectItem,
  },
  data() {
    return {
      // examplesList: [],
      // filteredImagesList: [],
    };
  },
  // watch: {
  //   imagesList() {
  //     this.filterImageList();
  //   },
  // },
  props: {
    workExamplesList: {
      type: Array,
      default() {
        return [];
      },
    },
    // example_description: {
    //   type: String,
    //   default() {
    //     return "";
    //   },
    // },
    // example_image: {
    //   type: Number,
    //   default() {
    //     return 0;
    //   },
    // },
  },
  created() {
    // this.loadExamplesList();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerShopUrl", "getServerInformationUrl"]),
  },
  methods: {
    // loadExamplesList() {
    //   this.axios
    //     .get(`${this.getServerInformationUrl}/work_examples_main`)
    //     .then((response) => {
    //       this.examplesList = response.data.data;
    //     })
    //     .catch(function (error) {
    //       console.error(error);
    //     });
    // },
    // filterImageList() {
    //   for (let image in this.imagesList) {
    //     if (
    //       this.imagesList[Number(image)].attributes.examples[0].name ===
    //       this.example_name
    //     ) {
    //       this.filteredImagesList.push(this.imagesList[Number(image)]);
    //     }
    //   }
    // },
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
