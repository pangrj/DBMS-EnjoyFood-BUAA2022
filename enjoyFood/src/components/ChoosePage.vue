<script>
import { useRoute } from "vue-router";

import {ref} from 'vue'
const userName = ref('')
const passWord = ref('')

import ChooseView from './ChoosePage/ChooseView.vue';
import ChosenView from './ChoosePage/ChosenView.vue';

export default {
    setup(){
        let route = useRoute()
        userName.value = route.query.userName;
        console.log(userName);
        return {userName};
    },
    components: {
        ChooseView,
        ChosenView
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
        toggleSearch(){
            this.deepSearch = !this.deepSearch
        },
        ClickUserFilled(){
            console.log(userName);
            this.$router.push({
                path: '/InfomationPage',
                query: {
                    userName: userName.value,
                },
            });
        }
    }
}
</script>

<!-- <template>
    <div>
    <el-header class = "header">
        <h2 class = "name">{{userName}}</h2>
        <el-button plain @click="ClickUserFilled()">
            <el-icon><UserFilled /></el-icon>
            Your Profile
        </el-button>
    </el-header>
    <el-main>
    <div class="ChoosePage">
    <div class="leftTop">
        <el-input 
            class = "common"
            v-if="!deepSearch"
            v-model="searchRequset"
            size="large"
            placeholder="Search">
            <template #suffix>
                <el-icon><Search /></el-icon>
            </template>
        </el-input> 

        <template calss="deep" v-if="deepSearch">
            <el-form :model="deepRequest" label-width="120px">
                <el-form-item label="Category">
                    <el-input v-model="deepRequest.category" placeholder="please write category"
                        :style="{width: '100%'}" />
                </el-form-item>
                <el-form-item label="cuisine">
                    <el-select v-model="deepRequest.cuisine" placeholder="please select the cuisine">
                        <el-option label="sweet" value="One" />
                        <el-option label="soul" value="Two" />
                    </el-select>
                </el-form-item>
                <el-form-item label="calories">
                    <el-input v-model="deepRequest.caloriesLeast" placeholder="least num of calories" 
                        :style="{width: '30%'}" />
                    <el-col :span="2" class="text-center">
                        <span class="text-gray-500">-</span>
                    </el-col>
                    <el-input v-model="deepRequest.caloriesMost" placeholder="most num of calories" 
                        :style="{width: '30%'}" />
                </el-form-item>
                <el-form-item label="price">
                    <el-input v-model="deepRequest.priceLeast" placeholder="least num of price" 
                        :style="{width: '30%'}" />
                    <el-col :span="2" class="text-center">
                        <span class="text-gray-500">-</span>
                    </el-col>
                    <el-input v-model="deepRequest.priceMost" placeholder="most num of price" 
                        :style="{width: '30%'}" />
                </el-form-item>
            </el-form>
        </template>
    </div>
    <div class="rightTop"> 
        <el-button v-if="deepSearch" @click="toggleSearch" type="primary" plain>common search</el-button>
        <el-button v-if="!deepSearch" @click="toggleSearch" type="primary" plain>deep search</el-button>
    </div>
    <div class="chooseBox">
    </div>
    </div>
    </el-main>
    </div>
</template>

<style scoped>
.header{
    background-color: rgba(0,50,255,0.6);
}
.name{
    align-content: left;
}
.ChoosePage {
  width: 100%;
  height: 22px;
  display: flex;
  flex-direction: row;
  padding-top: 3%;
}
.ChoosePage > div {
  height: 22px;
  flex: 1;
}
.common{
    padding-left: 100px;
    width: 100%;
}
.deep{
    width: 100%;
    border: 1px solid #409eff;
    padding-left: 250px;
    padding-top: 100px;
}
</style> -->
<template>
    <div class="ChoosePage">
        <Header v-bind:userName="userName"/>
    <el-container>
      <el-header>
        Enjoy Your Life
    </el-header>
      <el-main>
        <el-row :gutter="20" class="choose_title">
            <!-- 左侧的选择栏 -->
            <el-col :span="14"><div class="grid-content ep-bg-purple"> 
                选择内容
            </div></el-col>
            <!-- 右侧的已选栏 -->
            <el-col :span="10"><div class="grid-content ep-bg-purple">
                已选内容
            </div></el-col>
        </el-row>
    
        <el-row :gutter="20" class="content">
            <!-- 左侧的选择栏 -->
            <el-col :span="14">
                <div class="grid-content bg-purple"> 
                <ChooseView></ChooseView>
                </div>
            </el-col>
            <!-- 右侧的已选栏 -->
            <el-col :span="10">
                <div class="grid-content bg-purple">
                <ChosenView></ChosenView>
                </div>
            </el-col>
        </el-row>

        <el-row :gutter="20" class="conclusion">
            <!-- 下方的总结栏 -->
            <el-col :span="15">
                <el-descriptions title="计划总结" direction="vertical" :column="2" :size="size" border>
                    <el-descriptions-item label="摄入能量">500</el-descriptions-item>
                    <el-descriptions-item label="消耗能量">100</el-descriptions-item>
                </el-descriptions>
            </el-col>
            <el-col :span="8">
                <div class="grid-content bg-purple">
                    饼状图
                </div>
            </el-col>
        </el-row>
        <p></p>
        <el-button type="success">确认提交</el-button>
        

      </el-main>
    </el-container>
  </div>
</template>

<style scoped>
.title {
  height: 30px;
}
.content {
  height: 300px;
}

.ChoosePage{
    background: url('../assets/chopping_board.jpg') no-repeat center;
    margin-bottom: 0px;
}

.choose_title{
    font-size: large;
    font-weight:bold;
    color: antiquewhite;
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
    height: 600px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
</style>
