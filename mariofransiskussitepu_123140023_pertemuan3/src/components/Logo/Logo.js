// src/components/Logo/Logo.js
import React from 'react';
import './Logo.css';

const Logo = ({ className = '' }) => {
  return (
    <div className={`logo-container ${className}`}>
      <div className="logo-icon">
        <svg
          width="48"
          height="48"
          viewBox="0 0 48 48"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <rect
            width="48"
            height="48"
            rx="12"
            fill="url(#gradient1)"
          />
          <path
            d="M14 18C14 16.8954 14.8954 16 16 16H32C33.1046 16 34 16.8954 34 18V30C34 31.1046 33.1046 32 32 32H16C14.8954 32 14 31.1046 14 30V18Z"
            fill="white"
            fillOpacity="0.9"
          />
          <path
            d="M18 20H30M18 24H26M18 28H24"
            stroke="url(#gradient2)"
            strokeWidth="2"
            strokeLinecap="round"
          />
          <defs>
            <linearGradient id="gradient1" x1="0" y1="0" x2="48" y2="48" gradientUnits="userSpaceOnUse">
              <stop stopColor="#667eea" />
              <stop offset="1" stopColor="#764ba2" />
            </linearGradient>
            <linearGradient id="gradient2" x1="18" y1="24" x2="30" y2="24" gradientUnits="userSpaceOnUse">
              <stop stopColor="#667eea" />
              <stop offset="1" stopColor="#764ba2" />
            </linearGradient>
          </defs>
        </svg>
      </div>
      <div className="logo-text">
        <span className="logo-name">EasyBook</span>
        <span className="logo-tagline">App</span>
      </div>
    </div>
  );
};

export default Logo;

