<template>
    <!-- 菜品表格 -->
    <el-table :data="getSportListHandler()"  max-height="400" class="table">
        <!-- <el-table-column fixed prop="sp_id" label="运动编号" min-width="10%" align="center"/> -->
        <el-table-column fixed prop="sp_name" label="运动名称" min-width="20%" align="center"/>
        <el-table-column prop="sp_content" label="运动内容" min-width="20%" align="center"/>
        <el-table-column prop="sp_difficulty" label="运动难度" min-width="10%" align="center"/>
        <el-table-column prop="sp_calories" label="消耗热量" min-width="10%" align="center"/>
        <el-table-column prop="sp_time" label="花费时间" min-width="10%" align="center"/>
        <el-table-column label="运动场地" min-width="10%" align="center">
            <template v-slot="scope">
                <el-button link type="primary" size="small" @click="showLocation(scope.row)">查看详情</el-button>
            </template>
        </el-table-column>
        <el-table-column fixed="right" label="操作" min-width="10%" slot-scope="scope" align="center">
            <template v-slot="scope">
                <el-button link type="primary" size="small" @click="chooseSportHandler(scope.row)" v-show="isChoose">选择运动</el-button>
                <el-button link type="primary" size="small" @click="deleteSportHandler(scope.row)" v-show="isChosen">删除运动</el-button>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
import { mapGetters, mapMutations} from 'vuex';
import { toRaw } from 'vue';
import axios from "axios";

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
            lifeCircle: 1,
        }
    },
    computed:{
        ...mapGetters(["getSportList", "getChosenSport", "getLifeCircle"]),
    },
    methods:{
        ...mapMutations(["initSportList", "chooseSport", "deleteSport"]),
        chooseSportHandler(val) {
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
        deleteSportHandler(val) {
            let array=toRaw(val)  
            console.log(array);
            this.deleteSport(array);
        },
        showLocation(val) {
            console.log("showLoc")
        }
    },
    beforeMount: function(){
        this.isChoose = (this.type == "choose");
        this.isChosen = (this.type == "chosen");
        this.lifeCircle = this.getLifeCircle;
        console.log((this.lifeCircle == 1)?"北航生活圈":"五道口生活圈")
        //获取后端的数据
        axios.post("http://localhost:8000/sport/searchByCircle/", JSON.stringify({
            u_name: 123456,
            c_name: (this.lifeCircle == 1)?"北航生活圈":"五道口生活圈"
        })).then(res => {
            console.log(res.data);
            this.initSportList(res.data);
        })
    },
    
}

</script>

<style scoped>
    .table {
        width: 80%;
        margin: auto;
    }
</style>