<script>
import LoginPage from './components/LoginPage.vue'
import ChoosePage from './components/ChoosePage.vue'
import InfomationPage from './components/InfomationPage.vue'
import EditInfoPage from './components/EditInfoPage.vue'

export default {
  name: 'app',
  components: { 
    LoginPage,
    ChoosePage,
    InfomationPage, 
    EditInfoPage,
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