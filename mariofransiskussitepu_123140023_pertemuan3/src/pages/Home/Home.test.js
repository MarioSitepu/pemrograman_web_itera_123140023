// src/pages/Home/Home.test.js
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import { BookProvider } from '../../context/BookContext';
import Home from './Home';

// Wrapper component untuk menyediakan context dan router
const Wrapper = ({ children }) => (
  <BrowserRouter>
    <BookProvider>{children}</BookProvider>
  </BrowserRouter>
);

test('should add a new book and display it in the list', async () => {
  render(<Home />, { wrapper: Wrapper });

  // Isi form
  fireEvent.change(screen.getByLabelText(/judul/i), {
    target: { value: 'Buku Baru' },
  });
  fireEvent.change(screen.getByLabelText(/penulis/i), {
    target: { value: 'Penulis Baru' },
  });

  // Klik tombol simpan
  fireEvent.click(screen.getByRole('button', { name: /simpan/i }));

  // Tunggu hingga buku muncul di daftar
  await waitFor(() => {
    expect(screen.getByText('Buku Baru')).toBeInTheDocument();
    expect(screen.getByText('oleh Penulis Baru')).toBeInTheDocument();
  });
});