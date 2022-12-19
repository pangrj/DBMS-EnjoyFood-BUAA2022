<script>
import { useRoute } from "vue-router";

import {ref} from 'vue'
const userName = ref('')
const passWord = ref('')

import Header from "./Header.vue"
import RecommendCard from "./MainPage/RecommendCard.vue"
import Chart from "./MainPage/Chart.vue"
import Graph from './MainPage/Graph.vue';
import HistoryPlans from './MainPage/HistoryPlans.vue'

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
        Graph,
        HistoryPlans,
    },
}
</script>

<template>
<div class="total">
    <Header v-bind:userName="userName"/>
    <div class="MainPage">
        <el-container>
        <el-aside width="70%">
            <el-container>
                <el-header>
                    <div title='chart'><Chart /></div>
                </el-header>
                <el-main>
                    <div class='cards'>
                        <RecommendCard />
                    </div>
                </el-main>
            </el-container>
        </el-aside>
        <el-main>
            <HistoryPlans class='myplans' v-bind:userName="userName"/>
        </el-main>
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
Chart{
    size: 50%;
    height: 200px;
}
Graph{
    size: 50%,
    height 200px;
}
.myplans{
    margin-top: 15%;
}
.cards{
    margin-left: 5%;
}
</style>

12.21开始
1. 设计文档
2. 数据、图片搜集
3. 前端优化
4. 测试