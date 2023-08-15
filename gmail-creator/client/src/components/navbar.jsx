import { NavLink, Link } from 'react-router-dom'

const Navbar = () => (
        <nav className="navbar navbar-expand-lg bg-light p-2">
            <div className="container-fluid">
                <Link className="navbar-brand" to="/">EMH</Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                            <NavLink className={ isActive => isActive ? 'nav-link active' : 'nav-link' } aria-current="page" to="/">Home</NavLink>
                        </li>
                    </ul>
                    <form className="d-flex">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item">
                                <NavLink className={ isActive => isActive ? 'nav-link active' : 'nav-link' } aria-current="page" to="/admin">Administration</NavLink>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </nav>
    )

export default Navbar