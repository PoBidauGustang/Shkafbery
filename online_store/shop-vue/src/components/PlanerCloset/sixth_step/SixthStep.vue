<template>
  <div>
    <h1>Выберите дверной профиль и ручки</h1>
    <p>выбранная система дверей: {{ GETDOORSSYSTEM }}</p>
    <!-- <p>выбранные размеры: {{ GETDIMENSIONS }}</p>
    <p>подходящие схемы наполнения: {{ GETSUITABLEFILLINGSCHEMES }}</p>
    <p>подходящие по заданным размерам схемы: {{ filteredSchemesByDimensions }}</p>
    <p>данные подходящих по заданным размерам схем: {{ filteredSchemesData }}</p> -->
    <!-- <p>ВСЕ ПРОФИЛИ: {{ profilesList }}</p>
    <p>Фильтрованные профили: {{ filteredProfilesList }}</p>
    <p>ВСЕ РУЧКИ:{{ doorHandlesList }}</p>
    <p>Фильтрованные ручки: {{ filteredHandlesList }}</p> -->
    <div>
      <div>
        <TheDoorProfile
          v-for="profile in filteredProfilesList"
          :key="profile.id"
          :profile_name="profile.attributes.name"
          :profile_description="profile.attributes.description"
        />
      </div>
      <div>
        <TheDoorHandle
          v-for="handle in filteredHandlesList"
          :key="handle.id"
          :handle_name="handle.attributes.name"
          :handle_description="handle.attributes.description"
        />
      </div>
      <!-- <div v-show="visible">
        <p>{{ profilesList }}</p>
        <p>{{ doorHandlesList }}</p>
      </div> -->
      <!-- <p>в сторе: {{ GETFILLINGSCHEME }}</p> -->
      <!-- <p>{{ filteredBodyColourList }}</p> -->
    </div>
  </div>
</template>

<script>
import TheDoorProfile from "./TheDoorProfile.vue";
import TheDoorHandle from "./TheDoorHandle.vue";
import { mapGetters } from "vuex";
export default {
  name: "sixth_step",
  components: {
    TheDoorProfile,
    TheDoorHandle,
  },
  data() {
    return {
      profilesList: [],
      doorHandlesList: [],
      filteredProfilesList: [],
      filteredHandlesList: [],
      visible: false,
    };
  },
  watch: {
    profilesList() {
      this.filterProfilesBySystems();
    },
    doorHandlesList() {
      this.filterHandlesBySystems();
    },
  },
  created() {
    this.loadProfilesList();
    this.loadDoorHandlesList();
  },
  beforeUpdate() {
    // this.filterProfilesBySystems();
    // this.filterHandlesBySystems();
  },
  computed: {
    ...mapGetters("api_urls", ["getServerClosetUrl"]),
    ...mapGetters("closet_configurator", ["GETDOORSSYSTEM"]),
  },
  methods: {
    loadProfilesList() {
      this.axios
        .get(`${this.getServerClosetUrl}/step_sixth_profiles`)
        .then((response) => {
          this.profilesList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    loadDoorHandlesList() {
      this.axios
        .get(`${this.getServerClosetUrl}/step_sixth_handle`)
        .then((response) => {
          this.doorHandlesList = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    filterProfilesBySystems() {
      for (let profile in this.profilesList) {
        for (let system in this.profilesList[Number(profile)].attributes
          .doors_system) {
          if (
            this.profilesList[Number(profile)].attributes.doors_system[
              Number(system)
            ].name === this.GETDOORSSYSTEM
          ) {
            this.filteredProfilesList.push(this.profilesList[Number(profile)]);
          }
        }
      }
    },
    filterHandlesBySystems() {
      for (let handle in this.doorHandlesList) {
        for (let system in this.doorHandlesList[Number(handle)].attributes
          .doors_system) {
          if (
            this.doorHandlesList[Number(handle)].attributes.doors_system[
              Number(system)
            ].name === this.GETDOORSSYSTEM
          ) {
            this.filteredHandlesList.push(this.doorHandlesList[Number(handle)]);
          }
        }
      }
    },
  },
};
</script>

<style></style>
