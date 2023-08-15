import puppeteer from 'puppeteer-extra'
import stealthPluguin from 'puppeteer-extra-plugin-stealth'
import { getRandomUser, getSimPhone, checkSimActivation } from '../api/index.js'
import { random_email, random_password, waitForSec } from '../static/functions.js'

puppeteer.use(stealthPluguin())

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

// 373678700

const typeInfo = (page, option, proxy) => new Promise(async (resolve, reject) => {
    try {
        let el = true
        while(el) {
        const user = await getRandomUser()

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
                },
                proxy
            }

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
    } catch (err) {
        reject(err)
    }
})

const getSimNumber = (page, use_api_phone, { country, operator, product }, option) => new Promise(async (resolve, reject) => {
    let el = true
    let id
    try {
        
        
        while(el) {
            if(use_api_phone) {
                const data = await getSimPhone({ country, operator, product })
                // const data = await checkSimActivation({ sim_id: 373678700 })
                user_infos.recovery_number = data.phone
                id = data.id
                console.log(data)
            }
            else user_infos.recovery_number = await page.evaluate(() => prompt('enter number', '+212'))

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

const getVerificationCode = (page, sim_id, use_api_phone, option) => new Promise(async (resolve, reject) => {
    let el = true

    try {
        while(el) {

            let verfication_code

            if(use_api_phone) {
                await new Promise(async function(resolve, reject) {
                    try {
                        while(!verfication_code) {
                            const data = await checkSimActivation({ sim_id })
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

const startBrowser = async (i, proxy, use_api_phone, sim_api, option, { executablePath, userDataDir }, from) => new Promise(async (resolve, reject) => {

    try {

        const browser = await puppeteer.launch({
            headless: false,
            executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
            // executablePath,
            // userDataDir: 'C:/Users/admin3/Documents/Chrome profiles/exmple-' + i.toString(),
            userDataDir : 'C:/Users/admin4/AppData/Roaming/creation_boit/profile' +(parseInt(i)+ parseInt(from)),
            defaultViewport: null,
            args: [
                '--start-maximized',
                `--proxy-server=${proxy}`
            ]
        });
    
        const pages = await browser.pages();
    
        const page = await browser.newPage();

    
        pages.forEach(p => p.close());

        await page.setDefaultTimeout(300000)
    
        // await page.goto('https://gmail.com/')
        await page.goto('https://www.google.com/gmail/about/')

        // **************************************************************************************************************

        await Promise.all([page.click('body > header > div > div > div > a:nth-child(3)'), page.waitForNavigation()])

        await typeInfo(page, option, proxy)

        await page.waitForSelector('#phoneNumberId')

        await waitForSec(1000)
        
        const sim_id = await getSimNumber(page, use_api_phone, sim_api, option)

        await page.waitForSelector('#code')

        await waitForSec(1000)

        await getVerificationCode(page, sim_id, use_api_phone, option)

        await page.waitForSelector('#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.akwVEf.OcVpRe > div.d2CFce.cDSmF.OcVpRe > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')

        await waitForSec(1000)


        // 

        await page.evaluate(() => document.querySelector('#phoneNumberId').value = '')
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
        resolve({ ...err, code: 'err' })
    }
})

export { startBrowser }