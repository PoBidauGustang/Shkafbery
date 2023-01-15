<template>
  <div class="log_in_area">
    <section class="log_in_form_wrapper">
      <div class="log_in_tab_button_wrapper">
        <button
          v-for="tab in tabs"
          :key="tab"
          :class="['tab_item', { current: currentTab === tab }]"
          @click="currentTab = tab"
        >
          <span class="material-symbols-outlined">{{ tab.tabIcon }}</span>
          <span class="tab_name">{{ tab }}</span>
        </button>
      </div>
      <SignUp v-if="currentTab == tabs[1]" />
      <SignIn v-if="currentTab == tabs[0]" />
    </section>

    <!-- <form class="login" @submit.prevent="login">
      <h1>Sign in</h1>
      <label>username</label>
      <input required v-model="email" type="text" placeholder="Name" />
      <label>Password</label>
      <input
        required
        v-model="password"
        type="password"
        placeholder="Password"
      />
      <hr />
      <button type="submit">Log in</button>
    </form>
    <form class="signup" @submit.prevent="signup">
      <h1>Sign un</h1>
      <label>Username</label>
      <input v-model="signupUsername" type="text" placeholder="Name" />
      <label>Email</label>
      <input required v-model="signupEmail" type="email" placeholder="e-mail" />
      <label>Password</label>
      <input
        required
        v-model="signupPassword1"
        type="password"
        placeholder="Password"
      />
      <label>Retype password</label>
      <input
        required
        v-model="signupPassword2"
        type="password"
        placeholder="Password"
      />
      <hr />
      <button type="submit">Sign up</button>
    </form> -->
  </div>
</template>

<script>
import SignUp from "./Registration.vue";
import SignIn from "./SignIn.vue";
import { mapActions } from "vuex";
export default {
  name: "Login",
  components: {
    SignUp,
    SignIn,
  },
  data() {
    return {
      email: "",
      password: "",
      signupEmail: "",
      signupPassword1: "",
      signupPassword2: "",
      signupUsername: "",
      currentTab: "Вход",
      tabs: ["Вход", "Регистрация"],
    };
  },
  computed: {
    // ...mapGetters("api_urls", ["getServerAuthUrl"]),
  },
  methods: {
    ...mapActions("auth", ["loginUser", "registerUser"]),
    login() {
      let username = this.email;
      let password = this.password;
      this.loginUser({ username, password })
        .then(() => this.$router.push("/dashboard"))
        .catch((err) => console.log(err));
    },
    signup() {
      let username = this.signupUsername;
      let email = this.signupEmail;
      let password = this.signupPassword1;
      this.registerUser({ username, email, password })
        .then(() => console.log("Регистрация прошла"))
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style>
.log_in_area {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  padding-left: 24px;
  padding-right: 24px;
  background-color: var(--palette-neutral95);
}

.log_in_form_wrapper {
  grid-column: 5 / span 4;
  margin-top: 32px;
  margin-bottom: 32px;
}

.log_in_tab_button_wrapper {
  grid-column: 5 / span 4;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
  background-color: var(--palette-neutral98);
  border-radius: 16px;
  box-shadow: 0px 0px 0px 1px var(--outline-light);
  margin-bottom: 32px;
}

.tab_item {
  flex: 1;
  display: flex;
  flex-direction: column;
  row-gap: 4px;
  align-items: center;
  justify-content: center;
  color: var(--on-surface-variant-light);
  background-color: transparent;
  padding-left: 0px;
  padding-right: 0px;
  padding-top: 12px;
  padding-bottom: 12px;
  border-radius: 16px;
  cursor: pointer;
}

.tab_item:last-child {
  border-right: 0;
}

.tab_name {
  font-weight: 500;
  font-size: 16px;
  line-height: 24px;
}

.tab_item .material-symbols-outlined {
  transition: font-weight 0.5s ease, font-variation-settings 0.5s ease,
    transform 0.5s ease;
}

.material-symbols-outlined:empty {
  display: none;
}

.tab_item .tab_name {
  transition: font-weight 0.5s ease;
}

/* hover */
.tab_item:hover {
  background-color: var(--palette-neutral95);
  transition: background-color 0.1s;
}

.tab_item:hover .material-symbols-outlined {
  font-weight: 700;
  font-variation-settings: "WGHT" 700;
  transition: font-weight 0.2s ease, font-variation-settings 0.2s ease;
}

.tab_item:hover .tab_name {
  font-weight: 700;
  transition: font-weight 0.2s ease;
}

/* focus */
.tab_item:focus-visible {
  background-color: var(--palette-neutral95);
  transition: background-color 0.1s;
}

.tab_item:focus-visible .material-symbols-outlined {
  font-weight: 700;
  font-variation-settings: "WGHT" 700;
  transition: font-weight 0.2s ease, font-variation-settings 0.2s ease;
}

.tab_item:focus-visible .tab_name {
  font-weight: 700;
  transition: font-weight 0.2s ease;
}

/* active */
.tab_item:active {
  background-color: var(--palette-neutral90);
  transition: background-color 0.1s;
}

.tab_item:active .material-symbols-outlined {
  transform: scale(0.92);
  transition: transform 0.2s ease;
}

/* current */
.tab_item.current {
  color: var(--primary-light);
  background-color: #fff;
  box-shadow: 0px 0px 0px 1px var(--outline-light);
  transition: box-shadow 0.1s ease;
  z-index: 2;
}

.tab_item.current .material-symbols-outlined {
  font-variation-settings: "FILL" 1;
}

.tab_item.current .tab_name {
  font-weight: 700;
}

@media (max-width: 1239px) {
  .tab_item {
    padding-top: 10px;
    padding-bottom: 10px;
  }

  .tab_name {
    font-size: 14px;
    line-height: 20px;
  }
}
</style>
