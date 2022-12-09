<template>
    <el-button type="success" @click="chooseContent(1)">食物</el-button>
    <el-button type="success" @click="chooseContent(2)">运动</el-button>
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

