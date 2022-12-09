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
        passWord.value = route.query.passWord;
        console.log(userName, passWord);
        return {userName, passWord};
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
            console.log(userName, passWord);
            this.$router.push({
                path: '/InfomationPage',
                query: {
                    userName: userName.value,
                    passWord: passWord.value,
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
    <div class="common-layout">
    <el-container>
      <el-header>Header</el-header>
      <el-main>
        <!-- <template> -->
        <el-row :gutter="20">
            <!-- 左侧的选择栏 -->
            <el-col :span="14"><div class="grid-content ep-bg-purple"> 
                选择
            </div></el-col>
            <!-- 右侧的已选栏 -->
            <el-col :span="10"><div class="grid-content ep-bg-purple">
                已选
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
        <!-- </template> -->
      </el-main>
    </el-container>
  </div>
</template>

<style scoped>
.title {
  height: 30px;
}
.content {
  height: 400px;
}
.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    /* line-height: 160px; */
    height: 600px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>
