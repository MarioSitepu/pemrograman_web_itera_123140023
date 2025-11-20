"""
Program Sistem Manajemen Perpustakaan Sederhana
Menggunakan konsep OOP: Abstract Class, Inheritance, Encapsulation, dan Polymorphism.

Author: Mario Fransiskus Sitepu
NIM: 123140023
"""

from library import Library
from book import Book
from magazine import Magazine
import os


def clear_screen():
    """Fungsi untuk membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Fungsi untuk menampilkan header program."""
    print("="*80)
    print(" "*20 + "SISTEM MANAJEMEN PERPUSTAKAAN SEDERHANA")
    print(" "*25 + "Menggunakan Konsep OOP Python")
    print("="*80)
    print()


def print_menu():
    """Fungsi untuk menampilkan menu utama."""
    print("\n" + "="*80)
    print("MENU UTAMA")
    print("="*80)
    print("1. Tampilkan Semua Item")
    print("2. Tampilkan Item yang Tersedia")
    print("3. Tambah Item Baru")
    print("4. Cari Item berdasarkan ID")
    print("5. Cari Item berdasarkan Judul")
    print("6. Cari Item berdasarkan Penulis/Editor")
    print("7. Pinjam Item")
    print("8. Kembalikan Item")
    print("9. Tampilkan Statistik Perpustakaan")
    print("0. Keluar")
    print("="*80)


def input_book(library: Library):
    """Fungsi untuk input data buku baru."""
    print("\n" + "="*80)
    print("TAMBAH BUKU BARU")
    print("="*80)
    
    try:
        title = input("Judul Buku        : ").strip()
        if not title:
            print("❌ Judul tidak boleh kosong!")
            return
        
        author = input("Penulis           : ").strip()
        if not author:
            print("❌ Penulis tidak boleh kosong!")
            return
        
        year = int(input("Tahun Terbit      : "))
        if year < 0 or year > 2024:
            print("❌ Tahun tidak valid!")
            return
        
        isbn = input("ISBN              : ").strip()
        if not isbn:
            print("❌ ISBN tidak boleh kosong!")
            return
        
        pages = int(input("Jumlah Halaman    : "))
        if pages <= 0:
            print("❌ Jumlah halaman harus lebih dari 0!")
            return
        
        genre = input("Genre (opsional)  : ").strip() or "Umum"
        
        # Buat objek Book
        book = Book(title, author, year, isbn, pages, genre)
        
        # Tambahkan ke library
        if library.add_item(book):
            print(f"\n✅ Buku berhasil ditambahkan dengan ID: {book.id}")
            print(book.display_info())
        else:
            print("❌ Gagal menambahkan buku. Item dengan ID yang sama sudah ada.")
    
    except ValueError:
        print("❌ Input tidak valid! Pastikan tahun dan halaman berupa angka.")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")


def input_magazine(library: Library):
    """Fungsi untuk input data majalah baru."""
    print("\n" + "="*80)
    print("TAMBAH MAJALAH BARU")
    print("="*80)
    
    try:
        title = input("Judul Majalah     : ").strip()
        if not title:
            print("❌ Judul tidak boleh kosong!")
            return
        
        author = input("Editor/Penerbit   : ").strip()
        if not author:
            print("❌ Editor/Penerbit tidak boleh kosong!")
            return
        
        year = int(input("Tahun Terbit      : "))
        if year < 0 or year > 2024:
            print("❌ Tahun tidak valid!")
            return
        
        issue_number = input("Nomor Edisi       : ").strip()
        if not issue_number:
            print("❌ Nomor edisi tidak boleh kosong!")
            return
        
        publisher = input("Penerbit          : ").strip()
        if not publisher:
            print("❌ Penerbit tidak boleh kosong!")
            return
        
        frequency = input("Frekuensi (opsional, default: Bulanan): ").strip() or "Bulanan"
        
        # Buat objek Magazine
        magazine = Magazine(title, author, year, issue_number, publisher, frequency)
        
        # Tambahkan ke library
        if library.add_item(magazine):
            print(f"\n✅ Majalah berhasil ditambahkan dengan ID: {magazine.id}")
            print(magazine.display_info())
        else:
            print("❌ Gagal menambahkan majalah. Item dengan ID yang sama sudah ada.")
    
    except ValueError:
        print("❌ Input tidak valid! Pastikan tahun berupa angka.")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")


def add_item_menu(library: Library):
    """Fungsi untuk menu tambah item."""
    print("\n" + "="*80)
    print("TAMBAH ITEM BARU")
    print("="*80)
    print("1. Tambah Buku")
    print("2. Tambah Majalah")
    print("0. Kembali")
    print("="*80)
    
    choice = input("Pilih jenis item (1/2/0): ").strip()
    
    if choice == "1":
        input_book(library)
    elif choice == "2":
        input_magazine(library)
    elif choice == "0":
        return
    else:
        print("❌ Pilihan tidak valid!")


def search_by_id(library: Library):
    """Fungsi untuk mencari item berdasarkan ID."""
    print("\n" + "="*80)
    print("CARI ITEM BERDASARKAN ID")
    print("="*80)
    
    item_id = input("Masukkan ID item: ").strip()
    if not item_id:
        print("❌ ID tidak boleh kosong!")
        return
    
    item = library.search_by_id(item_id)
    
    if item:
        print("\n✅ Item ditemukan:")
        print(item.display_info())
    else:
        print(f"❌ Item dengan ID '{item_id}' tidak ditemukan.")


def search_by_title(library: Library):
    """Fungsi untuk mencari item berdasarkan judul."""
    print("\n" + "="*80)
    print("CARI ITEM BERDASARKAN JUDUL")
    print("="*80)
    
    title = input("Masukkan judul (atau sebagian): ").strip()
    if not title:
        print("❌ Judul tidak boleh kosong!")
        return
    
    results = library.search_by_title(title)
    
    if results:
        print(f"\n✅ Ditemukan {len(results)} item:")
        print("="*80)
        for item in results:
            print(item.display_info())
            print()
    else:
        print(f"❌ Tidak ada item dengan judul yang mengandung '{title}'.")


def search_by_author(library: Library):
    """Fungsi untuk mencari item berdasarkan penulis."""
    print("\n" + "="*80)
    print("CARI ITEM BERDASARKAN PENULIS/EDITOR")
    print("="*80)
    
    author = input("Masukkan nama penulis/editor (atau sebagian): ").strip()
    if not author:
        print("❌ Nama penulis/editor tidak boleh kosong!")
        return
    
    results = library.search_by_author(author)
    
    if results:
        print(f"\n✅ Ditemukan {len(results)} item:")
        print("="*80)
        for item in results:
            print(item.display_info())
            print()
    else:
        print(f"❌ Tidak ada item dengan penulis/editor yang mengandung '{author}'.")


def borrow_item(library: Library):
    """Fungsi untuk meminjam item."""
    print("\n" + "="*80)
    print("PINJAM ITEM")
    print("="*80)
    
    item_id = input("Masukkan ID item yang ingin dipinjam: ").strip()
    if not item_id:
        print("❌ ID tidak boleh kosong!")
        return
    
    item = library.search_by_id(item_id)
    
    if not item:
        print(f"❌ Item dengan ID '{item_id}' tidak ditemukan.")
        return
    
    if item.borrow():
        print(f"\n✅ Item '{item.title}' berhasil dipinjam!")
        print(item.display_info())
    else:
        print(f"❌ Item '{item.title}' sedang tidak tersedia (sudah dipinjam).")


def return_item(library: Library):
    """Fungsi untuk mengembalikan item."""
    print("\n" + "="*80)
    print("KEMBALIKAN ITEM")
    print("="*80)
    
    item_id = input("Masukkan ID item yang ingin dikembalikan: ").strip()
    if not item_id:
        print("❌ ID tidak boleh kosong!")
        return
    
    item = library.search_by_id(item_id)
    
    if not item:
        print(f"❌ Item dengan ID '{item_id}' tidak ditemukan.")
        return
    
    if item.return_item():
        print(f"\n✅ Item '{item.title}' berhasil dikembalikan!")
        print(item.display_info())
    else:
        print(f"❌ Item '{item.title}' sudah tersedia (belum dipinjam).")


def display_statistics(library: Library):
    """Fungsi untuk menampilkan statistik perpustakaan."""
    print("\n" + "="*80)
    print("STATISTIK PERPUSTAKAAN")
    print("="*80)
    
    stats = library.get_statistics()
    
    print(f"Nama Perpustakaan     : {library.name}")
    print(f"Total Item            : {stats['total_items']}")
    print(f"  - Buku              : {stats['books']}")
    print(f"  - Majalah           : {stats['magazines']}")
    print(f"Item Tersedia         : {stats['available']}")
    print(f"Item Dipinjam         : {stats['borrowed']}")
    print("="*80)


def initialize_sample_data(library: Library):
    """Fungsi untuk menginisialisasi data contoh."""
    # Tambahkan beberapa buku contoh
    book1 = Book("Pemrograman Python untuk Pemula", "John Doe", 2023, 
                 "978-1234567890", 350, "Teknologi")
    book2 = Book("Struktur Data dan Algoritma", "Jane Smith", 2022, 
                 "978-0987654321", 500, "Komputer")
    book3 = Book("Database Management System", "Bob Johnson", 2024, 
                 "978-1122334455", 420, "Teknologi")
    
    # Tambahkan beberapa majalah contoh
    magazine1 = Magazine("Teknologi Informatika", "Tim Editor IT", 2024, 
                        "Vol. 15 No. 3", "PT Media Teknologi", "Bulanan")
    magazine2 = Magazine("Computer Science Today", "Dr. Alice Brown", 2023, 
                        "Issue 2023-12", "CS Publications", "Bulanan")
    
    # Tambahkan ke library
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(book3)
    library.add_item(magazine1)
    library.add_item(magazine2)
    
    # Pinjam satu item sebagai contoh
    book1.borrow()


def main():
    """Fungsi utama program."""
    # Buat objek Library
    library = Library("Perpustakaan ITERA")
    
    # Inisialisasi data contoh
    initialize_sample_data(library)
    
    # Loop utama program
    while True:
        clear_screen()
        print_header()
        print_menu()
        
        choice = input("\nPilih menu (0-9): ").strip()
        
        if choice == "1":
            clear_screen()
            print_header()
            print(library.display_all_items())
            input("\nTekan Enter untuk kembali ke menu...")
        
        elif choice == "2":
            clear_screen()
            print_header()
            print(library.display_available_items())
            input("\nTekan Enter untuk kembali ke menu...")
        
        elif choice == "3":
            clear_screen()
            print_header()
            add_item_menu(library)
            input("\nTekan Enter untuk kembali ke menu...")
        
        elif choice == "4":
            clear_screen()
            print_header()
            search_by_id(library)
            input("\nTekan Enter untuk kembali ke menu...")
        
        elif choice == "5":
            clear_screen()
            print_header()
            search_by_title(library)
            input("\nTekan Enter untuk kembali ke menu...")
        
        elif choice == "6":
            clear_screen()
            print_header()
            search_by_author(library)
            input("\nTekan Enter untuk kembali ke menu...")
        
        elif choice == "7":
            clear_screen()
            print_header()
            borrow_item(library)
            input("\nTekan Enter untuk kembali ke menu...")
        
        elif choice == "8":
            clear_screen()
            print_header()
            return_item(library)
            input("\nTekan Enter untuk kembali ke menu...")
        
        elif choice == "9":
            clear_screen()
            print_header()
            display_statistics(library)
            input("\nTekan Enter untuk kembali ke menu...")
        
        elif choice == "0":
            clear_screen()
            print("\n" + "="*80)
            print("Terima kasih telah menggunakan Sistem Manajemen Perpustakaan!")
            print("="*80 + "\n")
            break
        
        else:
            print("❌ Pilihan tidak valid! Silakan pilih menu 0-9.")
            input("\nTekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()

