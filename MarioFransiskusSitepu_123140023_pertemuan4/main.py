# -*- coding: utf-8 -*-
"""
Program Pengelolaan Data Nilai Mahasiswa
Dibuat untuk memenuhi Tugas Praktikum dengan fitur lengkap dan desain terbaik.
"""

# Mengimpor library yang dibutuhkan untuk menampilkan tabel
from tabulate import tabulate

# --- DATA AWAL MAHASISWA ---
# List berisi dictionary data mahasiswa, sesuai persyaratan.
data_mahasiswa = [
    {
        "nama": "Ahmad Rizki",
        "nim": "121140001",
        "nilai_uts": 85,
        "nilai_uas": 90,
        "nilai_tugas": 88
    },
    {
        "nama": "Siti Nurhaliza",
        "nim": "121140002",
        "nilai_uts": 78,
        "nilai_uas": 82,
        "nilai_tugas": 80
    },
    {
        "nama": "Budi Santoso",
        "nim": "121140003",
        "nilai_uts": 65,
        "nilai_uas": 70,
        "nilai_tugas": 68
    },
    {
        "nama": "Dewi Lestari",
        "nim": "121140004",
        "nilai_uts": 92,
        "nilai_uas": 95,
        "nilai_tugas": 90
    },
    {
        "nama": "Eko Prasetyo",
        "nim": "121140005",
        "nilai_uts": 50,
        "nilai_uas": 55,
        "nilai_tugas": 52
    },
    {
        "nama": "Fitri Handayani",
        "nim": "121140006",
        "nilai_uts": 75,
        "nilai_uas": 72,
        "nilai_tugas": 78
    }
]

# --- FUNGSI-FUNGSI INTI ---

def hitung_nilai_akhir(nilai_uts, nilai_uas, nilai_tugas):
    """
    Menghitung nilai akhir mahasiswa berdasarkan bobot.
    Rumus: (30% UTS) + (40% UAS) + (30% Tugas)

    Args:
        nilai_uts (float/int): Nilai UTS mahasiswa.
        nilai_uas (float/int): Nilai UAS mahasiswa.
        nilai_tugas (float/int): Nilai Tugas mahasiswa.

    Returns:
        float: Nilai akhir yang telah dihitung.
    """
    return (0.30 * nilai_uts) + (0.40 * nilai_uas) + (0.30 * nilai_tugas)

def tentukan_grade(nilai_akhir):
    """
    Menentukan grade berdasarkan nilai akhir.

    Args:
        nilai_akhir (float/int): Nilai akhir mahasiswa.

    Returns:
        str: Grade (A, B, C, D, atau E).
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"

def tampilkan_data_tabel(data):
    """
    Menampilkan data mahasiswa dalam format tabel yang rapi.
    Termasuk perhitungan nilai akhir dan grade untuk setiap mahasiswa.

    Args:
        data (list): List berisi dictionary data mahasiswa.
    """
    if not data:
        print("\n--- Tidak ada data mahasiswa yang dapat ditampilkan. ---")
        return

    # Header untuk tabel
    headers = ["No", "Nama", "NIM", "Nilai UTS", "Nilai UAS", "Nilai Tugas", "Nilai Akhir", "Grade"]
    
    # List untuk menyimpan baris data tabel
    table_data = []
    
    # Mengisi data tabel
    for i, mhs in enumerate(data, 1):
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        
        # Memformat nilai akhir menjadi 2 angka di belakang koma
        row = [
            i,
            mhs['nama'],
            mhs['nim'],
            mhs['nilai_uts'],
            mhs['nilai_uas'],
            mhs['nilai_tugas'],
            f"{nilai_akhir:.2f}",
            grade
        ]
        table_data.append(row)
        
    # Menampilkan tabel menggunakan library tabulate
    print("\n--- Data Nilai Mahasiswa ---")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def cari_nilai_extremum(data, mode='tertinggi'):
    """
    Mencari mahasiswa dengan nilai tertinggi atau terendah.

    Args:
        data (list): List berisi dictionary data mahasiswa.
        mode (str): 'tertinggi' untuk mencari nilai maksimum, 'terendah' untuk minimum.

    Returns:
        dict: Dictionary data mahasiswa dengan nilai ekstrem, atau None jika data kosong.
    """
    if not data:
        return None

    # Menggunakan fungsi max/min dengan key untuk menemukan mahasiswa
    # berdasarkan nilai akhir yang dihitung secara dinamis.
    if mode == 'tertinggi':
        mahasiswa_extremum = max(data, key=lambda m: hitung_nilai_akhir(m['nilai_uts'], m['nilai_uas'], m['nilai_tugas']))
    else: # mode == 'terendah'
        mahasiswa_extremum = min(data, key=lambda m: hitung_nilai_akhir(m['nilai_uts'], m['nilai_uas'], m['nilai_tugas']))
        
    return mahasiswa_extremum

# --- FUNGSI FITUR TAMBAHAN ---

def input_data_mahasiswa_baru():
    """
    Meminta input dari pengguna untuk menambahkan data mahasiswa baru.
    Melakukan validasi input untuk memastikan data berupa angka.
    """
    print("\n--- Tambah Data Mahasiswa Baru ---")
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    
    # Loop untuk validasi input nilai UTS
    while True:
        try:
            nilai_uts = float(input("Masukkan Nilai UTS: "))
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka untuk nilai.")
            
    # Loop untuk validasi input nilai UAS
    while True:
        try:
            nilai_uas = float(input("Masukkan Nilai UAS: "))
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka untuk nilai.")
            
    # Loop untuk validasi input nilai Tugas
    while True:
        try:
            nilai_tugas = float(input("Masukkan Nilai Tugas: "))
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka untuk nilai.")

    # Membuat dictionary baru dan menambahkannya ke list utama
    mahasiswa_baru = {
        "nama": nama,
        "nim": nim,
        "nilai_uts": nilai_uts,
        "nilai_uas": nilai_uas,
        "nilai_tugas": nilai_tugas
    }
    data_mahasiswa.append(mahasiswa_baru)
    print(f"\nData mahasiswa atas nama {nama} berhasil ditambahkan!")

def filter_berdasarkan_grade(data, grade_target):
    """
    Menyaring dan menampilkan mahasiswa berdasarkan grade tertentu.

    Args:
        data (list): List berisi dictionary data mahasiswa.
        grade_target (str): Grade yang ingin disaring (A, B, C, D, E).
    """
    # List comprehension untuk membuat list baru yang sudah disaring
    data_terfilter = [
        mhs for mhs in data 
        if tentukan_grade(hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])) == grade_target.upper()
    ]
    
    print(f"\n--- Data Mahasiswa dengan Grade '{grade_target.upper()}' ---")
    if not data_terfilter:
        print(f"Tidak ada mahasiswa dengan grade '{grade_target.upper()}'.")
    else:
        tampilkan_data_tabel(data_terfilter)

def hitung_rata_rata_kelas(data):
    """
    Menghitung dan menampilkan rata-rata nilai akhir seluruh kelas.

    Args:
        data (list): List berisi dictionary data mahasiswa.
    """
    if not data:
        print("\n--- Tidak dapat menghitung rata-rata, data mahasiswa kosong. ---")
        return
        
    total_nilai = 0
    for mhs in data:
        total_nilai += hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        
    rata_rata = total_nilai / len(data)
    print(f"\n--- Rata-Rata Nilai Kelas ---")
    print(f"Rata-rata nilai akhir dari {len(data)} mahasiswa adalah: {rata_rata:.2f}")

# --- PROGRAM UTAMA ---

def main():
    """
    Fungsi utama yang menjalankan menu program.
    """
    while True:
        print("\n" + "="*40)
        print("   MENU PROGRAM PENGELOLAAN NILAI MAHASISWA")
        print("="*40)
        print("1. Tampilkan Semua Data Mahasiswa")
        print("2. Tambah Data Mahasiswa Baru")
        print("3. Cari Mahasiswa dengan Nilai Tertinggi")
        print("4. Cari Mahasiswa dengan Nilai Terendah")
        print("5. Filter Mahasiswa Berdasarkan Grade")
        print("6. Hitung Rata-Rata Nilai Kelas")
        print("7. Keluar")
        print("="*40)

        pilihan = input("Masukkan pilihan menu (1-7): ")

        if pilihan == '1':
            tampilkan_data_tabel(data_mahasiswa)
        elif pilihan == '2':
            input_data_mahasiswa_baru()
        elif pilihan == '3':
            mhs_terbaik = cari_nilai_extremum(data_mahasiswa, 'tertinggi')
            if mhs_terbaik:
                print("\n--- Mahasiswa dengan Nilai Tertinggi ---")
                tampilkan_data_tabel([mhs_terbaik])
            else:
                print("\nData mahasiswa kosong.")
        elif pilihan == '4':
            mhs_terendah = cari_nilai_extremum(data_mahasiswa, 'terendah')
            if mhs_terendah:
                print("\n--- Mahasiswa dengan Nilai Terendah ---")
                tampilkan_data_tabel([mhs_terendah])
            else:
                print("\nData mahasiswa kosong.")
        elif pilihan == '5':
            grade_filter = input("Masukkan grade yang ingin dicari (A/B/C/D/E): ")
            if grade_filter.upper() in ['A', 'B', 'C', 'D', 'E']:
                filter_berdasarkan_grade(data_mahasiswa, grade_filter)
            else:
                print("Grade yang dimasukkan tidak valid!")
        elif pilihan == '6':
            hitung_rata_rata_kelas(data_mahasiswa)
        elif pilihan == '7':
            print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("\nPilihan tidak valid. Silakan masukkan angka antara 1 hingga 7.")
        
        # Jeda agar user dapat membaca output sebelum menu muncul kembali
        input("\nTekan Enter untuk kembali ke menu utama...")

# Menjalankan program utama jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()