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
      },
      {
        d_id: '3',
        d_name: '4eg',
        d_category: '11',
        d_cuisine: '1',
        d_calories: '1',
        d_price: '1',
      },
      {
        d_id: '3',
        d_name: 'afd',
        d_category: '11',
        d_cuisine: '1',
        d_calories: '1',
        d_price: '1',
      },
      {
        d_id: '3',
        d_name: 'sd',
        d_category: '11',
        d_cuisine: '1',
        d_calories: '1',
        d_price: '1',
      },
      {
        d_id: '3',
        d_name: 'xxx',
        d_category: '11',
        d_cuisine: '1',
        d_calories: '1',
        d_price: '1',
      }
    ],
    chosenFood:[],
    SportList: [
      {
        sp_id: '1',
        sp_name: '篮球',
        sp_content: 'xxx',
        sp_difficulty: 'y',
        sp_calories: 'z',
        sp_time: 'a',
      },
      {
        sp_id: '2',
        sp_name: '5555',
        sp_content: 'xxx',
        sp_difficulty: 'y',
        sp_calories: 'z',
        sp_time: 'a',
      },
      {
        sp_id: '3',
        sp_name: '3',
        sp_content: 'xxx',
        sp_difficulty: 'y',
        sp_calories: 'z',
        sp_time: 'a',
      },
      {
        sp_id: '4',
        sp_name: '4',
        sp_content: 'xxx',
        sp_difficulty: 'y',
        sp_calories: 'z',
        sp_time: 'a',
      },
      {
        sp_id: '5',
        sp_name: '5',
        sp_content: 'xxx',
        sp_difficulty: 'y',
        sp_calories: 'z',
        sp_time: 'a',
      },
      {
        sp_id: '6',
        sp_name: '6',
        sp_content: 'xxx',
        sp_difficulty: 'y',
        sp_calories: 'z',
        sp_time: 'a',
      },
      {
        sp_id: '7',
        sp_name: '7',
        sp_content: 'xxx',
        sp_difficulty: 'y',
        sp_calories: 'z',
        sp_time: 'a',
      },
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
    getFoodList(state, food){
      console.log(food)
      state.foodList = food;
    },
    getSportList(state, sport){
      console.log(sport)
      state.sportList = sport;
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
    }
  },
  actions: {
    asyncgetFoodList({commit}) {
        axios.get("http://iwenwiki.com/api/generator/list.php")
        .then(res => {
            commit.getFoodList(res.data)
        })
    },
    asyncgetSportList({commit}) {
        axios.get("http://iwenwiki.com/api/generator/list.php")
        .then(res => {
            commit.getSportList(res.data)
        })
    },
  },
  modules: {
  }
})
