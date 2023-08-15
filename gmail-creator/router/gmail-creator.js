import  { Router } from 'express'
import { info, start } from '../controller/GmailCreatorController.js'

const router = Router()

router.get('', info)
router.post('', start)

export default router