<template>
  <button class="icon_button">
    <span class="material-symbols-outlined">{{ IconName }}</span>
  </button>
</template>
  
<script>
export default {
  name: "IconButton",
  props: ['IconName']
}
  
</script>

<style scoped>
  .icon_button {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    color: var(--on-surface-variant-light);
    background-color: transparent;
    padding: 8px;
    border-radius: 100px;
    cursor: pointer;
    transition: background-color 0.1s ease;
  }
  .icon_button .material-symbols-outlined {
    transition: font-weight 0.5s ease, font-variation-settings 0.5s ease, transform 0.5s ease;
  }

  .small {
    padding: 6px;
  }
  .small .material-symbols-outlined {
    font-size: 20px;
    font-variation-settings: 'OPSZ' 20;    
  }

  /* filled */

  .icon_button.filled .material-symbols-outlined {
    font-variation-settings: 'FILL' 1;
  }
  .icon_button.filled:hover .material-symbols-outlined {
    font-variation-settings: 'FILL' 1;
  }
  .icon_button.filled:focus-visible .material-symbols-outlined {
    font-variation-settings: 'FILL' 1;
  }
  .icon_button.filled:active .material-symbols-outlined {
    font-variation-settings: 'FILL' 1;
  }

  
  .icon_button:hover {
    background-color: var(--palette-neutral-variant90);
    transition: background-color 0.1s;
  }
  .icon_button:hover .material-symbols-outlined {
    font-weight: 700;
    font-variation-settings: 'WGHT' 700;
    transition: font-weight 0.2s ease, font-variation-settings 0.2s ease;
  }
  
  .icon_button:focus-visible {
    background-color: var(--palette-neutral-variant90);
    transition: background-color 0.1s;
  }
  .icon_button:focus-visible .material-symbols-outlined {
    font-weight: 700;
    font-variation-settings: 'WGHT' 700;
    transition: font-weight 0.2s ease, font-variation-settings 0.2s ease;
  }
  
  .icon_button:active {
    background-color: var(--palette-neutral-variant80);
    transition: background-color 0.1s;
  }
  .icon_button:active .material-symbols-outlined {
    transform: scale(0.92);
    transition: transform 0.2s ease;
  }


  /* primary */

  .icon_button.primary {
    color: var(--primary-light);
  }

  .icon_button.primary:hover {
    background-color: var(--palette-primary80);
  }

  .icon_button.primary:focus-visible {
    background-color: var(--palette-primary80);
  }

  .icon_button.primary:active {
    background-color: var(--palette-primary70);
  }
  

</style>