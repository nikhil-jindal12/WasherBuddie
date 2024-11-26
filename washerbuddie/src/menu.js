import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import './Menu.css';

function Menu() {
  const [isOpen, setIsOpen] = useState(false);
  const navigate = useNavigate();

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  const handleLogout = () => {
    toast.success('Success!');
    setTimeout(() => {
      navigate('/');
    }, 1000); // Redirect after 1 second to allow the toast to be visible
  };

  return (
    <div className="menu-container">
      <button className="menu-toggle" onClick={toggleMenu}>
        Menu
      </button>
      {isOpen && (
        <div className="dropdown-menu">
          <ul>
            <li><button onClick={handleLogout}>Log out</button></li>
            <button onClick={() => navigate('/login')}>User Preferences</button>
          </ul>
        </div>
      )}
      <ToastContainer position="top-right" autoClose={1000} hideProgressBar={false} newestOnTop={false} closeOnClick rtl={false} pauseOnFocusLoss draggable pauseOnHover />
    </div>
  );
}
export default Menu;