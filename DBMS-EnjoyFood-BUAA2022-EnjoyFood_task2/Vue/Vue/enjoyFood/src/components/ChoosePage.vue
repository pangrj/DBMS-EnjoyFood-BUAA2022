<script>
import { useRoute } from "vue-router";

import {ref} from 'vue'
const userName = ref('')
const passWord = ref('')

export default {
    setup(){
        let route = useRoute()
        userName.value = route.query.userName;
        passWord.value = route.query.passWord;
        console.log(userName, passWord);
        return {userName, passWord};
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

<template>
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
</style>