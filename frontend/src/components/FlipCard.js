import React, { useState } from 'react';
import './FlipCard.css';

function FlipCard() {
  const [signupName, setSignupName] = useState('');
  const [signupEmail, setSignupEmail] = useState('');
  const [signupPassword, setSignupPassword] = useState('');
  const [loginEmail, setLoginEmail] = useState('');
  const [loginPassword, setLoginPassword] = useState('');
  const [message, setMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleSignupSubmit = (e) => {
    e.preventDefault();

    fetch('http://localhost:5000/api/v1/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name: signupName, email: signupEmail, password: signupPassword })
    })
    .then(response => response.json())
    .then(data => {
      setMessage(data.message || 'User signed up successfully!');
      setErrorMessage(''); // Limpa a mensagem de erro ao sucesso
      setSignupName('');
      setSignupEmail('');
      setSignupPassword('');
    })
    .catch(error => {
      console.error('Error:', error);
      setErrorMessage('Error signing up.'); // Define a mensagem de erro
    });
  };

  const handleLoginSubmit = (e) => {
    e.preventDefault();

    fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email: loginEmail, password: loginPassword })
    })
    .then(response => response.json())
    .then(data => {
      setMessage(data.message || 'Login successful!');
      setErrorMessage(''); // Limpa a mensagem de erro ao sucesso
      setLoginEmail('');
      setLoginPassword('');
    })
    .catch(error => {
      console.error('Error:', error);
      setErrorMessage('Error logging in.'); // Define a mensagem de erro
    });
  };

  return (
    <div className="wrapper">
      <div className="card-switch">
        <label className="switch">
          <input type="checkbox" className="toggle" />
          <span className="slider"></span>
          <span className="card-side"></span>
          <div className="flip-card__inner">
            <div className="flip-card__front">
              <div className="title">Log in</div>
              <form className="flip-card__form" onSubmit={handleLoginSubmit}>
                <input
                  className="flip-card__input"
                  name="email"
                  placeholder="Email"
                  type="email"
                  value={loginEmail}
                  onChange={(e) => setLoginEmail(e.target.value)}
                  required
                />
                <input
                  className="flip-card__input"
                  name="password"
                  placeholder="Password"
                  type="password"
                  value={loginPassword}
                  onChange={(e) => setLoginPassword(e.target.value)}
                  required
                />
                <button className="flip-card__btn">Let's go!</button>
              </form>
            </div>
            <div className="flip-card__back">
              <div className="title">Sign up</div>
              <form className="flip-card__form" onSubmit={handleSignupSubmit}>
                <input
                  className="flip-card__input"
                  placeholder="Name"
                  type="text"
                  value={signupName}
                  onChange={(e) => setSignupName(e.target.value)}
                  required
                />
                <input
                  className="flip-card__input"
                  name="email"
                  placeholder="Email"
                  type="email"
                  value={signupEmail}
                  onChange={(e) => setSignupEmail(e.target.value)}
                  required
                />
                <input
                  className="flip-card__input"
                  name="password"
                  placeholder="Password"
                  type="password"
                  value={signupPassword}
                  onChange={(e) => setSignupPassword(e.target.value)}
                  required
                />
                <button className="flip-card__btn">Confirm!</button>
              </form>
            </div>
          </div>
        </label>
      </div>
      <div className="error-container">
        {errorMessage && <p className="error-message">{errorMessage}</p>}
      </div>
    </div>
  );
}

export default FlipCard;
