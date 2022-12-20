<script>
import { reactive } from "vue"
import {useRoute} from 'vue-router'
import Comments from './PlanPage/Comments.vue';
import Header from "./Header.vue"

export default {
    name:'ArticleComment',
    components:{
        Header,
        Comments,
    },
    setup() {
        let route = useRoute()
        const planId = route.query.planId;
        console.log(planId);

        const plan = reactive({
            p_id: "123321",
            u_id: "123123",
            p_name: "测试计划",
            p_description: "",
        });
        const foods = [{id:'1'}, {id:'2'}, {id:'3'}, {id:'4'}, {id:'3'}, {id:'4'}, {id:'3'}, {id:'4'}, {id:'3'}, {id:'4'}];
        const sports = [{id:'3'}, {id:'4'}, {id:'3'}, {id:'4'}, {id:'3'}, {id:'4'}, {id:'3'}, {id:'4'}, {id:'3'}, {id:'4'}, {id:'3'}, {id:'4'}];
        const username = "pangrj";
        const planUserName = "pangrj";
        return {planId, plan, foods, sports, username, planUserName}
    },
    data(){
        return{
        }
    },
    methods: {
        async initInfor(){
            const response = await request.post(
                '/plan/getInfor/',
                this.planId,
            );
            console.log(response)
            this.plan = response.plan;
            console(this.plan)
        },  
    }
}

</script>

<template>
    <div>
        <Header v-bind:userName="userName"/>
    <div class="Body">
        <el-header class="header">
                <h1>{{plan.p_name}}</h1>
                <h3>from {{planUserName}}</h3>
        </el-header>
        <el-main>
            <h2> foods </h2>
            <div class="scroll-food">
                <el-scrollbar>
                    <div class="scrollbar-flex-content">
                        <p v-for="food in foods" :key="food.id" class="scrollbar-demo-item">
                        {{ food.id }}
                        </p>
                    </div>
                </el-scrollbar>
            </div>
            <h2> sports </h2>
            <div class="scroll-sport">
                <el-scrollbar>
                    <div class="scrollbar-flex-content">
                        <p v-for="sport in sports" :key="sport.id" class="scrollbar-demo-item">
                        {{ sport.id }}
                        </p>
                    </div>
                </el-scrollbar>
            </div>
            <div class="comments">
                <comments></comments>
            </div>
        </el-main>
    </div>
    </div>
</template>

<style scoped>
.header{
    padding-top: 10%;
    padding-bottom: 18%;
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
    padding-top: 8%;
}
</style>