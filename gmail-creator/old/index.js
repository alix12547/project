const puppeteer = require('puppeteer-extra');
const puppeteerStealth = require('puppeteer-extra-plugin-stealth')
const axios = require('axios');
const fs = require('fs/promises');

puppeteer.use(puppeteerStealth());

const PROXY_SERVER = [
    '63.143.52.66:92',
    '96.44.151.14:92',
    '74.208.49.150:92',
    '104.129.13.138:92',
    '64.62.173.218:92',
    '216.218.222.216:92',
    '184.105.162.195:92',
    '184.105.205.190:92',
    '140.99.150.3:92',
    '45.146.186.18:92',
    '170.130.0.202:92',
    '38.96.139.79:92',
    '216.250.122.5:92',
    '74.63.222.162:92',
    '140.99.150.6:92',
    '212.193.4.3:92'
]

const USE_API_NUMPER = true

const random_user = axios.create({
    baseURL: 'https://randomuser.me/api/'
});

const get_sim = axios.create({
    baseURL: 'https://5sim.net/v1/user/',
    headers: { Authorization: `Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Nzc2MTQ1MjYsImlhdCI6MTY0NjA3ODUyNiwicmF5IjoiYTY5MjdjMjY1YmY3MjE2NmNlNjI5NmMxMDJhYTk5M2UiLCJzdWIiOjk1Nzg2N30.JzNg9T_c9ptHR4RVKd1fJx525FzK3Z35dIYGNzamlVfEjCFdmcwUbpUL-rz6cUsxYGRllXVyH56gVv_OQYORNAfchKi3EZ9thdZtbqcvTjXdBHHGhRlzDZPd-T1-IELi5xXXv3Ga_jOAYh-QWkhfiuPsYGnnuJHLrDogFCpIKp7vfeM3DM13rpxOvZS5TXTtIyWvEy7mTjWlBTnXTbvKphJ0ltOwFjxdDCQMU1R9WfJDinSdm0Zpagr_dPy6dzVmmATHpgLoYHADLpOvEejyy_7aG6y-r6YvjDuLq3NsflNR9yWfR0uHeaJxgomBAJvlNIEAoemKbT8bOhZyUuZaOA` }
});

let user_infos = {
    first_name: '',
    last_name: '',
    email: '',
    gender: '',
    password: '',
    email_recovery: '',
    recovery_number: {
        id: null,
        phone: '',
        operator: '',
        product: '',
        price: 0,
        status: '',
        expires: '',
        sms: [],
        created_at: '',
        country: ''
    },
    birthday: {
        year: '',
        month: '',
        day: ''
    }
}

const random_password = (max) => Array(max).fill("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.+-*@&#%$!?").map(x => x[Math.floor(Math.random() * x.length)] ).join('');
const random_email = (username, max) => username + Array(max).fill("0123456789abcdefghijklmnopqrstuvwxyz").map(x => x[Math.floor(Math.random() * x.length)] ).join('') + '@gmail.com';

const waitForSec = (ms) => new Promise((reslove, reject) => {
    if (typeof ms === 'number') setTimeout(() => reslove() , ms)
    else reject('not a number')
});

const startBrowser = async (i) => new Promise(async (resolve, reject) => {
    try {

        console.log(`--proxy-server=${PROXY_SERVER[i]}`)

        const option = { delay: 10 };

        const browser = await puppeteer.launch({
            headless: false,
            executablePath: 'C:/Users/admin3/AppData/Local/Blisk/Application/blisk.exe',
            // userDataDir: 'C:/Users/admin3/Documents/Chrome profiles/exmple-' + i.toString(),
            defaultViewport: null,
            args: [
                '--start-maximized',
                `--proxy-server=${PROXY_SERVER[i]}`
            ]
        });
    
        const pages = await browser.pages();
    
        const page = await browser.newPage();
    
        pages.forEach(p => p.close());

        await page.setDefaultTimeout(300000)
    
        await page.goto('https://www.google.com/gmail/about/')

        // **************************************************************************************************************

        await Promise.all([page.click('body > header > div > div > div > a:nth-child(3)'), page.waitForNavigation()])

        await new Promise(async function(resolve, reject) {
            let el = true

            while(el) {
                const { data: { results: [user] } } = await random_user.get();

                user_infos = {
                    first_name: user.name.first,
                    last_name: user.name.last,
                    email: random_email(`${user.email.replace('@example.com', '')}`, 3),
                    gender: user.gender,
                    password: random_password(14),
                    email_recovery: random_email(`${user.email.replace('@example.com', '')}`, 5),
                    recovery_number: '',
                    birthday: {
                        year: user.dob.date.split('T')[0].split('-')[0],
                        month: user.dob.date.split('T')[0].split('-')[1],
                        day: user.dob.date.split('T')[0].split('-')[2]
                    }
                }

                // const { data } = await get_sim.get(`https://5sim.net/v1/user/check/${370413127}`)

                // console.log(data)

                // await waitForSec(1000000)

                // console.log(user_infos)

                const type_input = (selector, text) => new Promise(async (resolve, reject) => {
                    try {
                        const input = await page.$(selector);
                        await input.click({ clickCount: 3 })
                        await page.type(selector, text, option)
                        resolve()
                    } catch (err) {
                        reject(err)
                    }
                })

                await type_input('#firstName', user_infos.first_name)
                await type_input('#lastName', user_infos.last_name)
                await type_input('#username', user_infos.email.replace('@gmail.com', ''))
                await type_input('#passwd > div.aCsJod.oJeWuf > div > div.Xb9hP > input', user_infos.password)
                await type_input('#confirm-passwd > div.aCsJod.oJeWuf > div > div.Xb9hP > input', user_infos.password)
                
                await page.click('#accountDetailsNext > div > button')
                await waitForSec(1000)
                el = await page.$('#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.akwVEf.OcVpRe > div.d2CFce.cDSmF.OcVpRe > div > div.LXRPh > div.dEOOab.RxsGPe > div')
            }
            resolve()
        })

        await page.waitForSelector('#phoneNumberId')

        await waitForSec(1000)
        
        const sim_id = await new Promise(async (resolve, reject) => {
            let el = true
            let id
            try {
                
                
                while(el) {
                    const { country, operator, product } = { country: 'usa', operator: 'any', product: 'google' }
    
                    if(USE_API_NUMPER) {
                        const { data } = await get_sim.get(`buy/activation/${country}/${operator}/${product}`)
                        // const { data } = await get_sim.get(`https://5sim.net/v1/user/check/${372940521}`)
                        user_infos.recovery_number = data.phone
                        id = data.id

                        console.log(data)
                    }
    
                    
                    else user_infos.recovery_number = await page.evaluate(() => prompt('enter number', '+212'))
    
                    // const { recovery_number } = await get_sim.get(`https://5sim.net/v1/user/check/${370413127}`)
    
                    await waitForSec(1000)
                    await page.waitForSelector('#phoneNumberId')
                    const input = await page.$('#phoneNumberId')
                    await input.click({ clickCount: 3 })
                    await page.type('input#phoneNumberId', user_infos.recovery_number, option)
                    await page.click('#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button')
    
                    await waitForSec(1000)
                    el = await page.$('#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.bAnubd.OcVpRe.Jj6Lae > div.VsO7Kb > div.gFxJE > div.jPtpFe > div')
                    if(el) console.log('yes', el) 
                    else console.log('not')
                }
    
                resolve(id)
            } catch (err) {
                reject(err)
            }
        })


        await page.waitForSelector('#code')

        await waitForSec(1000)

        await new Promise(async (resolve, reject) => {
            let el = true

            try {
                while(el) {

                    let verfication_code
    
                    if(USE_API_NUMPER) {
                        await new Promise(async function(resolve, reject) {
                            try {
                                while(!verfication_code) {
                                    const { data } = await get_sim.get(`https://5sim.net/v1/user/check/${sim_id}`)
                                    console.log(data.sms)
                                    if(data?.sms && data?.sms?.length !== 0){
                                        verfication_code = data?.sms[0]?.code
                                        console.log(data.sms[0])
                                    }
                                    await waitForSec(1000)
                                }
                                resolve()
                            } catch (err) {
                                reject(err)
                            }
                        })
                    }
    
                    else verfication_code = await page.evaluate(() => prompt('Verification code'))
    
                    
                    // const verfication_code = user_infos?.recovery_number?.sms[0]?.code
    
                    await waitForSec(1000)
                    await page.waitForSelector('#code')
                    const input = await page.$('#code');
                    await input.click({ clickCount: 3 })
                    console.log('1', verfication_code)
                    await page.type('#code', verfication_code, option)
                    await page.click('#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button')
                    await waitForSec(1000)
                    el = await page.$('#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.d2CFce.cDSmF.OcVpRe.PkCcVd > div > div.LXRPh > div.dEOOab.RxsGPe > div')
                    if(el) console.log('yes') 
                    else console.log('not')
                }
    
                resolve()
            } catch (err) {
                reject()
            }
        })

        await page.waitForSelector('#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.akwVEf.OcVpRe > div.d2CFce.cDSmF.OcVpRe > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')

        await waitForSec(1000)

        await page.type('#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.akwVEf.OcVpRe > div.d2CFce.cDSmF.OcVpRe > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input', user_infos.email_recovery, option)

        await page.select('#month', parseInt(user_infos.birthday.month).toString())
        await page.type('#day', user_infos.birthday.day, option)
        await page.type('#year', user_infos.birthday.year, option)

        await page.select('#gender', user_infos.gender === 'male' ? '1' : '2')
    
        await page.click('#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button')

        await waitForSec((2000))
        // await page.waitForSelector('button[type="button"]#learnMore')
        // await page.waitForSelector('button[type="button"]#moreOptions')
        await page.click('#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div.dG5hZc > div.qhFLie > div > div > button')

        await waitForSec((2000))
        // await page.waitForSelector('a[data-link="privacy"][href="https://policies.google.com/terms?hl=en&gl=US"]')
        // await page.waitForSelector('a[data-link="privacy"][href="https://policies.google.com/privacy?hl=en&gl=US"]')
        await page.click('#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button')

        await page.waitForNavigation()

        // await browser.close()
        
        resolve(user_infos)

    } catch (err) {
        console.log(err)
        reject(err)
    }
})

const start = async () => {
    try {
        for(i = 0;i < 1;i++) {
            const user_infos = await startBrowser(i);
            console.log(i)

            try {
                const dataFile = await fs.readFile('users.json')
                console.log(typeof dataFile)
                const jsonFile = JSON.parse(dataFile.toString())
                await fs.writeFile('users.json', JSON.stringify([ ...jsonFile, user_infos ]))
            } catch (err) {
                console.log(err)
                await fs.writeFile('users.json', JSON.stringify([ user_infos ]))
            }
        }
    } catch (err) {
        console.log(err)
    }
    
}

start()