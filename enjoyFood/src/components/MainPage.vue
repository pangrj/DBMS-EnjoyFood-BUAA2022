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
        passWord.value = route.query.passWord;
        console.log(userName, passWord);
        return {userName, passWord};
    },
    components: {
        Header,
    },
}
</script>

<template>
    <div>
        <Header />
        MainPage
    </div>
</template>

<style scoped>

</style>