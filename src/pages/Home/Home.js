// src/pages/Home/Home.js
import React, { useState, useMemo } from 'react';
import { useBook } from '../../context/BookContext';
import BookForm from '../../components/BookForm/BookForm';
import BookList from '../../components/BookList/BookList';
import BookFilter from '../../components/BookFilter/BookFilter';
import SearchBar from '../../components/SearchBar/SearchBar';
import './Home.css';

const Home = () => {
  const { books, addBook, deleteBook, updateBook, startEdit, cancelEdit, editingBook } = useBook();
  const [filter, setFilter] = useState('semua');
  const [searchTerm, setSearchTerm] = useState('');

  // Memoisasi daftar buku yang sudah difilter dan dicari
  const filteredBooks = useMemo(() => {
    let processedBooks = books;

    // Filter berdasarkan status
    if (filter !== 'semua') {
      processedBooks = processedBooks.filter((book) => book.status === filter);
    }

    // Filter berdasarkan istilah pencarian
    if (searchTerm) {
      processedBooks = processedBooks.filter(
        (book) =>
          book.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
          book.author.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }

    return processedBooks;
  }, [books, filter, searchTerm]);

  const handleAddBook = (book) => {
    addBook(book);
  };

  const handleUpdateBook = (book) => {
    updateBook({ ...book, id: editingBook.id });
  };

  // Template literals untuk rendering dinamis - informasi statistik
  const statsMessage = useMemo(() => {
    const total = books.length;
    const filtered = filteredBooks.length;
    if (searchTerm || filter !== 'semua') {
      return `Menampilkan ${filtered} dari ${total} buku`;
    }
    return `Total ${total} buku dalam koleksi`;
  }, [books.length, filteredBooks.length, searchTerm, filter]);

  return (
    <div className="home-container">
      <div className="main-content">
        <BookForm
          onSubmit={editingBook ? handleUpdateBook : handleAddBook}
          initialData={editingBook}
          onCancel={cancelEdit}
        />
        <SearchBar searchTerm={searchTerm} onSearchChange={setSearchTerm} />
        <BookFilter currentFilter={filter} onFilterChange={setFilter} />
        {books.length > 0 && (
          <p className="stats-info">{statsMessage}</p>
        )}
        <BookList
          books={filteredBooks}
          onEdit={startEdit}
          onDelete={deleteBook}
        />
      </div>
    </div>
  );
};

export default Home;