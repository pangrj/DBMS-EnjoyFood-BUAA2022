<template>
    <!-- 菜品表格 -->
    <el-table :data="getFoodListHandler()" height="250" max-height="500" class="table">
        <el-table-column fixed prop="d_id" label="菜品编号" min-width="10%" class="table-row" align="center"/>
        <el-table-column prop="d_name" label="菜品名称" min-width="20%" class="table-row" align="center"/>
        <el-table-column prop="d_category" label="菜品种类" min-width="10%" class="table-row" align="center"/>
        <el-table-column prop="d_cuisine" label="菜系" min-width="10%" class="table-row" align="center"/>
        <el-table-column prop="d_calories" label="热量" min-width="10%" class="table-row" align="center"/>
        <el-table-column prop="d_price" label="价格" min-width="10%" class="table-row" align="center"/>
        <el-table-column fixed="right" label="操作" min-width="10%" slot-scope="scope" class="table-row" align="center">
            <template v-slot="scope">
                <el-button type="primary" size="small" @click="selectFood(scope.row)" v-show="isChoose">选择菜品</el-button>
                <el-button link type="primary" size="small" @click="deleteFood(scope.row)" v-show="isChosen">删除菜品</el-button>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
import { mapGetters, mapMutations} from 'vuex';
import { toRaw } from 'vue';

export default {
    name: "FoodView",
    props: {
        type:{
            type:String,
            default:""
        },
    },
    data(){
        return {
            isChoose: false,
            isChosen: false,
        }
    },
    computed:{
        ...mapGetters(["getFoodList"]),
        ...mapGetters(["getChosenFood"]),
        // isChoose: function() {
        //     type == "choose";
        // },
        // isChosen: function() {
        //     type == "chosen";
        // }
    },
    methods:{
        ...mapMutations(["chooseFood"]),
        selectFood(val) {
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
        // isChoose() {
        //     return type == "choose";
        // }
    },
    beforeMount: function(){
        this.isChoose = (this.type == "choose");
        this.isChosen = (this.type == "chosen");
    },
    
}

</script>

<style scoped>
    /*最外层透明*/
    .el-table, .el-table__expanded-cell, .header-cell-style, .el-table-column{
        background-color: transparent !important;
        text-align: center !important;
    }
    /* 表格内背景颜色 */
    ::v-deep .el-table__header-wrapper .el-table th, .el-table tr, .el-table td {
        background-color: transparent !important;
        text-align: center !important;
    }
    

</style>