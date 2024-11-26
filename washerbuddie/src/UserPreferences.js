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

  const handleEmailUpdate = (e) => {
    e.preventDefault();
    if (email !== reEmail) {
      toast.error('Emails do not match!', { position: toast.POSITION.TOP_RIGHT });
      return;
    }
    // Logic to update email
    toast.success('Email updated successfully!', { position: toast.POSITION.TOP_RIGHT });
  };

  const handlePasswordUpdate = (e) => {
    e.preventDefault();
    if (password !== rePassword) {
      toast.error('Passwords do not match!', { position: toast.POSITION.TOP_RIGHT });
      return;
    }
    // Logic to update password
    toast.success('Password updated successfully!', { position: toast.POSITION.TOP_RIGHT });
  };

  const handlePhoneUpdate = (e) => {
    e.preventDefault();
    if (phone !== rePhone) {
      toast.error('Phone numbers do not match!', { position: toast.POSITION.TOP_RIGHT });
      return;
    }
    // Logic to update phone number
    toast.success('Phone number updated successfully!', { position: toast.POSITION.TOP_RIGHT });
  };

  const handleNotificationUpdate = (e) => {
    e.preventDefault();
    // Logic to update notification settings
    toast.success('Notification settings updated successfully!', { position: toast.POSITION.TOP_RIGHT });
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
                <option value="email">Email</option>
                <option value="phone">Phone</option>
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