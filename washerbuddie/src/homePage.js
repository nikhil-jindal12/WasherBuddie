import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import 'react-toastify/dist/ReactToastify.css';
import '../App.css';

function HomePage() {
    const [machines, setMachines] = useState([
        { id: 1, type: 'Washer', status: 'Free', timeRemaining: 0 },
        { id: 2, type: 'Washer', status: 'In Use', timeRemaining: 15 },
        { id: 3, type: 'Dryer', status: 'Free', timeRemaining: 0 },
        { id: 4, type: 'Dryer', status: 'In Use', timeRemaining: 20 },
    ]);
    const [notificationMethod, setNotificationMethod] = useState('email');
    const [isAdmin, setIsAdmin] = useState(false);
    const [message, setMessage] = useState('');

    const handleStartEndUse = (id) => {
        setMachines((prevMachines) =>
            prevMachines.map((machine) =>
                machine.id === id
                    ? {
                          ...machine,
                          status: machine.status === 'Free' ? 'In Use' : 'Free',
                          timeRemaining: machine.status === 'Free' ? 30 : 0,
                      }
                    : machine
            )
        );
    };

    const handleNotificationChange = (e) => {
        setNotificationMethod(e.target.value);
    };

    const handleAdminToggle = () => {
        setIsAdmin(!isAdmin);
    };

    const handleSendMessage = () => {
        // Implement send message functionality
        console.log('Message sent:', message);
    };

    return (
        <div>
            <h1>Home Page</h1>
            <button onClick={handleAdminToggle}>
                {isAdmin ? 'Switch to User Mode' : 'Switch to Admin Mode'}
            </button>
            {isAdmin && (
                <div>
                    <textarea
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                    />
                    <button onClick={handleSendMessage}>Send</button>
                </div>
            )}
            <div>
                <h2>Notification Preference:</h2>
                <label>
                    <input
                        type="radio"
                        value="email"
                        checked={notificationMethod === 'email'}
                        onChange={handleNotificationChange}
                    />
                    Email
                </label>
                <label>
                    <input
                        type="radio"
                        value="phone"
                        checked={notificationMethod === 'phone'}
                        onChange={handleNotificationChange}
                    />
                    Phone
                </label>
            </div>
            <div>
                {machines.map((machine) => (
                    <div key={machine.id}>
                        <h3>
                            {machine.type} {machine.id}
                        </h3>
                        <p>Status: {machine.status}</p>
                        <p>Time Remaining: {machine.timeRemaining} mins</p>
                        <button
                            onClick={() => handleStartEndUse(machine.id)}
                            disabled={machine.status === 'In Use'}
                        >
                            {machine.status === 'Free' ? 'Start Use' : 'End Use'}
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default HomePage;
