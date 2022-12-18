<template>
  <div>
    <h2>Личный кабинет</h2>
    <p>{{ GETUSER }}</p>
    <p>{{ GETUSERDATA }}</p>
    <div @click="ordersVisability = !ordersVisability">Мои заказы</div>
    <div v-if="ordersVisability">
      <div>Мои заказы</div>
      <p>{{ userID }}</p>
      <div v-if="ordersData.length">
        <!-- <p>{{ ordersData }}</p> -->
        <p>{{ filteredUserOrders }}</p>
      </div>
    </div>
    <a @click="logout">
      <span class="material-symbols-outlined">person</span>
      <span class="header_middle_bar_item_lnk" @click="logout">Выйти</span>
    </a>
    -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Dashboard",
  data() {
    return {
      ordersVisability: false,
      ordersData: [],
    };
  },
  created() {
    this.loadUserData();
    this.loadOrders();
  },
  computed: {
    ...mapGetters("auth", ["GETUSERDATA", "GETUSER"]),
    ...mapGetters("api_urls", ["getServerOrdersUrl"]),
    userID() {
      return this.GETUSERDATA["id"];
    },
    filteredUserOrders() {
      let tempOrders = this.ordersData;
      tempOrders = tempOrders.filter((item) => {
        return item.relationships.user.data.id == this.userID;
      });
      return tempOrders;
    },
  },
  methods: {
    ...mapActions("auth", ["loadUserData", "logoutUser"]),
    logout() {
      this.logoutUser().then(() => {
        this.$router.push("/login");
      });
    },
    loadOrders() {
      let token = localStorage.getItem("token");
      const options = {
        headers: {
          "Content-Type": "application/json",
          Authorization: "Token " + token,
        },
      };
      // const data = {
      //   headers: {
      //     "Content-Type": "application/json",
      //   },
      // };
      this.axios
        .get(`${this.getServerOrdersUrl}/orders_list`, options)
        .then((response) => {
          this.ordersData = response.data.data;
        })
        .catch(function (error) {
          console.error(error);
        });
    },
  },
};
</script>

<style></style>
