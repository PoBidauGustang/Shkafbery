<template>
  <div>
    <BaseMegaMenu
      v-if="isMegaMenuVisible"
      :links_list="links_list"
      @closeMegaMenu="closeMegaMenu"
    />
    <nav class="header">
      <div class="header_top">
        <ul class="top_menu">
          <li class="top_menu_input">
            <router-link class="top_menu_link" to="/about">О нас</router-link>
          </li>
          <li class="top_menu_input">
            <router-link class="top_menu_link" to="/contacts"
              >Контакты</router-link
            >
          </li>
          <li class="top_menu_input">
            <router-link class="top_menu_link" to="/services"
              >Установка</router-link
            >
          </li>
          <li class="top_menu_input">
            <router-link class="top_menu_link" to="/services"
              >Замеры</router-link
            >
          </li>
          <li class="top_menu_input">
            <router-link class="top_menu_link" to="/partners"
              >Партнерам</router-link
            >
          </li>
          <li class="top_menu_input">
            <router-link class="top_menu_link" to="/photos"
              >Фото работ</router-link
            >
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
      <div class="header_middle">
        <button class="search">
          <span class="material-icons-outlined md-24">search</span>
        </button>
        <div class="logo">
          <svg
            width="125"
            height="24"
            viewBox="0 0 125 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M0.869507 21.9999H19.9375V2.3999H16.5495V18.7239H12.0975V2.3999H8.7095V18.7239H4.2575V2.3999H0.869507V21.9999ZM32.3548 
          21.9999H36.2748L30.1708 10.9399L35.4348 2.3999H31.4588L28.1828 8.1399L27.0348 10.4359V2.3999H23.6468V21.9999H27.0348V15.8959L28.2388 
          14.0199L32.3548 21.9999ZM46.1477 21.9999H49.7317L44.9157 2.3999H41.2197L36.4037 21.9999H39.9877L40.7717 18.4439H45.3637L46.1477 
          21.9999ZM41.4717 15.1679L42.2557 11.5279C42.5357 10.1839 42.8437 8.0279 43.0117 6.7119H43.0957C43.2917 8.0279 43.5997 10.1839 43.8797 
          11.5279L44.6637 15.1679H41.4717ZM57.6655 23.8479H61.0815V21.6359H61.4735C65.3095 21.6359 68.2495 19.0319 68.2495 14.3839V10.1839C68.2495 
          5.4799 65.3095 2.7639 61.4735 2.7639H61.0815V0.691895H57.6655V2.7639H57.2735C53.4375 2.7639 50.4975 5.4799 50.4975 10.1839V14.3839C50.4975 
          19.0319 53.4375 21.6359 57.2735 21.6359H57.6655V23.8479ZM57.1055 18.3319C55.2855 18.3319 53.9415 17.2119 53.9415 14.3839V10.1839C53.9415 
          7.2439 55.2855 6.0679 57.1055 6.0679H57.6655V18.3319H57.1055ZM61.0815 18.3319V6.0679H61.6135C63.4615 6.0679 64.8055 7.2439 64.8055 
          10.1839V14.3839C64.8055 17.2119 63.4615 18.3319 61.6135 18.3319H61.0815ZM70.7328 21.9999H76.3608C80.3368 21.9999 82.3808 20.0399 
          82.3808 15.9799C82.3808 12.4239 80.3368 9.9879 76.3608 9.9879H74.1768V5.6199H81.2888V2.3999H70.7328V21.9999ZM74.1768 
          18.7239V13.2079H76.1088C77.7888 13.2079 78.8248 14.1039 78.8248 15.9799C78.8248 17.8839 77.7888 18.7239 76.1088 
          18.7239H74.1768ZM88.4502 18.7519V13.6279H94.3302V10.4919H88.4502V5.6479H94.8622V2.3999H85.0062V21.9999H95.1422V18.7519H88.4502ZM103.454 
          2.3999H98.0218V21.9999H101.466V15.4199H103.454C107.402 15.4199 109.726 13.0399 109.726 8.92389C109.726 4.80789 107.402 2.3999 103.454 
          2.3999ZM103.426 12.1719H101.466V5.6759H103.426C105.274 5.6759 106.198 6.76789 106.198 8.92389C106.198 11.0799 105.274 12.1719 103.426 
          12.1719ZM112.049 21.9999H115.465L119.413 12.9559C120.001 11.6119 120.533 10.0439 121.037 8.69989L121.121 8.7839C120.897 10.8559 
          120.757 14.0479 120.757 15.8959V21.9999H124.117V2.3999H120.673L116.501 11.9759C115.969 13.1519 115.493 14.4959 115.073 15.5879L114.989 
          15.5319C115.241 13.4039 115.409 10.4359 115.409 8.8119V2.3999H112.049V21.9999Z"
              fill="#1B1B1F"
            />
          </svg>
        </div>
        <div class="navbar_wrapper">
          <a class="cart" href="/"
            ><span class="material-icons-outlined md-24">shopping_cart</span></a
          >
          <a class="cart" href="/"
            ><span class="material-icons-outlined md-24"
              >favorite_border</span
            ></a
          >
        </div>
        <a class="login" href="/"
          ><span class="material-icons-outlined md-24">person</span
          ><span class="login_text">Войти</span></a
        >
      </div>
      <div class="header_bottom">
        <ul class="bottom_menu">
          <li class="bottom_menu_input">
            <!-- <base-mega-menu/> -->
            <a class="bottom_menu_link" @click="showMegaMenu">
              <span class="btm_link">Шкафы-купе</span>
              <span class="icon_wrapper">
                <span class="material-icons-outlined md-18">expand_more</span>
              </span>
            </a>
          </li>
          <li class="bottom_menu_input">
            <a class="bottom_menu_link" @click="showMegaMenu">
              <span class="btm_link">Двери-купе</span>
              <span class="icon_wrapper">
                <span class="material-icons-outlined md-18">expand_more</span>
              </span>
            </a>
          </li>
          <li class="bottom_menu_input">
            <router-link class="bottom_menu_link" to="/wardrobe"
              >Гардеробные</router-link
            >
          </li>
          <li class="bottom_menu_input">
            <a class="bottom_menu_link" @click="showMegaMenu">
              <span class="btm_link">Материалы</span
              ><span class="icon_wrapper">
                <span class="material-icons-outlined md-18">expand_more</span>
              </span>
            </a>
          </li>
          <li class="bottom_menu_input">
            <a class="bottom_menu_link" @click="showMegaMenu">
              <span class="btm_link">Услуги</span
              ><span class="icon_wrapper">
                <span class="material-icons-outlined md-18">expand_more</span>
              </span>
            </a>
          </li>
          <li class="bottom_menu_input">
            <router-link class="bottom_menu_link" to="/kitchen"
              >Кухни</router-link
            >
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
import BaseMegaMenu from "./BaseMegaMenu";
export default {
  name: "THeheader",
  components: {
    BaseMegaMenu,
  },
  props: {},
  data() {
    return {
      isMegaMenuVisible: false,
      links_list: [
        { id: "1", attributes: "Разде 1" },
        { id: "2", attributes: "Раздел 2" },
        { id: "3", attributes: "Раздел 3" },
      ],
    };
  },
  computed: {},
  methods: {
    showMegaMenu() {
      this.isMegaMenuVisible = true;
    },
    closeMegaMenu() {
      this.isMegaMenuVisible = false;
    },
  },
};
</script>

<style scoped>
.header {
  display: grid;
}

.header_top {
  grid-row: 1;
  display: flex;
  justify-content: space-between;
  list-style: none;
  padding-left: 48px;
  padding-right: 41px;
}

.top_menu {
  list-style: none;
  display: flex;
  padding-top: 4px;
  padding-bottom: 4px;
}

.top_menu_input {
  margin-right: 4px;
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
  color: #000000;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  text-align: center;
}

.top_menu_link:hover {
  font-weight: 700;
  background-color: #f0f0f0;
}

.phone_link {
  text-decoration: none;
  color: #000000;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  text-align: right;
}

.phone {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 4px;
  padding-bottom: 4px;
}

.phone_info {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 7px;
  border-radius: 100px;
}

.phone_info:hover {
  background-color: #f0f0f0;
}

.header_middle {
  grid-row: 2;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-column-gap: 24px;
  padding-left: 48px;
  padding-right: 48px;
  padding-top: 16px;
  padding-bottom: 16px;
}

.navbar_wrapper {
  grid-column-start: 9;
  grid-column-end: span 2;
  justify-self: end;
  display: flex;
}

.cart {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  border-radius: 100px;
  padding: 11px;
  text-decoration: none;
  color: #000000;
  border: 1px solid rgba(0, 0, 0, 1);
}

.cart:last-child {
  margin-left: 16px;
}

.cart:hover {
  background-color: #f0f0f0;
}

.login {
  grid-column-start: 11;
  grid-column-end: span 2;
  justify-self: end;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  text-decoration: none;
  color: #000000;
  padding: 11px 15px 11px 11px;
  border: 1px solid rgba(0, 0, 0, 1);
  border-radius: 16px;
}

.login:hover {
  background-color: #f0f0f0;
}

.login_text {
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  padding-left: 8px;
}

.search {
  grid-column-start: 1;
  justify-self: start;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  background-color: #ffffff;
  border: none;
  border-radius: 100px;
  padding: 12px;
}

.search:hover {
  background-color: #f0f0f0;
}

.logo {
  grid-column-start: 5;
  grid-column-end: span 4;
  justify-self: center;
  align-self: center;
}

.header_bottom {
  grid-row: 3;
  display: grid;
  height: 60px;
  border-top: 1px solid rgba(0, 0, 0, 1);
  border-bottom: 1px solid rgba(0, 0, 0, 1);
}

.bottom_menu {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  list-style: none;
}

.bottom_menu_input {
  display: grid;
  border-right: 1px solid rgba(0, 0, 0, 1);
  background: #f0f0f0;
}

.bottom_menu_input:last-child {
  border-right: 0px;
}

.icon_wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-left: 8px;
}

.bottom_menu_link {
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  color: #000000;
  font-size: 16px;
  font-weight: 500;
  line-height: 24px;
  text-align: center;
}

.bottom_menu_link:hover {
  background: #fafafa;
}

.btm_link {
  padding-left: 4px;
}
</style>
