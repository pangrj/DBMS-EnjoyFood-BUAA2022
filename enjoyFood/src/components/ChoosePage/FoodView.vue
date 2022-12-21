<template>
    <!-- 菜品表格 -->
    <el-table :data="getFoodListHandler()" max-height="400" class="table">
        <!-- <el-table-column fixed prop="d_id" label="菜品编号" min-width="10%" class="table-row" align="center"/> -->
        <el-table-column fixed prop="d_name" label="菜品名称" min-width="20%" class="table-row" align="center"/>
        <el-table-column prop="d_category" label="菜品种类" min-width="10%" class="table-row" align="center"/>
        <el-table-column prop="d_cuisine" label="菜系" min-width="10%" class="table-row" align="center"/>
        <el-table-column prop="d_calories" label="热量" min-width="10%" class="table-row" align="center"/>
        <el-table-column prop="d_price" label="价格" min-width="10%" class="table-row" align="center"/>
        <el-table-column label="店铺" min-width="10%" align="center">
            <template #default>
                <el-button link type="primary" size="small" @click="showLocation">查看详情</el-button>
            </template>
        </el-table-column>
        <el-table-column fixed="right" label="操作" min-width="10%" slot-scope="scope" class="table-row" align="center">
            <template v-slot="scope">
                <el-button link type="primary" size="small" @click="chooseFoodHandler(scope.row)" v-show="isChoose">选择菜品</el-button>
                <el-button link type="primary" size="small" @click="deleteFoodHandler(scope.row)" v-show="isChosen">删除菜品</el-button>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
import { mapGetters, mapMutations, mapActions} from 'vuex';
import { toRaw } from 'vue';
import axios from "axios";
import request from '../../https/axios.js'

export default {
    name: "FoodView",
    props: {
        type:{
            type: String,
            default:""
        },
    },
    data(){
        return {
            isChoose: false,
            isChosen: false,
            lifeCircle: 1,
        }
    },
    computed:{
        ...mapGetters(["getFoodList", "getChosenFood", "getLifeCircle"]),
        // isChoose: function() {
        //     type == "choose";
        // },
        // isChosen: function() {
        //     type == "chosen";
        // }
    },
    methods:{
        ...mapMutations(["initFoodList", "chooseFood", "deleteFood"]),
        chooseFoodHandler(val) {
            let array=toRaw(val)  
            console.log(array);
            this.chooseFood(array);
        },
        getFoodListHandler() {
            if(this.type == "choose") {
                return this.getFoodList;
            } else if (this.type == "chosen") {
                return this.getChosenFood;
            }
            return this.getFoodList
        },
        deleteFoodHandler(val) {
            let array=toRaw(val)  
            console.log(array);
            this.deleteFood(array);
        },
        showLocation() {
            console.log("show location")
        }
    },
    beforeMount: function(){
        this.isChoose = (this.type == "choose");
        this.isChosen = (this.type == "chosen");
        console.log(this.lifeCircle)
        this.lifeCircle = this.getLifeCircle;
        console.log(this.lifeCircle)
        console.log((this.lifeCircle == 1)?"北航生活圈":"五道口生活圈")
        //获取后端的数据
        axios.post("http://localhost:8000/dish/searchByCircle/", JSON.stringify({
            u_name: "123456",
            c_name: (this.lifeCircle == 1)?"北航生活圈":"五道口生活圈"
        })).then(res => {
            console.log(res.data);
            this.initFoodList(res.data);
        })
    },
}

</script>

<style scoped>
    .table {
        width: 80%;
        margin: auto;
    }
    /*最外层透明*/
    :deep(.el-table, .el-table__expanded-cell, .header-cell-style, .el-table-column){
        background-color: rgba(239, 231, 224, 0.7);
        text-align: center;
    }
    /* 表格内背景颜色 */
    :deep(.el-table__header-wrapper .el-table th, .el-table tr, .el-table td ){
        background-color: rgba(239, 231, 224, 0.7);
        text-align: center;
    }


</style>