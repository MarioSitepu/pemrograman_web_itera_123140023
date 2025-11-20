"""
Modul untuk Abstract Base Class LibraryItem dan implementasinya.
Menggunakan konsep OOP: Abstract Class, Inheritance, Encapsulation, dan Polymorphism.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional


class LibraryItem(ABC):
    """
    Abstract Base Class untuk semua item di perpustakaan.
    Kelas ini mendefinisikan interface yang harus diimplementasikan oleh semua subclass.
    
    Attributes:
        _id (str): ID unik item (protected)
        _title (str): Judul item (protected)
        _author (str): Penulis/penerbit item (protected)
        _year (int): Tahun terbit (protected)
        _is_available (bool): Status ketersediaan item (protected)
    """
    
    # Class variable untuk counter ID otomatis
    _id_counter = 1000
    
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor untuk LibraryItem.
        
        Args:
            title (str): Judul item
            author (str): Penulis/penerbit item
            year (int): Tahun terbit
        """
        # Protected attributes menggunakan underscore prefix
        self._id = f"LIB{LibraryItem._id_counter}"
        LibraryItem._id_counter += 1
        self._title = title
        self._author = author
        self._year = year
        self._is_available = True
        self._date_added = datetime.now()
    
    # Property decorator untuk title dengan getter dan setter
    @property
    def title(self) -> str:
        """Getter untuk title."""
        return self._title
    
    @title.setter
    def title(self, value: str):
        """Setter untuk title dengan validasi."""
        if not value or not value.strip():
            raise ValueError("Title tidak boleh kosong")
        self._title = value.strip()
    
    @property
    def id(self) -> str:
        """Getter untuk ID (read-only property)."""
        return self._id
    
    @property
    def author(self) -> str:
        """Getter untuk author."""
        return self._author
    
    @property
    def year(self) -> int:
        """Getter untuk year."""
        return self._year
    
    @property
    def is_available(self) -> bool:
        """Getter untuk status ketersediaan."""
        return self._is_available
    
    def borrow(self) -> bool:
        """
        Method untuk meminjam item.
        
        Returns:
            bool: True jika berhasil dipinjam, False jika tidak tersedia
        """
        if self._is_available:
            self._is_available = False
            return True
        return False
    
    def return_item(self) -> bool:
        """
        Method untuk mengembalikan item.
        
        Returns:
            bool: True jika berhasil dikembalikan, False jika sudah tersedia
        """
        if not self._is_available:
            self._is_available = True
            return True
        return False
    
    @abstractmethod
    def get_item_type(self) -> str:
        """
        Abstract method yang harus diimplementasikan oleh subclass.
        Mengembalikan tipe item.
        
        Returns:
            str: Tipe item (contoh: "Book", "Magazine")
        """
        pass
    
    @abstractmethod
    def get_details(self) -> dict:
        """
        Abstract method yang harus diimplementasikan oleh subclass.
        Mengembalikan detail lengkap item dalam bentuk dictionary.
        
        Returns:
            dict: Dictionary berisi detail item
        """
        pass
    
    @abstractmethod
    def display_info(self) -> str:
        """
        Abstract method yang harus diimplementasikan oleh subclass.
        Mengembalikan string informasi item untuk ditampilkan.
        
        Returns:
            str: String informasi item
        """
        pass
    
    def __str__(self) -> str:
        """String representation dari LibraryItem."""
        status = "Tersedia" if self._is_available else "Dipinjam"
        return f"[{self._id}] {self._title} - {self._author} ({self._year}) - {status}"
    
    def __repr__(self) -> str:
        """Representation untuk debugging."""
        return f"LibraryItem(id={self._id}, title={self._title}, available={self._is_available})"

