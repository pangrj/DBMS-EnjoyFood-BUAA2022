import { createStore } from 'vuex'

export default createStore({
  state: {
    foodList: [],
    chosenFood:[],
    sportList: [],
    chosenSport:[],
    lifeCircle: 1,
  },
  getters: {
    getFoodList(state) {
			return state.foodList;
		},
    getChosenFood(state) {
      return state.chosenFood;
    },
    getSportList(state) {
			return state.sportList;
		},
    getChosenSport(state) {
      return state.chosenSport;
    },
    getLifeCircle(state) {
      return state.lifeCircle;
    }
  },
  mutations: {
    initFoodList(state, food){
      var foodContent = []
      var dishes = food.dishes
      for(var p in dishes) {
        foodContent.push(dishes[p].fields)
      }
      console.log(foodContent)
      state.foodList = foodContent;
    },
    initSportList(state, sport){
      var sportContent = []
      var sports = sport.sports
      for(var p in sports) {
        sportContent.push(sports[p].fields)
      }
      console.log(sportContent)
      state.sportList = sportContent;
    },
    chooseFood(state, food) { //传入一个list，表示一个food的所有信息
      console.log(food)
      state.chosenFood.push(food);
      console.log(state.chosenFood)
    },
    chooseSport(state, sport) {
      console.log(sport)
      state.chosenSport.push(sport);
      console.log(state.chosenSport)
    },
    deleteFood(state, food) {
      console.log(food)
      state.chosenFood.splice(state.chosenFood.indexOf(food), 1);
      console.log(state.chosenFood)
    },
    deleteSport(state, sport) {
      console.log(sport)
      state.chosenSport.splice(state.chosenSport.indexOf(sport), 1);
      console.log(state.chosenSport)
    },
    changeLifeCircle(state, circle) {
      state.lifeCircle = circle;
    }
  },
  actions: {
    // asyncinitFoodList({commit}) {
    //     axios.get("http://iwenwiki.com/api/generator/list.php")
    //     .then(res => {
    //         commit.getFoodList(res.data)
    //     })
    // },
    // asyncinitSportList({commit}) {
    //     axios.get("http://iwenwiki.com/api/generator/list.php")
    //     .then(res => {
    //         commit.getSportList(res.data)
    //     })
    // },
  },
  modules: {
  }
})
