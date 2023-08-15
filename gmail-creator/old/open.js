const puppeteer = require('puppeteer-extra');
const fs = require('fs/promises');

// puppeteer.use(puppeteerStealth);

const PROXY_SERVER = '134.73.164.189:92'

const waitForSec = (ms) => new Promise((reslove, reject) => {
    if (typeof ms === 'number') setTimeout(() => reslove() , ms)
    else reject('not a number')
});

const startBrowser = async (i) => new Promise(async (resolve, reject) => {
    try {

        const option = { delay: 10 };

        const browser = await puppeteer.launch({
            headless: false,
            // executablePath: 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe',
            userDataDir: 'C:/Users/admin3/Documents/Chrome profiles/exmple-' + i.toString(),
            defaultViewport: null,
            args: [
                '--start-maximized',
                `--proxy-server=${PROXY_SERVER}`
            ]
        });
    
        const pages = await browser.pages();
    
        const page = await browser.newPage();

        // pages.forEach(p => p.close());
    
        // await page.goto('https://gmail.com//')
        await page.goto('https://gmail.com/')

        await waitForSec(2000)

        // await page.click('table > tbody:nth-child(2) > tr')

        // await waitForSec(100000)

        await page.click('body > div:nth-child(20) > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(5) > div > div > div > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div')

        // await page.waitForNavigation()

        await waitForSec(500000);
    
        await page.close();

        const dataFile = await fs.readFile('users.json');
        const jsonFile = JSON.parse(dataFile.toString());

        console.log(jsonFile);

        // await fs.writeFile('users.json', JSON.stringify([ ...jsonFile, user_infos ]));

        resolve('created : ', 'user_infos')

    } catch (err) {
        console.log(err)
        reject(err)
    }
})




const start = async () => {
    for(i = 0;i < 1;i++) {
        await startBrowser(i);
        console.log(i)
    }
}

start()