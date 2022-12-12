<script>
import * as echarts from 'echarts'

export default({
    setup() {
        
    },
    data(){
        return {
            charts: '',
            opinionData: ["60", "61", "61", "62", "61", "59", "60"]
        }
    },
    methods: {
        drawLine(id) {
				this.charts = echarts.init(document.getElementById(id))
				this.charts.setOption({
                    title:{
                        left:'3%',
                        top:'5%',
                        text:"weight flows",//标题文本，支持使用 \n 换行。
                    },
					tooltip: {
						trigger: 'axis'
					},
					legend: {
                        align:'right',//文字在前图标在后
                        left:'3%',
                        top:'15%',
						data: ['week']
					},
					grid: {
                        top:'30%',
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
						data: this.opinionData
					}]
				})
			}
		},
        mounted(){
            this.$nextTick(function() {
				this.drawLine('main')
			})
        }

})

</script>

<template>
    <div>
        <div id="main" style="width: 100%;height: 520px;background:#fff"></div>
    </div>
</template>

<style scoped>
.main{
    padding-top: 5%;
    size: 50%;
}
</style>