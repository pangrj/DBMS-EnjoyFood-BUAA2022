<template>
    <!-- 菜品表格 -->
    <el-table :data="getSportListHandler()" style="width: 100%" height="250" max-height="500" >
        <el-table-column fixed prop="d_id" label="运动编号" min-width="10%" align="center"/>
        <el-table-column prop="d_name" label="运动名称" min-width="20%" align="center"/>
        <el-table-column prop="d_category" label="运动种类" min-width="10%" align="center"/>
        <el-table-column prop="d_cuisine" label="菜系" min-width="10%" align="center"/>
        <el-table-column prop="d_calories" label="热量" min-width="10%" align="center"/>
        <el-table-column prop="d_price" label="价格" min-width="10%" align="center"/>
        <el-table-column fixed="right" label="操作" min-width="10%" slot-scope="scope" align="center">
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