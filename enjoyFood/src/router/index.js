import { createRouter, createWebHistory } from "vue-router";

import ChoosePage from '../components/ChoosePage.vue'
import InfomationPage from '../components/InfomationPage.vue'
import LoginPage from '../components/LoginPage.vue'
import SignupPage from '../components/SignupPage.vue'
import MainPage from '../components/MainPage.vue'
import PlanPage from '../components/PlanPage.vue'

const routes = [
        { path: '/', redirect: '/LoginPage'},
        { path: '/ChoosePage', query:{userName:String} , component: ChoosePage},
        { path: '/InfomationPage', query:{userName:String} ,component: InfomationPage},
        { path: '/MainPage', query:{userName:String} ,component: MainPage},
        { path: '/LoginPage', component: LoginPage},
        { path: '/SignupPage', component: SignupPage},
        { path: '/PlanPage', query:{planId:String} , component: PlanPage}
]

const router = createRouter({
        routes: routes,
        history: createWebHistory()
})

export default router