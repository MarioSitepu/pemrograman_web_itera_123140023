// src/components/BookList/BookList.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import BookList from './BookList';

const mockBooks = [
  { id: 1, title: 'Book 1', author: 'Author 1', status: 'milik' },
  { id: 2, title: 'Book 2', author: 'Author 2', status: 'baca' },
];

test('renders a list of books', () => {
  render(<BookList books={mockBooks} onEdit={() => {}} onDelete={() => {}} />);
  
  expect(screen.getByText('Book 1')).toBeInTheDocument();
  expect(screen.getByText('oleh Author 1')).toBeInTheDocument();
  expect(screen.getByText('Book 2')).toBeInTheDocument();
  expect(screen.getByText('oleh Author 2')).toBeInTheDocument();
});

test('renders empty message when no books are provided', () => {
  render(<BookList books={[]} onEdit={() => {}} onDelete={() => {}} />);
  expect(screen.getByText(/tidak ada buku yang ditemukan/i)).toBeInTheDocument();
});