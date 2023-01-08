<template>
    <div v-if="isOpen" @click="close" class="back_drop">
        <slot name="MyComponent"></slot>
    </div>
</template>


<script>


export default {
    name: "BaseModal",
    components: {
    
  },

  props: {
    isOpen: {
    type: Boolean,
    },
  },

  emits: {
    close: null,
  },

  mounted() {
    document.addEventListener("keydown", this.handleKeydown);
  },
  beforeUnmount() {
    document.removeEventListener("keydown", this.handleKeydown);
  },

  methods: {
    handleKeydown(e) {
      if (this.isOpen && e.key === "Escape") {
        this.close();
      }
    },


    close() {
      this.$emit("close");
    },
  },
}

</script>


<style scoped>

.back_drop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 100;
  background-color: rgba(0, 0, 0, 0.8);
}


</style>