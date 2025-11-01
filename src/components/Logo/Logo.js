// src/components/Logo/Logo.js
import React from 'react';
import logoImage from '../../logobuku.png';
import './Logo.css';

const Logo = ({ className = '' }) => {
  return (
    <div className={`logo-container ${className}`}>
      <div className="logo-icon">
        <img 
          src={logoImage} 
          alt="EasyBookApp Logo" 
          className="logo-image"
        />
      </div>
      <div className="logo-text">
        <span className="logo-name">EasyBook</span>
        <span className="logo-tagline">App</span>
      </div>
    </div>
  );
};

export default Logo;

