<template>
  <div>
    <form class="product_card_form_wrapper">
      <fieldset
        class="product_card_form_section"
        v-if="!Object.keys(GETUSERDATA).length"
      >
        <legend class="product_card_form_section_header">Ваши данные</legend>
        <div class="product_card_form_input_wrapper">
          <BaseInput InputLabelName="Ваше имя" type="text" v-model="name" />
        </div>
        <div class="product_card_form_input_wrapper">
          <BaseInput InputLabelName="Ваша почта" type="email" v-model="email" />
        </div>
        <div class="product_card_form_input_wrapper">
          <BaseInput InputLabelName="Ваш телефон" type="tel" v-model="phone" />
        </div>
      </fieldset>
      <fieldset class="product_card_form_section" v-else>
        <legend class="product_card_form_section_header">Ваши данные</legend>
        <div class="product_card_form_input_wrapper">
          <BaseInput InputLabelName="Ваше имя" type="text" v-model="name" />
        </div>
        <div class="product_card_form_input_wrapper">
          <BaseInput InputLabelName="Ваша почта" type="email" v-model="email" />
        </div>
        <div class="product_card_form_input_wrapper">
          <BaseInput InputLabelName="Ваш телефон" type="tel" v-model="phone" />
        </div>
      </fieldset>
      <fieldset class="product_card_form_section">
        <legend class="product_card_form_section_header">
          Дополнительные услуги
        </legend>
        <div class="product_card_form_services_wrapper">
          <ToggleInputOutline />
        </div>
      </fieldset>
      <fieldset class="product_card_form_section">
        <legend class="product_card_form_section_header">
          Способ доставки
        </legend>
        <p class="product_card_form_delivery_info">
          Доставка осуществляется по Санкт-Петербургу и некоторым населенным
          пунктам Ленинградской области. Узнать подробную информацию о зонах и
          условиях доставки можно в разделе доставка
        </p>
        <!-- <div> -->
        <label class="product_card_form_delivery_input radio_input_store_area">
          <div class="radio_input_store_header_wrapper">
            <div class="radio_input_store_header">
              <span class="radio_input_store_header_name">Доставка</span>
              <span class="radio_input_store_header_meta"
                >3-5 рабочих дней</span
              >
            </div>
            <input
              class="radio_input_store_input"
              type="radio"
              value="Доставка"
              id="delivery"
              v-model="delivery"
            />
          </div>
          <span class="radio_input_store_price">От 1000 ₽</span>
        </label>
        <label class="product_card_form_delivery_input radio_input_store_area">
          <div class="radio_input_store_header_wrapper">
            <div class="radio_input_store_header">
              <span class="radio_input_store_header_name">Самовывоз</span>
              <span class="radio_input_store_header_meta">ул.КАКАЯ_ТО</span>
            </div>
            <input
              class="radio_input_store_input"
              type="radio"
              value="Самовывоз"
              id="delivery"
              v-model="delivery"
            />
          </div>
          <span class="radio_input_store_price">Бесплатно</span>
        </label>
      </fieldset>
      <fieldset
        class="product_card_form_section"
        v-if="delivery === 'Доставка'"
      >
        <legend class="product_card_form_section_header">Адрес доставки</legend>
        <div class="product_card_form_large_input_wrapper">
          <BaseInput InputLabelName="Ваш адрес" type="text" v-model="address" />
        </div>
        <div class="product_card_form_input_wrapper small_input">
          <BaseInput
            InputLabelName="Кв. / офис"
            type="text"
            v-model="appartment"
          />
        </div>
        <div class="product_card_form_input_wrapper small_input">
          <BaseInput InputLabelName="Этаж" type="number" v-model="floor" />
        </div>
      </fieldset>
      <div class="product_card_form_submit_button_wrapper">
        <BaseIconButton
          class="primary"
          @click="
            (orderCompleteVisability = !orderCompleteVisability), sendOrder()
          "
          ButtonMeta="Перейти к оплате"
          ButtonIcon="shopping_cart"
        />
        <div v-if="orderCompleteVisability">Заказ оформлен</div>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import BaseIconButton from "../../components/AllButtons/BaseIconButton.vue";
import BaseInput from "../../components/AllInputs/BaseInput.vue";
import ToggleInputOutline from "../../components/AllInputs/ToggleInput.vue";
export default {
  name: "Product-Cart-Form",
  components: {
    ToggleInputOutline,
    BaseInput,
    BaseIconButton,
  },
  data() {
    return {
      orderCompleteVisability: false,
      name: localStorage.getItem("user_data")
        ? JSON.parse(localStorage.getItem("user_data")).attributes.username
        : "",
      phone: "",
      email: localStorage.getItem("user_data")
        ? JSON.parse(localStorage.getItem("user_data")).attributes.email
        : "",
      address: "",
      appartment: "",
      floor: "",
      delivery: "",
    };
  },
  computed: {
    ...mapGetters("auth", ["GETUSERDATA"]),
    // loggedUserData() {
    //   if (Object.keys(this.GETUSERDATA).length) {
    //     return "dsfsafd"
    //   }
    //   else {
    //     return ""
    //   }
    // },
  },
  methods: {
    sendOrder() {
      console.log("start");
      let token = localStorage.getItem("token");
      const options = {
        headers: {
          "Content-Type": "application/json",
          Authorization: "Token " + token,
          Accept: "application/json",
        },
      };
      const data = {
        user: "1",
        full_name: "aaaaaaa aaaaaaaa",
        email: "123ss@sss.com",
        address: "aaaaaaa aaaaaaaa",
        town: "aaaaaaa aaaaaaaa",
        phone: "11111111",
        total_order_price: "11111111",
        payment_option: "наличка",
        billing_status: false,
      };
      this.axios
        .post(`${this.getServerOrdersUrl}/orders_list/`, data, options)
        .then((response) => {
          console.log(response.data.data);
        })
        .catch(function (error) {
          console.error(error);
        });
      console.log("end");
    },
  },
};
</script>

<style>
.product_card_form_wrapper {
  display: flex;
  flex-direction: column;
  padding-left: 16px;
  padding-right: 16px;
  row-gap: 48px;
}

.product_card_form_section {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-column-gap: 32px;
  grid-row-gap: 24px;
}

.product_card_form_section_header {
  grid-column: span 6;
  font-weight: 500;
  font-size: 24px;
  line-height: 32px;
  margin-bottom: 24px;
  color: var(--on-surface-light);
}

.product_card_form_input_wrapper {
  grid-column: span 3;
  position: relative;
  display: flex;
  flex-direction: column;
}

.product_card_form_services_wrapper {
  grid-column: span 6;
}

.product_card_form_delivery_info {
  grid-column: span 6;
  font-size: 14px;
  line-height: 20px;
  margin: 0;
}

.product_card_form_delivery_input {
  grid-column: span 3;
}

.product_card_form_large_input_wrapper {
  grid-column: span 6;
  position: relative;
  display: flex;
  flex-direction: column;
}

@media (max-width: 904px) {
  .product_card_form_section {
    grid-template-columns: repeat(8, 1fr);
  }

  .product_card_form_section_header {
    grid-column: span 8;
  }

  .product_card_form_input_wrapper {
    grid-column: span 4;
  }

  .product_card_form_services_wrapper {
    grid-column: span 8;
  }

  .product_card_form_delivery_info {
    grid-column: span 8;
  }

  .product_card_form_delivery_input {
    grid-column: span 4;
  }

  .product_card_form_large_input_wrapper {
    grid-column: span 8;
  }
}

@media (max-width: 599px) {
  .product_card_form_section {
    grid-template-columns: repeat(4, 1fr);
  }

  .product_card_form_section_header {
    grid-column: span 4;
  }

  .product_card_form_input_wrapper {
    grid-column: span 4;
  }

  .product_card_form_services_wrapper {
    grid-column: span 4;
  }

  .product_card_form_delivery_info {
    grid-column: span 4;
  }

  .product_card_form_delivery_input {
    grid-column: span 4;
  }

  .product_card_form_large_input_wrapper {
    grid-column: span 4;
  }

  .small_input {
    grid-column: span 2;
  }
}

.radio_input_store_area {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 12px 16px 16px 16px;
  background-color: rgb(255, 255, 255);
  border-radius: 12px;
}

.radio_input_store_area:hover {
  box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.3),
    0px 1px 3px 1px rgba(0, 0, 0, 0.15);
}

.radio_input_store_header_wrapper {
  display: flex;
  justify-content: space-between;
  column-gap: 16px;
  margin-bottom: 32px;
}

.radio_input_store_header {
  display: flex;
  flex-direction: column;
  row-gap: 4px;
}

.radio_input_store_header_name {
  font-weight: 700;
  font-size: 16px;
  line-height: 24px;
  color: var(--on-surface-light);
}

.radio_input_store_header_meta {
  font-size: 14px;
  line-height: 20px;
  color: var(--on-surface-variant-light);
}

.radio_input_store_price {
  font-weight: 500;
  font-size: 16px;
  line-height: 24px;
  color: var(--on-surface-light);
}

.radio_input_store_input {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  margin: 0px;
  width: 24px;
  height: 24px;
}

.radio_input_store_input::after {
  font-family: "Material Symbols Outlined";
  content: "radio_button_unchecked";
  font-variation-settings: "wght" 400, "opsz" 24;
  font-size: 24px;
  line-height: 1;
  color: var(--on-surface-variant-light);
}

.radio_input_store_input:hover::after {
  font-variation-settings: "wght" 700;
}

.radio_input_store_input:checked::after {
  font-family: "Material Symbols Outlined";
  content: "radio_button_checked";
  font-size: 24px;
  line-height: 1;
  color: var(--primary-light);
}

.radio_input_store_input:checked:hover::after {
  font-variation-settings: "wght" 700;
}
</style>
