<template>
    <a class="base_tag">
        {{ BaseTagTitile }}
    </a>
</template>

<script>

export default {
    name: "BaseTag",
    props: ['BaseTagTitile']

}

</script>

<style scoped>

.base_tag {
    display: flex;
    text-decoration: none;
    font-weight: 500;
    font-size: 12px;
    line-height: 16px;
    color: var(--on-tertiary-light);
    background-color: var(--tertiary-light);
    padding-left: 8px;
    padding-top: 4px;
    padding-right: 8px;
    padding-bottom: 4px;
    border-radius: 100px;
}

</style>