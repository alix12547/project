import { createBrowserRouter } from 'react-router-dom'
import App from './App'
import HomePage from './routes/Home'
import AdminPage from './routes/Admin'
import GmailCreator from './routes/gmail-creator'

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                path: "",
                element: <HomePage />,
                children: [
                    {
                        path: "gmail-creator",
                        element: <GmailCreator />,
                    },
                ],
            },
            {
                path: "admin",
                element: <AdminPage />,
            },              
        ]
    },
    {
        path: 'login',
        element: <h1>login</h1>,
    },
])

export default router