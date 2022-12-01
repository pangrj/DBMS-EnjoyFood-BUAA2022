import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})

/*const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDepencies: true,
  devServer:{
    port: 8080,
    proxy:{
      '/api':{
        target: 'http://156.61.146.85:8078',
        pathRewrite:{ '^/api': ''},
        ws: true,
        changeOrigin: true
      },
    }
  }
})*/
