<template>
    <div>
        <!-- <img :src=" require('../assets/images/' + post_data.image) " alt="img"> -->
        <h1>Карточка статьи</h1>
        <p>{{ post_data.title }}</p>
        <router-link :to=" '/post/' + post_data.slug "><button>Читать</button></router-link>
    </div>
</template>

<script>
export default {
    name: "the-post-view",
    props: {
        post_data: {
            type: Object,
            default() {
                return {}
            }
        }
    }

}
</script>

<style>

</style>