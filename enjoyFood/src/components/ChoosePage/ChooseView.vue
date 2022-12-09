<template>
    <!-- <nav>
        <el-button type="success"><router-link to="/choosePage/foodView/choose">食物</router-link></el-button>
        <el-button type="success"><router-link to="/choosePage/sportView/choose">运动</router-link></el-button>
    </nav> -->
    <!-- <router-view name="chooseView"/> -->
    <el-button type="success" @click="chooseContent(1)">食物</el-button>
    <el-button type="success" @click="chooseContent(2)">运动</el-button>
    <FoodView1 v-if="(contentType == 1)" type="choose"></FoodView1>
    <SportView1 v-else-if="(contentType == 2)" type="choose"></SportView1>
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

