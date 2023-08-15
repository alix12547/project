import  { Router } from 'express'
import { helloWorld } from '../controller/HomeController.js'

const router = Router()

router.get('', helloWorld)

export default router