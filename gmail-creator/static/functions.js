import fs from 'fs/promises'

const random_password = (max) => Array(max).fill("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.+-*@&#%$!?").map(x => x[Math.floor(Math.random() * x.length)] ).join('');
const random_email = (username, max) => username + Array(max).fill("0123456789abcdefghijklmnopqrstuvwxyz").map(x => x[Math.floor(Math.random() * x.length)] ).join('') + '@gmail.com';

const waitForSec = (ms) => new Promise((reslove, reject) => {
    if (typeof ms === 'number') setTimeout(() => reslove() , ms)
    else reject('not a number')
})

const saveToFile = (fileName, user_infos) => new Promise(async (resolve, reject) => {
    if(!fileName) return reject('file name is required !')
    try {
            const dataFile = await fs.readFile(fileName)
            const jsonFile = JSON.parse(dataFile.toString())
            await fs.writeFile(fileName, JSON.stringify([ ...jsonFile, user_infos ]))
        } catch (err) {
            console.log(err)
            await fs.writeFile(fileName, JSON.stringify([ user_infos ]))
        }   
})

export { random_email, random_password, waitForSec, saveToFile }