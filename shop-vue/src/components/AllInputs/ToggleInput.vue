<template>
<div class="toggle_input_area">
    <div class="toggle_input_meta_wrapper">
      <span class="material-symbols-outlined size_40">handyman</span>
      <div class="toggle_input_meta">
        <span class="toggle_input_meta_name">Сборка и установка</span>
        <span class="toggle_input_meta_info">Оплачивается отдельно</span>
      </div>
    </div>
    <label class="toggle_input_switcher_wrapper">
        <input type="checkbox" name="switchValue">
        <span class="toggle_input_switcher"></span>
    </label>  
</div>
</template>

<script>

export default {
    name: "Toggle-Input-Outline",

}
</script>

<style>


.toggle_input_area {
  display: flex;
  justify-content: space-between;
  align-items: center;
  column-gap: 16px;
  padding-top: 12px;
  padding-bottom: 12px;
  border-top: 1px solid var(--outline-light);
  border-bottom: 1px solid var(--outline-light);
}

.toggle_input_meta_wrapper {
  display: flex;
  column-gap: 16px;
  align-items: center;
}

.toggle_input_meta {
  display: flex;
  flex-direction: column;
}

.toggle_input_meta_name {
  font-weight: 500;
  font-size: 16px;
  line-height: 24px;
  color: var(--on-surface-light);
}

.toggle_input_meta_info {
  font-size: 16px;
  line-height: 24px;
  color: var(--on-surface-variant-light);
}

/* The switch - the box around the slider */
.toggle_input_switcher_wrapper {
  position: relative;
  display: inline-block;
  width: 52px;
  height: 32px;
}

/* Hide default HTML checkbox */
.toggle_input_switcher input {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  margin: 0px;
}

/* The slider */
.toggle_input_switcher {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 100px;
  background-color: var(--surface-variant-light);
  -webkit-transition: .3s;
  transition: .3s;
}

.toggle_input_switcher:before {
  position: absolute;
  content: "";
  height: 28px;
  width: 28px;
  top: 2px;
  left: 2px;
  border-radius: 100px;
  box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.3), 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
  background-color: white;
  -webkit-transition: .3s;
  transition: .3s;
}

input:checked + .toggle_input_switcher {
  background-color: var(--primary-light);
}

/* input:focus + .toggle_input_switcher {
  box-shadow: 0 0 1px #2196F3;
} */

input:checked + .toggle_input_switcher:before {
  -webkit-transform: translateX(20px);
  -ms-transform: translateX(20px);
  transform: translateX(20px);
}


</style>