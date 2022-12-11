<script>
import { useRouter } from 'vue-router'

import {ref} from 'vue'
import SignupPage from './SignupPage.vue'
const userName = ref('')
const passWord = ref('')

import request from '../https/axios.js'

export default {
  components: { SignupPage },
    data(){
        return {
            userName,
            passWord,
        }
    },
    setup(){
        const inputMode = ref('Login')
        return{ inputMode }
    },
    methods: {
        async onClickLogin(){
            console.log(userName.value, passWord.value)
            await request({
                method: 'POST',
                url: '/user/login/',
                data: {   u_name: userName.value,
                    u_password: passWord.value,}
                }
            ).then(function(response) {
                console.log(response);
            }).catch(function(error) {
                console.log(error);
            })
            this.$router.push({
                path: '/ChoosePage',
                query: {
                    userName: userName.value,
                    passWord: passWord.value,
                },
            });
        },
        onClickSignUp(){
            this.$router.push({
                path: '/SignupPage',
            });
        }
    }
}

</script>

<template>
    <div class = "LoginPage">
        <div class = "header">
            <el-radio-group v-model="inputMode" label="input mode" class="control">
                <el-radio-button label="Login">Login</el-radio-button>
                <el-radio-button label="Signup">Signup</el-radio-button>
            </el-radio-group>
        </div>
        {{userName}}
        <el-container>
        <el-header class = 'head'>
            <h1 class='Head'> Welcome to EnjoyFood! </h1>
        </el-header>
        <el-container>
        <el-aside width="50%">
        <div title="WelcomeBox">
            <h1 class='welcome'>Some of New Delicious Food </h1>
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
        <div title="LoginBox" v-if="inputMode=='Login'">
            <div class = "InputBox">
            <!--el-card shadow="always"w-->
                <h1 class="title">登录点菜系统</h1>
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
                <el-button @click="onClickLogin()" type="login" round style="margin-right: 15px"><p>login</p></el-button>
                <el-button @click="onClickSignUp()" type="login" round><p>signUp</p></el-button>
            <!--/el-card-->
            </div>
        </div>
        <div title="SignupBox" v-if="inputMode=='Signup'">
            <SignupPage />
        </div>
        </el-main>
        </el-container>
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
  padding-top: 50px;
  position: fixed;
}
.header{
    height: 70px;
}
.control{
    float: right;
    margin-right: 10%;
}
.head{
    padding-bottom: 130px;
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
    padding-right: 20%;
}
.runningPicture{
    padding-left: 15%;
    padding-right: 10%;
    padding-top: 0%;
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
.Head{
    font-weight: 900;
    margin-bottom: 20px;
    font-size: 200%;
}
.welcome{
    font-weight: 700;
    font-size: 150%;
}
.title{
    font-weight: 700;
    margin-right: 15px;
    font-size: 150%;
}
h1{
    font-weight: 800;
}
p{
    font-weight: bold;
}

</style>
