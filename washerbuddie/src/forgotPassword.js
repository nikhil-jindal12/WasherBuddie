import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Header from './Header';

function ForgotPassword() {
  const [email, setEmail] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    // Here you can add logic to handle the password reset request
    toast.success('Success!', { position: toast.POSITION.TOP_RIGHT });
    setTimeout(() => {
      navigate('/login'); // Redirect to login page after form submission
    }, 1000); // Delay to allow the toast to be visible before redirect
  };

  return (
    <>
      <Header />
      <div>
        <h1>Forgot Password</h1>
        <form onSubmit={handleSubmit}>
          <label>
            Enter Email
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </label>
          <button type="submit">Submit</button>
        </form>
      </div>
      <ToastContainer />
    </>
  );
}

export default ForgotPassword;