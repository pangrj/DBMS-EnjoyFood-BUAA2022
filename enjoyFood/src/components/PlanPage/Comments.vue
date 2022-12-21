<script>
import {ref, reactive, onMounted} from 'vue'
import request from '../../https/axios.js'

export default {
  props:{
    userName: String,
    planId: String,
  },
  setup(props) {
    const stars = ref(null)
    const colors = ref(['#99A9BF', '#F7BA2A', '#FF9900'])
    return {stars, colors}
  },
  data() {
    return {
        comments: [{r_comment:"GOGOGO!", r_data: "12.1", r_star: 3.5, user:{u_name:"John"}},
            {r_comment:"KFC!", r_data: "12.2", r_star: 4.0, user:{u_name:"Bob"}},
            {r_comment:"Vme50!", r_data: "12.3", r_star: 4.5, user:{u_name:"John"}},
            ],
        curComment: "",
    };
  },
  methods: {
    async initInfor(){
            console.log(this.planId.toString())
            request({
                method: 'POST',
                url: '/comment/getCommentOfPlan/',
                data: this.planId.toString(),
                header: {'Content-Type': 'application/json'},
            }).then(function(response) {
                console.log(response);
                this.comments = response.data.comments;
                console.log(this.comments);
            }).catch(function(error) {
                console.log("error");
                console.log(error);
            });
        },
    async send(){
        request({
                method: 'POST',
                url: '/comment/publishComment/',
                data: {   
                    u_name: this.userName,
                    p_id: this.planId,
                    r_star: this.stars,
                    r_content: this.curComment,
                    }
                }
            ).then(function(response) {
                console.log(response);
            });
        this.initInfor();
    }
  },
  mounted(){
        this.initInfor();
  },
}
</script>

<template>
<div class='body'>
    <div class="input">
        <el-rate class="stars" v-model="stars" :colors="colors" />
        <div class="send">
        <el-input
            v-model="curComment"
            autosize
            type="textarea"
            placeholder="输入评论..."
        />
        <el-button round type="Default" class="button" @click="send()">Send</el-button>
        </div>
    </div>
    <div class="one" v-for="comment in comments" :key="comment">
        <el-divider>
            <el-icon><star-filled /></el-icon>
        </el-divider>
        <el-container> 
            <el-header>
                <el-container>
                    <el-aside width="10%">
                        <el-avatar :size="50" src= "../src/assets/male.jpg" />
                    </el-aside>
                    <el-aside width="7%">
                        <p class="name">{{comment.user.u_name}}</p>
                        <span class="date">{{comment.r_data}}</span>
                    </el-aside>
                    <el-main>
                        <el-rate
                            v-model="comment.r_star"
                            disabled
                            show-score
                            text-color="#ff9900"
                            score-template=""
                        />
                    </el-main>
                    <el-aside width="65%"></el-aside>
                </el-container>
            </el-header>
            <el-main>
                <p class="content">{{comment.r_comment}}</p>
            </el-main>
        </el-container>
    </div>
</div>
</template>

<style scoped>
.body{
    padding-top: 1%;
}
.input{
    background-color: #fcf8f8;
    padding-top: 2%;
    padding-left: 7%;
    padding-right: 7%;
    padding-bottom: 2%;
    margin-left: 3%;
    margin-right: 3%;
}
.send{
    padding-top: 1%;
    display: flex;
}
.one{
    padding-left: 10%;
    padding-right: 10%;
}
.name{
    text-align: left;
    font-weight: bolder !important;
}
.date{
    text-align: left;
    font-weight: light !important;
}
.content{
    padding-left: 20%;
    text-align: left;
}
.button{
    margin-left: 4%;
}
.demo-rate-block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  display: inline-block;
  width: 49%;
  box-sizing: border-box;
}
.demo-rate-block:last-child {
  border-right: none;
}
.demo-rate-block .demonstration {
  display: block;
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}
</style>