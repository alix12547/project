import { startBrowser } from '../puppeteer/gmail-creator.js'
import { saveToFile } from '../static/functions.js'

const info = (_, res) => res.send('Gmail Creator')

const start = async (req, res) => {
    const data = []
    const { proxy_list, use_api_phone, sim_api, type_option, browserOptions, from } = req.body
    if(!proxy_list || !type_option) return res.status(400).send('params err')
    if(!proxy_list.length) return res.status(400).send('proxys err')
    res.send('started')
    try {
        for(let index in proxy_list) {
            const user_infos = await startBrowser(index, proxy_list[index], use_api_phone, sim_api, type_option, browserOptions, from)
            if(user_infos?.code !== 'err') {
                await saveToFile('users.json', user_infos)
                data.push(user_infos)
            }
        }
    } catch (err) {
        console.log(err)
    }
}

export { info, start }