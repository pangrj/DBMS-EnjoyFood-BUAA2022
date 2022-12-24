<script>
import {ref, reactive, onMounted} from 'vue'
import request from '../../https/axios.js'

export default {
  props:{
    userName: String,
    planId: String,
  },
  setup(props) {
    const stars = ref(null);
    const colors = ref(['#99A9BF', '#F7BA2A', '#FF9900'])
    const comments = ref([{r_content:"GOGOGO!", r_data: "12.1", r_star: 3.5, u_name:"John", date: "12-1"},
            {r_content:"KFC!", r_data: "12.2", r_star: 4.0, u_name:"Bob", date: "12-2"},
            {r_content:"Vme50!", r_data: "12.3", r_star: 4.5, u_name:"John", date: "12-3"},
            ]);
    function initInfor(){
            console.log(props.planId)
            request({
                method: 'POST',
                url: '/comment/getCommentOfPlan/',
                data: {p_id: props.planId},
            }).then(function(response) {
                console.log(response);
                var commentList = []
                var field = {}
                for( var p in response.data.comments){
                    field = response.data.comments[p].fields
                    field["p_id"] = response.data.comments[p].pk
                    field["date"] = field["r_data"].match(/([0-9]*-[0-9]*)( )([0-9]*:[0-9]*)/)[1]
                    console.log(field.date)
                    comments.value.push(field)
                }
                console.log(comments);
            }).catch(function(error) {
                console.log("error");
                console.log(error);
            });
        };
        initInfor();
    return {stars, colors, comments}
  },
  data() {
    return {
        curComment: "",
    };
  },
  methods: {
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
                        <p class="name">{{comment.u_name}}</p>
                        <span class="date">{{comment.date}}</span>
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
                <p class="content">{{comment.r_content}}</p>
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