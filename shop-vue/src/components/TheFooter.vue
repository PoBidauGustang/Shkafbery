<template>
  <section class="footer_area">
    <div class="footer_list_wrapper">
      <ul class="footer_list">
        <li class="footer_item_title">Покупателям</li>
        <li>
          <a class="footer_item_link" href="#/products_catalog"
            >Каталог товаров</a
          >
        </li>
        <li>
          <a class="footer_item_link" href="#/faq">Частые вопросы</a>
        </li>
        <li>
          <a class="footer_item_link" href="#/assembly">Сборка и установка</a>
        </li>
        <li>
          <a class="footer_item_link" href="#/measurements">Замеры</a>
        </li>
        <li>
          <a class="footer_item_link" href="#/photos">Примеры работ</a>
        </li>
        <li>
          <a class="footer_item_link" href="#/partners">Партнерам</a>
        </li>
      </ul>
      <ul class="footer_list">
        <li class="footer_item_title">Помощь</li>
        <li>
          <a class="footer_item_link">Что такое сookies?</a>
        </li>
        <li>
          <a class="footer_item_link">Договор оферты</a>
        </li>
        <li>
          <a class="footer_item_link">Доставка и оплата</a>
        </li>
        <li>
          <a class="footer_item_link">Обмен и возврат</a>
        </li>
        <li>
          <a class="footer_item_link">Политика конфиденциальности</a>
        </li>
      </ul>
      <ul class="footer_list">
        <li class="footer_item_title">О компании</li>
        <li>
          <a class="footer_item_link" href="#/contacts">Контакты</a>
        </li>
        <li>
          <a class="footer_item_link" href="#/posts">Блог</a>
        </li>
        <li>
          <a class="footer_item_link" href="#/about">О нас</a>
        </li>
      </ul>
    </div>
    <div class="footer_area_contact_wrapper">
      <form class="footer_area_contact_form">
        <fieldset>
          <legend class="footer_area_contact_form_title">
            Подписка на акции и новости
          </legend>
          <div class="footer_area_form_input_wrapper">
            <input
              class="footer_area_form_input"
              type="email"
              id="mail"
              placeholder=" "
              required
            />
            <label class="footer_area_form_input_label" for="mail"
              >Ваша почта</label
            >
            <button class="footer_area_input_submit">
              <span class="material-symbols-outlined">send</span>
            </button>
          </div>
          <span class="footer_area_input_prompt"
            >Отправляя свой e-mail, вы соглашаетесь с политикой
            конфиденциальности</span
          >
        </fieldset>
      </form>
      <ul class="footer_area_contacts">
        <li class="footer_area_contacts_title">
          Мы на связи
          <span class="footer_area_contacts_prompt"
            >Ежедневно с 9:00 до 20:00</span
          >
        </li>
        <li>
          <a class="footer_item_link_wrapper">
            <span class="material-symbols-outlined">call</span>
            <span class="footer_item_link">+7 999 987 78 89</span>
          </a>
        </li>
        <li>
          <a class="footer_item_link_wrapper">
            <span class="material-symbols-outlined">mail</span>
            <span class="footer_item_link">contact@shkafbrerry.ru</span>
          </a>
        </li>
        <li>
          <a class="footer_item_link_wrapper">
            <span class="material-symbols-outlined">location_on</span>
            <span class="footer_item_link"
              >Санкт-Петербург, Рижская ул., д.9 к.2</span
            >
          </a>
        </li>
      </ul>
      <ul class="footer_socials">
        <li>
          <a class="footer_social_link"> </a>
        </li>
        <li>
          <a class="footer_social_link"> </a>
        </li>
        <li>
          <a class="footer_social_link"> </a>
        </li>
      </ul>
    </div>
    <div class="footer_prompt_info">
      <span class="footer_area_contacts_prompt">© 2022 Шкафбери</span>
    </div>
  </section>
</template>

<script>
export default {
  name: "The-Footer",
};
</script>

<style>
.footer_area {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  padding-left: 24px;
  padding-right: 24px;
  background-color: var(--surface-dark);
}

.footer_list_wrapper {
  grid-column: span 6;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-column-gap: 32px;
  grid-row-gap: 48px;
  padding-left: 16px;
  padding-top: 48px;
  padding-right: 16px;
  padding-bottom: 48px;
  border-right: 1px solid var(--outline-dark);
}

.footer_list {
  grid-column: span 2;
  display: flex;
  flex-direction: column;
  list-style: none;
  gap: 12px;
}

.footer_item_title {
  font-weight: 700;
  font-size: 16px;
  line-height: 24px;
  color: var(--on-surface-variant-dark);
  margin-bottom: 8px;
}

.footer_item_link {
  font-weight: 500;
  font-size: 16px;
  line-height: 24px;
  color: var(--on-surface-dark);
}
.footer_item_link:hover {
  font-weight: 700;
  color: var(--primary-dark);
  text-decoration: underline;
  text-decoration-color: var(--primary-dark);
}

.footer_area_contact_wrapper {
  grid-column: 7 / span 6;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-column-gap: 32px;
  grid-row-gap: 48px;
  padding-left: 16px;
  padding-top: 48px;
  padding-right: 16px;
  padding-bottom: 48px;
}

.footer_area_contact_form {
  grid-row: 1;
  grid-column: span 3;
}

.footer_area_contact_form_title {
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 32px;
  line-height: 40px;
  text-transform: uppercase;
  color: var(--on-surface-dark);
  margin-bottom: 24px;
}

.footer_area_form_input_wrapper {
  position: relative;
  display: flex;
  flex-direction: column;
}

.footer_area_form_input_label {
  position: absolute;
  bottom: 16px;
  left: 16px;
  font-weight: 400;
  font-size: 16px;
  line-height: 24px;
  color: var(--on-surface-dark);
  pointer-events: none;
  transform-origin: 0 50%;
  transition: transform 200ms;
}

.footer_area_form_input {
  height: 56px;
  font-size: 16px;
  line-height: 24px;
  padding-top: 24px;
  padding-left: 16px;
  padding-right: 16px;
  padding-bottom: 8px;
  background-color: var(--surface-variant-dark);
  border: 1px solid var(--outline-dark);
  border-radius: 8px;
}

.footer_area_form_input:focus ~ .footer_area_form_input_label,
.footer_area_form_input:not(:placeholder-shown)
  ~ .footer_area_form_input_label {
  font-weight: 500;
  font-size: 12px;
  line-height: 16px;
  transform: translateY(-16px);
}

.footer_area_form_input:focus {
  outline-color: var(--primary-dark);
}

.footer_area_input_prompt {
  font-size: 12px;
  line-height: 16px;
  margin-top: 4px;
  color: var(--on-surface-variant-dark);
}

.footer_area_input_submit {
  position: absolute;
  top: 8px;
  right: 8px;
  z-index: 3;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 8px;
  color: var(--on-surface-variant-dark);
}

.footer_area_contacts {
  grid-column: span 3;
  grid-row: 2;
  display: flex;
  flex-direction: column;
  row-gap: 12px;
  list-style: none;
}

.footer_area_contacts_title {
  display: flex;
  flex-direction: column;
  font-weight: 700;
  font-size: 16px;
  line-height: 24px;
  color: var(--on-surface-dark);
  margin-bottom: 8px;
}

.footer_area_contacts_prompt {
  font-weight: 400;
  font-size: 12px;
  line-height: 16px;
  color: var(--on-surface-variant-dark);
}

.footer_item_link_wrapper {
  display: flex;
  column-gap: 8px;
  color: var(--on-surface-dark);
}

.footer_prompt_info {
  grid-row: 2;
  grid-column: span 12;
  display: flex;
  justify-content: center;
  padding-top: 16px;
  padding-bottom: 16px;
  margin-left: -24px;
  margin-right: -24px;
  padding-left: 40px;
  padding-right: 40px;
  border-top: 1px solid var(--outline-dark);
}

.footer_socials {
  grid-row: 1;
  grid-column: 4 / span 3;
  display: flex;
  justify-content: end;
  gap: 8px;
  list-style: none;
}

.footer_social_link {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
  border: 1px solid var(--outline-dark);
  border-radius: 100px;
}

@media (max-width: 1239px) {
  .footer_area {
    padding-left: 16px;
    padding-right: 16px;
  }

  .footer_item_title {
    font-size: 14px;
    line-height: 20px;
  }

  .footer_list {
    grid-column: span 3;
  }

  .footer_item_link {
    font-size: 14px;
    line-height: 20px;
  }

  .footer_area_contact_form {
    grid-column: span 6;
  }

  .footer_area_contact_form_title {
    font-size: 28px;
    line-height: 36px;
  }

  .footer_area_contacts {
    grid-column: span 6;
  }

  .footer_area_contacts_title {
    font-size: 14px;
    line-height: 20px;
  }

  .footer_item_link_wrapper .material-symbols-outlined {
    font-size: 20px;
    font-variation-settings: "OPSZ" 20;
  }

  .footer_prompt_info {
    margin-left: -16px;
    margin-right: -16px;
    padding-left: 32px;
    padding-right: 32px;
    padding-bottom: 88px;
  }

  .footer_socials {
    grid-row: 3;
    grid-column: span 6;
    justify-content: start;
  }
}

@media (max-width: 904px) {
  .footer_area {
    grid-template-columns: repeat(8, 1fr);
  }

  .footer_list_wrapper {
    grid-column: span 4;
    grid-template-columns: repeat(4, 1fr);
  }

  .footer_list {
    grid-column: span 2;
  }

  .footer_item_link {
    overflow-wrap: break-word;
  }

  .footer_area_contact_wrapper {
    grid-column: 5 / span 4;
    grid-template-columns: repeat(4, 1fr);
  }

  .footer_area_contact_form {
    grid-column: span 4;
  }

  .footer_area_contacts {
    grid-column: span 4;
  }

  .footer_prompt_info {
    grid-column: span 8;
  }

  .footer_socials {
    grid-column: span 4;
  }
}

@media (max-width: 599px) {
  .footer_area {
    grid-template-columns: repeat(4, 1fr);
    padding-left: 0px;
    padding-right: 0px;
  }

  .footer_list_wrapper {
    grid-column: span 4;
    grid-template-columns: repeat(4, 1fr);
    padding-bottom: 32px;
    border-right: 0px;
    border-bottom: 1px solid var(--outline-dark);
  }

  .footer_area_contact_wrapper {
    grid-row: 2;
    grid-column: span 4;
    grid-template-columns: repeat(4, 1fr);
    padding-top: 32px;
  }

  .footer_prompt_info {
    grid-row: 3;
    grid-column: span 4;
    margin-left: 0px;
    margin-right: 0px;
    padding-left: 16px;
    padding-right: 16px;
  }

  .footer_socials {
    justify-content: center;
  }
}
</style>
