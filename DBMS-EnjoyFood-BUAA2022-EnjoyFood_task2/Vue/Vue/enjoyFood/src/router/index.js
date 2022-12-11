import { createRouter, createWebHistory } from "vue-router";

import ChoosePage from '../components/ChoosePage.vue'
import InfomationPage from '../components/InfomationPage.vue'
import LoginPage from '../components/LoginPage.vue'
import EditInfoPage from '../components/EditInfoPage.vue'

const routes = [
        { path: '/', redirec: '/LoginPage'},
        { path: '/ChoosePage', query:{userName:String, passWord:String} , component: ChoosePage},
        { path: '/InfomationPage', query:{userName:String, passWord:String} ,component: InfomationPage},
        { path: '/LoginPage', component: LoginPage},
        { path: '/EditInfoPage', component: EditInfoPage}
]

const router = createRouter({
        routes: routes,
        history: createWebHistory()
})

export default router