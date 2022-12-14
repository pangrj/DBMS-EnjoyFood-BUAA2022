<template>
    <el-button type="success" @click="chooseContent(1)">食物</el-button>
    <el-button type="success" @click="chooseContent(2)">运动</el-button>
    <p></p>
    <FoodView2 v-if="(contentType == 1)" type="chosen"></FoodView2>
    <SportView2 v-else-if="(contentType == 2)" type="chosen"></SportView2>
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