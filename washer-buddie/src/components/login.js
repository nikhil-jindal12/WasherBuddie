import React from 'react';
import '../App.css';

function Login() {
  return (
    <div className="login-box">
      <h2>Login</h2>
      <form>
        <input type="text" placeholder="Username" className="input-field" />
        <input type="password" placeholder="Password" className="input-field" />
        <button type="submit" className="login-button">Log In</button>
      </form>
      <div className="login-options">
        <a href="#" className="forgot-password">Forgot Password?</a>
        <a href="#" className="create-account">Create Account</a>
      </div>
    </div>
  );
}

export default Login;
