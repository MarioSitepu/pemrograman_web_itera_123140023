// src/components/BookItem/BookItem.js
import React from 'react';
import './BookItem.css';

const BookItem = ({ book, onEdit, onDelete }) => {
  const statusBadgeClass = {
    milik: 'badge-owned',
    baca: 'badge-reading',
    beli: 'badge-want-to-buy',
  };

  // Template literals untuk rendering dinamis
  const statusLabels = {
    milik: 'Dimiliki',
    baca: 'Sedang Dibaca',
    beli: 'Ingin Dibeli',
  };
  const statusLabel = statusLabels[book.status] || 'Tidak Diketahui';
  const bookDescription = `Buku "${book.title}" ditulis oleh ${book.author}`;

  return (
    <div className="book-item">
      <div className="book-info">
        <h3 className="book-title">{book.title}</h3>
        <p className="book-author" title={bookDescription}>oleh {book.author}</p>
        <span className={`badge ${statusBadgeClass[book.status]}`}>
          {statusLabel}
        </span>
      </div>
      <div className="book-actions">
        <button 
          type="button"
          onClick={(e) => {
            e.preventDefault();
            e.stopPropagation();
            console.log('Edit button clicked', book);
            if (onEdit && typeof onEdit === 'function') {
              onEdit(book);
            } else {
              console.warn('onEdit is not a function or not provided');
            }
          }} 
          className="btn-edit"
        >
          <span className="btn-action-icon">✏️</span>
          <span>Edit</span>
        </button>
        <button 
          type="button"
          onClick={(e) => {
            e.preventDefault();
            e.stopPropagation();
            console.log('Delete button clicked', book.id);
            if (onDelete && typeof onDelete === 'function') {
              onDelete(book.id);
            } else {
              console.warn('onDelete is not a function or not provided');
            }
          }} 
          className="btn-delete"
        >
          <span className="btn-action-icon">🗑️</span>
          <span>Hapus</span>
        </button>
      </div>
    </div>
  );
};

export default BookItem;