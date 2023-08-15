import Navbar from '../components/navbar'
import Sidebar from '../components/sidebar'

const Home = () => (
    <>
        <Navbar />
        <div className="content-wrapper d-flex flex-row">
            <Sidebar />
            <h3>ADMIN</h3>
        </div>
    </>
)

export default Home