import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './login';
import CreateAccount from './CreateAccount';
import HomePage from './HomePage';
import Home from './Home';
import ForgotPassword from './ForgotPassword';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Header from './Header';
import UserPreferences from '/UserPreferences';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/create-account" element={<CreateAccount />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/home-page" element={<HomePage />} />
        <Route path="/user-preferences" element={<UserPreferences />} />
      </Routes>
      <ToastContainer />
    </Router>
  );
}

export default App;