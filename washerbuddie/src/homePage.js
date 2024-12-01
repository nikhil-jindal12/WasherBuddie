import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Header from './Header';
import Menu from './menu';
import './App.css';

function HomePage() {
    const [machines, setMachines] = useState([]);
    const navigate = useNavigate();
    const userName = 'test_user'; // Replace with the logged-in user's name

    const fetchMachines = async () => {
        try {
            const response = await fetch('/get_machines'); // Replace with your API URL
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();
            console.log('Fetched Data:', data);
    
            // Access DB_machines array and map it to the required format
            if (Array.isArray(data.DB_machines)) {
                const machineArray = data.DB_machines.map((machine) => {
                    // Parse start and end times
                    const startTime = new Date(machine._start_time);
                    const endTime = new Date(machine._end_time);
                    const now = new Date();
    
                    let timeRemaining = 0;
                    if (machine._current_state === 'In Use' && now < endTime) {
                        // Calculate remaining time in minutes
                        timeRemaining = Math.max(0, Math.round((endTime - now) / 60000));
                    }
    
                    return {
                        id: machine._machine_id, // Access _machine_id for the id
                        type: machine._machine_type, // Access _machine_type for the type
                        status: machine._current_state, // Access _current_state for the status
                        timeRemaining, // Calculated time remaining
                    };
                });
                setMachines(machineArray);
            } else {
                console.error('Expected an array of machines but got:', data);
            }
        } catch (error) {
            console.error('Error fetching machine data:', error);
        }
    };

    useEffect(() => {
        // Fetch machines on component mount
        fetchMachines();

        // Set up an interval to fetch machines every minute
        const interval = setInterval(fetchMachines, 60000); // 60000ms = 1 minute

        // Cleanup interval on component unmount
        return () => clearInterval(interval);
    }, []); // Empty dependency array ensures this runs only on mount/unmount

    const handleStartEndUse = async (id) => {
        const machine = machines.find((m) => m.id === id);

        if (machine) {
            if (machine.status === 'Available') {
                try {
                    // Make a POST request to /create_session
                    const response = await fetch('/create_session', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            machine_id: machine.id,
                            user_name: userName, // Replace with the actual user's name
                        }),
                    });

                    const result = await response.json();
                    if (response.ok && result.success) {
                        console.log('Session created:', result.message);
                        setMachines((prevMachines) =>
                            prevMachines.map((m) =>
                                m.id === id
                                    ? { ...m, status: 'In Use', timeRemaining: 50 }
                                    : m
                            )
                        );
                    } else {
                        console.error('Failed to create session:', result.error);
                    }
                } catch (error) {
                    console.error('Error creating session:', error);
                }
            } else {
                // Handle end use (logic for ending a session, if applicable)
                console.log(`Ending use for machine ${id}`);
                setMachines((prevMachines) =>
                    prevMachines.map((m) =>
                        m.id === id
                            ? { ...m, status: 'Available', timeRemaining: 0 }
                            : m
                    )
                );
            }
        }
    };

    const handleLogout = () => {
        navigate('/login');
    };

    return (
        <div>
            <Menu />
            <Header />
            <div className="machine-list">
                {machines.map((machine) => (
                    <div key={machine.id} className="machine-tile">
                        <h3>
                            {machine.type} {machine.id}
                        </h3>
                        <p>Status: {machine.status}</p>
                        <p>Time Remaining: {machine.timeRemaining} mins</p>
                        <button 
                            onClick={() => handleStartEndUse(machine.id)} 
                            disabled={machine.status !== 'Available'} 
                            style={{
                                backgroundColor: machine.status === 'Available' ? '#007bff' : '#d3d3d3',
                                color: machine.status === 'Available' ? '#fff' : '#808080',
                                cursor: machine.status === 'Available' ? 'pointer' : 'not-allowed',
                            }}
                        >
                            {machine.status === 'Available' ? 'Start Use' : 'End Use'}
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default HomePage;
