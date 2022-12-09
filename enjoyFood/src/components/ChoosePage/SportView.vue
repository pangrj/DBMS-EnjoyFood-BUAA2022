<template>
    <!-- 菜品表格 -->
    <el-table :data="getSportListHandler()" style="width: 100%" height="250" max-height="500">
        <el-table-column fixed prop="d_id" label="菜品编号" width="100" />
        <el-table-column prop="d_name" label="菜品名称" width="200" />
        <el-table-column prop="d_category" label="菜品种类" width="100" />
        <el-table-column prop="d_cuisine" label="菜系" width="100" />
        <el-table-column prop="d_calories" label="热量" width="100" />
        <el-table-column prop="d_price" label="价格" width="100" />
        <el-table-column fixed="right" label="操作" width="100" slot-scope="scope">
            <template v-slot="scope">
                <el-button link type="primary" size="small" @click="selectSport(scope.row)" v-show="isChoose">选择运动</el-button>
                <el-button link type="primary" size="small" @click="deleteSport(scope.row)" v-show="isChosen">删除运动</el-button>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
import { mapGetters, mapMutations} from 'vuex';
import { toRaw } from 'vue';

export default {
    name: "SportsView",
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
        ...mapGetters(["getSportList"]),
        ...mapGetters(["getChosenSport"]),
    },
    methods:{
        ...mapMutations(["chooseSport"]),
        selectSport(val) {
            let array=toRaw(val)  
            console.log(array);
            this.chooseSport(array);
        },
        getSportListHandler() {
            if(this.type == "choose") {
                return this.getSportList;
            } else if (this.type == "chosen") {
                return this.getChosenSport;
            }
            return this.getSportList
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