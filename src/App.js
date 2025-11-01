// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { BookProvider } from './context/BookContext';
import Home from './pages/Home/Home';
import Stats from './pages/Stats/Stats';
import FloatingParticles from './components/FloatingParticles/FloatingParticles';
import Logo from './components/Logo/Logo';
import './App.css';

function App() {
  return (
    <BookProvider>
      <Router>
        <div className="app">
          <FloatingParticles />
          <nav className="navbar">
            <Link to="/" className="nav-brand">
              <Logo />
            </Link>
            <div className="nav-links">
              <Link to="/" className="nav-link">
                <span className="nav-icon">📖</span>
                <span className="nav-text">Koleksi</span>
              </Link>
              <Link to="/stats" className="nav-link">
                <span className="nav-icon">📊</span>
                <span className="nav-text">Statistik</span>
              </Link>
            </div>
          </nav>
          <main>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/stats" element={<Stats />} />
            </Routes>
          </main>
        </div>
      </Router>
    </BookProvider>
  );
}

export default App;