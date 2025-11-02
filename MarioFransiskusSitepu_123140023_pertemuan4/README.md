# Program Pengelolaan Data Nilai Mahasiswa

Program Python untuk mengelola data nilai mahasiswa dengan fitur lengkap yang dibuat untuk memenuhi Tugas Praktikum.

## 📋 Fitur Utama

### Persyaratan Wajib
- ✅ **Data Mahasiswa**: List berisi 6 dictionary data mahasiswa (lebih dari minimal 5)
- ✅ **Perhitungan Nilai Akhir**: Formula (30% UTS + 40% UAS + 30% Tugas)
- ✅ **Sistem Grading**: A (≥80), B (≥70), C (≥60), D (≥50), E (<50)
- ✅ **Tampilan Tabel**: Format tabel yang rapi menggunakan library `tabulate`
- ✅ **Pencarian Extremum**: Mencari mahasiswa dengan nilai tertinggi/terendah

### Fitur Tambahan
- ✅ **Input Data Baru**: Menambah data mahasiswa dengan validasi input
- ✅ **Filter Berdasarkan Grade**: Menyaring mahasiswa berdasarkan grade tertentu
- ✅ **Rata-Rata Kelas**: Menghitung rata-rata nilai seluruh kelas

## 🚀 Cara Menjalankan

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Jalankan Program
```bash
python main.py
```

## 📊 Menu Program

1. **Tampilkan Semua Data Mahasiswa** - Menampilkan semua data dalam format tabel
2. **Tambah Data Mahasiswa Baru** - Menambah data mahasiswa baru dengan validasi
3. **Cari Mahasiswa dengan Nilai Tertinggi** - Menampilkan mahasiswa terbaik
4. **Cari Mahasiswa dengan Nilai Terendah** - Menampilkan mahasiswa dengan nilai terendah
5. **Filter Mahasiswa Berdasarkan Grade** - Menyaring berdasarkan grade A/B/C/D/E
6. **Hitung Rata-Rata Nilai Kelas** - Menghitung statistik kelas
7. **Keluar** - Exit program

## 💡 Implementasi

### Fungsi-Fungsi Utama
- `hitung_nilai_akhir(uts, uas, tugas)` - Menghitung nilai akhir dengan bobot
- `tentukan_grade(nilai_akhir)` - Menentukan grade berdasarkan nilai
- `tampilkan_data_tabel(data)` - Menampilkan data dalam tabel
- `cari_nilai_extremum(data, mode)` - Mencari nilai tertinggi/terendah

### Fitur Tambahan
- `input_data_mahasiswa_baru()` - Input data dengan validasi
- `filter_berdasarkan_grade(data, grade)` - Filtering data
- `hitung_rata_rata_kelas(data)` - Perhitungan statistik

## 📝 Struktur Data

Setiap data mahasiswa disimpan dalam format dictionary:
```python
{
    "nama": "Ahmad Rizki",
    "nim": "121140001",
    "nilai_uts": 85,
    "nilai_uas": 90,
    "nilai_tugas": 88
}
```

## ✅ Kriteria Penilaian

| Aspek | Bobot | Status |
|-------|-------|--------|
| Fungsi-fungsi berjalan dengan benar | 35% | ✅ **LENGKAP** |
| Penggunaan struktur data (list, dict) | 25% | ✅ **LENGKAP** |
| Implementasi input/output yang baik | 20% | ✅ **LENGKAP** |
| Dokumentasi dan kerapian kode | 20% | ✅ **LENGKAP** |

## 👨‍💻 Author

**Mario Fransiskus Sitepu**  
NIM: 123140023  
Program Studi Teknik Informatika ITERA

## 📄 License

Program ini dibuat untuk keperluan pendidikan praktikum Pemrograman Web ITERA.

