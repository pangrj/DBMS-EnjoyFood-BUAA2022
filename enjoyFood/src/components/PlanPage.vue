<script type="text/javascript">
import {ref, reactive, onMounted} from 'vue'
import {useRoute} from 'vue-router'
import request from '../https/axios.js'
import Comments from './PlanPage/Comments.vue';
import Header from "./Header.vue"
import { ElMessage } from 'element-plus'
import * as echarts from 'echarts'

export default {
    name:'',
    components:{
        Header,
        Comments,
    },
    setup() {
        let route = useRoute()
        const planId = route.query.planId;
        const username = route.query.userName;;
        console.log(planId);

        const plan = reactive({
            p_id: "123321",
            u_id: "123123",
            p_name: "测试计划",
            p_description: "test",
            username: "testUser",
            calories_in: 300,
            calories_consume: 180,
        });

        const foods = ref([]);
        const sports = ref([]);
        const planUserName = "";

        // init:
        function init() {
            console.log("init")
            request({
                method: 'POST',
                url: '/plan/getInfor/',
                data: {   
                    p_id: planId,
                    }
                }
            ).then(function(response) {
                console.log("reponse: ")
                console.log(response);
                plan.p_id = response.data.plan[0].pk;
                console.log("plan: ")
                var field = response.data.plan[0].fields
                plan.p_name = field.p_name
                plan.p_description = field.p_description
                plan.username = field.u_name
                plan.calories_in = field.calories_in
                plan.calories_consume = field.calories_consume
                console.log(plan)
                var foodList = []
                field = {}
                for (var p in response.data.dishes){
                    field = response.data.dishes[p].fields
                    foodList.push(field)
                }
                foods.value = foodList
                var sportList = []
                field = {}
                for (var p in response.data.exercises){
                    field = response.data.exercises[p].fields
                    sportList.push(field)
                }
                sports.value = sportList;

                draw("chart");
            }).catch(function(error) {
                console.log("error");
                console.log(error);
            })
        };

        function draw(id) {
		    var chart = echarts.init(document.getElementById(id))
            chart.setOption({
                xAxis: {
                    data: ['摄入', '消耗']
                },
                yAxis: {},
                series: [{
                    type: 'bar',
                    data: [plan.calories_in, plan.calories_consume]
                }]
            })
        }

        onMounted(() => {
            init();
        });
        
        return {planId, plan, foods, sports, username, planUserName}
    },
    data(){
        return{
            deleteDialogVisiable: false
        }
    },
    methods: {
        deleteP(){
            console.log(this.planId);
            request({
                method: 'POST',
                url: '/plan/delete/',
                data: {   
                    plan_id: this.planId,
                    }
                }
            ).then(function(response) {
                console.log(response);
            })
            ElMessage.success('删除成功 !')
            this.$router.push({
                    path: '/MainPage',
                    query: {
                        userName: this.username,
                    },
                });
        },
        sureToDelete(){
            if(this.username != this.plan.username){
                ElMessage.error('只有创建者有权限删除计划 !')
            }else{
                this.deleteDialogVisiable = true;
            }
        }
    }
}

</script>

<template>
    <div>
        <Header v-bind:userName="username"/>
    <div class="Body">
        <el-header class="header">
                <h1 style="color: white">{{plan.p_name}}</h1>
                <h3 style="color: white">from {{plan.username}}</h3>
                <h3 style="color: white">{{plan.p_description}}</h3>
        </el-header>
        <el-main>
            <el-container>
            <el-aside width="55%">
            <h2> 美食 </h2>
            <div class="scroll-food">
                <el-scrollbar>
                    <div class="scrollbar-flex-content">
                        <div v-for="food in foods" :key="food.id" class="scrollbar-demo-item">
                        <el-tooltip 
                            raw-content
                            effect="customized">
                            <template #content>
                                <p></p>
                                <span>口味：{{food.d_cuisine}}</span>
                                <p></p>
                                <span>卡路里：{{food.d_calories}}</span>
                            </template>
                        {{ food.d_name }}
                        </el-tooltip>
                        </div>
                    </div>
                </el-scrollbar>
            </div>
            <h2> 运动 </h2>
            <div class="scroll-sport">
                <el-scrollbar>
                    <div class="scrollbar-flex-content">
                        <div v-for="sport in sports" :key="sport.id" class="scrollbar-demo-item">
                        <el-tooltip 
                            raw-content
                            effect="customized">
                            <template #content>
                                <p></p>
                                <span>内容：{{sport.sp_content}}</span>
                                <p></p>
                                <span>难度：{{sport.sp_difficulty}}</span>
                            </template>
                            {{ sport.sp_name }}
                        </el-tooltip>
                        </div>
                    </div>
                </el-scrollbar>
            </div>
            </el-aside>
            <el-main>
                <div id="chart" style="width:100%; height:350px;"></div>
                <div><el-button type="danger" plain @click="sureToDelete()">删除计划</el-button></div>
            </el-main>
            </el-container>
            <div class="comments"> 
                <h2> 评价 </h2>
                <comments :userName="username" :planId="planId"></comments>
            </div>
        </el-main>
    </div>

    <el-dialog
        v-model="deleteDialogVisiable"
        title="Sure"
        width="30%"
        align-center
    >
        <span>你确定删除该计划吗？</span>
        <template #footer>
            <span class="dialog-footer">
                <el-button @click="deleteDialogVisiable = false">取消</el-button>
                <el-button type="primary" @click="deleteP()">
                确定
                </el-button>
            </span>
        </template>
    </el-dialog>

    </div>
</template>

<style scoped>
.header{
    padding-top: 10%;
    padding-bottom: 20%;
    background: url("./src/assets/jianfei.jpg");
}
.scrollbar-flex-content {
  display: flex;
}
.scrollbar-demo-item {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 50px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-danger-light-9);
  color: var(--el-color-danger);
}
.el-popper.is-customized {
  /* Set padding to ensure the height is 32px */
  padding: 6px 20px;
  background: linear-gradient(90deg, rgb(159, 229, 151), rgb(204, 229, 129));
}

.el-popper.is-customized .el-popper__arrow::before {
  background: linear-gradient(45deg, #b2e68d, #bce689);
  right: 0;
}
.dialog-footer button:first-child {
  margin-right: 10px;
}
.scroll-food{
    padding-top: 3%;
    padding-bottom: 5%;
    padding-left: 8%;
    padding-right: 8%;
}
.scroll-sport{
    padding-top: 3%;
    padding-bottom: 5%;
    padding-left: 8%;
    padding-right: 8%;
}
.comments{
    padding-top: 3%;
}

</style>