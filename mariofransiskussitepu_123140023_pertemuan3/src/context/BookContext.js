// src/context/BookContext.js
import React, { createContext, useState, useContext } from 'react';
import useLocalStorage from '../hooks/useLocalStorage';

// Membuat context
const BookContext = createContext();

// Custom hook untuk menggunakan BookContext dengan mudah
export const useBook = () => {
  const context = useContext(BookContext);
  if (!context) {
    throw new Error('useBook harus digunakan di dalam BookProvider');
  }
  return context;
};

// Provider component
export const BookProvider = ({ children }) => {
  const [books, setBooks] = useLocalStorage('books', []);
  const [editingBook, setEditingBook] = useState(null);

  // Fungsi untuk menambah buku baru
  const addBook = (book) => {
    setBooks((prevBooks) => [...prevBooks, { ...book, id: Date.now() }]);
  };

  // Fungsi untuk menghapus buku
  const deleteBook = (id) => {
    // Konfirmasi sebelum menghapus
    const book = books.find((b) => b.id === id);
    const confirmMessage = book
      ? `Apakah Anda yakin ingin menghapus buku "${book.title}"?`
      : 'Apakah Anda yakin ingin menghapus buku ini?';
    
    if (window.confirm(confirmMessage)) {
      setBooks((prevBooks) => prevBooks.filter((book) => book.id !== id));
    }
  };

  // Fungsi untuk memperbarui buku
  const updateBook = (updatedBook) => {
    setBooks((prevBooks) =>
      prevBooks.map((book) =>
        book.id === updatedBook.id ? updatedBook : book
      )
    );
    setEditingBook(null); // Reset form setelah edit
  };

  // Fungsi untuk memulai mode edit
  const startEdit = (book) => {
    setEditingBook(book);
  };

  // Fungsi untuk membatalkan mode edit
  const cancelEdit = () => {
    setEditingBook(null);
  };

  const value = {
    books,
    editingBook,
    addBook,
    deleteBook,
    updateBook,
    startEdit,
    cancelEdit,
  };

  return <BookContext.Provider value={value}>{children}</BookContext.Provider>;
};