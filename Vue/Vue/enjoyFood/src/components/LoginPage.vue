<script>
import { useRouter } from 'vue-router'

import {ref} from 'vue'
const userName = ref('')
const passWord = ref('')

export default {
    data(){
        return {
            userName,
            passWord,
        }
    },
    methods: {
        onClick(){
            console.log(userName, passWord)
            this.$router.push({
                path: '/ChoosePage',
                query: {
                    userName: userName.value,
                    passWord: passWord.value,
                },
            });
        }
    }
}

</script>

<template>
    <div class = "LoginPage">
        {{userName}}
        <el-container>
        <el-aside width="50%">
        <div title="WelcomeBox">
            <h1>Welcome to EnjoyFood!</h1>
            <div class="runningPicture">
            <el-carousel height="175px">
                <el-carousel-item v-for="item in 4" :key="item">
                    <h3 class="small justify-center" text="2xl">{{ item }}</h3>
                </el-carousel-item>
            </el-carousel>
            </div>
        </div>
        </el-aside>
        <el-main>
        <div title="LoginBox" >
            <div class = "InputBox">
            <!--el-card shadow="always"w-->
                <h2 >登录点菜系统</h2>
                <div style="margin: 20px 0"/>
                <div class = "InputBox">
                <el-input 
                    v-model="userName" 
                    placeholder="请输入用户名" >
                    <template #prefix>
                        <el-icon><UserFilled /></el-icon>
                    </template>
                </el-input>
                <div style="margin: 20px 0" />
                <el-input 
                    v-model="passWord" 
                    type="password" 
                    placeholder="请输入密码" 
                    show-password >
                    <template #prefix>
                        <el-icon><Key /></el-icon>
                    </template>
                </el-input>
                </div>
                <div style="margin: 20px 0" />
                <el-button @click="onClick()" type="login" round>login</el-button>
            <!--/el-card-->
            </div>
        </div>
        </el-main>
        </el-container>
    </div>
</template>

 
<style lang='postcss'>

.LoginPage {
  background: url("./src/assets/background.jpg");
  background-size: cover;
  opacity: 0.75;
  width: 100%;
  height: 100%;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  padding-top: 250px;
  position: fixed;
}
/*.LoginPage > div {
  height: 22px;
  flex: 1;
}*/
.WelcomeBox{
    padding-left: 20%;
}
.LoginBox{
}
.InputBox {
    padding-left: 10%;
    padding-right: 25%;
}
.runningPicture{
    padding-left: 15%;
    padding-right: 10%;
    padding-top: 5%;
}
.demonstration {
  color: var(--el-text-color-secondary);
}
.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
  background-image: url("./src/assets/yimian.jpg");
  background-size: 100%;
}

</style>
