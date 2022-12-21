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
        planName: String,
        planId: String,
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
        <div style="padding: 14px">
          <span>{{planName}}</span>
          <div class="bottom">
            <el-button text class="button" @click="toPlanPage(this.planId)">more</el-button>
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
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}
</style>