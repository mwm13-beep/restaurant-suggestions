import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../../App.css';

function Login() {
    const navigate = useNavigate();
    const handleClick = () => {
        navigate('/suggestions');
    };

    return (
        <div className='App'>
            <header className="Nav-bar">
                <button className="Login-button" onClick={handleClick}>Login</button>
            </header>
        </div>
    );
}
  
  export default Login;
