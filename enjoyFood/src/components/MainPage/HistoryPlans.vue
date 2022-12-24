<script lang="js">
import {ref, reactive, onMounted} from 'vue'
import request from '../../https/axios.js'
export default {
  props: {
    userName: String,
  },
  setup(props){
    const centerDialogVisible = ref(false)
    const plans = ref([
        /*{id:"", p_name:"plan1 GOGOGO",p_description:"", p_time:"12-3 10:16", calories_in:0,calories_consume:0},
        {id:"", p_name:"plan2 KFC",p_description:"",  p_time:"12-5 12:15", calories_in:0,calories_consume:0},
        {id:"", p_name:"plan3 Crazy",p_description:"",  p_time:"12-5 12:26", calories_in:0,calories_consume:0},
        {id:"", p_name:"plan4 Vme50",p_description:"",  p_time:"12-6 00:17", calories_in:0,calories_consume:0}
        */]);
    const mode = ref("None");
    // init:
        function init() {
            console.log("init")
             request({
                 method: 'POST',
                url: '/user/getPlans/',
                data: {  
                    u_name: props.userName,
                    }
                }
            ).then(function(response) {
                console.log("reponse: ")
                console.log(response);
                var field = {}
                for(var i=0; i<response.data.num;i++){
                    field = response.data.p_Array[i].fields
                    field["p_id"] = response.data.p_Array[i].pk
                    plans.value.push(field);
                }
                if(response.data.num > 0 && response.data.num < 4){
                    mode.value = "less";
                }else if(response.data.num >= 4 ){
                    mode.value = "more";
                }
                console.log(plans);
                console.log(mode.value);
            }).catch(function(error) {
                console.log("error");
                console.log(error);
            })
        };

        onMounted(() => {
            init();
        });
    return {plans, centerDialogVisible, mode};
  },
  data() {
    return {
    };
  },
  methods: {
    async initInfor(){
            const response = await request.post(
                'c',
                this.userName,
            );
            console.log(response)
            plans = response.p_Array
    },
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
<div class='body'>
    <h2 style="font-weight: 700; color:black"> 我的计划 </h2>
    <el-timeline v-if='(mode == "more")'>
        <el-timeline-item center v-bind:timestamp="plans[0].p_time" placement="top">
            <el-card>
                <h4>{{plans[0].p_name}}</h4>
                <p>{{userName}} 发表于 {{plans[0].p_time}}</p>
            </el-card>
        </el-timeline-item>
        <el-timeline-item center v-bind:timestamp="plans[1].p_time" placement="top">
            <el-card>
                <h4>{{plans[1].p_name}}</h4>
                <p>{{userName}} 发表于 {{plans[1].p_time}}</p>
            </el-card>
        </el-timeline-item>
        <el-timeline-item center v-bind:timestamp="plans[2].p_time" placement="top">
            <el-card>
                <h4>{{plans[2].p_name}}</h4>
                <p>{{userName}} 发表于 {{plans[2].p_time}}</p>
            </el-card>
        </el-timeline-item>
        <el-timeline-item center v-bind:timestamp="plans[3].p_time" placement="top">
            <el-card>
                <h4>{{plans[3].p_name}}</h4>
                <p>{{userName}} 发表于 {{plans[3].p_time}}</p>
            </el-card>
        </el-timeline-item>
    </el-timeline>

    <el-timeline v-if='(mode == "less")'>
            <el-timeline-item center v-for="plan in plans" :key="plan.p_id"
                v-bind:timestamp="plan.p_time"  placement="top"
            >
                <el-card>
                    <div class="bottom">
                        <h4 class="title">{{plan.p_name}}</h4>
                        <el-button text @click="toPlanPage(plan.p_id)">
                            更多信息
                        </el-button>
                    </div>
                    <p>{{userName}} 发表于 {{plan.p_time}}</p>
                </el-card>
            </el-timeline-item>
        </el-timeline>

    <el-timeline v-if='(mode == "none")'>
            <p>还没有制定计划哦</p>
        </el-timeline>

    <div class="more">
        <el-button type="success" circle @click="centerDialogVisible = true" title="more">
            <template #icon><el-icon><DArrowRight /></el-icon></template>
        </el-button>
    </div>

    <el-dialog
        v-model="centerDialogVisible"
        title="所有计划"
        width="30%"
        align-center
    >
        <el-timeline>
            <el-timeline-item center v-for="plan in plans" :key="plan.p_id"
                v-bind:timestamp="plan.p_time"  placement="top"
            >
                <el-card>
                    <div class="bottom">
                        <h4 class="title">{{plan.p_name}}</h4>
                        <el-button text @click="toPlanPage(plan.p_id)">
                            更多信息
                        </el-button>
                    </div>
                    <p>{{userName}} 发表于 {{plan.p_time}}</p>
                </el-card>
            </el-timeline-item>
        </el-timeline>
        <template #footer>
          <span class="dialog-footer">
            <el-button type="primary" @click="centerDialogVisible = false">
              Confirm
         </el-button>
         </span>
        </template>
    </el-dialog>
</div>
</template>

<style scoped>
h4{
    color: black;
}
.dialog-footer button:first-child {
  margin-right: 10px;
}
.more{
    float: right;
    padding-right: 15%;
}
.body{
    padding-right: 6%;
}
.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.title{
    padding-left: 10%;
    color: black;
}
</style>