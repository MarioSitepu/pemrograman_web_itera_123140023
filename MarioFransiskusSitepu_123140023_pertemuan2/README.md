Aplikasi Manajemen Tugas Mahasiswa V2
=====================================

Aplikasi web berbasis JavaScript yang dirancang khusus untuk membantu mahasiswa mengelola tugas akademik mereka dengan antarmuka futuristik dan animasi yang menarik.

TENTANG APLIKASI
-----------------

Aplikasi ini memungkinkan mahasiswa untuk:
- Menambah, mengedit, dan menghapus tugas akademik
- Menandai tugas sebagai selesai atau belum selesai
- Memfilter dan mencari tugas berdasarkan berbagai kriteria
- Melihat statistik tugas secara real-time
- Menyimpan data secara lokal di browser

Aplikasi menggunakan desain futuristik dengan efek glassmorphism, gradien neon, dan animasi halus untuk memberikan pengalaman pengguna yang modern dan menarik.

SCREENSHOT APLIKASI
-------------------

1. Dashboard Utama
   Tampilan dashboard dengan statistik tugas, form penambahan tugas, dan daftar tugas yang sudah ada.
   Lihat: https://assignment-master.page.gd/1.png

2. Form Penambahan Tugas
   Form interaktif untuk menambah tugas baru dengan validasi real-time dan pesan error yang jelas.
   Lihat: https://assignment-master.page.gd/2.png

3. Fitur Filter dan Pencarian
   Panel filter untuk menyaring tugas berdasarkan status, mata kuliah, dan kata kunci pencarian.
   Lihat: https://assignment-master.page.gd/3.png

4. Modal Edit Tugas
   Modal edit tugas dengan animasi halus dan form yang sudah terisi dengan data tugas yang dipilih.
   Lihat: https://assignment-master.page.gd/4.png

DEMO ONLINE
-----------

Anda dapat mencoba aplikasi secara langsung di: https://assignment-master.page.gd

CARA MENJALANKAN APLIKASI
--------------------------

Langkah 1: Clone Repository
  git clone https://github.com/username/aplikasi-manajemen-tugas.git
  cd pemrograman_web_itera_123140023

Langkah 2: Buka di Browser
  Cukup buka file index.html di browser modern Anda (Chrome, Firefox, Safari, Edge).

  Untuk pengguna macOS:
    open index.html

  Untuk pengguna Windows:
    start index.html

  Atau cukup klik dua kali file index.html.

Langkah 3: Gunakan Aplikasi
  Aplikasi siap digunakan tanpa perlu instalasi server atau database tambahan.

FITUR YANG TELAH DITERAPKAN
----------------------------

Fitur Utama:
- CRUD Lengkap: Create, Read, Update, Delete tugas
- Penyimpanan Lokal: Data tersimpan di localStorage browser
- Validasi Form: Validasi real-time untuk semua input
- Filter & Pencarian: Filter berdasarkan status dan mata kuliah
- Statistik Real-time: Jumlah total, selesai, dan pending tugas
- Desain Responsif: Berfungsi di desktop dan mobile

Fitur Tambahan:
- Animasi Futuristik: Efek glassmorphism dan gradien neon
- Indikator Deadline: Tandai tugas yang terlambat
- Konfirmasi Hapus: Dialog konfirmasi sebelum menghapus
- Feedback Visual: Pesan sukses dan error yang jelas
- Loading Animation: Spinner saat memuat data
- Empty State: Pesan ketika tidak ada tugas

PERUBAHAN PADA VERSI TERBARU
-----------------------------

Peningkatan Arsitektur Kode:
- Pendekatan Berbasis Class: Mengimplementasikan class TaskManager untuk mengelola semua state dan logika terkait tugas
- Enkapsulasi State: Semua data dan fungsi terkait tugas dienkapsulasi dalam satu class
- Global Scope yang Bersih: Hanya satu objek (taskManager) yang diekspos ke global scope

Penerapan Fitur ES6+ yang Lebih Baik:
- Arrow Functions Konsisten: Semua metode menggunakan arrow function untuk mempertahankan konteks this
- Async/Await: Menggunakan async/await untuk operasi asinkron (loading data)
- Template Literals: Rendering dinamis dengan template literals untuk kode yang lebih bersih
- Konstanta dan Let: Penggunaan const dan let yang tepat untuk deklarasi variabel

Manfaat dari Perubahan:
- Kode Lebih Terstruktur: Organisasi kode yang lebih baik dengan pendekatan OOP
- Mudah Dikelola: Logika bisnis terpisah dari UI, memudahkan pemeliharaan
- Scalable: Arsitektur yang memudahkan penambahan fitur baru di masa depan
- Performa Lebih Baik: Pengelolaan memori yang lebih efisien dengan enkapsulasi

PENJELASAN TEKNIS
-----------------

Implementasi Class TaskManager:
  Aplikasi menggunakan class TaskManager untuk mengelola semua fungsi terkait tugas:

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
      
      // Metode lainnya...
  }

Penggunaan localStorage:
  Aplikasi menggunakan localStorage untuk menyimpan data tugas secara lokal di browser pengguna:

  Menyimpan Data:
    saveTasks = async () => {
        this.showLoading();
        await new Promise(resolve => setTimeout(resolve, 500)); // Simulasi async operation
        localStorage.setItem('tasks', JSON.stringify(this.tasks));
        this.updateCourseFilter();
        this.renderTasks();
        this.updateStats();
        this.hideLoading();
    }

  Memuat Data:
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

Validasi Form:
  Aplikasi mengimplementasikan validasi form yang komprehensif untuk memastikan data yang dimasukkan valid:

  validateForm = (taskName, courseName, taskDeadline, prefix = '') => {
      let isValid = true;
      
      // Reset error messages
      document.getElementById(`${prefix}taskNameError`).style.display = 'none';
      document.getElementById(`${prefix}courseNameError`).style.display = 'none';
      document.getElementById(`${prefix}taskDeadlineError`).style.display = 'none';
      
      // Validate task name
      if (!taskName.trim()) {
          document.getElementById(`${prefix}taskNameError`).style.display = 'block';
          isValid = false;
      }
      
      // Validate course name
      if (!courseName.trim()) {
          document.getElementById(`${prefix}courseNameError`).style.display = 'block';
          isValid = false;
      }
      
      // Validate deadline
      if (!taskDeadline) {
          document.getElementById(`${prefix}taskDeadlineError`).style.display = 'block';
          isValid = false;
      }
      
      return isValid;
  }

Template Literals untuk Rendering Dinamis:
  Aplikasi menggunakan template literals untuk rendering dinamis yang lebih bersih:

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

TEKNOLOGI YANG DIGUNAKAN
------------------------

- HTML5: Struktur halaman web
- CSS3: Styling dengan animasi dan efek modern
- Vanilla JavaScript (ES6+): Logika aplikasi dengan fitur-fitur modern
- Font Awesome: Ikon untuk UI
- Google Fonts: Font Orbitron dan Exo 2 untuk tampilan futuristik
- localStorage: Penyimpanan data lokal

KOMPATIBILITAS BROWSER
----------------------

Aplikasi kompatibel dengan browser modern:
- Chrome (versi 60+)
- Firefox (versi 55+)
- Safari (versi 12+)
- Edge (versi 79+)

KONTRIBUSI
----------

Kontribusi sangat diterima! Jika Anda ingin meningkatkan aplikasi ini:

1. Fork repository
2. Buat branch fitur baru (git checkout -b fitur-baru)
3. Commit perubahan Anda (git commit -am 'Tambah fitur baru')
4. Push ke branch (git push origin fitur-baru)
5. Buat Pull Request

LISENSI
-------

Proyek ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detailnya.

AUTHOR
------

Dibuat dengan ❤️ oleh Mario Fransiskus Sitepu

Jika Anda memiliki pertanyaan atau menemukan bug, silakan buka issue di repository ini.