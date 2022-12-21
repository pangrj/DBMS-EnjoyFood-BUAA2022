<template>
    <!-- <nav>
        <el-button type="success"><router-link to="/choosePage/foodView/choose">食物</router-link></el-button>
        <el-button type="success"><router-link to="/choosePage/sportView/choose">运动</router-link></el-button>
    </nav> -->
    <!-- <router-view name="chooseView"/> -->
    <el-button type="info" @click="chooseLifeCircle(1)">北航生活圈</el-button>
    <el-button type="info" @click="chooseLifeCircle(2)">五道口生活圈</el-button>
    <p></p>
    <el-button type="success" @click="chooseContent(1)">食物</el-button>
    <el-button type="success" @click="chooseContent(2)">运动</el-button>
    <!-- 搜索栏 -->
    <div style="margin-top: 5px;">
        <el-input 
            class = "search"
            v-model="searchRequset"
            size="large"
            placeholder="输入搜索内容">
            <template #suffix>
                <el-icon style="color: brown;"><Search @click="search"/></el-icon>
            </template>
        </el-input> 
    </div>
    <!-- 筛选器 -->
    <el-radio-group v-model="radio" v-if="(contentType == 1)" >
        <el-radio :label="1" border class="radio">基于菜名搜索</el-radio>
        <el-radio :label="2" border class="radio">基于菜品种类搜索</el-radio>
        <el-radio :label="3" border class="radio">基于卡路里上限搜索</el-radio>
        <el-radio :label="4" border class="radio">基于饭店搜索</el-radio>
    </el-radio-group>
    <el-radio-group v-model="radio" v-else-if="(contentType == 2)">
        <el-radio :label="6" border class="radio">基于运动难度搜索</el-radio>
        <el-radio :label="7" border class="radio">基于卡路里下限搜索</el-radio>
    </el-radio-group>
    <p></p>
    <!-- 列表栏 -->
    <div class="list">
        <FoodView1 v-if="(contentType == 1)" type="choose" :lifeCicle="lifeCircle"></FoodView1>
        <SportView1 v-else-if="(contentType == 2)" type="choose" :lifeCicle="lifeCircle"></SportView1>
    </div>
</template>

<script>
import FoodView1 from "./FoodView.vue"
import SportView1 from "./SportView.vue"
import axios from "axios";
import { mapGetters, mapMutations, mapActions} from 'vuex';
export default{
    name: "ChooseView",
    components: {
        FoodView1,
        SportView1
    },
    data() {
        return {
            searchRequset: "",
            contentType: 1, //用于选择展示什么页面
            lifeCircle: 1,
            radio: 0,
        }
    },
    methods: {
        ...mapMutations(["initFoodList"]),
        chooseContent(type) {
            this.contentType = type;
            console.log(type);
        },
        chooseLifeCircle(type) {
            this.lifeCircle = type;
        },
        search() {
            console.log("搜索" + this.radio)
            var url = " "
            var content = {}
            switch(this.radio) {
                case 1: 
                    url = "http://localhost:8000/dish/searchByName/";
                    content = {
                        u_name: "123456",
                        d_name: this.searchRequset
                    };
                    break;
                case 2:
                    url = "http://localhost:8000/dish/searchByCategory/";
                    content = {
                        u_name: "123456",
                        d_category: this.searchRequset
                    };
                    break;
                case 3:
                    url = "http://localhost:8000/dish/searchByCalorie/"
                    content = {
                        u_name: "123456",
                        d_calories: this.searchRequset
                    }
                    break;
                case 4:
                    url = "http://localhost:8000/dish/searchByRestaurant/"
                    content = {
                        u_name: "123456",
                        re_name: this.searchRequset
                    }
                    break;
                case 6:
                    url = "http://localhost:8000/sport/searchByDifficulty/"
                    content = {
                        u_name: "123456",
                        re_name: this.searchRequset
                    }
                    break;
                case 7:
                    url = "http://localhost:8000/sport/searchByCalorie/"
                    content = {
                        u_name: "123456",
                        re_name: this.searchRequset
                    }
                    break;
                default:
                    url = "lalala"
                    content = {
                        id:"lalala",
                    }

            }
            console.log(url)
            console.log(content)
            axios.post(url, JSON.stringify(content))
            .then(res => {
                console.log(res.data);
                if(res.data.code != 200) {
                    alert(res.data.message)
                } else{
                    this.initFoodList(res.data);
                }
            })
        }
    }
}
</script>

<style scoped>
.radio {
    color: whitesmoke;
    background-color: rgba(239, 231, 224, 0.7);
}

.list {
    text-align: center;
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

