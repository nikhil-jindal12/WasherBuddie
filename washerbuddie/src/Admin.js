import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Header from './Header';
import Menu from './menu';
import './App.css';

function AdminPage() {
    const [machines, setMachines] = useState([
        { id: 1, type: 'Washer', status: 'Available' },
        { id: 2, type: 'Dryer', status: 'In Use' },
        { id: 3, type: 'Washer', status: 'Available' },
    ]);
    const [users, setUsers] = useState([
        { id: 1, name: 'test_user1', role: 'User' },
        { id: 2, name: 'test_user2', role: 'Admin' },
        { id: 3, name: 'test_user3', role: 'User' },
    ]);
    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    // Handler to set machine out of order
    const handleSetOutOfOrder = (id) => {
        setMachines((prevMachines) =>
            prevMachines.map((m) =>
                m.id === id ? { ...m, status: 'Out of Order' } : m
            )
        );
    };

    // Handler to delete user account
    const handleDeleteUser = (id) => {
        setUsers((prevUsers) => prevUsers.filter((user) => user.id !== id));
    };

    // Handler to promote user
    const handlePromoteUser = (id) => {
        setUsers((prevUsers) =>
            prevUsers.map((user) =>
                user.id === id ? { ...user, role: 'Admin' } : user
            )
        );
    };

    // Handler to send a message
    const handleSendMessage = () => {
        if (message.trim()) {
            alert(`Message sent: ${message}`);
            setMessage('');
        }
    };

    return (
        <div>
            <Menu />
            <Header />
            <div className="admin-controls">
                {/* Machines section */}
                <div className="section">
                    <h2>Machines</h2>
                    <div className="machine-list">
                        {machines.map((machine) => (
                            <div key={machine.id} className="machine-tile">
                                <h3>
                                    {machine.type} {machine.id}
                                </h3>
                                <p>Status: {machine.status}</p>
                                <button
                                    onClick={() => handleSetOutOfOrder(machine.id)}
                                    style={{
                                        backgroundColor: machine.status === 'Available' ? '#ff0000' : '#d3d3d3',
                                        color: machine.status === 'Available' ? '#fff' : '#808080',
                                        cursor: machine.status === 'Available' ? 'pointer' : 'not-allowed',
                                    }}
                                    disabled={machine.status !== 'Available'}
                                >
                                    Set Out of Order
                                </button>
                            </div>
                        ))}
                    </div>
                </div>

                {/* Users section */}
                <div className="section">
                    <h2>Users</h2>
                    <div className="machine-list">
                        {users.map((user) => (
                            <div key={user.id} className="machine-tile">
                                <h3>{user.name}</h3>
                                <p>Role: {user.role}</p>
                                <button onClick={() => handleDeleteUser(user.id)} style={{ backgroundColor: '#ff0000', color: '#fff' }}>
                                    Delete Account
                                </button>
                                <button
                                    onClick={() => handlePromoteUser(user.id)}
                                    style={{
                                        backgroundColor: user.role === 'Admin' ? '#d3d3d3' : '#007bff',
                                        color: user.role === 'Admin' ? '#808080' : '#fff',
                                    }}
                                    disabled={user.role === 'Admin'}
                                >
                                    Promote
                                </button>
                            </div>
                        ))}
                    </div>
                </div>

                {/* Send Message section */}
                
                {/* <div className="section">
                    <h2>Send Message</h2>
                    <div className='machine-list'>
                    <div className='machine-tile'>
                    <textarea
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        placeholder="Enter your message"
                    />
                    <button onClick={handleSendMessage}>Send Message</button>
                    </div>
                    </div>
                </div> */}
            </div>
        </div>
    );
}

export default AdminPage;
