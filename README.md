# 📚 EasyBookApp

Aplikasi Personal Dashboard untuk Manajemen Koleksi Buku yang modern, interaktif, dan mudah digunakan. Aplikasi ini membantu Anda mengelola koleksi buku pribadi dengan fitur CRUD lengkap, penyimpanan lokal, dan antarmuka yang menarik.

## 🎯 Tentang Aplikasi

**EasyBookApp** adalah aplikasi web berbasis React untuk mengelola koleksi buku pribadi. Aplikasi ini memungkinkan pengguna untuk:

- ✅ Menambah buku baru ke koleksi
- ✏️ Mengedit informasi buku yang sudah ada
- 🗑️ Menghapus buku dari koleksi
- 🔍 Mencari buku berdasarkan judul atau penulis
- 🏷️ Memfilter buku berdasarkan status (Dimiliki, Sedang Dibaca, Ingin Dibeli)
- 📊 Melihat statistik koleksi buku
- 💾 Menyimpan data secara lokal di browser menggunakan localStorage

Aplikasi ini dibangun dengan teknologi modern menggunakan React, dan mengimplementasikan berbagai fitur ES6+ untuk kode yang lebih efisien dan mudah dirawat.

---

## ✨ Fitur-Fitur Aplikasi

### Fitur Utama
- **CRUD Lengkap**: Create, Read, Update, Delete untuk manajemen buku
- **Penyimpanan Lokal**: Data tersimpan otomatis di localStorage browser
- **Pencarian Real-time**: Cari buku berdasarkan judul atau nama penulis
- **Filter Status**: Filter buku berdasarkan status (Dimiliki, Sedang Dibaca, Ingin Dibeli)
- **Statistik Dashboard**: Lihat ringkasan koleksi buku di halaman statistik
- **Validasi Form**: Validasi input untuk memastikan data yang dimasukkan valid

### Fitur UI/UX
- **Desain Modern**: Interface dengan efek glassmorphism dan gradient
- **Animasi Halus**: Transitions dan animations yang smooth
- **Responsive Design**: Optimal di desktop, tablet, dan mobile
- **Visual Feedback**: Pesan error dan sukses yang jelas
- **Empty States**: Pesan informatif ketika tidak ada buku
- **Loading States**: Animasi saat memuat data

---

## 📸 Screenshot Aplikasi

### Halaman Utama - Koleksi Buku
![Halaman Utama](screenshots/home.png)
*Halaman utama menampilkan form untuk menambah buku, search bar, filter, dan daftar buku*

### Halaman Statistik
![Halaman Statistik](screenshots/stats.png)
*Dashboard statistik menampilkan ringkasan koleksi buku dengan card yang menarik*

### Form Tambah/Edit Buku
![Form Buku](screenshots/form.png)
*Form dengan layout grid modern dan status selector berbasis card*

---

## 🚀 Cara Menjalankan Aplikasi

### Prasyarat
- Node.js (versi 14 atau lebih tinggi)
- npm atau yarn

### Instalasi

1. **Clone repository atau download project**
```bash
git clone https://github.com/MarioSitepu/pemrograman_web_itera_123140023.git
cd mariofransiskussitepu_123140023_pertemuan3
```

2. **Install dependencies**
```bash
npm install
```

3. **Jalankan aplikasi**
```bash
npm start
```

Aplikasi akan berjalan di [http://localhost:3000](http://localhost:3000)

### Build untuk Production

```bash
npm run build
```

Build files akan tersimpan di folder `build/`

---

## 🚀 Cara Deploy ke Netlify

Aplikasi ini sudah dikonfigurasi untuk deploy ke Netlify dengan mudah. Ada beberapa cara yang bisa digunakan:

### Metode 1: Deploy via Netlify UI (Paling Mudah)

1. **Persiapkan Build**
   ```bash
   npm run build
   ```
   Pastikan folder `build/` berhasil dibuat tanpa error.

2. **Login ke Netlify**
   - Buka [https://app.netlify.com](https://app.netlify.com)
   - Login atau buat akun baru (bisa menggunakan GitHub, GitLab, atau email)

3. **Deploy dengan Drag & Drop**
   - Di dashboard Netlify, klik **"Add new site"** → **"Deploy manually"**
   - Drag & drop folder `build/` ke area yang disediakan
   - Tunggu hingga deploy selesai
   - Netlify akan memberikan URL untuk aplikasi Anda

### Metode 2: Deploy via Netlify CLI

1. **Install Netlify CLI**
   ```bash
   npm install -g netlify-cli
   ```

2. **Login ke Netlify**
   ```bash
   netlify login
   ```

3. **Deploy Aplikasi**
   ```bash
   # Build aplikasi terlebih dahulu
   npm run build
   
   # Deploy ke Netlify
   netlify deploy --prod --dir=build
   ```

   Atau untuk deploy preview pertama kali:
   ```bash
   netlify deploy --dir=build
   ```

### Metode 3: Deploy via Git (Continuous Deployment)

1. **Push Project ke GitHub/GitLab/Bitbucket**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <repository-url>
   git push -u origin main
   ```

2. **Connect Repository ke Netlify**
   - Di dashboard Netlify, klik **"Add new site"** → **"Import an existing project"**
   - Pilih provider Git Anda (GitHub/GitLab/Bitbucket)
   - Authorize dan pilih repository Anda

3. **Konfigurasi Build Settings**
   Netlify akan otomatis mendeteksi konfigurasi dari file `netlify.toml`:
   - **Build command:** `npm run build`
   - **Publish directory:** `build`
   
   Jika tidak terdeteksi otomatis, masukkan manual:
   - Build command: `npm run build`
   - Publish directory: `build`

4. **Deploy**
   - Klik **"Deploy site"**
   - Netlify akan otomatis build dan deploy aplikasi
   - Setiap kali Anda push ke repository, Netlify akan otomatis deploy ulang

### Catatan Penting

- ✅ File `netlify.toml` sudah dikonfigurasi untuk menangani routing React Router (SPA)
- ✅ File `public/_redirects` juga sudah disiapkan sebagai backup untuk routing
- ✅ Setelah deploy, pastikan aplikasi bisa diakses melalui URL yang diberikan Netlify
- ✅ Jika menggunakan routing (seperti `/stats`), pastikan semua route berfungsi dengan benar

### Troubleshooting

**Problem:** Route tidak berfungsi saat diakses langsung (misal `/stats`)
- **Solution:** File `netlify.toml` dan `_redirects` sudah dikonfigurasi untuk menangani ini. Pastikan kedua file sudah ter-push ke repository.

**Problem:** Build gagal
- **Solution:** Pastikan semua dependencies terinstall dengan `npm install` dan tidak ada error saat build lokal.

**Problem:** Aplikasi tidak muncul setelah deploy
- **Solution:** Pastikan publish directory di Netlify diset ke `build`, bukan `public` atau folder lain.

---

## 💻 Fitur ES6+ yang Diimplementasikan

Aplikasi ini mengimplementasikan berbagai fitur modern ES6+ untuk kode yang lebih bersih, efisien, dan mudah dirawat:

### 1. **Let dan Const**
Penggunaan `let` dan `const` secara tepat untuk deklarasi variabel:

```javascript
// src/pages/Home/Home.js
const Home = () => {
  const { books, addBook, deleteBook } = useBook();
  const [filter, setFilter] = useState('semua');
  const [searchTerm, setSearchTerm] = useState('');
  
  let processedBooks = books;
  // ...
}
```

**Lokasi Implementasi:**
- `src/pages/Home/Home.js`
- `src/components/BookForm/BookForm.js`
- `src/components/BookItem/BookItem.js`
- `src/hooks/useLocalStorage.js`
- Dan semua file komponen lainnya

### 2. **Arrow Functions**
Implementasi arrow functions untuk fungsi yang lebih ringkas dan menjaga konteks `this`:

```javascript
// src/components/BookForm/BookForm.js
const BookForm = ({ onSubmit, initialData, onCancel }) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    // ...
  };
  // ...
}

// src/pages/Home/Home.js
const filteredBooks = useMemo(() => {
  let processedBooks = books;
  if (filter !== 'semua') {
    processedBooks = processedBooks.filter((book) => book.status === filter);
  }
  return processedBooks;
}, [books, filter, searchTerm]);
```

**Lokasi Implementasi:**
- `src/pages/Home/Home.js` - Komponen Home sebagai arrow function
- `src/components/BookForm/BookForm.js` - Komponen BookForm
- `src/components/BookList/BookList.js` - Komponen BookList
- `src/components/BookItem/BookItem.js` - Komponen BookItem
- `src/components/SearchBar/SearchBar.js` - Komponen SearchBar
- `src/components/BookFilter/BookFilter.js` - Komponen BookFilter
- `src/pages/Stats/Stats.js` - Komponen Stats
- `src/hooks/useBookStats.js` - Custom hook useBookStats
- `src/hooks/useLocalStorage.js` - Fungsi async helper

### 3. **Template Literals**
Penggunaan template literals untuk rendering dinamis dan string interpolation:

```javascript
// src/pages/Home/Home.js
const statsMessage = useMemo(() => {
  const total = books.length;
  const filtered = filteredBooks.length;
  if (searchTerm || filter !== 'semua') {
    return `Menampilkan ${filtered} dari ${total} buku`;
  }
  return `Total ${total} buku dalam koleksi`;
}, [books.length, filteredBooks.length, searchTerm, filter]);

// src/components/BookItem/BookItem.js
const bookDescription = `Buku "${book.title}" ditulis oleh ${book.author}`;

// src/pages/Stats/Stats.js
const statCards = [
  { value: stats.total, label: 'Total Buku', description: `Total ${stats.total} buku dalam koleksi` },
  { value: stats.owned, label: 'Dimiliki', description: `${stats.owned} buku yang dimiliki` },
  { value: stats.reading, label: 'Sedang Dibaca', description: `${stats.reading} buku sedang dibaca` },
  { value: stats.wantToBuy, label: 'Ingin Dibeli', description: `${stats.wantToBuy} buku yang ingin dibeli` },
];
```

**Lokasi Implementasi:**
- `src/pages/Home/Home.js` - Statistik message
- `src/components/BookItem/BookItem.js` - Deskripsi buku
- `src/pages/Stats/Stats.js` - Deskripsi statistik cards
- `src/utils/BookValidator.js` - Pesan validasi error

### 4. **Async/Await dan Promises**
Implementasi async/await untuk operasi asinkron pada localStorage:

```javascript
// src/hooks/useLocalStorage.js
const getLocalStorageAsync = async (key) => {
  return new Promise((resolve) => {
    try {
      const item = window.localStorage.getItem(key);
      resolve(item ? JSON.parse(item) : null);
    } catch (error) {
      console.error('Error reading from localStorage:', error);
      resolve(null);
    }
  });
};

const setLocalStorageAsync = async (key, value) => {
  return new Promise((resolve) => {
    try {
      window.localStorage.setItem(key, JSON.stringify(value));
      resolve(true);
    } catch (error) {
      console.error('Error writing to localStorage:', error);
      resolve(false);
    }
  });
};

// Menggunakan useEffect untuk sinkronisasi async
useEffect(() => {
  const loadData = async () => {
    const data = await getLocalStorageAsync(key);
    if (data !== null) {
      setStoredValue(data);
    }
  };
  loadData();
}, [key]);
```

**Lokasi Implementasi:**
- `src/hooks/useLocalStorage.js` - Fungsi `getLocalStorageAsync()` dan `setLocalStorageAsync()` dengan async/await
- `src/hooks/useLocalStorage.js` - `useEffect` dengan async function `loadData()`

### 5. **Classes (ES6 Classes)**
Implementasi class untuk validasi data:

```javascript
// src/utils/BookValidator.js
class BookValidator {
  constructor() {
    this.minTitleLength = 2;
    this.maxTitleLength = 200;
    this.minAuthorLength = 2;
    this.maxAuthorLength = 100;
  }

  validateTitle(title) {
    if (!title || typeof title !== 'string') {
      return {
        isValid: false,
        message: 'Judul harus berupa teks dan tidak boleh kosong.',
      };
    }
    // ...
  }

  validateAuthor(author) {
    // ...
  }

  validateStatus(status) {
    // ...
  }

  validateBook(book) {
    const errors = [];
    const titleValidation = this.validateTitle(book.title);
    const authorValidation = this.validateAuthor(book.author);
    const statusValidation = this.validateStatus(book.status);
    // ...
  }
}

// Penggunaan di BookForm
const validator = new BookValidator();
const validation = validator.validateBook({ title, author, status });
```

**Lokasi Implementasi:**
- `src/utils/BookValidator.js` - Class `BookValidator` dengan constructor dan methods
- `src/components/BookForm/BookForm.js` - Instansiasi dan penggunaan `BookValidator`

---

## 📁 Struktur Project

```
mariofransiskussitepu_123140023_pertemuan3/
├── public/                          # Static files
│   ├── index.html                   # HTML template
│   ├── favicon.ico                  # Favicon
│   ├── favicon2.ico
│   ├── favicon3.ico
│   ├── logo192.png                  # Logo untuk PWA
│   ├── logo512.png
│   ├── manifest.json                # PWA manifest
│   ├── robots.txt                   # SEO robots file
│   └── _redirects                   # Netlify redirects untuk SPA routing
│
├── src/                             # Source code
│   ├── components/                  # Reusable components
│   │   ├── BookForm/                # Form untuk tambah/edit buku
│   │   │   ├── BookForm.js
│   │   │   ├── BookForm.css
│   │   │   └── BookForm.test.js
│   │   ├── BookList/                # Daftar buku
│   │   │   ├── BookList.js
│   │   │   ├── BookList.css
│   │   │   └── BookList.test.js
│   │   ├── BookItem/                # Item buku individual
│   │   │   ├── BookItem.js
│   │   │   └── BookItem.css
│   │   ├── BookFilter/              # Filter berdasarkan status
│   │   │   ├── BookFilter.js
│   │   │   └── BookFilter.css
│   │   ├── SearchBar/               # Bar pencarian
│   │   │   ├── SearchBar.js
│   │   │   └── SearchBar.css
│   │   ├── Logo/                    # Logo aplikasi
│   │   │   ├── Logo.js
│   │   │   └── Logo.css
│   │   └── FloatingParticles/       # Partikel animasi background
│   │       ├── FloatingParticles.js
│   │       └── FloatingParticles.css
│   │
│   ├── pages/                       # Page components
│   │   ├── Home/                    # Halaman utama (koleksi buku)
│   │   │   ├── Home.js
│   │   │   ├── Home.css
│   │   │   └── Home.test.js
│   │   └── Stats/                  # Halaman statistik
│   │       ├── Stats.js
│   │       └── Stats.css
│   │
│   ├── hooks/                      # Custom React hooks
│   │   ├── useLocalStorage.js      # Hook untuk localStorage operations
│   │   ├── useLocalStorage.test.js
│   │   ├── useBookStats.js         # Hook untuk menghitung statistik buku
│   │   └── useBookStats.test.js
│   │
│   ├── context/                    # React Context
│   │   └── BookContext.js          # Context API untuk state management global
│   │
│   ├── utils/                      # Utility functions
│   │   └── BookValidator.js        # Class untuk validasi data buku
│   │
│   ├── App.js                      # Main App component
│   ├── App.css                     # Global app styles
│   ├── App.test.js                 # App tests
│   ├── index.js                    # Entry point aplikasi
│   ├── index.css                   # Global styles
│   ├── setupTests.js              # Test configuration
│   ├── reportWebVitals.js          # Web vitals reporting
│   ├── logo.svg                    # React logo (default)
│   └── logobuku.png                # Logo buku asset
│
├── screenshots/                    # Screenshots aplikasi
│   ├── home.png                    # Screenshot halaman utama
│   ├── form.png                    # Screenshot form buku
│   └── stats.png                   # Screenshot halaman statistik
│
├── build/                          # Production build (dibuat setelah npm run build)
│   ├── index.html
│   ├── static/
│   │   ├── css/                    # Compiled CSS
│   │   ├── js/                     # Compiled JavaScript
│   │   └── media/                  # Optimized media files
│   └── ...
│
├── node_modules/                   # Dependencies (auto-generated)
├── .git/                           # Git repository
├── .gitignore                     # Git ignore rules
├── netlify.toml                    # Netlify deployment configuration
├── package.json                    # Project dependencies & scripts
├── package-lock.json               # Locked dependency versions
└── README.md                       # Dokumentasi proyek
```

### Penjelasan Struktur

#### 📂 `public/`
Berisi file-file static yang akan di-copy ke folder `build/` saat build production. Termasuk HTML template, favicon, dan file konfigurasi.

#### 📂 `src/`
Folder utama untuk source code aplikasi:
- **components/**: Komponen React yang reusable, diorganisir per komponen dengan folder sendiri
- **pages/**: Komponen halaman utama aplikasi (Home, Stats)
- **hooks/**: Custom hooks untuk logic yang bisa di-reuse
- **context/**: React Context untuk state management global
- **utils/**: Utility functions dan helper classes

#### 📂 `screenshots/`
Screenshot aplikasi untuk dokumentasi.

#### 📂 `build/`
Folder output setelah menjalankan `npm run build`. Folder ini berisi file-file yang sudah di-optimize dan siap untuk di-deploy ke production.

#### 📄 File Konfigurasi
- **netlify.toml**: Konfigurasi untuk deploy di Netlify
- **package.json**: Dependencies dan npm scripts
- **.gitignore**: File yang di-ignore oleh Git

---

## 🛠️ Teknologi yang Digunakan

- **React** - Library JavaScript untuk membangun UI
- **React Router** - Routing untuk single page application
- **CSS3** - Styling dengan modern CSS features
- **localStorage API** - Penyimpanan data lokal di browser
- **ES6+ Features** - Arrow functions, template literals, async/await, classes

---

## 📝 Cara Menggunakan

1. **Menambah Buku Baru**
   - Isi form di bagian atas halaman
   - Masukkan judul buku dan nama penulis
   - Pilih status buku (Dimiliki, Sedang Dibaca, atau Ingin Dibeli)
   - Klik tombol "Tambah Buku"

2. **Mencari Buku**
   - Gunakan search bar untuk mencari berdasarkan judul atau penulis
   - Pencarian dilakukan secara real-time

3. **Memfilter Buku**
   - Klik tombol filter (Semua, Dimiliki, Sedang Dibaca, Ingin Dibeli)
   - Daftar akan otomatis terfilter sesuai pilihan

4. **Mengedit Buku**
   - Klik tombol "Edit" pada buku yang ingin diedit
   - Form akan terisi dengan data buku tersebut
   - Ubah data yang diinginkan dan klik "Perbarui Buku"

5. **Menghapus Buku**
   - Klik tombol "Hapus" pada buku yang ingin dihapus
   - Buku akan langsung terhapus dari koleksi

6. **Melihat Statistik**
   - Klik menu "Statistik" di navbar
   - Lihat ringkasan koleksi buku dengan statistik visual

---

## 🎨 Fitur Desain

### Glassmorphism Effect
- Background blur dan transparansi untuk efek kaca modern
- Border dengan opacity rendah
- Shadow yang halus

### Animations
- Fade in animations untuk komponen
- Slide in animations untuk list items
- Hover effects dengan transform dan shadow
- Ripple effects pada buttons
- Staggered animations untuk multiple items

### Color Scheme
- Primary: Purple-Blue Gradient (#667eea → #764ba2)
- Success: Green Gradient
- Warning: Yellow Gradient
- Danger: Red Gradient

---

## 📊 Statistik Implementasi ES6+

| Fitur ES6+ | Jumlah Implementasi | Lokasi File |
|------------|---------------------|-------------|
| **Let & Const** | 50+ | Semua komponen React |
| **Arrow Functions** | 25+ | Semua komponen, hooks, dan utilities |
| **Template Literals** | 10+ | Home.js, BookItem.js, Stats.js, BookValidator.js |
| **Async/Await** | 3 | useLocalStorage.js |
| **Classes** | 1 | BookValidator.js |

---

## 👤 Author

**Mario Fransiskus Sitepu**

---

## 📌 Catatan

- Data disimpan di localStorage browser, sehingga data akan hilang jika:
  - Browser cache dihapus
  - Mode incognito/private digunakan
  - Data localStorage dihapus manual

- Untuk penggunaan yang lebih baik, disarankan menggunakan browser modern dengan dukungan ES6+

---

## 🔄 Versi

**Version 1.0.0**

Aplikasi ini dikembangkan sebagai bagian dari tugas praktikum Pemrograman Web.

---

*Dibuat dengan ❤️ menggunakan React dan modern JavaScript*
