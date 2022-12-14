<template>
    <!-- <nav>
        <el-button type="success"><router-link to="/choosePage/foodView/choose">食物</router-link></el-button>
        <el-button type="success"><router-link to="/choosePage/sportView/choose">运动</router-link></el-button>
    </nav> -->
    <!-- <router-view name="chooseView"/> -->
    <!-- <el-button type="success" @click="chooseContent(1)">食物</el-button>
    <el-button type="success" @click="chooseContent(2)">运动</el-button> -->
    <!-- 搜索栏 -->
    <!-- <div style="margin-top: 5px;">
        <el-input 
            class = "search"
            v-model="searchRequset"
            size="large"
            placeholder="输入搜索内容">
            <template #suffix>
                <el-icon><Search /></el-icon>
            </template>
        </el-input> 
    </div> -->

    <!-- 列表栏 -->
    <!-- <FoodView1 v-if="(contentType == 1)" type="choose"></FoodView1>
    <SportView1 v-else-if="(contentType == 2)" type="choose"></SportView1> -->
</template>

<script>
import FoodView1 from "./FoodView.vue"
import SportView1 from "./SportView.vue"
export default{
    name: "ChooseView",
    components: {
        FoodView1,
        SportView1
    },
    data() {
        return {
            searchRequset,
            contentType: 1, //用于选择展示什么页面
        }
    },
    methods: {
        chooseContent(type) {
            this.contentType = type;
            console.log(type);
        },
    }
}
</script>

<style scoped>
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

