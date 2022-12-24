<script>
import {ref, reactive, onMounted} from 'vue'
import * as echarts from 'echarts'
import request from '../../https/axios.js'
export default {
  props:{
    userName:String,
  },
  setup(props){
    const BMI = ref(20)
    const suggestion = ref("")
        function init() {
            console.log("init")
             request({
                 method: 'POST',
                url: '/user/suggest/',
                data: {  
                    u_name: props.userName,
                    }
                }
            ).then(function(response) {
                console.log("reponse: ")
                console.log(response);
                BMI.value = response.data.BMI;
                suggestion.value = response.data.suggestion;
                console.log(BMI.value)
                console.log(suggestion.value)
                setTimeout(() => {
                draw("graph", BMI.value.toFixed(2));
                }, 200);
            }).catch(function(error) {
                console.log("error");
                console.log(error);
            })
        };
    function draw(id, value) {
		    var chart = echarts.init(document.getElementById(id))
            chart.setOption({
                tooltip: {
                formatter: '{a} <br/>{b} : {c}%'
            },
            series: [
            {
                name: 'BMI',
                type: 'gauge',
                progress: {
                    show: true
                },
                detail: {
                    valueAnimation: true,
                    formatter: '{value}'
                },
            data: [
            {
                value: BMI.value.toFixed(2),
                name: 'BMI指数'
            }]
            }]
            })
        }
    onMounted(() => {
            init();        
        });
    return{BMI, suggestion};
  },
  data() {
    return {
    };
  },
}
</script>

<template>
<div class='body'>
  <el-container>
    <el-aside width="50%">
        <div class="suggest">
            <h2>建议:</h2>
            <p style="font-size: 1.5em;">{{suggestion}}</p>
        </div>
    </el-aside>
    <el-main>  
        <div id="graph" style="width:300px; height:300px;"></div>
    </el-main>
  </el-container>
</div>
</template>

<style scoped>
.suggest{
    width: 100%;
    padding-top: 20%;
}
</style>
