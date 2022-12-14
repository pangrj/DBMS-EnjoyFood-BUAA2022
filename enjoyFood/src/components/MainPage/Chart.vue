<script>
import * as echarts from 'echarts'

export default({
    setup() {
        
    },
    data(){
        return {
            lineCharts: '',
            lineOpinionData: ["60", "61", "61", "62", "61", "59", "60"],
        }
    },
    methods: {
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
                        data: ["周一","周二","周三","周四","周五","周六","周日"] //x坐标的名称
					
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
            initData() {
                this.requested = true;
                var res = [{value: 200, name: 'takeIn'}, {value: 300, name: 'cost'}, {value: 100, name: 'left'}];
                var getData = [];
                for (let i = 0; i < res.length; i++) {
                var obj = new Object();
                obj.name = res[i].name;//回答调查问卷的答案
                obj.value = res[i].value;//回答调查问卷的人数
                getData[i] = obj;
                }
                // 基于准备好的dom，初始化echarts实例
                var myChart = echarts.init(document.getElementById("sectorChart"));
                // 绘制图表
                myChart.setOption({
                title: {
                    text: '调查问卷详情',
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
                    name: "选项内容",
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
            this.$nextTick(function() {
				this.drawLine('lineChart');
                setTimeout(() => {
                    this.initData();
                    }, 200);
			    })
        }

})

</script>

<template>
<div title='body'>
    <el-container>
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
    padding-top: 5%;
}
</style>