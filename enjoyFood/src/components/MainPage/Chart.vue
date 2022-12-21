<script type="text/javascript">
import * as echarts from 'echarts'
import request from '../../https/axios.js'
import {ref, reactive, onMounted} from 'vue'

export default {
    props: {
        userName: String,
    },
    setup(props) {
        
    },
    data(){
        return {
            lineTimeData: ["11.5", "11.21", "11.23", "11.30", "12.5", "12.6"], 
            lineOpinionData: ["100", "80", "10", "-50", "-30", "70"],
            sectorPartName: ["takeIn", "cost", "left"],
            sectorPartData: [300, 100, 200],
        }
    },
    methods: {
        async initInfor(){
            console.log(this.userName)
            const response = await request.post(
                '/user/getPlanCal/',
                this.userName,
            );
            console.log("response");
            console.log(response);
            this.lineTimeData = ["11.5", "11.21", "11.23", "11.30", "12.5", "12.6"]
            this.lineOpinionData = ["100", "80", "10", "-50", "-30", "70"]
            this.sectorPartName =  ["takeIn", "cost", "left"]
            this.sectorPartData = [300, 100, 200]
        },
        drawLine(id) {
				this.lineCharts = echarts.init(document.getElementById(id))
				this.lineCharts.setOption({
                    title:{
                        left:'3%',
                        top:'4%',
                        text:"weight flows",//标题文本，支持使用 \n 换行。
                    },
					tooltip: {
						trigger: 'axis'
					},
					legend: {
                        align:'right',//文字在前图标在后
                        left:'3%',
                        top:'5%',
						data: ['week']
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
                        data: this.lineTimeData //x坐标的名称
					
					},
					yAxis: {
						type: 'value',
						boundaryGap: true,
                        splitNumber:4, //纵坐标数
                        interval:250 //强制设置坐标轴分割间隔
					},
 
					series: [{
						name: '近一周',
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
						data: this.lineOpinionData
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
        this.$nextTick(function() {
		this.drawLine('lineChart');
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
            <div id="lineChart" style="width;100%; height: 300px;"></div>
        </el-aside>
        <el-main>
            <div id="sectorChart" style="width:100%; height: 300px;"></div>
        </el-main>
    </el-container>
</div>
</template>

<style scoped>
.body{
    padding-top: 7%;
}
</style>