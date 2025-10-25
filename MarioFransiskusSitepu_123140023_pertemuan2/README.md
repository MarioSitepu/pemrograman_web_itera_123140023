# Aplikasi Manajemen Tugas Mahasiswa

Aplikasi web berbasis JavaScript yang dirancang khusus untuk membantu mahasiswa mengelola tugas akademik mereka dengan antarmuka futuristik dan animasi yang menarik.

## 🚀 Tentang Aplikasi

Aplikasi ini memungkinkan mahasiswa untuk:

* Menambah, mengedit, dan menghapus tugas akademik
* Menandai tugas sebagai selesai atau belum selesai
* Memfilter dan mencari tugas berdasarkan berbagai kriteria
* Melihat statistik tugas secara real-time
* Menyimpan data secara lokal di browser

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
cd pemrograman_web_itera_123140023/MarioFransiskusSitepu_123140023_pertemuan2
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

* ✅ **CRUD Lengkap**: Create, Read, Update, Delete tugas
* ✅ **Penyimpanan Lokal**: Data tersimpan di localStorage browser
* ✅ **Validasi Form**: Validasi real-time untuk semua input
* ✅ **Filter & Pencarian**: Filter berdasarkan status dan mata kuliah
* ✅ **Statistik Real-time**: Jumlah total, selesai, dan pending tugas
* ✅ **Desain Responsif**: Berfungsi di desktop dan mobile

### Fitur Tambahan

* ✅ **Animasi Futuristik**: Efek glassmorphism dan gradien neon
* ✅ **Indikator Deadline**: Tandai tugas yang terlambat
* ✅ **Konfirmasi Hapus**: Dialog konfirmasi sebelum menghapus
* ✅ **Feedback Visual**: Pesan sukses dan error yang jelas
* ✅ **Loading Animation**: Spinner saat memuat data
* ✅ **Empty State**: Pesan ketika tidak ada tugas

---

## 🔄 Perubahan pada Versi Terbaru

### Peningkatan Arsitektur Kode

* **Pendekatan Berbasis Class**: Mengimplementasikan `class TaskManager` untuk mengelola seluruh state dan logika terkait tugas.
* **Enkapsulasi State**: Seluruh data dan fungsi terkait tugas berada dalam satu class terpusat.
* **Global Scope yang Bersih**: Hanya satu objek global yang diekspos, yaitu `taskManager`.

### Penerapan Fitur ES6+ yang Lebih Baik

* **Arrow Functions Konsisten**: Seluruh metode menggunakan arrow function agar konteks `this` terjaga.
* **Async/Await**: Operasi I/O (mis. loading/penyimpanan) disusun dengan `async/await` untuk alur yang lebih jelas.
* **Template Literals**: Rendering UI dinamis menggunakan template literals untuk kode yang lebih ringkas dan mudah dibaca.
* **`const` dan `let`**: Deklarasi variabel lebih aman dan sesuai konteks mutabilitas.

### Manfaat dari Perubahan

* **Kode Lebih Terstruktur**: OOP memudahkan navigasi dan kolaborasi kode.
* **Lebih Mudah Dikelola**: Pemisahan logika bisnis dari UI menyederhanakan pemeliharaan.
* **Scalable**: Arsitektur siap ekspansi fitur di masa mendatang.
* **Performa Lebih Baik**: Enkapsulasi membantu efisiensi memori dan pembaruan UI.

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

* `localStorage.setItem(key, value)`: Menyimpan data dengan format key-value
* `JSON.stringify()`: Mengubah array JavaScript menjadi string JSON

#### Memuat Data

```javascript
function loadTasks() {
    const storedTasks = localStorage.getItem('tasks');
    if (storedTasks) {
        tasks = JSON.parse(storedTasks);
    }
}
```

* `localStorage.getItem(key)`: Mengambil data berdasarkan key
* `JSON.parse()`: Mengubah string JSON kembali menjadi array JavaScript

### Validasi Form

Aplikasi mengimplementasikan validasi form yang komprehensif untuk memastikan data yang dimasukkan valid:

#### Validasi Nama Tugas

```javascript
if (!taskName.trim()) {
    document.getElementById('taskNameError').style.display = 'block';
    isValid = false;
}
```

* Memastikan nama tugas tidak kosong
* Menggunakan `trim()` untuk menghapus spasi di awal dan akhir

#### Validasi Mata Kuliah

```javascript
if (!courseName.trim()) {
    document.getElementById('courseNameError').style.display = 'block';
    isValid = false;
}
```

* Memastikan nama mata kuliah tidak kosong

#### Validasi Deadline

```javascript
if (!taskDeadline) {
    document.getElementById('taskDeadlineError').style.display = 'block';
    isValid = false;
}
```

* Memastikan deadline diisi dan memvalidasi format tanggal (YYYY-MM-DD)

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

### Implementasi Class `TaskManager`

Aplikasi memusatkan state dan logika di dalam satu class:

```javascript
class TaskManager {
    constructor() {
        this.tasks = [];
        this.currentEditId = null;
        this.init();
    }

    // Inisialisasi aplikasi
    init = () => {
        this.loadTasks();
        this.setupEventListeners();
        this.updateStats();
    }

    // ... metode lain seperti renderTasks, addTask, deleteTask, dll.
}
```

### Async/Await untuk Operasi Penyimpanan & Pemuatan

Simulasi operasi asinkron untuk menjaga UX tetap responsif:

```javascript
saveTasks = async () => {
    this.showLoading();
    await new Promise(resolve => setTimeout(resolve, 500)); // Simulasi async operation
    localStorage.setItem('tasks', JSON.stringify(this.tasks));
    this.updateCourseFilter();
    this.renderTasks();
    this.updateStats();
    this.hideLoading();
}

loadTasks = async () => {
    this.showLoading();
    await new Promise(resolve => setTimeout(resolve, 500)); // Simulasi async operation
    const storedTasks = localStorage.getItem('tasks');
    if (storedTasks) {
        this.tasks = JSON.parse(storedTasks);
        this.updateCourseFilter();
        this.renderTasks();
        this.updateStats();
    }
    this.hideLoading();
}
```

### Template Literals untuk Rendering Dinamis

Contoh penggunaan template literals pada elemen tugas:

```javascript
taskElement.innerHTML = `
    <div style="display: flex; align-items: center;">
        <input type="checkbox" class="task-checkbox" ${task.completed ? 'checked' : ''}
            onchange="taskManager.toggleTaskCompletion('${task.id}')">
        <div class="task-info">
            <h3>${task.name} ${overdue ? '<span style="color: var(--accent-color);">(TERLAMBAT)</span>' : ''}</h3>
            <p><i class="fas fa-book"></i> ${task.course}</p>
            <p><i class="fas fa-calendar"></i> ${this.formatDate(task.deadline)}</p>
        </div>
    </div>
    <div class="task-actions">
        <button class="btn btn-sm btn-warning" onclick="taskManager.openEditModal('${task.id}')">
            <i class="fas fa-edit"></i>
        </button>
        <button class="btn btn-sm btn-danger" onclick="taskManager.deleteTask('${task.id}')">
            <i class="fas fa-trash"></i>
        </button>
    </div>
`;
```

---

## 🧩 Daftar Fitur ES6+ yang Diimplementasikan

* **let & const** untuk deklarasi variabel sesuai mutabilitas.
* **Arrow functions**: contoh `init = () => {}`, `saveTasks = async () => {}`, `loadTasks = async () => {}`, `validateForm = (...) => {}`.
* **Template literals** untuk rendering dinamis elemen tugas.
* **Async/Await** pada operasi penyimpanan & pemuatan data.
* **Class** `TaskManager` untuk enkapsulasi state & logika.

**Cuplikan singkat:**

```javascript
const STORAGE_KEY = 'tasks';
let tasks = []; // akan dimutasi (tambah/hapus)

class TaskManager {
  constructor() {
    this.tasks = [];
  }
  init = () => {
    const form = document.getElementById('taskForm');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      // ...
    });
  }
}
```

---

## 🎨 Teknologi yang Digunakan

* **HTML5**: Struktur halaman web
* **CSS3**: Styling dengan animasi dan efek modern
* **Vanilla JavaScript**: Logika aplikasi tanpa framework
* **Font Awesome**: Ikon untuk UI
* **Google Fonts**: Font Orbitron dan Exo 2 untuk tampilan futuristik
* **localStorage**: Penyimpanan data lokal

## 📱 Kompatibilitas Browser

Aplikasi kompatibel dengan browser modern:

* **Chrome** (versi 60+)
* **Firefox** (versi 55+)
* **Safari** (versi 12+)
* **Edge** (versi 79+)

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
