// src/hooks/useLocalStorage.js
import { useState, useEffect } from 'react';

/**
 * Fungsi async untuk membaca data dari localStorage
 * @param {string} key - Kunci untuk membaca dari localStorage.
 * @returns {Promise<any>} - Promise yang mengembalikan data dari localStorage.
 */
const getLocalStorageAsync = async (key) => {
  return new Promise((resolve) => {
    try {
      const item = window.localStorage.getItem(key);
      resolve(item ? JSON.parse(item) : null);
    } catch (error) {
      console.error('Error reading from localStorage:', error);
      resolve(null);
    }
  });
};

/**
 * Fungsi async untuk menyimpan data ke localStorage
 * @param {string} key - Kunci untuk menyimpan di localStorage.
 * @param {any} value - Nilai yang akan disimpan.
 * @returns {Promise<boolean>} - Promise yang mengembalikan true jika berhasil.
 */
const setLocalStorageAsync = async (key, value) => {
  return new Promise((resolve) => {
    try {
      window.localStorage.setItem(key, JSON.stringify(value));
      resolve(true);
    } catch (error) {
      console.error('Error writing to localStorage:', error);
      resolve(false);
    }
  });
};

/**
 * Custom hook untuk sinkronisasi state dengan localStorage dengan dukungan async.
 * @param {string} key - Kunci untuk menyimpan di localStorage.
 * @param {any} initialValue - Nilai awal state jika tidak ada di localStorage.
 * @returns {[any, Function]} - Mengembalikan nilai state dan fungsi untuk mengupdatenya.
 */
function useLocalStorage(key, initialValue) {
  // Mendapatkan nilai dari localStorage atau menggunakan initialValue
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(error);
      return initialValue;
    }
  });

  // Menggunakan useEffect untuk sinkronisasi async saat komponen dimount
  useEffect(() => {
    const loadData = async () => {
      const data = await getLocalStorageAsync(key);
      if (data !== null) {
        setStoredValue(data);
      }
    };
    loadData();
  }, [key]);

  // Fungsi untuk mengupdate nilai di state dan localStorage dengan async
  // Tetap kompatibel dengan penggunaan sync (mengabaikan promise)
  const setValue = (value) => {
    try {
      // Mengizinkan value menjadi fungsi, seperti useState
      const valueToStore =
        value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      // Menggunakan async/await untuk menyimpan ke localStorage
      setLocalStorageAsync(key, valueToStore).catch((error) => {
        console.error('Error saving to localStorage:', error);
      });
    } catch (error) {
      console.error(error);
    }
  };

  return [storedValue, setValue];
}

export default useLocalStorage;