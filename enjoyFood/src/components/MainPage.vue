<script>
import { useRoute } from "vue-router";

import {ref} from 'vue'
const userName = ref('')
const passWord = ref('')

import Header from "./Header.vue"

export default {
    setup(){
        let route = useRoute()
        userName.value = route.query.userName;
        console.log(userName);
        return {userName};
    },
    components: {
        Header,
    },
}
</script>

<template>
    <div>
        <Header v-bind:userName="userName"/>
        MainPage
    </div>
</template>

<style scoped>

</style>