// src/hooks/useBookStats.test.js
import { renderHook } from '@testing-library/react';
import useBookStats from './useBookStats';

test('should return correct stats for an empty book list', () => {
  const { result } = renderHook(() => useBookStats([]));
  expect(result.current).toEqual({ total: 0, owned: 0, reading: 0, wantToBuy: 0 });
});

test('should return correct stats for a populated book list', () => {
  const books = [
    { id: 1, title: 'A', author: 'X', status: 'milik' },
    { id: 2, title: 'B', author: 'Y', status: 'baca' },
    { id: 3, title: 'C', author: 'Z', status: 'beli' },
    { id: 4, title: 'D', author: 'W', status: 'milik' },
  ];
  const { result } = renderHook(() => useBookStats(books));
  expect(result.current).toEqual({ total: 4, owned: 2, reading: 1, wantToBuy: 1 });
});