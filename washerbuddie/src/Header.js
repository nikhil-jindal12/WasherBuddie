import React, { useState } from 'react';
import './Header.css';

function Header() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <header className="app-header">
      <div className="bubbles">
        <div className="bubble"></div>
        <div className="bubble"></div>
        <div className="bubble"></div>
        <div className="bubble"></div>
        <div className="bubble"></div>
        <div className="bubble"></div>
        <div className="bubble"></div>
        <div className="bubble"></div>
      </div>
      <div className="header-content">
        <h1>WasherBuddie</h1>
        <div className="menu-icon" onClick={toggleMenu}>
          <div className="bar"></div>
          <div className="bar"></div>
          <div className="bar"></div>
        </div>
        {isOpen && (
          <div className="dropdown-menu">
            <ul>
              <li>Menu Item 1</li>
              <li>Menu Item 2</li>
              <li>Menu Item 3</li>
            </ul>
          </div>
        )}
      </div>
    </header>
  );
}

export default Header;