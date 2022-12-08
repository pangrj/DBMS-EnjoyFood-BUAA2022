import axios from './axios'

export const alldata=(data)=>{
    return axios({
        url: '',
        method: 'post',
        //data: data,
    })
}

export default {alldata}