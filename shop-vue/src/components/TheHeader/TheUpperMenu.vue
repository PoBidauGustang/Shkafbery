<template>
  <div class="header_top_wrapper">
    <ul class="header_top_list">
      <li class="header_top_list_item">
        <router-link class="header_top_link" to="/about">О нас</router-link>
      </li>
      <li class="header_top_list_item">
        <router-link class="header_top_link" to="/contacts"
          >Контакты</router-link
        >
      </li>
      <li class="header_top_list_item">
        <router-link class="header_top_link" to="/installation"
          >Сборка и установка</router-link
        >
      </li>
      <li class="header_top_list_item">
        <router-link class="header_top_link" to="/measurements"
          >Замеры</router-link
        >
      </li>
      <li class="header_top_list_item">
        <router-link class="header_top_link" to="/partners"
          >Партнерам</router-link
        >
      </li>
      <li class="header_top_list_item">
        <router-link class="header_top_link" to="/photos"
          >Примеры работ</router-link
        >
      </li>
      <li class="header_top_list_item">
        <router-link class="header_top_link" to="/posts">Блог</router-link>
      </li>
    </ul>
    <div class="header_top_contact_wrapper">
      <a class="phone_link" href="/">+7 999 987 78 89</a>
      <div class="phone_info">
        <span class="material-symbols-outlined size">info</span>
      </div>
    </div>
  </div>
</template>

<script>
// import { mapGetters } from "vuex";
export default {
  name: "UpperMenu",
};
</script>

<style>
.header_top_wrapper {
  display: flex;
  justify-content: space-between;
  background: #000000;
  padding-left: 40px;
  padding-right: 40px;
}

.header_top_list {
  display: flex;
  list-style: none;
  margin-top: 4px;
  margin-bottom: 4px;
}

.header_top_list_item {
  display: flex;
  border-radius: 8px;
  padding-left: 12px;
  padding-right: 12px;
  padding-top: 6px;
  padding-bottom: 6px;
  text-align: center;
  margin-right: 8px;
}

.header_top_list_item:last-child {
  margin-right: 0px;
}

.header_top_link {
  color: #ffffff;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
}

.header_top_contact_wrapper {
  position: absolute;
  right: 34px;
  top: 4px;
  z-index: 2;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #ffffff;
}

.phone_link {
  text-decoration: none;
  color: #ffffff;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  text-align: right;
}

.phone_info {
  display: flex;
  color: #ffffff;
  padding: 6px;
  border-radius: 100px;
}

.size {
  font-size: 20px;
  font-variation-settings: "OPSZ" 20;
}

/* .header_top {
  display: flex;
  justify-content: space-between;
  background: #1c1c1c;
  padding-left: 40px;
  padding-right: 40px;
}

.top_menu {
  display: flex;
  list-style: none;
  padding-top: 4px;
  padding-bottom: 4px;
  margin: 0px;
  padding-left: 0px;
}

.top_menu_item {
  margin-right: 8px;
}
.top_menu_item:last-child {
  margin-right: 0px;
}

.top_menu_link {
  display: flex;
  border-radius: 8px;
  padding-left: 12px;
  padding-right: 12px;
  padding-top: 6px;
  padding-bottom: 6px;
  text-decoration: none;
  color: #ffffff;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  text-align: center;
}

.top_menu_link:hover {
  background-color: #000000;
}

.phone_link {
  text-decoration: none;
  color: #ffffff;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  text-align: right;
}

.phone {
  display: flex;
  justify-content: center;
  align-items: center;
  color: #ffffff;
  padding-top: 4px;
  padding-bottom: 4px;
}

.phone_info {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  font-variation-settings: "wght" 400, "opsz" 20;
  padding: 4px;
  border-radius: 100px;
}

.phone_info:hover {
  background-color: #000000;
} */
</style>
