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
        return{imgRef}
    },
    date:{
        plans: [{name: "意面计划", time: "12-17 10:38"},
            {name: "考试后狠狠奖励自己", time: "12-18 23.11"}]
    },
    methods: {
      async initInfo(){
        console.log("init")
            request({
                method: 'POST',
                url: '/user/getInfor/',
                data: {   
                    p_id: this.planId,
                    }
                }
            ).then(function(response) {
                console.log("reponse: ")
                console.log(response); 
                this.planName = response.data.code.p_name;
            }).catch(function(error) {
                console.log("error");
                console.log(error);
            })
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
})

</script>

<template>
  <el-row>
    <el-col
      v-for="(o, index) in 2"
      :key="o"
      :span="8"
      :offset="index > 0 ? 2 : 0"
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
  </el-row>
</template>

<style>
.time {
  font-size: 12px;
  color: #999;
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