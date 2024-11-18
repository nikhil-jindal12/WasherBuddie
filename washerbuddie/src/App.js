import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './login';
import CreateAccount from './CreateAccount';
import HomePage from './homePage';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Header from './Header';

function App() {
    return (
        <Router>
            <div>
                <ToastContainer />
                <Routes>
                    <Route path="/login" element={<Login />} />
                    <Route path="/create-account" element={<CreateAccount />} />
                    <Route path="/home" element={<HomePage />} />
                    <Route path="/" element={<Login />} /> {/* Default route */}
                </Routes>
            </div>
        </Router>
    );
}

export default App;