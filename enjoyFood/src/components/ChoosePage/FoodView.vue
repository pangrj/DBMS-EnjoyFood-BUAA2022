<template>
    <!-- 菜品表格 -->
    <el-table :data="getFoodListHandler()" style="width: 100%" height="250" max-height="500">
        <el-table-column fixed prop="d_id" label="菜品编号" width="100" />
        <el-table-column prop="d_name" label="菜品名称" width="200" />
        <el-table-column prop="d_category" label="菜品种类" width="100" />
        <el-table-column prop="d_cuisine" label="菜系" width="100" />
        <el-table-column prop="d_calories" label="热量" width="100" />
        <el-table-column prop="d_price" label="价格" width="100" />
        <el-table-column fixed="right" label="操作" width="100" slot-scope="scope">
            <template v-slot="scope">
                <el-button link type="primary" size="small" @click="selectFood(scope.row)" v-show="isChoose">选择菜品</el-button>
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

<style>

</style>