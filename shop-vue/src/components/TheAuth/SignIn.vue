<template>
  <form class="sign_in_form" @submit.prevent="login">
    <fieldset class="sign_in_form_wrapper">
      <legend class="sign_in_title">Войти</legend>
      <div>
        <BaseInput InputLabelName="Ваше имя" type="text" v-model="email" />
      </div>
      <div>
        <BaseInput
          InputLabelName="Ведите пароль"
          type="password"
          v-model="password"
        />
      </div>
      <BaseButton class="primary" type="submit" ButtonMeta="Войти" />
      <a class="sign_in_form_prompt">Забыли пароль?</a>
    </fieldset>
  </form>
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
    </form> -->
</template>

<script>
import BaseButton from "../AllButtons/BaseButton.vue";
import BaseInput from "../AllInputs/BaseInput.vue";
import { mapActions } from "vuex";

export default {
  name: "SignIn",
  components: {
    BaseInput,
    BaseButton,
  },
  data() {
    return {
      email: "",
      password: "",
    };
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

<style scoped>
.sign_in_form {
  background-color: var(--surface-variant-light);
  border-radius: 12px;
  padding-top: 24px;
  padding-left: 16px;
  padding-right: 16px;
  padding-bottom: 16px;
}

.sign_in_form_wrapper {
  display: flex;
  flex-direction: column;
  row-gap: 24px;
}

.sign_in_form_wrapper > button {
  margin-top: 8px;
}

.sign_in_title {
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 32px;
  line-height: 40px;
  text-transform: uppercase;
  text-align: center;
  color: var(--on-surface-light);
  margin-bottom: 24px;
}

.sign_in_input_wrapper {
  display: flex;
  flex-direction: column;
  row-gap: 24px;
  margin-bottom: 32px;
}

.sign_in_form_prompt {
  font-size: 16px;
  line-height: 24px;
  color: var(--primary-light);
}
</style>
