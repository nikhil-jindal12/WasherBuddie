import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Header from './Header';
import './App.css';

function HomePage() {
    const [machines, setMachines] = useState([
        { id: 1, type: 'Washer', status: 'Free', timeRemaining: 0 },
        { id: 2, type: 'Washer', status: 'In Use', timeRemaining: 30 },
        { id: 3, type: 'Washer', status: 'Free', timeRemaining: 0 },
        { id: 4, type: 'Dryer', status: 'Free', timeRemaining: 0 },
        { id: 5, type: 'Dryer', status: 'Free', timeRemaining: 0 },
        { id: 6, type: 'Dryer', status: 'In Use', timeRemaining: 20 },
    ]);

    const navigate = useNavigate();

    const handleStartEndUse = (id) => {
        setMachines((prevMachines) =>
            prevMachines.map((machine) =>
                machine.id === id
                    ? {
                          ...machine,
                          status: machine.status === 'Free' ? 'In Use' : 'Free',
                          timeRemaining: machine.status === 'Free' ? 50 : 0,
                      }
                    : machine
            )
        );
    };

    const handleLogout = () => {
        navigate('/login');
    };

    return (
        <div className="home-page">
            <Header />
            <div className="machines">
                {machines.map((machine) => (
                    <div
                        key={machine.id}
                        className={`machine ${machine.type.toLowerCase()}`}
                    >
                        <h3>
                            {machine.type} {machine.id}
                        </h3>
                        <p>Status: {machine.status}</p>
                        <p>Time Remaining: {machine.timeRemaining} mins</p>
                        <button
                            onClick={() => handleStartEndUse(machine.id)}
                        >
                            {machine.status === 'Free' ? 'Start Use' : 'End Use'}
                        </button>
                    </div>
                ))}
            </div>
            <button className="logout-button" onClick={handleLogout}>
                Logout
            </button>
        </div>
    );
}

export default HomePage;