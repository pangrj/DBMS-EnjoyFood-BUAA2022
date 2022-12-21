<template>
    <el-button type="success" @click="chooseLifeCircle(1)">五道口生活圈</el-button>
    <el-button type="success" @click="chooseLifeCircle(2)">知春路生活圈</el-button>
    <p></p>
    <el-button type="success" @click="chooseContent(1)">食物</el-button>
    <el-button type="success" @click="chooseContent(2)">运动</el-button>
    <p></p>
    <div class="selected">
        <FoodView2 v-if="(contentType == 1)" type="chosen"></FoodView2>
        <SportView2 v-else-if="(contentType == 2)" type="chosen"></SportView2>
    </div>
    <!-- 下方的总结栏 -->
    <el-row :gutter="20" class="conclusion">
        <el-col :span="20">
            <el-descriptions title="计划总结" direction="vertical" :column="2" :size="size">
                <el-descriptions-item label="摄入能量" align="center">500</el-descriptions-item>
                <el-descriptions-item label="消耗能量" align="center">100</el-descriptions-item>
            </el-descriptions>
        </el-col>
    </el-row>
</template>

<script>
import FoodView2 from "./FoodView.vue"
import SportView2 from "./SportView.vue"
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
    methods: {
        chooseContent(type) {
            this.contentType = type;
            console.log(type);
        }
    }
}
</script>

<style scoped>
.conclusion {
    margin-top: 50px;
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

<style scoped>
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