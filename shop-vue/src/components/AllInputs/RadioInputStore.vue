<template>
    <label class="radio_input_store_area">
        <div class="radio_input_store_header_wrapper">
            <div class="radio_input_store_header">
                <span class="radio_input_store_header_name">{{ InputOptionName }}</span>
                <span class="radio_input_store_header_meta">{{ InputOptionMeta }}</span>
            </div>
            <input class="radio_input_store_input" type="radio" name="InputOption">
        </div>
        <span class="radio_input_store_price">{{ InputOptionPrice }}</span>
    </label>  
</template>

<script>
export default {
    name: "Radio-Input-Store",
    props: ['InputOptionName', 'InputOptionMeta', 'InputOptionPrice']

}
</script>

<style>

.radio_input_store_area {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 12px 16px 16px 16px;
    background-color: rgb(255, 255, 255);
    border-radius: 12px;
}

.radio_input_store_area:hover {
  box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.3), 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
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
  font-family: 'Material Symbols Outlined';
  content: 'radio_button_unchecked';
  font-variation-settings: 'wght' 400, 'opsz' 24;
  font-size: 24px;
  line-height: 1;
  color: var(--on-surface-variant-light); 
}


.radio_input_store_input:hover::after {
  font-variation-settings: 'wght' 700;
}

.radio_input_store_input:checked::after {
  font-family: 'Material Symbols Outlined';
  content: 'radio_button_checked';
  font-size: 24px;
  line-height: 1;
  color: var(--primary-light);
}

.radio_input_store_input:checked:hover::after {
  font-variation-settings: 'wght' 700;
}

</style>