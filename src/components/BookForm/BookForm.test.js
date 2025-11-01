// src/components/BookForm/BookForm.test.js
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import BookForm from './BookForm';

test('renders BookForm with initial fields', () => {
  const mockSubmit = jest.fn();
  render(<BookForm onSubmit={mockSubmit} />);
  
  expect(screen.getByLabelText(/judul/i)).toBeInTheDocument();
  expect(screen.getByLabelText(/penulis/i)).toBeInTheDocument();
  expect(screen.getByLabelText(/status/i)).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /simpan/i })).toBeInTheDocument();
});

test('should call onSubmit with form data', () => {
  const mockSubmit = jest.fn();
  render(<BookForm onSubmit={mockSubmit} />);
  
  fireEvent.change(screen.getByLabelText(/judul/i), { target: { value: 'Test Book' } });
  fireEvent.change(screen.getByLabelText(/penulis/i), { target: { value: 'Test Author' } });
  fireEvent.click(screen.getByRole('button', { name: /simpan/i }));
  
  expect(mockSubmit).toHaveBeenCalledWith({
    title: 'Test Book',
    author: 'Test Author',
    status: 'milik',
  });
});

test('should display error message on submit with empty fields', () => {
  const mockSubmit = jest.fn();
  render(<BookForm onSubmit={mockSubmit} />);
  
  fireEvent.click(screen.getByRole('button', { name: /simpan/i }));
  
  expect(screen.getByText(/judul dan penulis tidak boleh kosong/i)).toBeInTheDocument();
  expect(mockSubmit).not.toHaveBeenCalled();
});