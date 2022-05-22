<template>
  <div class="the-select">
    <p class="title" @click="areOptionsVisible = !areOptionsVisible">
      {{ selected }}
    </p>
    <div class="options" v-if="areOptionsVisible">
      <p
        v-for="option in options"
        :key="option.value"
        @click="selectOption(option)"
      >
        {{ option.name }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "the-select",
  props: {
    options: {
      type: Array,
      default() {
        return [];
      },
    },
    selected: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      areOptionsVisible: false,
    };
  },
  methods: {
    selectOption(option) {
      this.$emit("select", option);
      this.areOptionsVisible = false;
    },
    hideSelect() {
      this.areOptionsVisible = false;
    },
  },
  mounted() {
    document.addEventListener("click", this.hideSelect.bind(this), true);
  },
  beforeUnmount() {
    document.removeEventListener("click", this.hideSelect);
  },
};
</script>

<style>
.the-select {
  position: relative;
  width: 200px;
  cursor: pointer;
}

.title {
  border: solid 1px #aeaeae;
}
.the-select p {
  margin: 0;
}

.options {
  border: solid 1px #aeaeae;
  position: absolute;
  top: 30px;
  right: 0;
  width: 100%;
}
.options p:hover {
  background: #e7e7e7;
}
</style>
