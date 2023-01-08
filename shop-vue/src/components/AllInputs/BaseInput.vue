<template>
      <div class="base_input_container">
        <input
            class="base_input"
            v-bind="$attrs"
            :value="modelValue"
            placeholder=" "
            @input="$emit('update:modelValue', $event.target.value)"
        >
        <label class="base_input_label">{{ InputLabelName }}</label>
        <slot name="InputButton"></slot>
      </div>
</template>

<script>
export default {
  name: "BaseInput",
  inheritAttrs: false,
  props: {
    InputLabelName: {
      type: String,
      default: ''
    },
    modelValue: {
      type: [String, Number],
      default: ''
    }
  }
}
</script>

<style scoped>

.base_input_container {
    position: relative;
    display: flex;
    flex-direction: column;
}

.base_input_label {
    position: absolute;
    bottom: 16px;
    left: 16px;
    font-weight: 400;
    font-size: 16px;
    line-height: 24px;
    color: var(--on-surface-light);
    pointer-events: none;
    transform-origin: 0 50%;
    transition: transform 200ms ease;
}

.base_input {
    height: 56px;
    font-size: 16px;
    line-height: 24px;
    padding-top: 24px;
    padding-left: 16px;
    padding-right: 16px;
    padding-bottom: 8px;
    border: 1px solid var(--outline-light);
    border-radius: 8px;
}

.base_input:focus ~ .base_input_label, 
.base_input:not(:placeholder-shown) ~ .base_input_label {
    font-weight: 500;
    font-size: 12px;
    line-height: 16px;
    color: var(--primary-light);
    transform: translateY(-16px);
}

.base_input:focus {
  outline-color: var(--primary-light);
}

</style>