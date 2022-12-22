<script>
import EditInfoPage from './EditInfoPage.vue'
import {useRoute} from 'vue-router'

export default {
    components: { EditInfoPage },
    setup(){
        let route = useRoute()
        const userName = route.query.userName;
        const passWord = route.query.passWord;
        console.log(userName, passWord);
        return {userName, passWord};
    },
    data(){
        return {
            information: {
                username: "pangrj",
                id: '',
                password: '',
                email :"pangrj@buaa.edu.cn",
                profilePhoto: '',
            },
        }
    },

    methods: {
        ClickEdit(){
            this.$router.push({path: '/EditInfoPage'})
        }
    }
}
</script>

<template>
  <div class="common-layout">
    <el-container>
    <el-header>
    <div class="infoBox">
        <div class="Total">
            <div class="TotalIn">
            <div class="photo" >
                <el-avatar :size="100" :src="circleUrl" />
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
                <el-button plain @click="ClickEdit()">
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
    <template>
        <el-radio-group v-model="isCollapse" style="margin-bottom: 20px">
            <el-radio-button :label="false">expand</el-radio-button>
            <el-radio-button :label="true">collapse</el-radio-button>
        </el-radio-group>
        <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            :collapse="isCollapse"
            @open="handleOpen"
            @close="handleClose"
        >
        <el-sub-menu index="1">
            <template #title>
                <el-icon><location /></el-icon>
                <span>Navigator One</span>
            </template>
            <el-menu-item-group>
                <template #title><span>Group One</span></template>
                <el-menu-item index="1-1">item one</el-menu-item>
                <el-menu-item index="1-2">item two</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="Group Two">
                <el-menu-item index="1-3">item three</el-menu-item>
            </el-menu-item-group>
            <el-sub-menu index="1-4">
                <template #title><span>item four</span></template>
                <el-menu-item index="1-4-1">item one</el-menu-item>
            </el-sub-menu>
        </el-sub-menu>
        <el-menu-item index="2">
            <el-icon><icon-menu /></el-icon>
            <template #title>Navigator Two</template>
        </el-menu-item>
        <el-menu-item index="3" disabled>
            <el-icon><document /></el-icon>
            <template #title>Navigator Three</template>
        </el-menu-item>
        <el-menu-item index="4">
            <el-icon><setting /></el-icon>
            <template #title>Navigator Four</template>
        </el-menu-item>
        </el-menu>
    </template>
    </div>
    </el-header>
    <el-container class = "down">
    <el-aside width="25%">
    </el-aside>
    <el-main>
        <h2> </h2>
            <div class="demo-collapse">
            <el-collapse v-model="activeName" accordion>
                <el-collapse-item name="1">
                    <template #title>
                        <el-icon class="header-icon"> 
                            <info-filled />
                        </el-icon>
                        —最新通知
                    </template>
                    <div>
                    Consistent with real life: in line with the process and logic of real
                    life, and comply with languages and habits that the users are used to;
                    </div>
                    <div>
                    Consistent within interface: all elements should be consistent, such
                    as: design style, icons and texts, position of elements, etc.
                    </div>
                </el-collapse-item>
                <el-collapse-item title="—个性推荐" name="2">
                    <div>
                    Operation feedback: enable the users to clearly perceive their
                    operations by style updates and interactive effects;
                    </div>
                    <div>
                    Visual feedback: reflect current state by updating or rearranging
                    elements of the page.
                    </div>
                </el-collapse-item>
                <el-collapse-item title="—我的点餐" name="3">
                    <div>
                    Simplify the process: keep operating process simple and intuitive;
                    </div>
                    <div>
                    Definite and clear: enunciate your intentions clearly so that the
                    users can quickly understand and make decisions;
                    </div>
                    <div>
                    Easy to identify: the interface should be straightforward, which helps
                    the users to identify and frees them from memorizing and recalling.
                    </div>
                </el-collapse-item>
                <el-collapse-item title="—浏览评论" name="4">
                    <div>
                    Decision making: giving advices about operations is acceptable, but do
                    not make decisions for the users;
                    </div>
                    <div>
                    Controlled consequences: users should be granted the freedom to
                    operate, including canceling, aborting or terminating current
                    operation.
                    </div>
                </el-collapse-item>
            </el-collapse>
        </div>
    </el-main>
    </el-container>
    </el-container>
  </div>
</template>

<style>
.common-layout{
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
    margin: 0px 16px 0px 0px;
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
.demo-collapse{
    padding-left: 10%;
    padding-right: 10%;
    padding-top: 5%;
    padding-bottom: 30%;
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
}
p{
    font-size: 1.0em;
    margin-block-start: 0.5em;
}
el-collapse-item{
    padding-left: 5%;
    padding-right: 5%;
}
</style>