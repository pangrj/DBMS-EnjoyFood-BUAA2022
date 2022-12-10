import { createRouter, createWebHistory } from "vue-router";

import ChoosePage from '../components/ChoosePage.vue'
import InfomationPage from '../components/InfomationPage.vue'
import LoginPage from '../components/LoginPage.vue'
import SignupPage from '../components/SignupPage.vue'

const routes = [
        { path: '/', redirect: '/LoginPage'},
        { path: '/ChoosePage', query:{userName:String, passWord:String} , component: ChoosePage},
        { path: '/InfomationPage', query:{userName:String, passWord:String} ,component: InfomationPage},
        { path: '/LoginPage', component: LoginPage},
        { path: '/SignupPage', component: SignupPage}
]

const router = createRouter({
        routes: routes,
        history: createWebHistory()
})

export default router