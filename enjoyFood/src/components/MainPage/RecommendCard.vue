<script lang="ts">
import { reactive, ref } from 'vue'
import img from '../../assets/yimian1.jpg' 
import request from '../../https/axios.js'

export default({
    props: {
        userName: String,
    },
    setup(props) {
        const imgRef = ref(img)
        
        const plans = ref([])
        function initInfo(){
          console.log("init")
          console.log(props.userName);
            request({
                method: 'POST',
                url: '/plan/suggest/',
                data: {   
                    u_name: props.userName,
                    }
                }
            ).then(function(response) {
                console.log("reponse: ")
                console.log(response); 
                var field = {}
                for(var i=0; i < response.data.plans.length; i++){
                    field = response.data.p_Array[i].fields
                    field["p_id"] = response.data.p_Array[i].pk
                    plans[i] =(field);
                }
                console.log(plans)
            }).catch(function(error) {
                console.log("error");
                console.log(error);
            })
          };
        initInfo();
        return{imgRef, plans}
    },
    data:{

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
    },
})

</script>

<template>
<el-scrollbar>
    <div class="scrollbar-flex-content">
      <p v-for="item in 5" :key="item" class="scrollbar-demo-item">
        <el-card :body-style="{ padding: '0px' }" shadow="hover">
        <img
          :src= "imgRef"
          class="image"
        />
        <div style="padding:4px">
          <h3 >努力干饭</h3> 
          <span >Cedric 发布于 12-8 18:12</span> 
          <div class="bottom">
            <el-button text class="button" @click="toPlanPage(this.planId)">更多信息</el-button>
          </div>
        </div>
      </el-card>
      </p>
    </div>
  </el-scrollbar>
  <!--el-row>
    <el-col
      v-for="(o, index) in 3"
      :key="o"
      :span="8"
      :offset="index > 0 ? 3 : 0"
    >
      <el-card :body-style="{ padding: '0px' }" shadow="hover">
        <img
          :src= "imgRef"
          class="image"
        />
        <div style="padding:4px">
          <h3 v-if="index==0">努力干饭</h3> 
          <h3 v-if="index==1">考完试狠狠庆祝</h3> 
          <span v-if="index==0">Test 发布于 12-7 11:10</span> 
          <span v-if="index==1">Cedric 发布于 12-8 18:12</span> 
          <div class="bottom">
            <el-button text class="button" @click="toPlanPage(this.planId)">更多信息</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
  </!--el-row-->
</template>

<style>
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
  height: 240px;
  margin: 20px;
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
  padding-left: 200px;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}
</style>