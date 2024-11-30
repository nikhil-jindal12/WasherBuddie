import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Header from './Header';
import Menu from './menu';
import './App.css';

function HomePage() {
    const [machines, setMachines] = useState([]);
    const navigate = useNavigate();

    // Fetch data from API and update state
    useEffect(() => {
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
                    const machineArray = data.DB_machines.map((machine) => ({
                        id: machine._machine_id, // Access _machine_id for the id
                        type: machine._machine_type, // Access _machine_type for the type
                        status: machine._current_state, // Access _current_state for the status
                        timeRemaining: machine._start_time ? 50 : 0, // Default timeRemaining to 50 if _start_time exists
                    }));
                    setMachines(machineArray);
                } else {
                    console.error('Expected an array of machines but got:', data);
                }
            } catch (error) {
                console.error('Error fetching machine data:', error);
            }
        };

        fetchMachines();
    }, []); // Empty dependency array to run only once when the component mounts

    const handleStartEndUse = (id) => {
        setMachines((prevMachines) =>
            prevMachines.map((machine) =>
                machine.id === id
                    ? {
                          ...machine,
                          status: machine.status === 'Available' ? 'In Use' : 'Available',
                          timeRemaining: machine.status === 'Available' ? 50 : 0,
                      }
                    : machine
            )
        );
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
                        <button onClick={() => handleStartEndUse(machine.id)}>
                            {machine.status === 'Available' ? 'Start Use' : 'End Use'}
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default HomePage;
