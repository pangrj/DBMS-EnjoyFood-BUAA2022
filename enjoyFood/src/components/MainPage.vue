<script>
import { useRoute } from "vue-router";
import { reactive, ref } from 'vue'
import img from '../assets/yimian1.jpg' 
import request from '../https/axios.js'

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

        const imgRef = ref(img)
        const plans = ref([])
        const num = ref(0)
        var numV = 0
        function initInfo(){
          console.log("init")
          console.log(userName);
            request({
                method: 'POST',
                url: '/plan/suggest/',
                data: {   
                    u_name: userName.value,
                    }
                }
            ).then(function(response) {
                console.log("reponse: ")
                console.log(response); 
                var datas = response.data.plans;
                var field = {}
                for(var i in datas){
                    field = datas[i].fields
                    field["p_id"] = datas[i].pk
                    plans.value.push(field);
                    numV = numV + 1
                }
                num.value = numV
                console.log(plans)
                console.log("num")
                console.log(numV)
            }).catch(function(error) {
                console.log("error");
                console.log(error);
            })
          };
        initInfo();

        return {imgRef, userName, plans, numV};
    },
    components: {
        Header, 
        RecommendCard,
        Chart,
        Graph,
        HistoryPlans,
    },
    methods: {
        toPlanPage(pid){
        this.$router.push({
                path: '/PlanPage',
                query: {
                    planId: pid,
                    userName: this.userName,
                },
            });    
        },
    }
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
                    <div title='chart'><Chart v-bind:userName="userName"/></div>
                </el-header>
                <el-main style="margin-top: 5%; margin-right: 12%; margin-left: 5%">
                    <div class='cards'>
                        <!--RecommendCard v-bind:userName="userName"/-->
                        <el-scrollbar>
                            <div class="scrollbar-flex-content">
                            <p v-for="plan in plans" :key="plan.p_id" class="scrollbar-demo-item">
                            <el-card :body-style="{ padding: '0px' }" shadow="hover">
                                <img
                                    :src= "imgRef"
                                    class="image"
                                />
                                <div style="padding:3px">
                                <h3>{{plan.p_name}}</h3> 
                                <span >{{plan.p_description}}</span> 
                                <div class="bottom">
                                <el-button class="button" @click="toPlanPage(plan.p_id)"><p>更多</p></el-button>
                                </div>
                                </div>
                            </el-card>
                            </p>
                            </div>
                        </el-scrollbar>
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
    position: fixed;
}
.el-header{
    margin-top: 5%;
    height: 450px;
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
    margin-right: 15%;
}
.cards{
    margin-left: 5%;
}
.time {
  font-size: 12px;
  color: #999;
}
.scrollbar-flex-content {
  display: flex;
}
.scrollbar-demo-item {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 250px;
  height: 260px;
  margin: 25px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-danger-light-9);
  color: var(--el-color-danger);
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  min-height: auto;
  margin-right: 15%;
}

.image {
  width: 100%;
  display: block;
}
</style>
