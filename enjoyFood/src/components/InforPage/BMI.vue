<script>
import {ref, reactive, onMounted} from 'vue'
import * as echarts from 'echarts'
import request from '../../https/axios.js'
export default {
  props:{
    userName:String,
  },
  setup(props){
    const BMI = ref(0)
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
            }).catch(function(error) {
                console.log("error");
                console.log(error);
            })
        };
    function draw(id) {
		    var chart = echarts.init(document.getElementById(id))
            chart.setOption({
                tooltip: {
                formatter: '{a} <br/>{b} : {c}%'
            },
            series: [
            {
                name: 'Pressure',
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
                value: BMI.value,
                name: 'BMI指数'
            }]
            }]
            })
        }
    onMounted(() => {
            init();
            draw("graph");
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
    <el-asider width='50%'>
    </el-asider>
    <el-main>  
        <div id="graph" style="width:200px; height:200px;"></div>
    </el-main>
  </el-container>
</div>
</template>

<style scoped>

</style>
