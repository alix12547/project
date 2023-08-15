import { NavLink } from 'react-router-dom'

const Sidebar = () => (
    <ul className="nav nav-side flex-column nav-tabs mt-4">
        <li className="nav-item">
          <NavLink className={isActive => isActive ? 'nav-link active' : 'nav-link'} to="/gmail-creator">GMAIL CREATOR</NavLink>
        </li>
    </ul>
)

export default Sidebar