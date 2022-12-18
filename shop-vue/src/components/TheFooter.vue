<template>
  <section class="footer_area">
    <div class="footer_area_items_wrapper">
      <ul class="footer_items_wrapper">
        <li class="footer_item_title">Покупателям</li>
        <li>
          <a class="footer_item_link">Каталог товаров</a>
        </li>
        <li>
          <a class="footer_item_link">Частые вопросы</a>
        </li>
        <li>
          <a class="footer_item_link">Сборка и установка</a>
        </li>
        <li>
          <a class="footer_item_link">Замеры</a>
        </li>
        <li>
          <a class="footer_item_link">Примеры работ</a>
        </li>
        <li>
          <a class="footer_item_link">Партнерам</a>
        </li>
      </ul>
      <ul class="footer_items_wrapper">
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
      <ul class="footer_items_wrapper">
        <li class="footer_item_title">О компании</li>
        <li>
          <a class="footer_item_link">Контакты</a>
        </li>
        <li>
          <a class="footer_item_link">Блог</a>
        </li>
        <li>
          <a class="footer_item_link">О нас</a>
        </li>
      </ul>
    </div>
    <div class="footer_area_contact_wrapper">
      <form class="footer_area_contact_form">
        <fieldset>
          <legend class="footer_area_contact_form_title">
            Подписка на акции и новости
          </legend>
          <div class="footer_area_form_input">
            <label for="mail">Ваша почта</label>
            <div class="test_submit">
              <input type="email" name="mail" id="mail" required />
              <button class="footer_area_input_submit">
                <span class="material-symbols-outlined">send</span>
              </button>
            </div>
            <span class="footer_area_input_prompt"
              >Отправляя свой e-mail вы соглашаетесь с политикой
              конфиденциальности</span
            >
          </div>
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
          <a class="footer_social_link"></a>
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
  name: "TheFooter",
};
</script>

<style>
.test_submit {
  display: flex;
}

.footer_area {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  padding-left: 24px;
  padding-right: 24px;
  padding-bottom: 16px;
  background-color: #f0f0f0;
}

.footer_area_items_wrapper {
  grid-column: span 6;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-column-gap: 32px;
  padding-left: 16px;
  padding-top: 48px;
  padding-right: 16px;
  padding-bottom: 48px;
  border-right: 1px solid;
}

.footer_items_wrapper {
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
  margin-bottom: 8px;
}

.footer_item_link {
  font-weight: 500;
  font-size: 16px;
  line-height: 24px;
}

.footer_area_contact_wrapper {
  grid-column: 7 / span 6;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-column-gap: 32px;
  padding-left: 16px;
  padding-top: 48px;
  padding-right: 16px;
  padding-bottom: 48px;
}

.footer_area_contact_form {
  grid-column: span 3;
  margin-bottom: 64px;
}

.footer_area_contact_form_title {
  font-family: "Akrobat", sans-serif;
  font-weight: 800;
  font-size: 32px;
  line-height: 40px;
  text-transform: uppercase;
  margin-bottom: 24px;
}

.footer_area_form_input {
  display: flex;
  flex-direction: column;
}

.footer_area_form_input label {
  margin-bottom: 8px;
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
}

.footer_area_form_input input {
  width: 100%;
  font-size: 16px;
  line-height: 24px;
  padding: 16px;
  border: 1px solid;
  border-radius: 8px;
  background-color: #fafafa;
}

.footer_area_input_prompt {
  font-size: 12px;
  line-height: 16px;
  margin-top: 4px;
}

.footer_area_input_submit {
  position: relative;
  top: 0px;
  right: 48px;
  z-index: 1;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 8px;
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
  margin-bottom: 8px;
}

.footer_area_contacts_prompt {
  font-weight: 400;
  font-size: 12px;
  line-height: 16px;
}

.footer_item_link_wrapper {
  display: flex;
  gap: 8px;
}

.footer_prompt_info {
  grid-row: 3;
  grid-column: span 12;
  display: flex;
  justify-content: center;
  padding-top: 16px;
  border-top: 1px solid;
}

.footer_socials {
  grid-column: 4 / span 3;
  grid-row: 1;
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
  border: 1px solid;
  border-radius: 100px;
}
</style>
