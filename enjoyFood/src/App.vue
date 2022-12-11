<script>
import LoginPage from './components/LoginPage.vue'
import ChoosePage from './components/ChoosePage.vue'
import InfomationPage from './components/InfomationPage.vue'
import SignupPage from './components/SignupPage.vue'
import MainPage from './components/MainPage.vue'

export default {
  name: 'app',
  components: { 
    LoginPage,
    ChoosePage,
    InfomationPage, 
    SignupPage,
    MainPage,
  },
  data () {
    return {
      msg: '测试msg'
    }
  }
}
</script>

<template>
  <div>
    <div>
    </div>
    <router-view></router-view>
  </div>
</template>
 
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
 
h1, h2 {
  font-weight: normal;
  text-align: center;
}
 
ul {
  list-style-type: none;
  padding: 0;
}
 
li {
  display: inline-block;
  margin: 0 10px;
}
 
a {
  color: #42b983;
}
</style>