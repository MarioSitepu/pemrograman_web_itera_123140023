# Aplikasi Manajemen Matakuliah dengan Pyramid

Aplikasi API sederhana untuk manajemen matakuliah menggunakan framework Pyramid dan SQLAlchemy. Aplikasi ini menyediakan endpoint REST API untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada data matakuliah.

## 📋 Deskripsi Proyek

Aplikasi ini dibuat untuk memenuhi Tugas Praktikum Pemrograman Web. Aplikasi menyediakan API endpoints untuk mengelola data mata kuliah dengan atribut:
- **ID**: Primary key (auto increment)
- **Kode MK**: Kode mata kuliah (unique, not null)
- **Nama MK**: Nama mata kuliah (not null)
- **SKS**: Jumlah SKS (not null)
- **Semester**: Semester pengambilan (not null)

## 🚀 Cara Instalasi

### 1. Membuat Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalasi Dependencies

Setelah virtual environment aktif, install semua dependencies yang diperlukan:

```bash
pip install -r requirements.txt
```

Atau install secara manual:

```bash
pip install pyramid==2.0.2
pip install pyramid-sqlalchemy==0.1
pip install SQLAlchemy==2.0.23
pip install alembic==1.12.1
pip install waitress==2.1.2
pip install python-dateutil==2.8.2
```

### 3. Konfigurasi Database

Database menggunakan SQLite yang akan dibuat otomatis. Konfigurasi database dapat dilihat di file `development.ini`:

```ini
sqlalchemy.url = sqlite:///matakuliah.db
```

## 🏃 Cara Menjalankan

### 1. Menjalankan Migrasi Database

Pertama, buat migrasi database dengan Alembic:

```bash
# Buat migrasi awal
alembic revision --autogenerate -m "Initial migration"

# Jalankan migrasi
alembic upgrade head
```

Atau gunakan script inisialisasi yang sudah disediakan:

```bash
python initialize_db.py
```

Script ini akan:
- Membuat tabel `matakuliah` di database
- Menambahkan 3 data matakuliah contoh

### 2. Menjalankan Server

Jalankan server dengan perintah:

```bash
python main.py
```

Server akan berjalan di `http://localhost:6543`

Atau menggunakan pserve:

```bash
pserve development.ini --reload
```

## 📡 API Endpoints

### 1. Get All Matakuliah

Mendapatkan semua data matakuliah.

**Request:**
```bash
curl -X GET http://localhost:6543/api/matakuliah
```

**Response:**
```json
{
  "matakuliahs": [
    {
      "id": 1,
      "kode_mk": "IF101",
      "nama_mk": "Algoritma dan Pemrograman",
      "sks": 3,
      "semester": 1
    },
    {
      "id": 2,
      "kode_mk": "IF102",
      "nama_mk": "Struktur Data",
      "sks": 3,
      "semester": 2
    },
    {
      "id": 3,
      "kode_mk": "IF201",
      "nama_mk": "Pemrograman Web",
      "sks": 3,
      "semester": 3
    }
  ]
}
```

### 2. Get Matakuliah by ID

Mendapatkan detail satu matakuliah berdasarkan ID.

**Request:**
```bash
curl -X GET http://localhost:6543/api/matakuliah/1
```

**Response:**
```json
{
  "id": 1,
  "kode_mk": "IF101",
  "nama_mk": "Algoritma dan Pemrograman",
  "sks": 3,
  "semester": 1
}
```

**Error Response (404):**
```json
{
  "error": "Matakuliah tidak ditemukan",
  "message": "Matakuliah dengan ID 999 tidak ditemukan"
}
```

### 3. Create Matakuliah

Menambahkan matakuliah baru.

**Request:**
```bash
curl -X POST http://localhost:6543/api/matakuliah \
  -H "Content-Type: application/json" \
  -d '{
    "kode_mk": "IF301",
    "nama_mk": "Basis Data",
    "sks": 3,
    "semester": 5
  }'
```

**Response (201):**
```json
{
  "id": 4,
  "kode_mk": "IF301",
  "nama_mk": "Basis Data",
  "sks": 3,
  "semester": 5
}
```

**Error Response (400) - Field tidak lengkap:**
```json
{
  "error": "Field tidak lengkap",
  "message": "Field kode_mk harus diisi"
}
```

**Error Response (400) - Kode duplikat:**
```json
{
  "error": "Data duplikat",
  "message": "Kode mata kuliah sudah ada"
}
```

### 4. Update Matakuliah

Mengupdate data matakuliah berdasarkan ID.

**Request:**
```bash
curl -X PUT http://localhost:6543/api/matakuliah/1 \
  -H "Content-Type: application/json" \
  -d '{
    "nama_mk": "Algoritma dan Pemrograman Dasar",
    "sks": 4
  }'
```

**Response:**
```json
{
  "id": 1,
  "kode_mk": "IF101",
  "nama_mk": "Algoritma dan Pemrograman Dasar",
  "sks": 4,
  "semester": 1
}
```

**Error Response (404):**
```json
{
  "error": "Matakuliah tidak ditemukan",
  "message": "Matakuliah dengan ID 999 tidak ditemukan"
}
```

### 5. Delete Matakuliah

Menghapus matakuliah berdasarkan ID.

**Request:**
```bash
curl -X DELETE http://localhost:6543/api/matakuliah/1
```

**Response:**
```json
{
  "message": "Matakuliah berhasil dihapus",
  "id": 1
}
```

**Error Response (404):**
```json
{
  "error": "Matakuliah tidak ditemukan",
  "message": "Matakuliah dengan ID 999 tidak ditemukan"
}
```

## 🧪 Testing

Berikut adalah contoh perintah curl untuk testing semua endpoint:

### 1. Test Get All Matakuliah
```bash
curl -X GET http://localhost:6543/api/matakuliah
```

### 2. Test Get Matakuliah by ID
```bash
curl -X GET http://localhost:6543/api/matakuliah/1
```

### 3. Test Create Matakuliah
```bash
curl -X POST http://localhost:6543/api/matakuliah \
  -H "Content-Type: application/json" \
  -d '{
    "kode_mk": "IF401",
    "nama_mk": "Pemrograman Mobile",
    "sks": 3,
    "semester": 7
  }'
```

### 4. Test Update Matakuliah
```bash
curl -X PUT http://localhost:6543/api/matakuliah/1 \
  -H "Content-Type: application/json" \
  -d '{
    "sks": 4,
    "semester": 2
  }'
```

### 5. Test Delete Matakuliah
```bash
curl -X DELETE http://localhost:6543/api/matakuliah/1
```

### Testing dengan PowerShell (Windows)

Jika menggunakan PowerShell, gunakan format berikut:

```powershell
# Get All
Invoke-RestMethod -Uri "http://localhost:6543/api/matakuliah" -Method Get

# Get by ID
Invoke-RestMethod -Uri "http://localhost:6543/api/matakuliah/1" -Method Get

# Create
$body = @{
    kode_mk = "IF401"
    nama_mk = "Pemrograman Mobile"
    sks = 3
    semester = 7
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:6543/api/matakuliah" -Method Post -Body $body -ContentType "application/json"

# Update
$body = @{
    sks = 4
    semester = 2
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:6543/api/matakuliah/1" -Method Put -Body $body -ContentType "application/json"

# Delete
Invoke-RestMethod -Uri "http://localhost:6543/api/matakuliah/1" -Method Delete
```

## 📁 Struktur Proyek

```
MarioFransiskusSitepu_123140023_pertemuan6/
│
├── __init__.py              # Application factory
├── models.py                # Model data Matakuliah
├── routes.py                # Konfigurasi routes
├── views.py                 # View handlers untuk API endpoints
├── main.py                  # Entry point untuk menjalankan server
├── development.ini          # Konfigurasi aplikasi dan database
├── setup.py                 # Setup file untuk package
├── initialize_db.py         # Script untuk inisialisasi database
├── requirements.txt         # Dependencies Python
├── alembic.ini              # Konfigurasi Alembic
├── README.md                # Dokumentasi proyek
│
└── alembic/                 # Direktori migrasi Alembic
    ├── env.py               # Environment configuration untuk Alembic
    ├── script.py.mako       # Template untuk migration files
    └── versions/            # Direktori untuk migration files
```

## 🔧 Konfigurasi

### Database

Database menggunakan SQLite dengan file `matakuliah.db`. Konfigurasi dapat diubah di file `development.ini`:

```ini
sqlalchemy.url = sqlite:///matakuliah.db
```

Untuk menggunakan database lain (misalnya PostgreSQL), ubah URL database:

```ini
sqlalchemy.url = postgresql://user:password@localhost/dbname
```

### Server

Server berjalan di port 6543 secara default. Untuk mengubah port, edit file `development.ini`:

```ini
[server:main]
port = 8080
```

## 📝 Catatan Penting

1. **Request Method**: Semua route sudah dikonfigurasi dengan `request_method` yang sesuai (GET, POST, PUT, DELETE).

2. **Validasi**: API melakukan validasi pada:
   - Field yang wajib diisi
   - Tipe data yang benar
   - Kode mata kuliah yang unique

3. **Error Handling**: Semua endpoint memiliki error handling yang sesuai dengan HTTP status code:
   - 200: Success
   - 201: Created
   - 400: Bad Request
   - 404: Not Found
   - 500: Internal Server Error

4. **Database Migration**: Gunakan Alembic untuk mengelola perubahan schema database.

## 🐛 Troubleshooting

### Problem: Import Error
**Solution**: Pastikan virtual environment sudah aktif dan semua dependencies sudah terinstall.

### Problem: Database tidak ditemukan
**Solution**: Jalankan `python initialize_db.py` atau `alembic upgrade head` untuk membuat database.

### Problem: Port sudah digunakan
**Solution**: Ubah port di file `development.ini` atau hentikan aplikasi yang menggunakan port 6543.

### Problem: Route tidak ditemukan
**Solution**: Pastikan server sudah di-restart setelah perubahan pada routes atau views.

## 👤 Author

**Mario Fransiskus Sitepu**  
NIM: 123140023

## 📄 License

Proyek ini dibuat untuk keperluan akademik.

