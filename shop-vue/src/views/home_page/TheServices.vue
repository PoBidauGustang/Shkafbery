<template>
  <div>
    <h2>Услуги</h2>
    <h4>Ochen` opitny personal</h4>
    <div v-for="service in servicesList" :key="service.id">
      <router-link :to="'/category/' + service.attributes.slug">
        <ul>
          <li>{{ service.attributes.name }}</li>
          <li>
            <img
              v-if="service.attributes.services_photo[0]"
              class=""
              :src="service.attributes.services_photo[0].image"
            />
          </li>
        </ul>
      </router-link>
    </div>
  </div>
</template>

<script>
// import { mapGetters } from "vuex";
export default {
  name: "TheCatalog",
  props: {
    servicesList: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  data() {
    return {};
  },
  //   computed: {
  //     ...mapGetters("data", ["GETMAINCATEGORIES"]),
  //   },
  methods: {},
};
</script>

<style></style>
