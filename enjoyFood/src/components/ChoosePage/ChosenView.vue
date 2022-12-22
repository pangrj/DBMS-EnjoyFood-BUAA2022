<template>
    <h3> 已选详情 </h3>
    <el-button type="success" @click="chooseContent(1)">食物</el-button>
    <el-button type="success" @click="chooseContent(2)">运动</el-button>
    <p></p>
    <div class="selected">
        <FoodView2 v-if="(contentType == 1)" type="chosen"></FoodView2>
        <SportView2 v-else-if="(contentType == 2)" type="chosen"></SportView2>
    </div>
    <!-- 下方的总结栏 -->
    <el-divider border-style="double" />
    <h3> 热量总结 </h3>
    <el-row :gutter="20" class="conclusion">
        <el-col :span="22">
            <el-descriptions  direction="vertical" :column="2" :size="size">
                <el-descriptions-item label="摄入能量" align="center">{{totalCaloryIn}}</el-descriptions-item>
                <el-descriptions-item label="消耗能量" align="center">{{totalCaloryOut}}</el-descriptions-item>
            </el-descriptions>
        </el-col>
    </el-row>
</template>

<script>
import FoodView2 from "./FoodView.vue"
import SportView2 from "./SportView.vue"
import { mapGetters } from "vuex"

export default{
    name: "ChooseView",
    components: {
        FoodView2,
        SportView2
    },
    data() {
        return {
            contentType: 1, //用于选择展示什么页面
        }
    },
    computed: {
        ...mapGetters(["totalCaloryIn", "totalCaloryOut"])
    },
    methods: {
        chooseContent(type) {
            this.contentType = type;
            console.log(type);
        }
    }
}
</script>

<style scoped>
h3 {
    margin-top: 3px;
    margin-bottom: 3px;
}
.selected {
    height: 300px;
    padding-right: 3%;
}
.conclusion {
    margin-top: 30px;
}

.el-descriptions__body .el-descriptions__table .el-descriptions-item__cell {
    text-align: center;
  }
.el-button {
    text-align: left;
}

:deep(.search)  {
    width: 80%;
    margin-bottom: 10px;
}

:deep(.el-input__wrapper){
    background-color: rgba(239, 231, 224, 0.7);
}

:deep(.el-input__inner) {
    color: black;
}
</style>