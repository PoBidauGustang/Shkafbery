<template>
  <div class="header_middle_wrapper">
    <button class="header_middle_search_button">
      <span class="material-symbols-outlined">search</span>
    </button>
    <div class="header_middle_logo_wrapper">
      <svg
        width="216"
        height="48"
        viewBox="0 0 216 48"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M10.001 40H40.5098V8.64003H35.089V34.7584H27.9658V8.64003H22.545V34.7584H15.4218V8.64003H10.001V40ZM60.3775 40H66.6495L56.8831 22.3041L65.3055 8.64003H58.9438L53.7022 17.824L51.8655 21.4977V8.64003H46.4446V40H51.8655V30.2337L53.7919 27.232L60.3775 40ZM82.4461 40H88.1805L80.4749 8.64003H74.5613L66.8557 40H72.5901L73.8445 34.3104H81.1917L82.4461 40ZM74.9645 29.0688L76.2189 23.2449C76.6669 21.0945 77.1597 17.6448 77.4285 15.5392H77.5629C77.8765 17.6448 78.3693 21.0945 78.8173 23.2449L80.0717 29.0688H74.9645ZM100.875 42.9568H106.34V39.4176H106.967C113.105 39.4176 117.809 35.2512 117.809 27.8145V21.0945C117.809 13.5681 113.105 9.22243 106.967 9.22243H106.34V5.90723H100.875V9.22243H100.247C94.1098 9.22243 89.4058 13.5681 89.4058 21.0945V27.8145C89.4058 35.2512 94.1098 39.4176 100.247 39.4176H100.875V42.9568ZM99.9785 34.1313C97.0666 34.1313 94.9162 32.3392 94.9162 27.8145V21.0945C94.9162 16.3905 97.0666 14.5089 99.9785 14.5089H100.875V34.1313H99.9785ZM106.34 34.1313V14.5089H107.191C110.148 14.5089 112.299 16.3905 112.299 21.0945V27.8145C112.299 32.3392 110.148 34.1313 107.191 34.1313H106.34ZM121.782 40H130.787C137.148 40 140.419 36.864 140.419 30.3681C140.419 24.6784 137.148 20.7808 130.787 20.7808H127.293V13.792H138.672V8.64003H121.782V40ZM127.293 34.7584V25.9329H130.384C133.072 25.9329 134.729 27.3664 134.729 30.3681C134.729 33.4144 133.072 34.7584 130.384 34.7584H127.293ZM150.13 34.8033V26.6049H159.538V21.5872H150.13V13.8369H160.39V8.64003H144.619V40H160.837V34.8033H150.13ZM174.136 8.64003H165.444V40H170.956V29.472H174.136C180.453 29.472 184.171 25.6641 184.171 19.0785C184.171 12.4929 180.453 8.64003 174.136 8.64003ZM174.091 24.2752H170.956V13.8816H174.091C177.048 13.8816 178.527 15.6288 178.527 19.0785C178.527 22.528 177.048 24.2752 174.091 24.2752ZM187.888 40H193.354L199.671 25.5297C200.611 23.3793 201.462 20.8704 202.269 18.72L202.403 18.8544C202.045 22.1697 201.821 27.2769 201.821 30.2337V40H207.197V8.64003H201.687L195.011 23.9616C194.16 25.8432 193.398 27.9936 192.726 29.7408L192.592 29.6512C192.995 26.2464 193.264 21.4977 193.264 18.8992V8.64003H187.888V40Z"
          fill="white"
        />
      </svg>
    </div>
    <ul class="header_middle_bar_wrapper">
      <li class="header_middle_bar_item">
        <a href="/#/cart">
          <span class="material-symbols-outlined">shopping_cart</span
          ><span class="header_middle_bar_item_lnk">Корзина</span>
        </a>
      </li>
      <li class="header_middle_bar_item">
        <a href="/">
          <span class="material-symbols-outlined">favorite</span
          ><span class="header_middle_bar_item_lnk">Избранное</span>
        </a>
      </li>
      <li class="header_middle_bar_item">
        <a href="/#/dashboard">
          <span class="material-symbols-outlined">person</span
          ><span class="header_middle_bar_item_lnk">Войти</span>
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "MiddleMenu",
  data() {
    return {};
  },
  computed: {},
  methods: {},
};
</script>

<style>
.header_middle_wrapper {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  align-items: center;
  background-color: #000000;
  padding-left: 24px;
  padding-right: 24px;
  max-height: 80px;
}

.header_middle_search_button {
  display: flex;
  justify-content: center;
  align-items: center;
  justify-self: start;
  color: #ffffff;
  padding: 8px;
  border-radius: 100px;
  margin-left: 16px;
}

.header_middle_logo_wrapper {
  justify-content: center;
  grid-column: 5 / 9;
  display: flex;
}

.header_middle_bar_wrapper {
  grid-column: 10 / 13;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  list-style: none;
}

.header_middle_bar_item {
  grid-column: span 1;
}

.header_middle_bar_item a {
  grid-column: span 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  padding-top: 16px;
  padding-bottom: 16px;
}

.header_middle_bar_item_lnk {
  padding-top: 8px;
  font-weight: 500;
  font-size: 12px;
  line-height: 16px;
  text-align: center;
}
</style>
