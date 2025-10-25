
# Aplikasi Manajemen Tugas Mahasiswa

Aplikasi web berbasis JavaScript yang dirancang khusus untuk membantu mahasiswa mengelola tugas akademik mereka dengan antarmuka futuristik dan animasi yang menarik.

## 🚀 Tentang Aplikasi

Aplikasi ini memungkinkan mahasiswa untuk:
- Menambah, mengedit, dan menghapus tugas akademik
- Menandai tugas sebagai selesai atau belum selesai
- Memfilter dan mencari tugas berdasarkan berbagai kriteria
- Melihat statistik tugas secara real-time
- Menyimpan data secara lokal di browser

Aplikasi menggunakan desain futuristik dengan efek glassmorphism, gradien neon, dan animasi halus untuk memberikan pengalaman pengguna yang modern dan menarik.

## 📸 Screenshot Aplikasi

### 1. Dashboard Utama
![Dashboard](https://assignment-master.page.gd/1.png)  
Tampilan dashboard dengan statistik tugas, form penambahan tugas, dan daftar tugas yang sudah ada.

### 2. Form Penambahan Tugas
![Form Tambah Tugas](https://assignment-master.page.gd/2.png)  
Form interaktif untuk menambah tugas baru dengan validasi real-time dan pesan error yang jelas.

### 3. Fitur Filter dan Pencarian
![Filter dan Pencarian](https://assignment-master.page.gd/3.png)  
Panel filter untuk menyaring tugas berdasarkan status, mata kuliah, dan kata kunci pencarian.

### 4. Modal Edit Tugas
![Edit Tugas](https://assignment-master.page.gd/4.png)  
Modal edit tugas dengan animasi halus dan form yang sudah terisi dengan data tugas yang dipilih.

## 🌐 Demo Online

Anda dapat mencoba aplikasi secara langsung di: [https://assignment-master.page.gd](https://assignment-master.page.gd)

## 💻 Cara Menjalankan Aplikasi

### Langkah 1: Clone Repository
```bash
git clone https://github.com/MarioSitepu/pemrograman_web_itera_123140023.git
cd pemrograman_web_itera_123140023/MarioFransiskusSitepu_123140023_pertemuan1
```

### Langkah 2: Buka di Browser
Cukup buka file `index.html` di browser modern Anda (Chrome, Firefox, Safari, Edge).

#### Untuk pengguna macOS:
```bash
open index.html
```

#### Untuk pengguna Windows:
```bash
start index.html
```

# Atau cukup klik dua kali file `index.html`.

### Langkah 3: Gunakan Aplikasi
Aplikasi siap digunakan tanpa perlu instalasi server atau database tambahan.

---

## ✨ Fitur yang Telah Diimplementasikan

### Fitur Utama
- ✅ **CRUD Lengkap**: Create, Read, Update, Delete tugas
- ✅ **Penyimpanan Lokal**: Data tersimpan di localStorage browser
- ✅ **Validasi Form**: Validasi real-time untuk semua input
- ✅ **Filter & Pencarian**: Filter berdasarkan status dan mata kuliah
- ✅ **Statistik Real-time**: Jumlah total, selesai, dan pending tugas
- ✅ **Desain Responsif**: Berfungsi di desktop dan mobile

### Fitur Tambahan
- ✅ **Animasi Futuristik**: Efek glassmorphism dan gradien neon
- ✅ **Indikator Deadline**: Tandai tugas yang terlambat
- ✅ **Konfirmasi Hapus**: Dialog konfirmasi sebelum menghapus
- ✅ **Feedback Visual**: Pesan sukses dan error yang jelas
- ✅ **Loading Animation**: Spinner saat memuat data
- ✅ **Empty State**: Pesan ketika tidak ada tugas

---

## 🛠 Penjelasan Teknis

### Penggunaan localStorage
Aplikasi menggunakan `localStorage` untuk menyimpan data tugas secara lokal di browser pengguna. Berikut adalah implementasinya:

#### Menyimpan Data
```javascript
function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}
```
- `localStorage.setItem(key, value)`: Menyimpan data dengan format key-value
- `JSON.stringify()`: Mengubah array JavaScript menjadi string JSON

#### Memuat Data
```javascript
function loadTasks() {
    const storedTasks = localStorage.getItem('tasks');
    if (storedTasks) {
        tasks = JSON.parse(storedTasks);
    }
}
```
- `localStorage.getItem(key)`: Mengambil data berdasarkan key
- `JSON.parse()`: Mengubah string JSON kembali menjadi array JavaScript

---

### Validasi Form
Aplikasi mengimplementasikan validasi form yang komprehensif untuk memastikan data yang dimasukkan valid:

#### Validasi Nama Tugas
```javascript
if (!taskName.trim()) {
    document.getElementById('taskNameError').style.display = 'block';
    isValid = false;
}
```
- Memastikan nama tugas tidak kosong
- Menggunakan `trim()` untuk menghapus spasi di awal dan akhir

#### Validasi Mata Kuliah
```javascript
if (!courseName.trim()) {
    document.getElementById('courseNameError').style.display = 'block';
    isValid = false;
}
```
- Memastikan nama mata kuliah tidak kosong

#### Validasi Deadline
```javascript
if (!taskDeadline) {
    document.getElementById('taskDeadlineError').style.display = 'block';
    isValid = false;
}
```
- Memastikan deadline diisi dan memvalidasi format tanggal (YYYY-MM-DD)

#### Fungsi Validasi Lengkap
```javascript
function validateForm(taskName, courseName, taskDeadline, prefix = '') {
    let isValid = true;

    // Reset error messages
    document.getElementById(prefix + 'taskNameError').style.display = 'none';
    document.getElementById(prefix + 'courseNameError').style.display = 'none';
    document.getElementById(prefix + 'taskDeadlineError').style.display = 'none';

    // Validate task name
    if (!taskName.trim()) {
        document.getElementById(prefix + 'taskNameError').style.display = 'block';
        isValid = false;
    }

    // Validate course name
    if (!courseName.trim()) {
        document.getElementById(prefix + 'courseNameError').style.display = 'block';
        isValid = false;
    }

    // Validate deadline
    if (!taskDeadline) {
        document.getElementById(prefix + 'taskDeadlineError').style.display = 'block';
        isValid = false;
    }

    return isValid;
}
```

### Teknik Validasi Tambahan
- **Real-time Validation**: Validasi terjadi saat form disubmit
- **Visual Feedback**: Pesan error muncul dengan animasi shake
- **Form Reset**: Form dikosongkan setelah berhasil menambah tugas
- **Modal Validation**: Form edit memiliki validasi yang sama

---

## 🎨 Teknologi yang Digunakan
- **HTML5**: Struktur halaman web
- **CSS3**: Styling dengan animasi dan efek modern
- **Vanilla JavaScript**: Logika aplikasi tanpa framework
- **Font Awesome**: Ikon untuk UI
- **Google Fonts**: Font Orbitron dan Exo 2 untuk tampilan futuristik
- **localStorage**: Penyimpanan data lokal

## 📱 Kompatibilitas Browser
Aplikasi kompatibel dengan browser modern:
- **Chrome** (versi 60+)
- **Firefox** (versi 55+)
- **Safari** (versi 12+)
- **Edge** (versi 79+)

---

## 🤝 Kontribusi
Kontribusi sangat diterima! Jika Anda ingin meningkatkan aplikasi ini:

1. Fork repository
2. Buat branch fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan Anda (`git commit -am 'Tambah fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## 📄 Lisensi
Proyek ini dilisensikan di bawah **MIT License** - lihat file LICENSE untuk detailnya.

## 👤 Author
Dibuat dengan ❤️ oleh **Mario Fransiskus Sitepu**

Jika Anda memiliki pertanyaan atau menemukan bug, silakan buka issue di repository ini.
