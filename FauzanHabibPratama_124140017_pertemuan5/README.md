# Praktikum PAW - Pertemuan 5: Python OOP

## Identitas Mahasiswa
- **Nama Lengkap** : Fauzan Habib Paratama
- **NIM**          : 124140017
- **Kelas Praktikum** : [RA / RB]

## Deskripsi Program
Sistem Manajemen Perpustakaan Sederhana berbasis OOP Python.

**Alur program:** `main.py` membuat objek `Library`, menambahkan beberapa `Book` dan `Magazine`,
menampilkan katalog item tersedia, mencari item berdasarkan judul/ID, lalu mensimulasikan
peminjaman dan pengembalian oleh `Member` (termasuk perhitungan denda).

**Penerapan 4 pilar OOP:**
1. **Class & Object** - `LibraryItem`, `Book`, `Magazine`, `Member`, dan `Library` adalah class yang
   diinstansiasi menjadi objek di `main.py`.
2. **Inheritance** - `Book` dan `Magazine` mewarisi abstract class `LibraryItem` dan memakai `super().__init__()`.
   Abstract method `get_detail()`, `hitung_denda()`, dan `durasi_pinjam()` wajib diimplementasikan.
3. **Encapsulation** - `__dipinjam` (private) pada `LibraryItem`, `__koleksi` (private) pada `Library`,
   `__daftar_pinjam` (private) pada `Member`, serta `_item_id` dan `_judul` (protected). Atribut
   diakses lewat `@property` (`item_id`, `judul`, `is_dipinjam`, `jumlah_pinjaman`).
4. **Polymorphism** - `print(item)` dan `hitung_denda()` memberi hasil berbeda untuk `Book` (Rp 1.000/hari)
   dan `Magazine` (Rp 2.000/hari) walau dipanggil lewat tipe induk `LibraryItem`.

## Panduan Menjalankan Program
```bash
cd tugas_perpustakaan
python main.py
```

## Screenshot Output
> Ganti bagian ini dengan screenshot terminal saat `python main.py` dijalankan.

Cuplikan teks output:
```
--- 1. Menambah Item ---
Item ditambahkan: Pemrograman Python
Item ditambahkan: Basis Data Lanjut
Item ditambahkan: Tech Today
Item ditambahkan: Sains Populer
Gagal: ID B001 sudah terdaftar.

=== Katalog Tersedia - Perpustakaan ITERA ===
  [B001] Buku 'Pemrograman Python' oleh Andi Wijaya (350 hlm) - Tersedia
  [B002] Buku 'Basis Data Lanjut' oleh Siti Rahma (420 hlm) - Tersedia
  [M001] Majalah 'Tech Today' edisi Nov 2026 (Gramedia) - Tersedia
  [M002] Majalah 'Sains Populer' edisi Okt 2026 (Kompas) - Tersedia

--- 2. Pencarian ---
Cari judul 'python': ['Pemrograman Python']
Cari ID 'M001'     : [M001] Majalah 'Tech Today' edisi Nov 2026 (Gramedia) - Tersedia
Cari ID 'X999'     : None

--- 3. Peminjaman ---
Budi berhasil meminjam 'Pemrograman Python' (maks 14 hari).
'Pemrograman Python' sedang dipinjam orang lain.
Budi berhasil meminjam 'Tech Today' (maks 7 hari).
Status buku B001 dipinjam? True

=== Katalog Tersedia - Perpustakaan ITERA ===
  [B002] Buku 'Basis Data Lanjut' oleh Siti Rahma (420 hlm) - Tersedia
  [M002] Majalah 'Sains Populer' edisi Okt 2026 (Kompas) - Tersedia

--- 4. Pengembalian ---
Budi mengembalikan 'Pemrograman Python'. Denda: Rp 3,000
Budi mengembalikan 'Tech Today'. Denda: Rp 6,000

=== Semua Koleksi - Perpustakaan ITERA ===
  [B001] Buku 'Pemrograman Python' oleh Andi Wijaya (350 hlm) - Tersedia
  [B002] Buku 'Basis Data Lanjut' oleh Siti Rahma (420 hlm) - Tersedia
  [M001] Majalah 'Tech Today' edisi Nov 2026 (Gramedia) - Tersedia
  [M002] Majalah 'Sains Populer' edisi Okt 2026 (Kompas) - Tersedia

--- 5. Uji Encapsulation ---
is_dipinjam read-only: tidak bisa diubah langsung (AttributeError)
```
