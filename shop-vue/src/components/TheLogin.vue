<template>
  <div>
    <input v-model="login" type="text" placeholder="Логин" />
    <input v-model="password" type="password" placeholder="Пароль" />
    <button @click="setLogin">Войти</button>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Login",
  data() {
    return {
      login: "",
      password: "",
    };
  },
  computed: {
    ...mapGetters("api_urls", ["getServerAuthUrl"]),
  },
  methods: {
    setLogin() {
      const options = {
        headers: {
          "Content-Type": "application/json",
        },
      };
      this.axios

        .post(
          `${this.getServerAuthUrl}/login/`,
          {
            username: this.login,
            password: this.password,
          },
          options
        )
        .then((response) => {
          sessionStorage.setItem(
            "auth_token",
            response.data.data.attributes.auth_token
          );
          this.$router.push({ name: "wardrobe" });
          alert("Мы здесь");
        })
        .catch((error) => console.log(error, error.response));
    },
  },
};
</script>

<style></style>
