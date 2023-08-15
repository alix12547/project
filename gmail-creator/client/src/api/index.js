import axios from 'axios'

const baseURL = 'http://localhost:5050/'

const api = axios.create({
    baseURL
})

const startCreate = fields => new Promise(async (reslove, reject) => {
    try {
        const { data } = await api.post('gmail-creator/', fields)
        reslove(data)
    } catch (err) {
        reject(err)
    }
})

export { api, startCreate }