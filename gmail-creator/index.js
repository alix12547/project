import express from "express"
import cors from 'cors'
import { home, gmail_creator } from './router/index.js'

const app = express()

app.use(express.json({ limit: '30mb', extended: true }))
app.use(express.urlencoded({ limit: '30mb', extended: true }))
app.use(cors())

app.use('/', home)
app.use('/gmail-creator/', gmail_creator)

const PORT = process.env.PORT || '5050'

app.listen(PORT, () => console.log(`app start at http://localhost:${PORT}/`))