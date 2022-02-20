<template>
  <div class="MegaMenu_wrapper" ref="MegaMenu_wrapper">
    <div class="MegaMenu">
      <ul class="MegaMenu_List">
        <li class="MegaMenu_Category" v-for="link in links_list" :key="link.id">
          <span class="MegaMenu_input">{{ link.attributes }}</span>
          <div class="Mega_Menu_Image_Wrapper">
            <img src="" class="MegaMenu_Image" />
          </div>
        </li>
      </ul>
      <div class="Mega_Menu_Conf"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MegaMenu",
  props: {
    links_list: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {};
  },
  methods: {
    closeMegaMenu() {
      this.$emit("closeMegaMenu");
    },
  },
  mounted() {
    let vm = this;
    document.addEventListener("click", function (item) {
      if (item.target === vm.$refs["MegaMenu_wrapper"]) {
        vm.closeMegaMenu();
      }
    });
  },
};
</script>

<style>
.MegaMenu_wrapper {
  background: rgba(64, 64, 64, 0.4);
  position: fixed;
  right: 0;
  left: 0;
  top: 180px;
  bottom: 0;
  width: 100vw;
}

.MegaMenu {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  background-color: #f0f0f0;
  grid-column-gap: 24px;
  position: fixed;
  top: 180px;
  padding-top: 32px;
  padding-bottom: 48px;
  padding-left: 48px;
  padding-right: 48px;
  width: 100%;
}

.MegaMenu_List {
  grid-column: span 9;
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  grid-column-gap: 24px;
  grid-auto-rows: max-content;
}

.MegaMenu_Category {
  grid-column: span 3;
  display: flex;
  flex-direction: column-reverse;
  background-color: #ffffff;
  padding: 16px;
  border-radius: 12px;
}

.MegaMenu_input {
  color: #1e1b16;
  font-size: 16px;
  font-weight: 700;
  line-height: 24px;
}

.Mega_Menu_Image_Wrapper {
  aspect-ratio: 16 / 9;
  min-height: 0;
  padding-bottom: 16px;
}

.MegaMenu_Image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.Mega_Menu_Conf {
  grid-column: 10 / span 3;
  display: flex;
  flex-direction: column;
  padding-top: 12px;
  padding-bottom: 16px;
  padding-left: 16px;
  padding-right: 16px;
  background-color: #ffffff;
  border-radius: 12px;
}
</style>
