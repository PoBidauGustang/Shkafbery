<template>
  <section class="projects_page_area">
    <h1 class="projects_page_title">Примеры работ</h1>
    <ul class="projects_page_item_list">
      <li
        class="projects_page_item"
        v-for="example in workExamplesList"
        :key="example.id"
      >
        <ProjectItem :projectItem="example" />
      </li>
    </ul>
  </section>
</template>

<script>
import ProjectItem from "../components/AllCards/ProjectItem.vue";
import { mapGetters } from "vuex";
export default {
  name: "ProjectsPage",
  components: {
    ProjectItem,
  },
  data() {
    return {
      workExamplesList: [],
    };
  },
  created() {
    this.loadWorkExamplesList();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerInformationUrl"]),
  },
  methods: {
    loadWorkExamplesList() {
      this.axios
        .get(`${this.getServerInformationUrl}/work_examples_main`)
        .then((response) => {
          this.workExamplesList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
  },
};
</script>

<style>
.projects_page_area {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  padding-left: 24px;
  padding-top: 48px;
  padding-right: 24px;
  padding-bottom: 48px;
}

.projects_page_title {
  grid-column: span 12;
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 64px;
  line-height: 72px;
  text-transform: uppercase;
  text-align: center;
  color: var(--on-surface-light);
  margin-bottom: 48px;
}

.projects_page_item_list {
  grid-column: span 12;
  grid-row: 2;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  list-style: none;
}

.projects_page_item {
  grid-column: span 6;
  border-right: 1px solid var(--outline-light);
  border-bottom: 1px solid var(--outline-light);
}

.projects_page_item > a {
  height: 100%;
}

.projects_page_item:first-child {
  margin-left: -24px;
}
.projects_page_item:first-child > a {
  padding-left: 24px;
}

.projects_page_item:nth-child(-n + 2) {
  border-top: 1px solid;
}

.projects_page_item:nth-child(2n) {
  border-right: 0px;
  margin-right: -24px;
}
.projects_page_item:nth-child(2n) > a {
  padding-right: 24px;
}

.projects_page_item:nth-child(2n + 1) {
  margin-left: -24px;
}
.projects_page_item:nth-child(2n + 1) > a {
  padding-left: 24px;
}
</style>
