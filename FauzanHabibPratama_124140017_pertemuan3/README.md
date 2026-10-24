
# Personal Library — Manajemen Buku Pribadi

## 1. Deskripsi Aplikasi

Personal Library merupakan aplikasi web sederhana yang dibuat menggunakan React untuk membantu pengguna mengelola koleksi buku pribadi. Aplikasi ini menyediakan fitur untuk menambahkan, mengedit, menghapus, mencari, dan memfilter buku berdasarkan statusnya.

Data buku disimpan menggunakan Local Storage sehingga data tetap tersedia ketika halaman dimuat ulang pada browser yang sama.

## 2. Teknologi yang Digunakan

- React
- Vite
- JavaScript
- CSS
- React Router DOM
- React Context API
- React Hooks
- Local Storage
- Vitest
- React Testing Library

## 3. Instalasi dan Cara Menjalankan

Pastikan Node.js sudah terpasang pada komputer.

### Langkah 1 — Instal dependensi

Buka terminal di folder proyek dan jalankan:

```bash
npm install
```

### Langkah 2 — Jalankan aplikasi

```bash
npm run dev
```

Buka alamat lokal yang ditampilkan di terminal pada browser.

### Langkah 3 — Menjalankan unit test

```bash
npm run test -- --run
```

### Langkah 4 — Memeriksa build aplikasi

```bash
npm run build
```

## 4. Screenshot Antarmuka Aplikasi

### Halaman Utama

![Halaman Utama](<src/assets/1.png>)

### Daftar Buku

![Daftar Buku](<src/assets/2.png>)

### Halaman Statistik

![Halaman Statistik](<src/assets/3.png>)

## 5. Fitur React yang Digunakan

### React Components

Digunakan untuk membagi antarmuka menjadi bagian-bagian seperti form buku, daftar buku, filter, dan halaman statistik.

### useState

Digunakan untuk mengelola state pada antarmuka, misalnya pencarian, filter, dan data form.

### Context API

Digunakan untuk membagikan data buku dan fungsi pengelolaannya ke komponen yang membutuhkan.

### Custom Hooks

Digunakan untuk memisahkan logika tertentu, seperti penyimpanan data dan perhitungan statistik, agar kode lebih mudah dikelola.

### Local Storage

Digunakan untuk menyimpan data buku di browser sehingga data tetap tersedia setelah halaman dimuat ulang.

### React Router DOM

Digunakan untuk mengatur navigasi antara halaman utama dan halaman statistik.

## 6. Hasil Pengujian

Unit test dijalankan menggunakan Vitest dan React Testing Library.

Screenshot berikut berisi hasil eksekusi pengujian dari terminal.

![Hasil Unit Test](<assets/foto 3.png>)

## 7. Komentar Kode

Komentar ditambahkan pada bagian penting dalam kode untuk menjelaskan fungsi atau proses yang dilakukan, seperti pengelolaan data buku, filter, dan penyimpanan Local Storage.

## 8. Penutup

Melalui proyek Personal Library, saya mempelajari penggunaan React untuk membangun aplikasi web, mengelola state dan data, membuat navigasi halaman, serta melakukan pengujian fungsi aplikasi.

---

**Nama:** Fauzan Habib Pratama  
**NIM:** 124140017  
**Tugas:** Praktikum PAW
