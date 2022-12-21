<script>
import { useRoute } from "vue-router";
import {ref} from 'vue'
import { ElMessageBox } from 'element-plus'

import ChooseView from './ChoosePage/ChooseView.vue';
import ChosenView from './ChoosePage/ChosenView.vue';
<<<<<<< HEAD
import Header from "./Header.vue";
=======
import Header from './Header.vue';
>>>>>>> f1cddbfa5d977bd4e5367a2399b7cb1e63f1b9dc

export default {
    setup(){
        const userName = ref('')
        const passWord = ref('')

        // 抽屉相关
        const drawer2 = ref(false)
        const direction = ref('rtl')
        const radio1 = ref('Option 1')
         let route = useRoute()
         userName.value = route.query.userName;
         console.log(userName);
        return {
            userName,
            drawer2,
            direction,
            radio1
        };
    },
    components: {
<<<<<<< HEAD
    ChooseView,
    ChosenView,
    Header
},
    props: {
        userName:{
            type:String,
            default:""
        }
=======
        ChooseView,
        ChosenView,
        Header,
>>>>>>> f1cddbfa5d977bd4e5367a2399b7cb1e63f1b9dc
    },
    data(){
        return {
            deepSearch: false,
            searchRequset: '',
            deepRequest: {
                category: '',
                cuisine: '',
                caloriesMost: '',
                caloriesLeast: '',
                priceMost: '',
                priceLeast: ''
            },
        }
    },
    methods:{
        // toggleSearch(){
        //     this.deepSearch = !this.deepSearch
        // },
        // ClickUserFilled(){
        //     console.log(userName);
        //     this.$router.push({
        //         path: '/InfomationPage',
        //         query: {
        //             userName: userName.value,
        //         },
        //     });
        // },
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
            ElMessageBox.confirm(`Are you confirm to chose ${radio1.value} ?`)
                .then(() => {
                    axios.post("http://localhost:8000/dish/searchByCircle/", JSON.stringify({
                        u_name: "123456",
                        c_name: (this.lifeCircle == 1)?"北航生活圈":"五道口生活圈"
                    })).then(res => {
                        console.log(res.data);
                        this.initFoodList(res.data);
                    })
                })
                .catch(() => {
                    // catch error
                })
        }
    }
}
</script>

<template>
<<<<<<< HEAD
    <Header v-bind:userName="userName"/>
=======
<div>
 <Header v-bind:userName="userName"/>
>>>>>>> f1cddbfa5d977bd4e5367a2399b7cb1e63f1b9dc
  <div class="ChoosePage">
    <el-container>
      <el-main>
        <!-- <el-row class="choose_title" justify="center"><div>
            可选列表
        </div></el-row> -->

        <!-- 列表栏 -->
        <el-row class="content">
            <el-col :span="24">
                    <ChooseView></ChooseView>
            </el-col>
        </el-row>
        
        
        <p></p>

        <!-- 已选按钮 -->
        <el-button type="primary" @click="drawer2 = true">
            已选内容
        </el-button>

        <!-- 抽屉内容(弹出方向：ltr,rtl,ttb,btt) -->
        <el-drawer v-model="drawer2" direction="ltr" size="50%"> 
            <template #title>
                <h4 style="margin-left:16px; text-align: left; font-size: larger; color:antiquewhite;">已选内容</h4>
            </template>
            <template #default>
                <div>
                    <ChosenView></ChosenView>
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
.title {
  height: 30px;
}
.content {
  height: 550px;
  text-align: center;
  /* margin-bottom: 10px; */
}

.ChoosePage{
    background: url('../assets/chopping_board.jpg') no-repeat center;
    margin-bottom: 0px;
    margin-left: 0px;
    margin-right: 0px;
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
    height: 650px;
    padding-top: 5 !important;
  }

  body > .el-container {
    margin-bottom: 40px;
  }
</style>
