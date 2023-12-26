import axios from 'axios'

// connection to fastapi endpoint

const api = axios.create({
    baseURL: 'http://localhost:8000',
})

export default api;