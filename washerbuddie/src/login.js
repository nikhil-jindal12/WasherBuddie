import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Header from './Header';
// import { login } from './api';

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    // const handleSubmit = async (e) => {
    //     e.preventDefault();
    //     try {
    //         const response = await login(email, password);
    //         if (response.success) {
    //             navigate('/home-page'); // Redirect to home page on successful login
    //         } else {
    //             setError(response.message); // Display error message from API
    //             toast.error(response.message, { position: toast.POSITION.TOP_RIGHT });
    //         }
    //     } catch (err) {
    //         setError('An error occurred. Please try again.');
    //         toast.error('An error occurred. Please try again.', { position: toast.POSITION.TOP_RIGHT });
    //     }
    // };

    return (
        <div>
            <Header />
            <h2>Login</h2>
            <form onSubmit={() => console.log('TODO')}> {/* TODO - link to DB */}
                <div>
                    <label>Email</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                        style={{ borderColor: error ? 'red' : '' }}
                    />
                </div>
                <div>
                    <label>Password</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        style={{ borderColor: error ? 'red' : '' }}
                    />
                </div>
                {error && <p style={{ color: 'red' }}>{error}</p>}
                <button type="submit">Log In</button>
            </form>
            <div>
                <Link to="/forgot-password">Forgot Password?</Link>
                <Link to="/create-Account">Create Account</Link>
            </div>
        </div>
    );
}

export default Login;
