<template>
  <div>
    <h2>Личный кабинет</h2>
    <a @click="logout">
      <span class="material-symbols-outlined">person</span>
      <span class="header_middle_bar_item_lnk">Выйти</span>
    </a>
    -->
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "Dashboard",
  data() {
    return {};
  },
  computed: {},
  methods: {
    ...mapActions("auth", ["logoutUser"]),
    logout() {
      this.logoutUser().then(() => {
        this.$router.push("/login");
      });
    },
  },
};
</script>

<style></style>
