// src/utils/BookValidator.js

/**
 * Class untuk validasi data buku
 * Mengimplementasikan ES6 Classes
 */
class BookValidator {
  constructor() {
    this.minTitleLength = 2;
    this.maxTitleLength = 200;
    this.minAuthorLength = 2;
    this.maxAuthorLength = 100;
  }

  /**
   * Memvalidasi judul buku
   * @param {string} title - Judul buku yang akan divalidasi.
   * @returns {Object} - Objek dengan properti isValid dan message.
   */
  validateTitle(title) {
    if (!title || typeof title !== 'string') {
      return {
        isValid: false,
        message: 'Judul harus berupa teks dan tidak boleh kosong.',
      };
    }

    const trimmedTitle = title.trim();
    if (trimmedTitle.length < this.minTitleLength) {
      return {
        isValid: false,
        message: `Judul minimal harus ${this.minTitleLength} karakter.`,
      };
    }

    if (trimmedTitle.length > this.maxTitleLength) {
      return {
        isValid: false,
        message: `Judul maksimal ${this.maxTitleLength} karakter.`,
      };
    }

    return { isValid: true, message: '' };
  }

  /**
   * Memvalidasi nama penulis
   * @param {string} author - Nama penulis yang akan divalidasi.
   * @returns {Object} - Objek dengan properti isValid dan message.
   */
  validateAuthor(author) {
    if (!author || typeof author !== 'string') {
      return {
        isValid: false,
        message: 'Penulis harus berupa teks dan tidak boleh kosong.',
      };
    }

    const trimmedAuthor = author.trim();
    if (trimmedAuthor.length < this.minAuthorLength) {
      return {
        isValid: false,
        message: `Nama penulis minimal harus ${this.minAuthorLength} karakter.`,
      };
    }

    if (trimmedAuthor.length > this.maxAuthorLength) {
      return {
        isValid: false,
        message: `Nama penulis maksimal ${this.maxAuthorLength} karakter.`,
      };
    }

    return { isValid: true, message: '' };
  }

  /**
   * Memvalidasi status buku
   * @param {string} status - Status buku yang akan divalidasi.
   * @returns {Object} - Objek dengan properti isValid dan message.
   */
  validateStatus(status) {
    const validStatuses = ['milik', 'baca', 'beli'];
    if (!validStatuses.includes(status)) {
      return {
        isValid: false,
        message: `Status harus salah satu dari: ${validStatuses.join(', ')}.`,
      };
    }
    return { isValid: true, message: '' };
  }

  /**
   * Memvalidasi seluruh data buku
   * @param {Object} book - Objek buku yang akan divalidasi.
   * @returns {Object} - Objek dengan properti isValid dan errors.
   */
  validateBook(book) {
    const errors = [];
    const titleValidation = this.validateTitle(book.title);
    const authorValidation = this.validateAuthor(book.author);
    const statusValidation = this.validateStatus(book.status);

    if (!titleValidation.isValid) {
      errors.push(titleValidation.message);
    }
    if (!authorValidation.isValid) {
      errors.push(authorValidation.message);
    }
    if (!statusValidation.isValid) {
      errors.push(statusValidation.message);
    }

    return {
      isValid: errors.length === 0,
      errors: errors,
    };
  }
}

export default BookValidator;

