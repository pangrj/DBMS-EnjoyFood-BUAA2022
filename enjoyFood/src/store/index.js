import { createStore } from 'vuex'

export default createStore({
  state: {
    foodList: [
      {
        d_id: '1',
        d_name: '麻婆豆腐',
        d_category: 'xxx',
        d_cuisine: 'y',
        d_calories: 'z',
        d_price: 'a',
      },
      {
        d_id: '2',
        d_name: '宫爆鸡丁',
        d_category: '11',
        d_cuisine: '1',
        d_calories: '1',
        d_price: '1',
      },
      {
        d_id: '3',
        d_name: '蒸蛋',
        d_category: '11',
        d_cuisine: '1',
        d_calories: '1',
        d_price: '1',
      }
    ],
    chosenFood:[],
    SportList: [
      {
        d_id: '1',
        d_name: '篮球',
        d_category: 'xxx',
        d_cuisine: 'y',
        d_calories: 'z',
        d_price: 'a',
      },
      {
        d_id: '2',
        d_name: '游泳',
        d_category: '11',
        d_cuisine: '1',
        d_calories: '1',
        d_price: '1',
      },
      {
        d_id: '3',
        d_name: '跑步',
        d_category: '11',
        d_cuisine: '1',
        d_calories: '1',
        d_price: '1',
      }
    ],
    chosenSport:[],
  },
  getters: {
    getFoodList(state) {
			return state.foodList;
		},
    getChosenFood(state) {
      return state.chosenFood;
    },
    getSportList(state) {
			return state.SportList;
		},
    getChosenSport(state) {
      return state.chosenSport;
    }
  },
  mutations: {
    chooseFood(state, food) {
      console.log(food)
      state.chosenFood.push(food);
      console.log(state.chosenFood)
    },
    chooseSport(state, sport) {
      console.log(sport)
      state.chosenSport.push(sport);
      console.log(state.chosenSport)
    },
  },
  actions: {
  },
  modules: {
  }
})
