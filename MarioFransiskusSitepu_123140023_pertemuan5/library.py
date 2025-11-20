"""
Modul untuk class Library yang mengelola koleksi item perpustakaan.
Mengimplementasikan konsep Encapsulation dengan access modifiers.
"""

from library_item import LibraryItem
from typing import List, Optional, Dict
from tabulate import tabulate


class Library:
    """
    Class Library untuk menyimpan dan mengelola koleksi item perpustakaan.
    Menggunakan encapsulation untuk melindungi data internal.
    
    Attributes:
        __items (List[LibraryItem]): List item perpustakaan (private)
        __name (str): Nama perpustakaan (private)
    """
    
    def __init__(self, name: str = "Perpustakaan ITERA"):
        """
        Constructor untuk Library.
        
        Args:
            name (str): Nama perpustakaan (default: "Perpustakaan ITERA")
        """
        # Private attributes menggunakan double underscore
        self.__items: List[LibraryItem] = []
        self.__name = name
    
    @property
    def name(self) -> str:
        """Getter untuk nama perpustakaan."""
        return self.__name
    
    @property
    def total_items(self) -> int:
        """Property untuk mendapatkan total jumlah item."""
        return len(self.__items)
    
    @property
    def available_items_count(self) -> int:
        """Property untuk mendapatkan jumlah item yang tersedia."""
        return sum(1 for item in self.__items if item.is_available)
    
    def add_item(self, item: LibraryItem) -> bool:
        """
        Method untuk menambahkan item ke perpustakaan.
        
        Args:
            item (LibraryItem): Item yang akan ditambahkan
            
        Returns:
            bool: True jika berhasil ditambahkan, False jika item sudah ada
        """
        # Cek apakah item dengan ID yang sama sudah ada
        if any(existing_item.id == item.id for existing_item in self.__items):
            return False
        
        self.__items.append(item)
        return True
    
    def remove_item(self, item_id: str) -> bool:
        """
        Method untuk menghapus item dari perpustakaan.
        
        Args:
            item_id (str): ID item yang akan dihapus
            
        Returns:
            bool: True jika berhasil dihapus, False jika tidak ditemukan
        """
        for i, item in enumerate(self.__items):
            if item.id == item_id:
                self.__items.pop(i)
                return True
        return False
    
    def get_all_items(self) -> List[LibraryItem]:
        """
        Method untuk mendapatkan semua item (read-only access).
        
        Returns:
            List[LibraryItem]: List semua item
        """
        return self.__items.copy()  # Return copy untuk encapsulation
    
    def search_by_id(self, item_id: str) -> Optional[LibraryItem]:
        """
        Method untuk mencari item berdasarkan ID.
        
        Args:
            item_id (str): ID item yang dicari
            
        Returns:
            Optional[LibraryItem]: Item jika ditemukan, None jika tidak
        """
        for item in self.__items:
            if item.id.upper() == item_id.upper():
                return item
        return None
    
    def search_by_title(self, title: str) -> List[LibraryItem]:
        """
        Method untuk mencari item berdasarkan judul (case-insensitive).
        
        Args:
            title (str): Judul yang dicari
            
        Returns:
            List[LibraryItem]: List item yang cocok dengan judul
        """
        title_lower = title.lower().strip()
        return [
            item for item in self.__items 
            if title_lower in item.title.lower()
        ]
    
    def search_by_author(self, author: str) -> List[LibraryItem]:
        """
        Method untuk mencari item berdasarkan penulis/author.
        
        Args:
            author (str): Nama penulis yang dicari
            
        Returns:
            List[LibraryItem]: List item yang cocok dengan penulis
        """
        author_lower = author.lower().strip()
        return [
            item for item in self.__items 
            if author_lower in item.author.lower()
        ]
    
    def display_all_items(self) -> str:
        """
        Method untuk menampilkan semua item dalam format tabel.
        
        Returns:
            str: String tabel berisi semua item
        """
        if not self.__items:
            return "Perpustakaan kosong. Belum ada item yang ditambahkan."
        
        # Siapkan data untuk tabel
        table_data = []
        for item in self.__items:
            status = "Tersedia" if item.is_available else "Dipinjam"
            table_data.append([
                item.id,
                item.get_item_type(),
                item.title,
                item.author,
                item.year,
                status
            ])
        
        headers = ["ID", "Tipe", "Judul", "Penulis/Editor", "Tahun", "Status"]
        table = tabulate(table_data, headers=headers, tablefmt="grid", stralign="left")
        
        return f"\n{'='*80}\n{self.__name}\n{'='*80}\n{table}\n{'='*80}\n"
    
    def display_available_items(self) -> str:
        """
        Method untuk menampilkan hanya item yang tersedia.
        
        Returns:
            str: String tabel berisi item yang tersedia
        """
        available = [item for item in self.__items if item.is_available]
        
        if not available:
            return "Tidak ada item yang tersedia saat ini."
        
        table_data = []
        for item in available:
            table_data.append([
                item.id,
                item.get_item_type(),
                item.title,
                item.author,
                item.year
            ])
        
        headers = ["ID", "Tipe", "Judul", "Penulis/Editor", "Tahun"]
        table = tabulate(table_data, headers=headers, tablefmt="grid", stralign="left")
        
        return f"\n{'='*80}\nItem Tersedia di {self.__name}\n{'='*80}\n{table}\n{'='*80}\n"
    
    def get_statistics(self) -> Dict[str, int]:
        """
        Method untuk mendapatkan statistik perpustakaan.
        
        Returns:
            Dict[str, int]: Dictionary berisi statistik
        """
        books = sum(1 for item in self.__items if item.get_item_type() == "Book")
        magazines = sum(1 for item in self.__items if item.get_item_type() == "Magazine")
        
        return {
            "total_items": len(self.__items),
            "books": books,
            "magazines": magazines,
            "available": self.available_items_count,
            "borrowed": len(self.__items) - self.available_items_count
        }
    
    def __str__(self) -> str:
        """String representation dari Library."""
        return f"{self.__name} - {len(self.__items)} item"
    
    def __repr__(self) -> str:
        """Representation untuk debugging."""
        return f"Library(name={self.__name}, items={len(self.__items)})"

