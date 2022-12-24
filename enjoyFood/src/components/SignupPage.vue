<script>
import {ref, reactive} from 'vue'
import { ElMessage } from 'element-plus'
import request from '../https/axios.js'

export default{
    setup(){
        const dialogVisible = ref(false)

        const information = reactive( {
                username: '',
                id: '',
                password: '',
                email : '' + "@buaa.edu.cn",
                profilePhoto: '',
                ensurePassword: '',
            });
        const labelPosition = ref('top')
        const openAlert1 = () => {
            ElMessage.error('Different Password !')
        }
        const openAlert2 = () => {
            ElMessage.error('Username Already Exists !')
        }
        return {information, labelPosition, dialogVisible, openAlert1, openAlert2};
    },

    methods: {
        async submit(){
            if(this.information.username.length > 10){
                
            }
            if(this.information.password != this.information.ensurePassword){
                console.log('in if');
                this.openAlert1();
            }
            else{
                console.log(this.information.username, this.information.password)

                const response = await request.post(
                    '/user/register/',
                    { u_name: this.information.username,
                      u_password: this.information.password,}      
                )
                console.log(response);
                if(response.data.code == 200){
                    this.dialogVisible = true;
                }else if(response.data.code == 400){
                    this.openAlert2();
                }
            }
        },

        async login(){
            console.log(this.information.username, this.information.password)

            const res = await request.post(
                '/user/login/',
                {   u_name: this.information.username,
                    u_password: this.information.password,}
            )
            console.log(res);
            this.$router.push({
                path: '/MainPage',
                query: {
                    userName: this.information.username,
                },
            });
        },

        async back(){
            this.dialogVisible = false;
        }
    }

}

const handleClose = () => {
  ElMessageBox.confirm('Are you sure to close this dialog?')
    .then(() => {
      done()
    })
    .catch(() => {
      // catch error
    })
}
</script>

<template>
<div class = 'SignupPage'>
    <div class = "SignUpBox">
        <h1 class="title">注册系统</h1>
        <div style="margin: 20px 0"/>
        <div class = "SignUpBox">
             <el-form
                :label-position="labelPosition"
                :model="information"
                style="max-width: 460px"
                class="signUpForm"
            >
                <el-form-item>
                    <el-input 
                        v-model="information.username" 
                        placeholder="请输入用户名" >
                        <template #prefix>
                            <el-icon><UserFilled /></el-icon>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item>
                    <el-input 
                        v-model="information.password" 
                        type="password" 
                        placeholder="请输入密码" 
                        show-password >
                        <template #prefix>
                            <el-icon><Key /></el-icon>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item>
                    <el-input 
                        v-model="information.ensurePassword" 
                        type="password" 
                        placeholder="请重复输入密码" 
                        show-password >
                        <template #prefix>
                            <el-icon><Key /></el-icon>
                        </template>
                    </el-input>
                </el-form-item>
            </el-form>
            <el-button type="login" round @click="submit()">
                <p class='buttonLabel'>Submit</p>
            </el-button>
            
            <el-dialog
                v-model="dialogVisible"
                title="Tips"
                width="30%"
                :before-close="handleClose"
            >
                <p> Your username is {{information.username}}.</p>
                <p> Your password is {{information.password}}.</p>
                <p> Please Complete Your Information. </p>
                <template #footer>
                    <el-button @click="back()"><p class='buttonLabel'>back</p></el-button>
                    <el-button type="login" @click="login()">
                        <p class='buttonLabel'>login</p>
                    </el-button>
                </template>
            </el-dialog>
        </div>
    </div>
</div>    
</template>

<style>
.Head{
    font-weight: 900;
    margin-bottom: 20px;
    font-size: 200%;
}
.signUpForm{
    padding-top: 5%;
    padding-bottom: 2%;
}
.SignUpBox {
    padding-left: 10%;
    padding-right: 20%;
}
.label{
    font-weight: bold;
}
.buttonLabel{
    font-weight: bold;
}
.dialog-footer button:first-child {
  margin-right: 10px;
}
.el-alert {
  margin: 20px 0 0;
}
</style>