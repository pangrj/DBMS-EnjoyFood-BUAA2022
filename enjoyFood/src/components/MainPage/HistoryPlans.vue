<script>
import {ref, reactive, onMounted} from 'vue'
import request from '../../https/axios.js'
export default {
  props: {
    userName: String,
  },
  setup(props){
    const centerDialogVisible = ref(false)
    const plans = [{p_name:"plan1 GOGOGO", p_time:"2022/10/5"},
        {p_name:"plan2 KFC", p_time:"2022/11/15"},
        {p_name:"plan3 Crazy", p_time:"2022/12/1"},
        {p_name:"plan4 Vme50", p_time:"2022/12/3"}];

    // init:
        // function init() {
        //     console.log("init")
        //     request({
        //         method: 'POST',
        //         url: '/user/getPlans/',
        //         data: {  
        //             u_name: props.userName,
        //             }
        //         }
        //     ).then(function(response) {
        //         console.log("reponse: ")
        //         console.log(response);
        //         plans = response.p_Array
        //     }).catch(function(error) {
        //         console.log("error");
        //         console.log(error);
        //     })
        // };

        onMounted(() => {
            init();
        });
    return {plans, centerDialogVisible};
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
                },
            });    
    },
  }
}
</script>

<template>
<div class='body'>
    <el-timeline>
        <el-timeline-item center v-bind:timestamp="plans[0].p_time" placement="top">
            <el-card>
                <h4>{{plans[0].p_name}}</h4>
                <p>{{userName}} published at {{plans[0].p_time}}</p>
            </el-card>
        </el-timeline-item>
        <el-timeline-item center v-bind:timestamp="plans[1].p_time" placement="top">
            <el-card>
                <h4>{{plans[1].p_name}}</h4>
                <p>{{userName}} published at {{plans[1].p_time}}</p>
            </el-card>
        </el-timeline-item>
        <el-timeline-item center v-bind:timestamp="plans[2].p_time" placement="top">
            <el-card>
                <h4>{{plans[2].p_name}}</h4>
                <p>{{userName}} published at {{plans[2].p_time}}</p>
            </el-card>
        </el-timeline-item>
        <el-timeline-item center v-bind:timestamp="plans[3].p_time" placement="top">
            <el-card>
                <h4>{{plans[3].p_name}}</h4>
                <p>{{userName}} published at {{plans[3].p_time}}</p>
            </el-card>
        </el-timeline-item>
    </el-timeline>
    <div class="more">
        <el-button type="success" circle @click="centerDialogVisible = true" title="more">
            <template #icon><el-icon><DArrowRight /></el-icon></template>
        </el-button>
    </div>

    <el-dialog
        v-model="centerDialogVisible"
        title="Warning"
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
                        <el-button text class="button" @click="toPlanPage(plan.p_id)">
                            moreInfo
                        </el-button>
                    </div>
                    <p>{{userName}} published at {{plan.p_time}}</p>
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