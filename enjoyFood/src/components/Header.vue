<script>
export default {
    props: {
        userName: String,
    },
    setup(){
        
    },
    methods: {
        clickToMain(){
            console.log(this.userName)
            this.$router.push({
                path: '/MainPage',
                query: {
                    userName: this.userName,
                },
            });
        },
        clickToInfor(){
            console.log(this.userName)
            this.$router.push({
                path: '/InfomationPage',
                query: {
                    userName: this.userName,
                },
            });
        },
        clickToChoose(){
            console.log(this.userName)
            this.$router.push({
                path: '/ChoosePage',
                query: {
                    userName: this.userName,
                },
            });
        },
    },
}
</script>

<template>
    <div class="boby">
        <ul style="display:flex">
            <div class="left">
            <li  style="padding-left:%5; margin-right:%200">
                <el-icon><KnifeFork /></el-icon>
                <a v-on:click="clickToMain()">广场页面</a>
            </li>
            <li  style="margin-left:20px; margin-right:30px">
                <a v-on:click="clickToChoose()">制订计划</a>
            </li>
            </div>
            <li>
                <span style="font-weight:550 ;margin-left:100px; margin-right:100px">Enjoy Lives !</span>
            </li>
            <div class="right">
            <li>
                <span>{{userName}}</span>
            </li>
            <li>
                <a @click="clickToInfor()" round>个人信息</a>
            </li>
            </div>
        </ul>
    </div>
</template>

<style scoped>
.body{
    margin-top: 10%;
    font-display: 700;
    height: 64px;
    position: fixed;
}
.ul{
    margin-top: 10%;
}
.left{
    display: flex;
    align-items: center;
    flex-shrink: 0;
    margin-left: 2%;
    margin-right: 20%;
}
.right{
    display: flex;
    align-items: center;
    flex-shrink: 0;
    margin-left: 20%;
    margin-right: 2%;
}
.li{
    border: 0;
    font-family: inherit;
    font-size: 100%;
    font-weight: 400;
    font-style: normal;
    line-height: 1.55;
    display: list-item;
    text-align: -webkit-match-parent;
}
span{
    font-size: 120%;
}
a{
    font-size: 120%;
    font-weight: 550;
}
</style>