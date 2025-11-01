// src/hooks/useBookStats.js
import { useMemo } from 'react';

/**
 * Custom hook untuk menghitung statistik berdasarkan daftar buku.
 * @param {Array} books - Array dari objek buku.
 * @returns {Object} - Objek berisi statistik buku.
 */
function useBookStats(books) {
  const stats = useMemo(() => {
    return books.reduce(
      (acc, book) => {
        acc.total++;
        if (book.status === 'milik') acc.owned++;
        if (book.status === 'baca') acc.reading++;
        if (book.status === 'beli') acc.wantToBuy++;
        return acc;
      },
      { total: 0, owned: 0, reading: 0, wantToBuy: 0 }
    );
  }, [books]);

  return stats;
}

export default useBookStats;