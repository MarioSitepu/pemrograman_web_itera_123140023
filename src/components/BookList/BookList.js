// src/components/BookList/BookList.js
import React from 'react';
import BookItem from '../BookItem/BookItem';
import './BookList.css';

const BookList = ({ books, onEdit, onDelete }) => {
  if (books.length === 0) {
    return (
      <div className="empty-list-container">
        <p className="empty-list">Tidak ada buku yang ditemukan.</p>
      </div>
    );
  }

  return (
    <div className="book-list">
      {books.map((book, index) => (
        <div
          key={book.id}
          className="book-item-wrapper"
          style={{ animationDelay: `${index * 0.1}s` }}
        >
          <BookItem
            book={book}
            onEdit={onEdit}
            onDelete={onDelete}
          />
        </div>
      ))}
    </div>
  );
};

export default BookList;