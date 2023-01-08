<template>
    <button class="base_icon_button">
        <span class="material-symbols-outlined">{{ ButtonIcon }}</span>
        {{ ButtonMeta }}
    </button>
</template>
  
  <script>
  export default {
    name: "BaseIconButton",
    props: ['ButtonMeta', 'ButtonIcon']
  }
  
  </script>
  
  <style scoped>
  
  .base_icon_button {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    column-gap: 8px;
    font-weight: 500;
    font-size: 14px;
    line-height: 20px;
    color: var(--on-primary-light);
    background-color: var(--primary-light);
    padding-top: 10px;
    padding-left: 16px;
    padding-right: 24px;
    padding-bottom: 10px;
    border-radius: 100px;
    cursor: pointer;
    transition: background-color 0.1s, box-shadow 0.5s ease, font-weight 0.5s ease;
  }
  .icon_right {
    flex-direction: row-reverse;
    padding-left: 24px;
    padding-right: 16px;
  }

  .base_icon_button .material-symbols-outlined {
    font-size: 20px;
    font-variation-settings: 'OPSZ' 20;
    transition: font-weight 0.5s ease, font-variation-settings 0.5s ease, transform 0.5s ease;
  }
  .base_icon_button.icon_filled .material-symbols-outlined {
    font-variation-settings: 'FILL' 1;
  }
  .base_icon_button.icon_filled:hover .material-symbols-outlined {
    font-variation-settings: 'FILL' 1;
  }
  .base_icon_button.icon_filled:focus-visible .material-symbols-outlined {
    font-variation-settings: 'FILL' 1;
  }
  .base_icon_button.icon_filled:active .material-symbols-outlined {
    font-variation-settings: 'FILL' 1;
  }
  
  .base_icon_button:hover {
    font-weight: 700;
    background-color: var(--palette-primary50);
    box-shadow: var(--elevation-light-1);
    transition: background-color 0.1s, box-shadow 0.2s ease, font-weight 0.2s ease;
  }
  .base_icon_button:hover .material-symbols-outlined {
    font-weight: 700;
    font-variation-settings: 'WGHT' 700;
    transition: font-weight 0.2s ease, font-variation-settings 0.2s ease;
  }

  
  .base_icon_button:focus-visible {
    font-weight: 700;
    background-color: var(--palette-primary50);
    transition: background-color 0.1s, font-weight 0.2s ease;
  }
  .base_icon_button:focus-visible .material-symbols-outlined {
    font-weight: 700;
    font-variation-settings: 'WGHT' 700;
    transition: font-weight 0.2s ease, font-variation-settings 0.2s ease;
  }

  
  .base_icon_button:active {
    font-weight: 700;
    background-color: var(--palette-primary60);
    transition: background-color 0.1s, font-weight 0.2s ease, box-shadow 0.2s ease;
    box-shadow: none;
  }
  .base_icon_button:active .material-symbols-outlined {
    transform: scale(0.92);
    transition: transform 0.2s ease;
  }
  
  
  /* tonal */
  
  .base_icon_button.tonal {
    color: var(--on-primary-container-light);
    background-color: var(--primary-container-light);
  }
  
  .base_icon_button.tonal:hover {
    background-color: var(--palette-primary80);
  }
  
  .base_icon_button.tonal:focus-visible {
    background-color: var(--palette-primary80);
  }
  
  .base_icon_button.tonal:active {
    background-color: var(--palette-primary70);
  }
  
  
  /* elevated */
  
  .base_icon_button.elevated {
    color: var(--primary-light);
    background-color: transparent;
    box-shadow: var(--elevation-light-1);
  }
  
  .base_icon_button.elevated:hover {
    background-color: var(--palette-primary90);
    box-shadow: var(--elevation-light-2);
  }
  
  .base_icon_button.elevated:focus-visible {
    background-color: var(--palette-primary90);
  }
  
  .base_icon_button.elevated:active {
    background-color: var(--palette-primary80);
  }


  /* text */

  .base_icon_button.text {
    color: var(--primary-light);
    background-color: transparent;
    padding-left: 12px;
    padding-right: 12px;
  }

  .base_icon_button.text:hover {
    background-color: var(--palette-primary90);
    box-shadow: none;
  }

  .base_icon_button.text:focus-visible {
    background-color: var(--palette-primary90);
  }
.base_icon_button.text:active {
    background-color: var(--palette-primary80);
  }
  
  
  /* primary */
  
  @media (min-width: 1240px) {
    .primary {
      font-size: 16px;
      line-height: 24px;
      padding-top: 12px;
      padding-bottom: 12px;
    }
    .primary .material-symbols-outlined {
      font-size: 24px;
      font-variation-settings: 'OPSZ' 24;
    }
  }
  
  
  </style>