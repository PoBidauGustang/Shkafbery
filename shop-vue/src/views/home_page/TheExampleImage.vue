<template>
  <div>
    <h4>название фото:{{ image_name }}</h4>
    <p>{{ image }}</p>
    <p>alt_text: {{ image_alt_text }}</p>
  </div>
</template>

<script>
export default {
  name: "TheExampleImage",
  data() {
    return {
      imagesList: [],
    };
  },
  props: {
    image_name: {
      type: String,
      default() {
        return "";
      },
    },
    image: {
      type: String,
      default() {
        return "";
      },
    },
    image_alt_text: {
      type: String,
      default() {
        return "";
      },
    },
  },
};
</script>

<style></style>
