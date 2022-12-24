<script>
import { useRoute } from "vue-router";
import {ref} from 'vue'
import { ElMessageBox } from 'element-plus'
import { mapGetters } from "vuex";
import axios from "axios";

import ChooseView from './ChoosePage/ChooseView.vue';
import ChosenView from './ChoosePage/ChosenView.vue';
import Header from "./Header.vue";

export default {
    setup(){
        const userName = ref('')
        // const passWord = ref('')

        // 抽屉相关
        const drawer2 = ref(false)
        const direction = ref('rtl')
        const radio1 = ref('Option 1')
         let route = useRoute()
         userName.value = route.query.userName;
         console.log("用户名："+ userName);
        return {
            userName,
            drawer2,
            direction,
            radio1
        };
    },
    components: {
    ChooseView,
    ChosenView,
    Header
},
    // props: {
    //     userName:{
    //         type:String,
    //         default:""
    //     }
    // },
    data(){
        return {
            p_name: "",
            p_description: "",
        }
    },
    computed:{
        ...mapGetters(["getChosenFoodId", "getChosenSportId","totalCaloryIn", "totalCaloryOut"]),
        caloryPrompt(){
            if(this.totalCaloryIn - this.totalCaloryOut > 200) {
                console.log("摄入热量超标啦!")
                return "\n摄入热量超标啦!"
            } else{
                return "";
            }
        },
    },
    methods:{
        handleClose(done) {
            this.$confirm('确认关闭？')
            .then(_ => {
                done();
            })
            .catch(_ => {});
        },
        cancelClick() {
            drawer2.value = false
        },
        confirmClick() {
            ElMessageBox.confirm(`是否确实提交选择的菜品和运动？` + this.caloryPrompt,{
                    // message: h,
                    confirmButtonText: '确认提交',
                    cancelButtonText: '我再想想',
                    type: 'warning',
                }).then(() => {
                if(this.p_name == "") {
                    ElMessage('计划名称不能为空');
                    return
                } else if(this.p_description == ""){
                    ElMessage('计划内容不能为空');
                    return
                } else if(this.getChosenFoodId == null && this.getChosenSportId == null) {
                    ElMessage('运动和食物不能全为空');
                    return
                }
                console.log("queren")
                    axios.post("http://localhost:8000/plan/addPlan/", JSON.stringify({
                        u_name: "fire",
                        d_id: this.getChosenFoodId,
                        sp_id: this.getChosenSportId,
                        p_name: this.p_name,
                        p_description: this.p_description
                    })).then(res => {
                        if(res.data.code != 200) {
                            alert(res.data.message)
                        } else{
                            console.log(res.data);
                        }
                    })
                })
                .catch(() => {
                    // catch error
                    console.log("计划名称或描述不能为空，运动和食物不能全为空")
                })
        }
    }
}
</script>

<template>
<div>
 <Header v-bind:userName="userName"/>
  <div class="ChoosePage">
    <el-container>
      <el-main>
        <!-- <el-row class="choose_title" justify="center"><div>
            可选列表
        </div></el-row> -->

        <!-- 列表栏 -->
        <el-row class="content">
            <el-col :span="24">
                    <ChooseView :userName="userName"></ChooseView>
            </el-col>
        </el-row>
        
        
        <p></p>
        <div style="height:10%"></div>
        <!-- 已选按钮 -->
        <el-button type="primary" @click="drawer2 = true">
            已选内容
        </el-button>

        <!-- 抽屉内容(弹出方向：ltr,rtl,ttb,btt) -->
        <el-drawer v-model="drawer2" direction="ltr" size="50%"> 
            <template #header>
                <div>
                    <el-col :span="23" style="height: 40px; margin-bottom: 10px;">
                    <el-input v-model="p_name">
                        <template #prepend>计划名称</template>
                    </el-input>
                    </el-col>
                    <el-col :span="23">
                    <el-input v-model="p_description">
                        <template #prepend>计划简介</template>
                    </el-input>
                    </el-col>
                </div>
                <!-- <h4 style="margin-left:16px; text-align: left; font-size: larger; color:antiquewhite;">已选内容</h4> -->
            </template>
            <template #default>
                <div>
                    <ChosenView :userName="userName"></ChosenView>
                </div>
            </template>
            <template #footer>
                <div style="flex: auto">
                    <!-- <el-button @click="cancelClick">关闭</el-button> -->
                    <el-button type="primary" @click="confirmClick">确认提交</el-button>
                </div>
            </template>
        </el-drawer>

      </el-main>
    </el-container>
  </div>
</div>
</template>

<style scoped>
input {
    outline-style: none ;
    border: 1px solid #ccc; 
    border-radius: 10px;
    background-color: rgba(255, 255, 255, 0.8);
}

::-webkit-input-placeholder :-ms-input-placeholder ::-moz-placeholder :-moz-placeholder {
    font-size: larger;
    color: aquamarine;
    padding-left: 50px;
}

:deep(.el-drawer__header){
    height: 120px;
}
.title {
  height: 30px;
}
.content {
  height: 600px;
  /* height: 70%; */
  text-align: center;
  /* margin-bottom: 10px; */
}

.ChoosePage{
    background: url('../assets/123.jpg') no-repeat center;
    opacity: 0.7;
    background-size: cover;
    margin-bottom: 0px;
    margin-left: 0px;
    margin-right: 0px;
    padding-top: 50px;
    padding-bottom: 50px;
}

.choose_title{
    font-size: large;
    font-weight:bold;
    color:antiquewhite;
    text-align: center;
    margin-bottom: 10px;
    
}

body {
    margin: 0 !important;
} 

:deep(.el-drawer__header)  {
    margin-bottom: 0;
    padding-top: 0;
    background-color:cadetblue;
}

:deep(.el-drawer__body) {
    padding: 10px 10px;
}

:deep(.el-drawer__close-btn)  {
    background-color: coral;
}

.el-row {
   /* margin-bottom: 20px; */
}
.el-col {
  border-radius: 4px;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.el-header{
    background-color: rgba(239, 231, 224, 0.7);
    color: #333;
    text-align: center;
    line-height: 60px;
    font-family:fantasy;
    font-size: large;
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
 .el-main {
    /* background-color: #E9EEF3; */
    color: #333;
    text-align: center;
    /* line-height: 160px; */
    height: 1000px;
    padding-top: 5 !important;
  }

  body > .el-container {
    margin-bottom: 40px;
  }
</style>
