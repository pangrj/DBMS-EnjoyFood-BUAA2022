<script>
import {ref, reactive, onMounted} from 'vue'
import {useRoute} from 'vue-router'
import request from '../https/axios.js'
import Comments from './PlanPage/Comments.vue';
import Header from "./Header.vue"

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
            p_description: "",
            username: "",
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
                console.log(field)
                plan.p_name = field.p_name
                plan.p_description = field.p_description
                plan.username = field.user.u_name
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
                console.log(foods);
                console.log(sports);
            }).catch(function(error) {
                console.log("error");
                console.log(error);
            })
        };

        onMounted(() => {
            init();
        });
        
        return {planId, plan, foods, sports, username, planUserName}
    },
    data(){
        return{
        }
    },
    methods: {
    }
}

</script>

<template>
    <div>
        <Header v-bind:userName="username"/>
    <div class="Body">
        <el-header class="header">
                <h1>{{plan.p_name}}</h1>
                <h3>from {{planUserName}}</h3>
                <h3>{{plan.p_description}}</h3>
        </el-header>
        <el-main>
            <h2> foods </h2>
            <div class="scroll-food">
                <el-scrollbar>
                    <div class="scrollbar-flex-content">
                        <p v-for="food in foods" :key="food.id" class="scrollbar-demo-item">
                        {{ food.d_name }}
                        </p>
                    </div>
                </el-scrollbar>
            </div>
            <h2> sports </h2>
            <div class="scroll-sport">
                <el-scrollbar>
                    <div class="scrollbar-flex-content">
                        <p v-for="sport in sports" :key="sport.id" class="scrollbar-demo-item">
                        {{ sport.sp_name }}
                        </p>
                    </div>
                </el-scrollbar>
            </div>
            <div class="comments">
                <h2> comments </h2>
                <comments :userName="username" :planId="planId"></comments>
            </div>
        </el-main>
    </div>
    </div>
</template>

<style scoped>
.header{
    padding-top: 10%;
    padding-bottom: 20%;
    background: url("./src/assets/yimian.jpg");
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
.comments{
    padding-top: 3%;
}
</style>