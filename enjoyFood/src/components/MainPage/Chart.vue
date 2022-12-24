<script type="text/javascript">
import * as echarts from 'echarts'
import request from '../../https/axios.js'
import {ref, reactive, onMounted, toRaw} from 'vue'

export default {
    props: {
        userName: String,
    },
    setup(props) {
        
    },
    data(){
        return {
            lineTimeData: ["12-1","12-2","12-3"], 
            lineOpinionData: [1,2,3],
            sectorPartName: ["takeIn", "cost", "left"],
            sectorPartData: [300, 100, 200],
        }
    },
    methods: {
        async initInfor(){
            console.log(this.userName)
            const response = await request.post(
                '/user/getPlanCal/',
                {u_name: this.userName},
            );
            console.log("response");
            console.log(response);
            var takein = 0
            var consume = 0

            for(var i=0; i<response.data.num; i++){
                var field = response.data.cals_in_list[i]-response.data.cals_minus_list[i];
                this.lineOpinionData[i] = (field);
                this.lineTimeData[i] = (response.data.time[i])
                takein = takein + response.data.cals_in_list[i]
                consume = consume + response.data.cals_minus_list[i]
            }
            this.sectorPartName =  ["takeIn", "cost", "left"]
            this.sectorPartData = [toRaw(takein), toRaw(consume), toRaw(takein - consume)]
            console.log(toRaw(this.lineOpinionData))
            this.drawLine('lineChart');
        },
        drawLine(id) {
				this.lineCharts = echarts.init(document.getElementById(id))
				this.lineCharts.setOption({
                    title:{
                        left:'3%',
                        top:'4%',
                        text:"卡路里 flows",//标题文本，支持使用 \n 换行。
                    },
					tooltip: {
						trigger: 'axis'
					},
					legend: {
                        align:'right',//文字在前图标在后
                        left:'3%',
                        top:'5%',
						data: ['Time']
					},
					grid: {
                        top:'15%',
						left: '5%',
						right: '5%',
						bottom: '5%',
						containLabel: true
					},
 
					toolbox: {
						feature: {
							saveAsImage: {} //保存为图片
						}
					},
					xAxis: {
						type: 'category',
                        boundaryGap:true,
                        axisTick:{
                            alignWithLabel:true //保证刻度线和标签对齐
                        },
                        data: toRaw(this.lineTimeData) //x坐标的名称
					
					},
					yAxis: {
						type: 'value',
						boundaryGap: true,
                        splitNumber:4, //纵坐标数
                        interval:250 //强制设置坐标轴分割间隔
					},
 
					series: [{
						name: 'plan',
						type: 'line', //折线图line;柱形图bar;饼图pie
						stack: '总量',
                        areaStyle: {
                            //显示区域颜色---渐变效果
                            color:{
                                type: 'linear',
                                x: 0,
                                y: 0,
                                x2: 0,
                                y2: 1,
                                colorStops: [{
                                    offset: 0, color: 'rgb(255,200,213)' // 0% 处的颜色
                                }, {
                                    offset: 1, color: '#ffffff' // 100% 处的颜色
                                }],
                                global: false // 缺省为 false
                            }
                        },
                        itemStyle: {
							color: 'rgb(255,96,64)', //改变折线点的颜色
							lineStyle: {
								color: 'rgb(255,96,64)' //改变折线颜色
							}
                            
                        },
						data: toRaw(this.lineOpinionData)
					}]
				})
			},
        drawSector() {
            this.requested = true;
            var getData = [];
            for (let i = 0; i < 3; i++) {
            var obj = new Object();
            obj.name = this.sectorPartName[i];
            obj.value = this.sectorPartData[i];
            getData[i] = obj;
            }
            // 基于准备好的dom，初始化echarts实例
                var myChart = echarts.init(document.getElementById("sectorChart"));
                // 绘制图表
                myChart.setOption({
                title: {
                    text: '卡路里含量',
                    x:'center'
                },
                tooltip: {
                    trigger: "item",
                    formatter: "{a} <br/>{b} : {c} ({d}%)",
                },
                legend: {
                    orient: 'vertical',
                    bottom: 'bottom',
                    data: getData
                },
                series: [
                    {
                    name: "部分",
                    type: "pie",
                    radius: "55%",
                    center: ["50%", "50%"],//位置
                    data: getData,
                    itemStyle: {
                        emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: "rgba(0, 0, 0, 0.5)",
                    },
                },
                },
            ],
            });
        this.requested = false;
        },
	},
    mounted(){
        this.initInfor();
        console.log(this.lineOpinionData)
        console.log(this.lineTimeData)
        console.log(["1","2","3"])
        this.$nextTick(function() {
        setTimeout(() => {
                this.drawSector();
                }, 200);
			})
        }
}

</script>

<template>
<div>
    <el-container class = 'body'>
        <el-aside width="50%">
            <div id="lineChart" style="width:90%; height: 350px;"></div>
        </el-aside>
        <el-main>
            <div id="sectorChart" style="width:90%; height: 300px;"></div>
        </el-main>
    </el-container>
</div>
</template>

<style scoped>
.body{
    padding-top: 7%;
    padding-left: 7%;
}
</style>