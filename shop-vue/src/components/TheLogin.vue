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
      // bla: '33sfsd'
    };
  },
  computed: {
    ...mapGetters("api_urls", ["getServerAuthUrl"]),
  },
  methods: {
    setLogin() {
      // const a = JSON.stringify(this.login)
      // const b = JSON.stringify(this.password)
      // this.login = (typeof this.login)
      // const data = JSON.stringify({username: this.login, password: this.password});
      const options = {
        headers: {
          "Content-Type": "application/json",
        },
      };
      // alert(this.login)
      // this.axios({
      //   method: 'POST',
      //   url: `${this.getServerAuthUrl}/login/`,
      //   // headers: {"Content-Type": "multipart/form-data; boundary=<calculated when request is sent>"},
      //   headers: {"Content-Type": 'multipart/form-data'},
      //   data: {
      //     username: "user1",
      //     password: "123pass1"
      //   },
      // });
      this.axios

        .post(
          `${this.getServerAuthUrl}/login/`,
          {
            // .post(`${this.getServerAuthUrl}/login`, data, options)
            // data: {
            username: "user2",
            password: "123pass2",
            // },
            // username: a,
            // password: b,
          },
          options
        )
        .then((response) => {
          alert("Спасибо что Вы с нами");
          sessionStorage.setItem(
            "auth_token",
            response.data.attributes.auth_token
          );
          this.$router.push({ name: "home" });
        })
        .catch((error) => console.log(error.response.request));
      // .catch((error) => {
      //   // if (error === 400) {
      //     console.error(error);
      //   // }
      // });
    },
  },
};
</script>

<style></style>
