import { createApp, VueElement } from 'vue'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import router from './router'
import axios from 'axios'
import store from './store'

import App from './App.vue'

const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
  }  

app.config.globalProperties.$https = axios

app.use(ElementPlus)
app.use(router)
app.use(store)
app.mount('#app')

// axios.defaults.baseURL = 'http://0.0.0.0:8000';