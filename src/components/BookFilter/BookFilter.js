// src/components/BookFilter/BookFilter.js
import React from 'react';
import './BookFilter.css';

const BookFilter = ({ currentFilter, onFilterChange }) => {
  const filters = ['semua', 'milik', 'baca', 'beli'];

  return (
    <div className="book-filter">
      {filters.map((filter) => (
        <button
          key={filter}
          className={`filter-btn ${currentFilter === filter ? 'active' : ''}`}
          onClick={() => onFilterChange(filter)}
        >
          {filter.charAt(0).toUpperCase() + filter.slice(1)}
        </button>
      ))}
    </div>
  );
};

export default BookFilter;