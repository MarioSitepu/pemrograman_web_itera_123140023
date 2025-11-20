"""
Modul untuk class Magazine yang mewarisi dari LibraryItem.
Mengimplementasikan konsep Inheritance dan Polymorphism.
"""

from library_item import LibraryItem
from typing import Optional


class Magazine(LibraryItem):
    """
    Class Magazine yang mewarisi dari LibraryItem.
    Merepresentasikan majalah di perpustakaan.
    
    Attributes:
        _issue_number (str): Nomor edisi majalah (protected)
        _publisher (str): Penerbit majalah (protected)
        _frequency (str): Frekuensi terbit (protected)
    """
    
    def __init__(self, title: str, author: str, year: int, 
                 issue_number: str, publisher: str, frequency: str = "Bulanan"):
        """
        Constructor untuk Magazine.
        
        Args:
            title (str): Judul majalah
            author (str): Editor/penerbit majalah
            year (int): Tahun terbit
            issue_number (str): Nomor edisi
            publisher (str): Penerbit majalah
            frequency (str): Frekuensi terbit (default: "Bulanan")
        """
        super().__init__(title, author, year)
        # Protected attributes
        self._issue_number = issue_number
        self._publisher = publisher
        self._frequency = frequency
    
    @property
    def issue_number(self) -> str:
        """Getter untuk nomor edisi."""
        return self._issue_number
    
    @property
    def publisher(self) -> str:
        """Getter untuk penerbit."""
        return self._publisher
    
    @property
    def frequency(self) -> str:
        """Getter untuk frekuensi terbit."""
        return self._frequency
    
    def get_item_type(self) -> str:
        """
        Implementasi abstract method dari LibraryItem.
        Mengembalikan tipe item sebagai "Magazine".
        
        Returns:
            str: "Magazine"
        """
        return "Magazine"
    
    def get_details(self) -> dict:
        """
        Implementasi abstract method dari LibraryItem.
        Mengembalikan detail lengkap majalah.
        
        Returns:
            dict: Dictionary berisi detail majalah
        """
        return {
            "id": self._id,
            "type": self.get_item_type(),
            "title": self._title,
            "author": self._author,
            "year": self._year,
            "issue_number": self._issue_number,
            "publisher": self._publisher,
            "frequency": self._frequency,
            "available": self._is_available,
            "date_added": self._date_added.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def display_info(self) -> str:
        """
        Implementasi abstract method dari LibraryItem.
        Mengembalikan string informasi majalah untuk ditampilkan.
        
        Returns:
            str: String informasi majalah
        """
        status = "✓ Tersedia" if self._is_available else "✗ Dipinjam"
        info = f"""
╔═══════════════════════════════════════════════════════════╗
║                      INFORMASI MAJALAH                     ║
╠═══════════════════════════════════════════════════════════╣
║ ID          : {self._id:<45} ║
║ Judul       : {self._title:<45} ║
║ Editor      : {self._author:<45} ║
║ Tahun       : {self._year:<45} ║
║ Edisi       : {self._issue_number:<45} ║
║ Penerbit    : {self._publisher:<45} ║
║ Frekuensi   : {self._frequency:<45} ║
║ Status      : {status:<45} ║
╚═══════════════════════════════════════════════════════════╝
        """
        return info.strip()
    
    def __str__(self) -> str:
        """String representation dari Magazine."""
        return f"[MAJALAH] {super().__str__()} | Edisi: {self._issue_number} | {self._publisher}"

