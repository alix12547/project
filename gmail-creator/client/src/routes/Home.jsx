import { Outlet } from 'react-router-dom'
import Navbar from '../components/navbar'
import Sidebar from '../components/sidebar'

const Home = () => (
    <>
        <Navbar />
        <div className="content-wrapper d-flex flex-row">
            <Sidebar />
            <Outlet />
        </div>
    </>
)

export default Home