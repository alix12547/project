import puppeteer from 'puppeteer-extra'
import StealthPlugin from 'puppeteer-extra-plugin-stealth'
import fs from 'fs/promises'

puppeteer.use(StealthPlugin())

const PROXY_SERVER = [
   '104.206.148.10:92',
   '170.130.0.204:92',
   '216.66.95.204:92',
   '216.66.81.98:92',
   '173.44.60.133:92',
   '45.146.186.21:92',
   '170.130.0.206:92',
   '184.171.250.164:92',
   '173.44.60.135:92',
   '199.168.189.66:92',
   '199.168.189.67:92',
   '199.168.189.68:92',
   '199.168.189.69:92',
   '45.146.186.19:92',
   '45.146.186.22:92',
   '108.175.11.29:92',
   '198.71.49.244:92',
   '62.151.178.249:92',
   '74.208.207.32:92',
   '216.218.141.12:92',
   '216.218.132.240:92',
   '216.218.141.11:92',
   '74.208.116.41:92',
   '66.160.199.145:92',
   '198.251.74.112:92',
   '66.175.234.95:92',
   '70.35.203.169:92',
   '74.208.175.143:92',
   '72.11.135.173:92',
   '96.44.151.12:92',
   '74.82.17.121:92',
   '74.208.233.226:92',
   '66.175.233.53:92',
   '140.99.88.107:92',
   '66.175.234.217:92',
   '72.11.135.171:92',
   '216.218.222.162:92',
   '72.11.135.172:92',
   '70.35.196.212:92',
   '216.218.132.237:92',
   '69.197.157.62:92',
   '140.99.88.106:92',
   '72.11.135.170:92',
   '216.218.222.163:92',
   '69.197.157.59:92',
   '74.82.17.120:92',
   '96.44.151.13:92',
   '172.245.57.244:92',
   '140.99.88.108:92',
   '172.245.57.240:92',
   '216.218.141.4:92',
   '69.197.157.58:92',
   '172.245.57.241:92',
   '72.11.135.174:92',
   '216.218.132.238:92',
   '63.143.52.66:92',
   '63.143.52.67:92',
   '63.143.52.68:92',
   '63.143.52.69:92',
   '63.143.52.70:92',
   '96.44.151.10:92',
   '172.245.57.243:92',
   '74.208.55.139:92',
   '69.197.157.61:92',
   '216.218.141.2:92',
   '216.218.141.3:92',
   '74.208.55.143:92',
   '62.151.179.83:92',
   '74.82.17.118:92',
   '140.99.88.109:92',
   '216.218.132.241:92',
   '74.208.216.225:92',
   '216.218.132.239:92',
   '216.218.222.164:92',
   '104.219.41.58:92',
]

let users = []

const option = { delay: 100 }

const waitForSec = (ms) => new Promise((reslove, reject) => {
   if (typeof ms === 'number') setTimeout(() => reslove() , ms)
   else reject('not a number')
})

const startBrowser = async (i) => new Promise(async (resolve, rejects) => {
   try {
      const browser = await puppeteer.launch({
         headless: false,
         // executablePath: 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe',
         userDataDir: 'C:/Users/admin3/Documents/Chrome profiles/exmple-' + i.toString(),
         defaultViewport: null,
         args: [
             '--start-maximized',
             `--proxy-server=${PROXY_SERVER[i]}`,
             '--no-sandbox',
             '--disable-setuid-sandbox'
         ]
     }); 
     const loginUrl = 'https://gmail.com/'
   
      // const loginUrl = "https://accounts.google.com/v3/signin/identifier?dsh=S520524147%3A1666205958046111&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWp4bo0NOfOA5aPvSZUjmRryaU5iWWRZK-Lu1LeGu0gpb7sj6ppj2JuAAFYp-Fo69b7a6i0e";
      const ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36'; 
      const pages = await browser.pages()
      const page = await browser.newPage()
      pages.forEach(p => p.close())

   
      await page.setUserAgent(ua)
      await page.goto(loginUrl, { waitUntil: 'networkidle2' })
      const login_url = await page.$('body > header.header:nth-child(2) > div.header__container > div.header__aside:nth-child(2) > div.header__aside__buttons > a.button.button--medium.button--mobile-before-hero-only:nth-child(2)')
      console
      if(true) {
         // await page.click('body > header.header:nth-child(2) > div.header__container > div.header__aside:nth-child(2) > div.header__aside__buttons > a.button.button--medium.button--mobile-before-hero-only:nth-child(2)')
         await waitForSec(2000)
         const btn_login = await page.$('input[type="email"][name="identifier"]')
         if(true) {
            await page.type('input[type="email"][name="identifier"]', users[i].email)
            await page.keyboard.press('Enter')
            await waitForSec(2000)
            // await page.waitForSelector('input[type="password"]')
            await page.waitForSelector('input[type="password"]')
            await page.type('input[type="password"]', users[i].password)
            await page.keyboard.press('Enter')
         }
      }

      // await page.keyboard.press('Enter')
      // await page.waitForTimeout(2000)
      // await page.type('input[type="password"]', users[i].password)
      // await page.keyboard.press('Enter')
      // await page.waitforNavigation()

      const messages_count = await page.$$eval('table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > div > div > div:nth-child(1) > span > span', els => els.length)

      if(messages_count) {
         await page.waitForSelector('[role="checkbox"]')
         await page.click('[role="checkbox"]')
         await page.waitForSelector('[aria-label="Delete"][data-tooltip="Delete"][role="button"]')
         await page.click('[aria-label="Delete"][data-tooltip="Delete"][role="button"]')
      }

      
      
      const instaPage = await browser.newPage()
      
      await instaPage.goto('https://www.instagram.com/accounts/emailsignup/')
      
      await instaPage.waitForSelector('input[Name ="emailOrPhone"]')
      
      await instaPage.type('input[Name ="emailOrPhone"]', users[i].email, option)
      await instaPage.type('input[Name ="fullName"]', `${users[i].first_name} ${users[i].last_name}`, option)
      await instaPage.type('input[Name ="username"]', users[i].email.replace('@gmail.com', ''), option)
      await instaPage.type('input[Name ="password"]', 'Emh12345678', option)
      
      await waitForSec(2000)
      await instaPage.click('button[Type="submit"]')
      
      await instaPage.waitForSelector('select[Title="Day:"]')
      
      await instaPage.select('select[Title="Day:"]', users[i].birthday.day)
      await instaPage.select('select[Title="Month:"]', users[i].birthday.month)
      await instaPage.select('select[Title="Year:"]', users[i].birthday.year)
      
      // await waitForSec(2000)

      await instaPage.waitForSelector('button._acan._acap._acaq._acas')
      await instaPage.click('button._acan._acap._acaq._acas')
      
      await instaPage.waitForSelector('input[Name ="email_confirmation_code"]')
      
      await waitForSec(2000)
      
      await page.reload()
      await page.waitForSelector('table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > div > div > div:nth-child(1) > span > span')
      const messageTitle = await page.$eval('table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > div > div > div:nth-child(1) > span > span', el => el.innerText)
      console.log(messageTitle)
      
      await instaPage.type('input[Name ="email_confirmation_code"]', messageTitle.split(' ')[0], option)
      
      await waitForSec(2000)
      await instaPage.click('button[Type="submit"]')
      
      
      /*
      //////////////////////////
      
      const fbPage = await browser.newPage()
      
      await fbPage.goto('https://www.facebook.com/')

      await fbPage.click('a[data-testid="open-registration-form-button"]')

      await fbPage.waitForSelector('input[name="firstname"]')

      await fbPage.type('input[name="firstname"]', users[i].first_name, option)
      await fbPage.type('input[name="lastname"]', users[i].last_name, option)
      await fbPage.type('input[name="reg_email__"]', users[i].email, option)
      await fbPage.waitForSelector('input[name="reg_email_confirmation__"]')
      await fbPage.type('input[name="reg_email_confirmation__"]', users[i].email, option)
      await fbPage.type('input[name="reg_passwd__"]', 'Emh12345678@', option)

      await fbPage.select('select[name="birthday_day"]', users[i].birthday.day)
      await fbPage.select('select[name="birthday_month"]', users[i].birthday.month)
      await fbPage.select('select[name="birthday_year"]', users[i].birthday.year)

      await fbPage.click(`input[type="radio"][name="sex"][value="${users[i].gender === 'femal' ? 1 : users[i].gender === 'male' ? 2 : -1}"]`)

      await fbPage.click('button[name="websubmit"]')

      // 'input[maxlength="5"]'
      // #scrollview > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x1t2pt76.x193iq5w.xl56j7k.x78zum5.x1qjc9v5 > div > div > div.xh8yej3.x14lw9ws > div > div > div > div > div > div > div > div:nth-child(3) > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xeuugli.x150jy0e.x1e558r4.x10b6aqq.x1yrsyyn > span > div
      // 'div:nth-child(2) > [aria-label="Next"]'



      const twitterPage = await browser.newPage()

      await twitterPage.goto('https://twitter.com/i/flow/signup/')

      await twitterPage.waitForSelector(('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu'))
      await twitterPage.click('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu')

      await twitterPage.waitForSelector('input[Name ="name"]')

      await twitterPage.type('input[Name ="name"]', `${users[i].first_name} ${users[i].last_name}`, option)
      await twitterPage.click('[role="button"]:nth-child(3)')
      await twitterPage.waitForSelector('input[name ="email"]')
      await twitterPage.type('input[name ="email"]', users[i].email, option)

      
      
      // await twitterPage.type('input[Name ="username"]', users[i].email.replace('@gmail.com', ''), option)
      // await twitterPage.type('input[Name ="password"]', 'Emh12345678', option)

      
      await twitterPage.select('select#SELECTOR_1', users[i].birthday.month)
      await twitterPage.select('select#SELECTOR_2', users[i].birthday.day)
      await twitterPage.select('select#SELECTOR_3', users[i].birthday.year)

      const btn_selector = '#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div'
      
      await twitterPage.click(btn_selector)
      await waitForSec(1000)
      await twitterPage.click(btn_selector)
      await waitForSec(1000)
      await twitterPage.click(btn_selector)
      await waitForSec(1000)
      await twitterPage.click(btn_selector)
      await waitForSec(1000)

      // await page.waitForSelector('button#home_children_button')
      // await page.click('button#home_children_button')

      await twitterPage.waitForSelector('input[name="verfication_code"]', { timeout: 300000 })

      await waitForSec(2000)

      await page.reload()
      await page.waitForSelector('table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > div > div > div:nth-child(1) > span > span')
      const messageTitle = await page.$eval('table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > div > div > div:nth-child(1) > span > span', el => el.innerText)
      console.log(messageTitle)


      await twitterPage.type('input[name="verfication_code"]', messageTitle.split(' ')[0], option)
      await waitForSec(1000)

      await twitterPage.click('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div')

      await twitterPage.waitForSelector('input[name="password"]')
      await twitterPage.type('input[name="password"]', 'Emh123465678', option)

      await waitForSec(1000)
      await twitterPage.click('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div')

      await waitForSec(1000)
      await twitterPage.waitForSelector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div')
      await twitterPage.click('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div')

      */


      

      await waitForSec(2000)

      
      // browser.close()
      resolve()
   } catch (err) {
      resolve()
      console.log(err)
   }
})

const start = async () => {

   const dataFile = await fs.readFile('users.json')
   users = await JSON.parse(dataFile.toString())

   for(let i = 5;i < 7;i++) {
      await startBrowser(i);
   }
   
}

start()
