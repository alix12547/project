const imaps = require('imap-simple');
const fs = require('fs/promises')

const readMail = async (EMAIL, PASSWORD) => new Promise(async (resolve, reject) => {

  const READ_MAIL_CONFIG = {
      imap: {
          user: EMAIL,
          password: PASSWORD,
          host: 'imap.gmail.com',
          port: 993,
          authTimeout: 10000,
          tls: true,
          tlsOptions: { rejectUnauthorized: false },
        },
  }

  try {
    const connection = await imaps.connect(READ_MAIL_CONFIG)
    const boxs = await connection.getBoxes()
    console.log('CONNECTION SUCCESSFUL', new Date().toString(), boxs)
    const box = await connection.openBox('INBOX')
    const searchCriteria = ['ALL']
    const fetchOptions = {
      bodies: ['HEADER'],
      markSeen: false
    };
    const results = await connection.search(searchCriteria, fetchOptions)

    //  Open a mailbox, and look at the 50 newest messages
    await connection.openBox('INBOX').then(() => connection.search(['ALL'], { bodies: ['HEADER'], markSeen: false }).then(async messages => {
      const uidsToDelete = messages.map(message => message.attributes.uid)
      await fs.writeFile('uidsToDelete1.json', JSON.stringify(uidsToDelete))
    if(uidsToDelete.length > 0) await connection.deleteMessage(uidsToDelete)
    }))
    await connection.openBox('[Gmail]/Spam').then(() => connection.search(['ALL'], { bodies: ['HEADER'], markSeen: false }).then(async messages => {
      const uidsToDelete = messages.map(message => message.attributes.uid)
      await fs.writeFile('uidsToDelete3.json', JSON.stringify(uidsToDelete))
    if(uidsToDelete.length > 0) await connection.deleteMessage(uidsToDelete)
    }))
    await connection.openBox('[Gmail]/Trash').then(() => connection.search(['ALL'], { bodies: ['HEADER'], markSeen: false }).then(async messages => {
      const uidsToDelete = messages.map(message => message.attributes.uid)
      await fs.writeFile('uidsToDelete4.json', JSON.stringify(uidsToDelete))
    if(uidsToDelete.length > 0) await connection.deleteMessage(uidsToDelete)
    }))    

    await connection.end()
    resolve(results.map(msg => ({ status: msg.parts[0].body['received-spf'][0].split(' ')[0], ip:  /client-ip=[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/.exec(msg.parts[0].body['received-spf'][0])[0].replace('client-ip=', '')})))
  } catch (error) {
    reject(error)
  }
})

const extract = async list_email => {
  try {
    for(auth of list_email.split('\n')) {
      const results = await readMail(auth.split(':')[0], auth.split(':')[1])
      await fs.writeFile('email_results.json', JSON.stringify(results))
      console.log('successful')
    }
  } catch (err) {
    console.error(err)
  }
  
}

extract('masha.sijtsemam1t@gmail.com:cpekixewisnqyxbp')



// client-ip=198.2.140.131

// pass