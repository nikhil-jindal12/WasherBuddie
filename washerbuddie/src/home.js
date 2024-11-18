import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Header from './Header';

function Home() {
  const navigate = useNavigate();

  useEffect(() => {
    const timer = setTimeout(() => {
      navigate('/login');
    }, 5000);

    return () => clearTimeout(timer);
  }, [navigate]);

  return (
    <>
      <Header />
      <div>
        <h1>Welcome to Washer Buddie</h1>
        <p>Your one-stop spot for all laundry needs!</p>
        <button onClick={() => navigate('/login')}>Continue</button>
      </div>
    </>
  );
}

export default Home;
