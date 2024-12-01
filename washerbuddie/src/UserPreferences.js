import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Header from './Header';

function UserPreferences() {
  const [email, setEmail] = useState('');
  const [reEmail, setReEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rePassword, setRePassword] = useState('');
  const [phone, setPhone] = useState('');
  const [rePhone, setRePhone] = useState('');
  const [notification, setNotification] = useState('email');
  const navigate = useNavigate();

  const handleEmailUpdate = async (e) => {
    e.preventDefault();
    if (email !== reEmail) {
      toast.error('Emails do not match!', { position: toast.POSITION.TOP_RIGHT });
      return;
    }
    try {
      // Make the POST request to the /update endpoint
      const response = await fetch('/update', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          code: 0, // Code for updating the password
          value: email, // The new password
        }),
      });
  
      // Parse the JSON response
      const result = await response.json();
  
      // Handle response success or failure
      if (response.ok && result.success) {
        toast.success('Email updated successfully!', { position: toast.POSITION.TOP_RIGHT });
      } else {
        const errorMessage = result.error || 'Password change failed. Please try again.';
        toast.error(errorMessage, { position: toast.POSITION.TOP_RIGHT });
      }
    } catch (err) {
      // Handle fetch or network errors
      const networkError = 'An error occurred while updating the password. Please try again.';
      toast.error(networkError, { position: toast.POSITION.TOP_RIGHT });
    }
  };

  const handlePasswordUpdate = async (e) => {
    e.preventDefault();
  
    // Check if passwords match
    if (password !== rePassword) {
      toast.error('Passwords do not match!', { position: toast.POSITION.TOP_RIGHT });
      return;
    }
  
    try {
      // Make the POST request to the /update endpoint
      const response = await fetch('/update', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          code: 1, // Code for updating the password
          value: password, // The new password
        }),
      });
  
      // Parse the JSON response
      const result = await response.json();
  
      // Handle response success or failure
      if (response.ok && result.success) {
        toast.success('Password updated successfully!', { position: toast.POSITION.TOP_RIGHT });
      } else {
        const errorMessage = result.error || 'Password change failed. Please try again.';
        toast.error(errorMessage, { position: toast.POSITION.TOP_RIGHT });
      }
    } catch (err) {
      // Handle fetch or network errors
      const networkError = 'An error occurred while updating the password. Please try again.';
      toast.error(networkError, { position: toast.POSITION.TOP_RIGHT });
    }
  };
  

  const handlePhoneUpdate = async (e) => {
    e.preventDefault();
    if (phone !== rePhone) {
      toast.error('Phone numbers do not match!', { position: toast.POSITION.TOP_RIGHT });
      return;
    }
    try {
      // Make the POST request to the /update endpoint
      const response = await fetch('/update', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          code: 2, // Code for updating the password
          value: phone, // The new password
        }),
      });
  
      // Parse the JSON response
      const result = await response.json();
  
      // Handle response success or failure
      if (response.ok && result.success) {
        toast.success('Phone number updated successfully!', { position: toast.POSITION.TOP_RIGHT });
      } else {
        const errorMessage = result.error || 'Password change failed. Please try again.';
        toast.error(errorMessage, { position: toast.POSITION.TOP_RIGHT });
      }
    } catch (err) {
      // Handle fetch or network errors
      const networkError = 'An error occurred while updating the phone number. Please try again.';
      toast.error(networkError, { position: toast.POSITION.TOP_RIGHT });
    }
  };

  const handleNotificationUpdate = async (e) => {
    e.preventDefault();
    try {
      // Make the POST request to the /update endpoint
      const response = await fetch('/update', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          code: 3, // Code for updating the password
          value: notification, // The new password
        }),
      });
  
      // Parse the JSON response
      const result = await response.json();
  
      // Handle response success or failure
      if (response.ok && result.success) {
        toast.success('Notification method updated successfully!', { position: toast.POSITION.TOP_RIGHT });
      } else {
        const errorMessage = result.error || 'Notification method change failed. Please try again.';
        toast.error(errorMessage, { position: toast.POSITION.TOP_RIGHT });
      }
    } catch (err) {
      // Handle fetch or network errors
      const networkError = 'An error occurred while updating the notification method. Please try again.';
      toast.error(networkError, { position: toast.POSITION.TOP_RIGHT });
    }
  };

  const handleAdminAccess = () => {
    // Logic to access admin settings
    navigate('/admin');
  };

  return (
    <>
      <Header />
      <div className="preferences-container">
        <div className="preferences-box">
          <h2>Update Email</h2>
          <form onSubmit={handleEmailUpdate}>
            <label>
              Email
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </label>
            <label>
              Re-enter Email
              <input
                type="email"
                value={reEmail}
                onChange={(e) => setReEmail(e.target.value)}
                required
              />
            </label>
            <button type="submit">Update Email</button>
          </form>
        </div>
        <div className="preferences-box">
          <h2>Update Password</h2>
          <form onSubmit={handlePasswordUpdate}>
            <label>
              Password
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </label>
            <label>
              Re-enter Password
              <input
                type="password"
                value={rePassword}
                onChange={(e) => setRePassword(e.target.value)}
                required
              />
            </label>
            <button type="submit">Update Password</button>
          </form>
        </div>
        <div className="preferences-box">
          <h2>Update Phone Number</h2>
          <form onSubmit={handlePhoneUpdate}>
            <label>
              Phone Number
              <input
                type="tel"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
                required
              />
            </label>
            <label>
              Re-enter Phone Number
              <input
                type="tel"
                value={rePhone}
                onChange={(e) => setRePhone(e.target.value)}
                required
              />
            </label>
            <button type="submit">Update Phone Number</button>
          </form>
        </div>
        <div className="preferences-box">
          <h2>Notification Settings</h2>
          <form onSubmit={handleNotificationUpdate}>
            <label>
              Notification
              <select
                value={notification}
                onChange={(e) => setNotification(e.target.value)}
              >
                <option value="Email">Email</option>
                <option value="Phone">Phone</option>
                <option value="off">Off</option>
              </select>
            </label>
            <button type="submit">Update Notification Settings</button>
          </form>
        </div>
        <div className="preferences-box">
          <h2>Admin Settings</h2>
          <button onClick={handleAdminAccess}>Access Admin Settings</button>
        </div>
      </div>
      <ToastContainer />
    </>
  );
}

export default UserPreferences;