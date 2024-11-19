import React, { useState } from 'react';
import './Menu.css';

function Menu() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="menu-container">
      <button className="menu-toggle" onClick={toggleMenu}>
        Menu
      </button>
      {isOpen && (
        <div className="dropdown-menu">
          <ul>
            <li><button>Log out</button></li>
            <li><button>Notification Preferences</button></li>
            <li><button>Password Preferences</button></li>
          </ul>
        </div>
      )}
    </div>
  );
}

export default Menu;