import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Header from './Header';
// import { createUser } from './api';
import './App.css';

{/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}

function CreateAccount() {
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

//   const handleSubmit = async (e) => {
//       e.preventDefault();
//       try {
//           const response = await createUser({ email, phone, password });
//           if (response.success) {
//               navigate('/home-page'); // Redirect to home page on successful account creation
//           } else {
//               setError(response.message); // Display error message from API
//               toast.error(response.message, { position: toast.POSITION.TOP_RIGHT });
//           }
//       } catch (err) {
//           setError('An error occurred. Please try again.');
//           toast.error('An error occurred. Please try again.', { position: toast.POSITION.TOP_RIGHT });
//       }
//   };

  return (
      <div>
         <Header />
          <h2>Create Account</h2>
          <form onSubmit={() => console.log('TODO')}> {/* TODO - link to DB   */}
              <div>
                  <label>Email</label>
                  <input
                      type="email"
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      required
                  />
              </div>
              <div>
                  <label>Phone</label>
                  <input
                      type="tel"
                      value={phone}
                      onChange={(e) => setPhone(e.target.value)}
                      required
                  />
              </div>
              <div>
                  <label>Password</label>
                  <input
                      type="password"
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      required
                  />
              </div>
              {error && <p style={{ color: 'red' }}>{error}</p>}
              <button type="submit">Create Account</button>
          </form>
          <div>
              <Link to="/login">Already have an account? Log In</Link>
          </div>
      </div>
  );
}

export default CreateAccount;