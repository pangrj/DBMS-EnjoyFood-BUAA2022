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
    getChosenFoodId(state) {
      var ids = []
      for(var p in state.chosenFood) {
        ids.push(state.chosenFood[p].d_id)
      }
      console.log("所有d_id：")
      console.log(ids)
      return ids
    },
    getSportList(state) {
			return state.sportList;
		},
    getChosenSport(state) {
      return state.chosenSport;
    },
    getChosenSportId(state) {
      var ids = []
      for(var p in state.chosenSport) {
        ids.push(state.chosenSport[p].sp_id)
      }
      console.log("所有sp_id：")
      console.log(ids)
      return ids
    },
    getLifeCircle(state) {
      return state.lifeCircle;
    },
    //计算总选中的热量
    totalCaloryIn(state) {
      var total = 0;
      for(var p in state.chosenFood) {
        total += state.chosenFood[p].d_calories;
      }
      return total;
    },
    totalCaloryOut(state) {
      var total = 0;
      for(var p in state.chosenSport) {
        total += state.chosenSport[p].sp_calories;
      }
      return total;
    },
  },
  mutations: {
    initFoodList(state, food){
      //console.log(food)
      var foodContent = []
      var dishes = food.dishes
      var fields = {}
      for(var p in dishes) {
        fields = dishes[p].fields
        fields["d_id"] = dishes[p].pk
        //console.log(fields)
        foodContent.push(fields)
      }
      console.log(foodContent)
      state.foodList = foodContent;
    },
    initSportList(state, sport){
      var sportContent = []
      var sports = sport.sports
      var fields = {}
      for(var p in sports) {
        fields = sports[p].fields
        fields["sp_id"] = sports[p].pk
        //console.log(fields)
        sportContent.push(fields)
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
