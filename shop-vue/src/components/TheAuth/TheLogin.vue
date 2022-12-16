<template>
  <div>
    <form class="login" @submit.prevent="login">
      <h1>Sign in</h1>
      <label>Email</label>
      <input required v-model="email" type="text" placeholder="Name" />
      <label>Password</label>
      <input
        required
        v-model="password"
        type="password"
        placeholder="Password"
      />
      <hr />
      <button type="submit">Login</button>
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
    };
  },
  computed: {
    // ...mapGetters("api_urls", ["getServerAuthUrl"]),
  },
  methods: {
    ...mapActions("auth", ["loginUser"]),
    login() {
      let username = this.email;
      let password = this.password;
      this.loginUser({ username, password })
        .then(() => this.$router.push("/dashboard"))
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style></style>
