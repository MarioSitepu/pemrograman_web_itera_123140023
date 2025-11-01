// src/components/BookForm/BookForm.js
import React, { useState, useEffect } from 'react';
import BookValidator from '../../utils/BookValidator';
import './BookForm.css';

const BookForm = ({ onSubmit, initialData, onCancel }) => {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [status, setStatus] = useState('milik');
  const [error, setError] = useState('');
  const validator = new BookValidator();

  // Mengisi form jika ada data awal (mode edit)
  useEffect(() => {
    if (initialData) {
      setTitle(initialData.title);
      setAuthor(initialData.author);
      setStatus(initialData.status);
    }
  }, [initialData]);

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Validasi menggunakan Class BookValidator
    const validation = validator.validateBook({ title, author, status });
    
    if (!validation.isValid) {
      setError(validation.errors.join(' '));
      return;
    }
    
    setError('');
    onSubmit({ title, author, status });
    // Reset form hanya jika menambah buku baru
    if (!initialData) {
      setTitle('');
      setAuthor('');
      setStatus('milik');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="book-form">
      <div className="form-header">
        <div className="form-icon">{initialData ? '✏️' : '➕'}</div>
        <h2>{initialData ? 'Edit Buku' : 'Tambah Buku Baru'}</h2>
        <p className="form-subtitle">
          {initialData ? 'Perbarui informasi buku Anda' : 'Isi detail buku untuk menambahkannya ke koleksi'}
        </p>
      </div>
      
      {error && (
        <div className="error-message">
          <span className="error-icon">⚠️</span>
          <span>{error}</span>
        </div>
      )}

      <div className="form-grid">
        <div className="form-group">
          <label htmlFor="title" className="form-label">
            <span className="label-icon">📖</span>
            <span>Judul Buku</span>
          </label>
          <div className="input-wrapper">
            <input
              type="text"
              id="title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Masukkan judul buku"
              className="form-input"
            />
          </div>
        </div>

        <div className="form-group">
          <label htmlFor="author" className="form-label">
            <span className="label-icon">✍️</span>
            <span>Penulis</span>
          </label>
          <div className="input-wrapper">
            <input
              type="text"
              id="author"
              value={author}
              onChange={(e) => setAuthor(e.target.value)}
              placeholder="Nama penulis"
              className="form-input"
            />
          </div>
        </div>

        <div className="form-group form-group-full">
          <label className="form-label">
            <span className="label-icon">🏷️</span>
            <span>Status Buku</span>
          </label>
          <div className="status-selector">
            <button
              type="button"
              onClick={() => setStatus('milik')}
              className={`status-option ${status === 'milik' ? 'active' : ''}`}
            >
              <span className="status-icon">✅</span>
              <span className="status-text">Dimiliki</span>
            </button>
            <button
              type="button"
              onClick={() => setStatus('baca')}
              className={`status-option ${status === 'baca' ? 'active' : ''}`}
            >
              <span className="status-icon">📖</span>
              <span className="status-text">Sedang Dibaca</span>
            </button>
            <button
              type="button"
              onClick={() => setStatus('beli')}
              className={`status-option ${status === 'beli' ? 'active' : ''}`}
            >
              <span className="status-icon">🛒</span>
              <span className="status-text">Ingin Dibeli</span>
            </button>
          </div>
        </div>
      </div>

      <div className="form-actions">
        <button type="submit" className="btn btn-primary btn-large">
          <span className="btn-icon">{initialData ? '💾' : '➕'}</span>
          <span>{initialData ? 'Perbarui Buku' : 'Tambah Buku'}</span>
        </button>
        {initialData && (
          <button type="button" onClick={onCancel} className="btn btn-secondary btn-large">
            <span className="btn-icon">❌</span>
            <span>Batal</span>
          </button>
        )}
      </div>
    </form>
  );
};

export default BookForm;