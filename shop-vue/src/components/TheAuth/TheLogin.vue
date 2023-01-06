<template>
  <div>
    <form class="login" @submit.prevent="login">
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
    </form>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
      signupEmail: "",
      signupPassword1: "",
      signupPassword2: "",
      signupUsername: "",
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

<style></style>
