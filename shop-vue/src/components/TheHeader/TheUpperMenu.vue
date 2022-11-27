<template>
  <div class="header_top">
    <ul class="top_menu">
      <li class="top_menu_input">
        <router-link class="top_menu_link" to="/about">О нас</router-link>
      </li>
      <li class="top_menu_input">
        <router-link class="top_menu_link" to="/contacts">Контакты</router-link>
      </li>
      <li class="top_menu_input">
        <router-link class="top_menu_link" to="/services"
          >Установка</router-link
        >
      </li>
      <li class="top_menu_input">
        <router-link class="top_menu_link" to="/services">Замеры</router-link>
      </li>
      <li class="top_menu_input">
        <router-link class="top_menu_link" to="/partners"
          >Партнерам</router-link
        >
      </li>
      <li class="top_menu_input">
        <router-link class="top_menu_link" to="/photos">Фото работ</router-link>
      </li>
      <li class="top_menu_input">
        <router-link class="top_menu_link" to="/posts">Блог</router-link>
      </li>
    </ul>
    <div class="phone">
      <a class="phone_link" href="/">+7 999 987 78 89</a>
      <div class="phone_info">
        <span class="material-icons-outlined md-18">info</span>
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
.header_top {
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

.top_menu_input {
  margin-right: 8px;
}
.top_menu_input:last-child {
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
}
</style>
