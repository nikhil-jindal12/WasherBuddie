import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import '../App.css';

function CreateAccount() {
  const [notificationMethod, setNotificationMethod] = useState(null);

  const handleNotificationChange = (e) => {
    setNotificationMethod(e.target.value);
  };

  return (
    <div className="create-account-box">
      <h2>Create Account</h2>
      <form>
        <input type="first" placeholder="First Name" className="input-field" required />
        <input type="last" placeholder="Last Name" className="input-field" required />
        <input type="email" placeholder="Email" className="input-field" required />
        <input type="phone" placeholder="Phone Numer" className="input-field" required />
        <input type="password" placeholder="Password" className="input-field" required />
        <input type="password" placeholder="Confirm Password" className="input-field" required />

        <div className="notification-preference">
          <label>Notification Preference:</label>
          <div>
            <input 
              type="radio" 
              id="email" 
              name="notification" 
              value="email" 
              onChange={handleNotificationChange} 
            />
            <label htmlFor="email">Email</label>
          </div>
          <div>
            <input 
              type="radio" 
              id="phone" 
              name="notification" 
              value="phone" 
              onChange={handleNotificationChange} 
            />
            <label htmlFor="phone">Phone</label>
          </div>
        </div>


        <button type="submit" className="create-account-button">Create Account</button>
      </form>
      <p>Already have an account? <Link to="/login">Log In</Link></p>
    </div>
  );
}

export default CreateAccount;

