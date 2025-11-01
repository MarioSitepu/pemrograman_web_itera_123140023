// src/hooks/useLocalStorage.test.js
import { renderHook, act } from '@testing-library/react';
import useLocalStorage from './useLocalStorage';

// Mock localStorage
const localStorageMock = (() => {
  let store = {};
  return {
    getItem(key) {
      return store[key] || null;
    },
    setItem(key, value) {
      store[key] = value.toString();
    },
    clear() {
      store = {};
    },
  };
})();
Object.defineProperty(window, 'localStorage', {
  value: localStorageMock,
});

test('should return initial value if localStorage is empty', () => {
  const { result } = renderHook(() => useLocalStorage('key', 'initial'));
  expect(result.current[0]).toBe('initial');
});

test('should return value from localStorage', () => {
  localStorage.setItem('key', JSON.stringify('stored value'));
  const { result } = renderHook(() => useLocalStorage('key', 'initial'));
  expect(result.current[0]).toBe('stored value');
});

test('should update localStorage when value is set', () => {
  const { result } = renderHook(() => useLocalStorage('key', 'initial'));
  const [, setValue] = result.current;
  act(() => {
    setValue('new value');
  });
  expect(result.current[0]).toBe('new value');
  expect(localStorage.getItem('key')).toBe(JSON.stringify('new value'));
});