"""
Modul untuk class Book yang mewarisi dari LibraryItem.
Mengimplementasikan konsep Inheritance dan Polymorphism.
"""

from library_item import LibraryItem
from typing import Optional


class Book(LibraryItem):
    """
    Class Book yang mewarisi dari LibraryItem.
    Merepresentasikan buku di perpustakaan.
    
    Attributes:
        _isbn (str): ISBN buku (private)
        _pages (int): Jumlah halaman (protected)
        _genre (str): Genre buku (protected)
    """
    
    def __init__(self, title: str, author: str, year: int, isbn: str, 
                 pages: int, genre: str = "Umum"):
        """
        Constructor untuk Book.
        
        Args:
            title (str): Judul buku
            author (str): Penulis buku
            year (int): Tahun terbit
            isbn (str): ISBN buku
            pages (int): Jumlah halaman
            genre (str): Genre buku (default: "Umum")
        """
        super().__init__(title, author, year)
        # Private attribute menggunakan double underscore
        self.__isbn = isbn
        # Protected attributes
        self._pages = pages
        self._genre = genre
    
    @property
    def isbn(self) -> str:
        """Getter untuk ISBN (read-only property)."""
        return self.__isbn
    
    @property
    def pages(self) -> int:
        """Getter untuk jumlah halaman."""
        return self._pages
    
    @property
    def genre(self) -> str:
        """Getter untuk genre."""
        return self._genre
    
    def get_item_type(self) -> str:
        """
        Implementasi abstract method dari LibraryItem.
        Mengembalikan tipe item sebagai "Book".
        
        Returns:
            str: "Book"
        """
        return "Book"
    
    def get_details(self) -> dict:
        """
        Implementasi abstract method dari LibraryItem.
        Mengembalikan detail lengkap buku.
        
        Returns:
            dict: Dictionary berisi detail buku
        """
        return {
            "id": self._id,
            "type": self.get_item_type(),
            "title": self._title,
            "author": self._author,
            "year": self._year,
            "isbn": self.__isbn,
            "pages": self._pages,
            "genre": self._genre,
            "available": self._is_available,
            "date_added": self._date_added.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def display_info(self) -> str:
        """
        Implementasi abstract method dari LibraryItem.
        Mengembalikan string informasi buku untuk ditampilkan.
        
        Returns:
            str: String informasi buku
        """
        status = "✓ Tersedia" if self._is_available else "✗ Dipinjam"
        info = f"""
╔═══════════════════════════════════════════════════════════╗
║                        INFORMASI BUKU                      ║
╠═══════════════════════════════════════════════════════════╣
║ ID          : {self._id:<45} ║
║ Judul       : {self._title:<45} ║
║ Penulis     : {self._author:<45} ║
║ Tahun       : {self._year:<45} ║
║ ISBN        : {self.__isbn:<45} ║
║ Halaman     : {self._pages:<45} ║
║ Genre       : {self._genre:<45} ║
║ Status      : {status:<45} ║
╚═══════════════════════════════════════════════════════════╝
        """
        return info.strip()
    
    def __str__(self) -> str:
        """String representation dari Book."""
        return f"[BUKU] {super().__str__()} | ISBN: {self.__isbn} | {self._pages} halaman"

