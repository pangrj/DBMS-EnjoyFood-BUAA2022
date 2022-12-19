<script>
import {useRoute} from 'vue-router'
import {ref, reactive, onMounted} from 'vue'
import { UploadFilled } from '@element-plus/icons-vue'
import request from '../https/axios.js'
import Header from './Header.vue'
import Personal from './InforPage/Personal.vue'

export default {
    components: { Header, Personal, Personal },
    setup(){
        let route = useRoute()
        const userName = route.query.userName;
        console.log(userName);
        
        const ava_path = new URL(`./src/assets/avatar.jpg`, import.meta.url).href

        const dialogVisible = ref(false);
        const information = reactive( {
                u_name: userName,
                u_id: 'initial',
                u_password: 'initial',
                u_position: 'initial',
                u_gender: "True",
                u_email : 'initial' + "@buaa.edu.cn",
                u_photo: File,
                u_age: 0,
                u_height: 0,
                u_weight: 0,
            });

        // init:
        /*function init() {
            request({
                method: 'POST',
                url: '/user/getInfor/',
                data: {   u_name: userName,
                    }
                }
            ).then(function(response) {
                console.log(response);
                this.information.u_id = response.u_id;
                this.information.u_position = response.u_position;
                this.information.u_gender = response.u_gender;
                this.information.u_email = response.u_email;
                this.information.u_photo = response.u_photo;
                this.information.u_age = response.u_age;
                this.information.u_height = response.u_height;
                this.information.u_weight = response.u_weight;
            }).catch(function(error) {
                console.log(error);
            })
        };

        onMounted(() => {
            init();
        });*/

        const settings = reactive( {
            NightMode: false, 
        });
        return {userName, dialogVisible, information};
    },
    data(){
        return {
        }
    },

    methods: {
        async initInfor(){
            const response = await request.post(
                '/user/getInfor/',
                this.userName,
            );
            console.log(response);
            this.information.u_id = response.u_id;
            this.information.u_position = response.u_position;
            this.information.u_gender = response.u_gender;
            this.information.u_email = response.u_email;
            this.information.u_photo = response.u_photo;
            this.information.u_age = response.u_age;
            this.information.u_height = response.u_height;
            this.information.u_weight = response.u_weight;
        },
        async updateInfo(){
            this.dialogVisible = false;
            console.log(this.information);

            let formData = new FormData();
            formData.append('u_name', this.information.u_name);
            formData.append('u_password', this.information.u_password);
            formData.append('u_height', this.information.u_height);
            formData.append('u_weight', this.information.u_weight);
            formData.append('u_age', this.information.u_age);
            formData.append('u_position', this.information.position);
            formData.append('u_gender', this.information.gender);
            formData.append('u_email', this.information.u_email);
            formData.append('u_avatar', this.information.u_photo);

            console.log(formData.get('u_avatar'));
            const res = await request.post(
                '/user/modify/',
                formData);
            console.log(res);  
            this.ava_path = res.img_path;
            /*const {data:res} = await request.post(
                '/student/modify',
                {   s_id: information.id,
                    s_passWord: information.passWord,
                    s_name: information.username,
                    s_dorm: '',
                    s_gender: '',
                }
            )*/
        },
        getImageFile:function(e){
            console.log("in getImgFunc!")
            let file = e.target.files[0];
            this.information.u_photo = file;
            console.log(file)
        },
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
<div>
    <Header v-bind:userName="userName"/>
  <div class="InfomationPage">
    <el-container>
    <el-header>
    <div class="infoBox">
        <div class="Total">
            <div class="TotalIn">
            <div class="photo" >
                <el-avatar :size="100" src= "ava_path" />
                
            </div>
            <div class="nameAndemail">
                <h2>{{userName}}</h2>
                <p inline='true'>
                    <el-icon class="emailIcon"><Message /></el-icon>emial
                </p>
            </div>
            </div>
        </div>
        <div class="Items">
            <div class="ItemsIn">
            <div class="leftItem">
                <el-button plain @click="dialogVisible = true">
                    <el-icon class="editIcon"><EditPen /></el-icon>
                    Edit Information
                </el-button>
            </div>
            <div class="rightItem">
                <el-button plain @click="ClickSettings()">
                    <el-icon class="setIcon"><Setting /></el-icon>
                    Settings
                </el-button>
            </div>
            </div>
        </div>
    </div>
    <div class="moreInfo">
    </div>
    </el-header>
    <el-container class = "down">
    <el-aside width="25%">
    </el-aside>

    <el-main>
        <h2></h2>
            <div class="mainPart">
            <el-collapse v-model="activeName" accordion>
                <el-collapse-item name="1">
                    <template #title style="font-weight: bold">
                        <p> Up-to-Date Notices </p>
                    </template>
                    <div>
                    </div>
                </el-collapse-item>
                <el-collapse-item name="2">
                    <template #title style="font-weight: bold">
                        <p> Personal Information </p>
                    </template>
                    <div>
                        <personal :information="information" />
                    </div>
                </el-collapse-item>
                <el-collapse-item name="3">
                    <template #title style="font-weight: bold">
                        <p> My Plans </p>
                    </template>
                    <div>
                    </div>
                </el-collapse-item>
                <el-collapse-item name="4">
                    <template #title style="font-weight: bold">
                        <p> Others </p>
                    </template>
                    <div>
                    </div>
                </el-collapse-item>
            </el-collapse>
        </div>
    </el-main>
    <el-aside width="25%">
    </el-aside>
    </el-container>
    </el-container>

    <el-dialog
        v-model="dialogVisible"
        title="Tips"
        width="30%"
        :before-close="handleClose"
    >
        <span>Please edit your informaion</span>
        <el-form
        :label-position="labelPosition"
        label-width="100px"
        :model="information"
        style="max-width: 460px; padding-top:20px"
        >
        <el-form-item label="username">
            <el-input v-model="information.u_name" />
        </el-form-item>
        <el-form-item label="id">
            <el-input v-model="information.u_id" />
        </el-form-item>
        <el-form-item label="email">
            <el-input v-model="information.u_email" />
        </el-form-item>
        <el-form-item label="password">
            <el-input v-model="information.u_password" />
        </el-form-item>
        <el-form-item label="position">
            <el-input v-model="information.u_position" />
        </el-form-item>
        <el-form-item label="age">
            <el-input v-model="information.u_age" />
        </el-form-item>
        <el-form-item label="avatar">
            <input type="file" @change="getImageFile" id="img" />
        </el-form-item>
        </el-form>
        <!--
        <el-upload
            class="upload"
            drag
            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
        >
            <el-icon class="el-icon--upload"><upload-filled /></el-icon>
            <div class="el-upload__text">
                Drop profilePhoto here <em>click to upload</em>
            </div>
            <template #tip>
                <div class="el-upload__tip">
                jpg/png files with a size less than 500kb
                </div>
            </template>
        </el-upload>
        -->
        <template #footer>
            <span class="dialog-footer">
            <el-button @click="dialogVisible = false">Cancel</el-button>
            <el-button type="primary" @click="updateInfo()">
            Confirm
            </el-button>
        </span>
        </template>
    </el-dialog>
    </div>
</div>
</template>

<style>
.InfomationPage{
    background-color: #F8F8F8;
    padding-top: 3%;
}
.down{
    padding-top: 3%;
}
.InfoBox{
    width: 100%;
    overflow: hidden;
    padding: 30px 50px 0px;
}
.Total{
    width : 50%;
    float: left;
}
.TotalIn{
    display: flex;
    width: auto;
    height: auto;
    padding: 13px 100px 8px;
}
.photo{
    display: flex;
    flex-wrap: nowrap;
    width: 120px;
    height: auto;
    margin: 0px 10px 0px 0px;
}
.nameAndemail{
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    width: auto;
    height: auto;
    box-sizing: border-box;
}
.emailIcon{
    padding-right: 5px;
}
.Items{
    flex-wrap: wrap;
    width: 50%;
    float: right;
    overflow: visible;
    height: auto;
    justify-content: flex-end;
    display: flex;
}
.ItemsIn{
    display: flex;
    flex-flow: row wrap;
    margin: 0px;
    overflow: visible;
    box-sizing: border-box;
    width: 100%;
    max-width: 100vw;
    justify-content: flex-end;
    height: 100%;
}
.leftItem{
    width: 50%;
    float: left; 
    padding-top: 60px;
}
.rightItem{
    width: 50%;
    float: right;
    padding-top: 60px;
}
.editIcon{
    padding-right:  7px;
}
.setIcon{
    padding-right: 7px;
}
.moreInfo{
    height: 70%;
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.mainPart{
    padding-left: 5%;
    padding-right: 5%;
    padding-top: 5%;
    padding-bottom: 80%;
    background-color: #fff;
    font-weight: bold;
}
header{
    
}
main{
    padding-top: 5%;
}
h2{
    font-size: 1.5em;
    margin-block-end: 0.2em;
    text-align: left;
    font-weight: bold;
}
p{
    font-size: 1.0em;
    font-weight: bold;
    margin-block-start: 0.5em;
    margin-left: 5px;
}
el-collapse-item{
    padding-left: 5%;
    padding-right: 5%;
    font-weight: bold;
}
</style>