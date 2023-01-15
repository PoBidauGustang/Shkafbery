<template>
  <form class="sign_up_form" @submit.prevent="signup">
    <fieldset class="sign_up_form_wrapper">
      <legend class="sign_up_title">Зарегестрироваться</legend>
      <div>
        <BaseInput
          InputLabelName="Ваше имя"
          type="text"
          v-model="signupUsername"
        />
      </div>
      <div>
        <BaseInput
          InputLabelName="Ваша почта"
          type="email"
          required
          v-model="signupEmail"
        />
      </div>
      <div>
        <BaseInput
          InputLabelName="Придумайте пароль"
          type="password"
          v-model="signupPassword1"
          SupportText="Пароль должен срдержать не менее 6 знаков"
        />
      </div>
      <div>
        <BaseInput
          InputLabelName="Повторите пароль"
          type="password"
          v-model="signupPassword2"
        />
      </div>
      <BaseButton class="primary" type="submit" ButtonMeta="Создать профиль" />
      <span class="sign_up_form_prompt"
        >Нажимая на кнопку "Войти", я даю своё согласие на обработку моих
        персональных данных в соответствии с законом № 152-ФЗ "О персональных
        данных" и принимаю условия Пользовательского соглашения</span
      >
    </fieldset>
  </form>
  <!-- <form class="signup" @submit.prevent="signup">
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
  <!-- <div>
    <h4>Register</h4>
    <form @submit.prevent="register">
      <label for="name">Name</label>
      <div>
        <input id="name" type="text" v-model="name" required autofocus />
      </div>
      <label for="email">E-Mail Address</label>
      <div>
        <input id="email" type="email" v-model="email" required />
      </div>
      <label for="password">Password</label>
      <div>
        <input id="password" type="password" v-model="password" required />
      </div>
      <label for="password-confirm">Confirm Password</label>
      <div>
        <input
          id="password-confirm"
          type="password"
          v-model="password_confirmation"
          required
        />
      </div>
      <div>
        <button type="submit">Register</button>
      </div>
    </form>
  </div> -->
</template>

<script>
import BaseButton from "../AllButtons/BaseButton.vue";
import BaseInput from "../AllInputs/BaseInput.vue";
import { mapActions } from "vuex";
export default {
  name: "SignUp",
  components: {
    BaseInput,
    BaseButton,
  },
  data() {
    return {
      signupEmail: "",
      signupPassword1: "",
      signupPassword2: "",
      signupUsername: "",
    };
  },
  methods: {
    ...mapActions("auth", ["registerUser"]),
    // register: function () {
    //   let data = {
    //     name: this.name,
    //     email: this.email,
    //     password: this.password,
    //     is_admin: this.is_admin,
    //   };
    //   this.registerUser(data)
    //     .then(() => this.$router.push("/"))
    //     .catch((err) => console.log(err));
    // },
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

<style scoped>
.sign_up_form {
  background-color: var(--surface-variant-light);
  border-radius: 12px;
  padding-top: 24px;
  padding-left: 16px;
  padding-right: 16px;
  padding-bottom: 16px;
}

.sign_up_form_wrapper {
  display: flex;
  flex-direction: column;
  row-gap: 24px;
}

.sign_up_form_wrapper > button {
  margin-top: 8px;
}

.sign_up_title {
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 32px;
  line-height: 40px;
  text-transform: uppercase;
  text-align: center;
  color: var(--on-surface-light);
  margin-bottom: 24px;
}

.sign_up_input_wrapper {
  display: flex;
  flex-direction: column;
  row-gap: 24px;
  margin-bottom: 32px;
}

.sign_up_form_prompt {
  font-size: 12px;
  line-height: 16px;
  color: var(--on-surface-variant-light);
}
</style>
