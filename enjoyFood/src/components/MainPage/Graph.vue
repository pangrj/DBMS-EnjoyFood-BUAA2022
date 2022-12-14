<script>
import * as echarts from 'echarts'

export default {
  name: "",
  data() {
    return {
    };
  },
  created() {
    setTimeout(() => {
          this.initData();
        }, 200);
    //this.initData();
  },
  methods: {
    //初始化饼状图数据
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
          var myChart = echarts.init(document.getElementById("main"));
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
}
</script>

<template>
<div>
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

</style>