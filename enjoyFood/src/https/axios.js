import axios from 'axios'

const request = axios.create({
    //baseURL: 'http://localhost:8000',
    baseURL: 'http://59.110.212.35:8000',
    timeout: 5000
})

export default request