<script>
import { useRoute } from "vue-router";

import {ref} from 'vue'
const userName = ref('')
const passWord = ref('')

import Header from "./Header.vue"
import RecommendCard from "./MainPage/RecommendCard.vue"
import Chart from "./MainPage/Chart.vue"

export default {
    setup(){
        let route = useRoute()
        userName.value = route.query.userName;
        console.log(userName);
        return {userName};
    },
    components: {
        Header, 
        RecommendCard,
        Chart,
    },
}
</script>

<template>
<div class="total">
    <Header v-bind:userName="userName"/>
    <div class="MainPage">
        <el-container>
        <el-header>
            <Chart />
        </el-header>
        <el-main>
            Main
            <RecommendCard />
        </el-main>
        <el-footer>
            Footer
        </el-footer>
        </el-container>
    </div>
</div>
</template>

<style scoped>
.MainPage{
  background: url("./src/assets/background.jpg");
  background-size: cover;
  opacity: 0.75;
  width: 100%;
  height: 100%;
}
.el-header{
    margin-top: 5%;
    height: 500px;
    margin-bottom: 5%;
}
.Chart{
    size: 50%;
    height: 200px;
}
</style>