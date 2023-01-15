<template>
  <section class="personal_area_wrapper">
    <div class="personal_area_menu_wrapper">
      <div class="pesonal_area_header">
        <h1 class="pesonal_area_headline">Личный кабинет</h1>
        <span class="pesonal_area_name">{{ GETUSER }}</span>
      </div>
      <ul class="personal_area_menu">
        <li class="personal_area_menu_item_wrapper">
          <a class="personal_area_menu_item">
            <div class="personal_area_menu_item_meta">
              <span class="material-symbols-outlined">manage_accounts</span>
              <span class="personal_area_menu_item_meta_name">Мои данные</span>
            </div>
            <span class="material-symbols-outlined">chevron_right</span>
          </a>
        </li>
        <li class="personal_area_menu_item_wrapper">
          <a class="personal_area_menu_item">
            <div class="personal_area_menu_item_meta">
              <span class="material-symbols-outlined">package</span>
              <span class="personal_area_menu_item_meta_name">Мои заказы</span>
            </div>
            <span class="material-symbols-outlined">chevron_right</span>
          </a>
        </li>
        <li class="personal_area_menu_item_wrapper">
          <a class="personal_area_menu_item">
            <div class="personal_area_menu_item_meta">
              <span class="material-symbols-outlined">favorite</span>
              <span class="personal_area_menu_item_meta_name">Избранное</span>
            </div>
            <span class="material-symbols-outlined">chevron_right</span>
          </a>
        </li>
        <li class="personal_area_menu_item_wrapper">
          <a class="personal_area_menu_item" href="#/cart">
            <div class="personal_area_menu_item_meta">
              <span class="material-symbols-outlined">shopping_cart</span>
              <span class="personal_area_menu_item_meta_name">Корзина</span>
            </div>
            <span class="material-symbols-outlined">chevron_right</span>
          </a>
        </li>
        <li class="personal_area_menu_item_wrapper">
          <a class="personal_area_menu_item">
            <div class="personal_area_menu_item_meta">
              <span class="material-symbols-outlined">playlist_add</span>
              <span class="personal_area_menu_item_meta_name"
                >Списки сравнения</span
              >
            </div>
            <span class="material-symbols-outlined">chevron_right</span>
          </a>
        </li>
        <li class="personal_area_menu_item_wrapper">
          <a class="personal_area_menu_item">
            <div class="personal_area_menu_item_meta">
              <span class="material-symbols-outlined">design_services</span>
              <span class="personal_area_menu_item_meta_name"
                >Мои конфигурации</span
              >
            </div>
            <span class="material-symbols-outlined">chevron_right</span>
          </a>
        </li>
        <li class="personal_area_menu_item_wrapper">
          <a class="personal_area_menu_item">
            <div class="personal_area_menu_item_meta">
              <span class="material-symbols-outlined">support_agent</span>
              <span class="personal_area_menu_item_meta_name">Помощь</span>
            </div>
            <span class="material-symbols-outlined">chevron_right</span>
          </a>
        </li>
        <li class="personal_area_menu_item_wrapper">
          <button class="personal_area_menu_item_exit">
            <span class="personal_area_menu_item_exit_text" @click="logout"
              >Выйти</span
            >
          </button>
        </li>
      </ul>
    </div>
    <div class="personal_area_content_wrapper">
      <!-- {{ GETUSERDATA }}
      {{ ordersData }} -->
    </div>
    <!-- <h2>Личный кабинет</h2>
    <p>{{ GETUSER }}</p>
    <p>{{ GETUSERDATA }}</p>
    <div @click="ordersVisability = !ordersVisability">Мои заказы</div>
    <div v-if="ordersVisability">
      <div>Мои заказы</div>
      <p>{{ userID }}</p>
      <div v-if="ordersData.length">
        <p>{{ ordersData }}</p>
        <p>{{ filteredUserOrders }}</p>
      </div>
    </div>
    <a @click="logout">
      <span class="material-symbols-outlined">person</span>
      <span class="header_middle_bar_item_lnk" @click="logout">Выйти</span>
    </a>
    -->
    -->
  </section>
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

<style>
.personal_area_wrapper {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  padding-left: 24px;
  padding-right: 24px;
}

.personal_area_menu_wrapper {
  grid-column: span 3;
  position: sticky;
  left: 0;
  top: 0;
  display: flex;
  flex-direction: column;
  background-color: #ffffff;
  border-right: 1px solid;
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
  margin-left: -24px;
  padding-bottom: 64px;
}

.pesonal_area_header {
  background-color: #f2efeb;
  padding-left: 40px;
  padding-top: 24px;
  padding-right: 16px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--outline-light);
}

.pesonal_area_headline {
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  padding-bottom: 4px;
  margin: 0;
}

.pesonal_area_name {
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 32px;
  line-height: 40px;
  text-transform: uppercase;
}

.personal_area_menu {
  display: flex;
  flex-direction: column;
  list-style: none;
}

.personal_area_menu_item_wrapper {
  border-bottom: 1px solid;
}

.personal_area_menu_item_wrapper:last-child {
  border-bottom: 0px;
}

.personal_area_menu_item {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding-left: 40px;
  padding-top: 16px;
  padding-right: 16px;
  padding-bottom: 16px;
}

.personal_area_menu_item_meta {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.personal_area_menu_item_meta_name {
  padding-left: 12px;
  font-weight: 500;
  font-size: 16px;
  line-height: 24px;
}

.personal_area_menu_item_exit {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding-left: 40px;
  padding-top: 16px;
  padding-right: 16px;
  padding-bottom: 16px;
  width: 100%;
}

.personal_area_menu_item_exit_text {
  font-weight: 500;
  font-size: 16px;
  line-height: 24px;
}

.personal_area_content_wrapper {
  grid-column: 4 / span 9;
}
</style>
