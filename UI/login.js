import { Link } from 'react-router-dom';
import CreateAccount from './CreateAccount';

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
        <Link to="/create-account" className="create-account">Create Account</Link>
      </div>
    </div>
  );
}

export default Login;

