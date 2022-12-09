/*const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  pluginOptions: {
    vuetify: {
			// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
		}
  }
})
*/
amodule.exports = {
  devServer: {
      host: '127.0.0.1',
      port: 8084,
      open: true,// vue项目启动时自动打开浏览器
      proxy: {
          '/api': { // '/api'是代理标识，用于告诉node，url前面是/api的就是使用代理的
              target: "http://xxx.xxx.xx.xx:8080", //目标地址，一般是指后台服务器地址
              changeOrigin: true, //是否跨域
              pathRewrite: { // pathRewrite 的作用是把实际Request Url中的'/api'用""代替
                  '^/api': "" 
              }
          }
      }
  }
}