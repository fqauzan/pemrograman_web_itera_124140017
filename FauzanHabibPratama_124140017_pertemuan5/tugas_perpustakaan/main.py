# ==============================================================================
# Berkas: main.py
# Deskripsi: Skrip uji sistem manajemen perpustakaan
# ==============================================================================
from library_item import Book, Magazine
from library import Library
from member import Member


def main():
    perpus = Library("Perpustakaan ITERA")

    # 1. Menambahkan item
    print("--- 1. Menambah Item ---")
    perpus.tambah_item(Book("B001", "Pemrograman Python", "Andi Wijaya", 350))
    perpus.tambah_item(Book("B002", "Basis Data Lanjut", "Siti Rahma", 420))
    perpus.tambah_item(Magazine("M001", "Tech Today", "Nov 2026", "Gramedia"))
    perpus.tambah_item(Magazine("M002", "Sains Populer", "Okt 2026", "Kompas"))
    perpus.tambah_item(Book("B001", "ID Duplikat", "-", 1))  # ditolak

    # 2. Menampilkan daftar
    perpus.tampilkan_tersedia()

    # 3. Pencarian
    print("\n--- 2. Pencarian ---")
    hasil = perpus.cari_by_judul("python")
    print("Cari judul 'python':", [i.judul for i in hasil])
    item = perpus.cari_by_id("M001")
    print("Cari ID 'M001'     :", item)
    print("Cari ID 'X999'     :", perpus.cari_by_id("X999"))

    # 4. Peminjaman & status ketersediaan
    print("\n--- 3. Peminjaman ---")
    budi = Member("A01", "Budi")
    siti = Member("A02", "Siti")
    buku = perpus.cari_by_id("B001")
    budi.pinjam_item(buku)
    siti.pinjam_item(buku)  # gagal, sedang dipinjam
    budi.pinjam_item(perpus.cari_by_id("M001"))
    print("Status buku B001 dipinjam?", buku.is_dipinjam)
    perpus.tampilkan_tersedia()

    # 5. Pengembalian + denda (polymorphism: denda berbeda tiap tipe)
    print("\n--- 4. Pengembalian ---")
    budi.kembalikan_item(buku, hari_terlambat=3)                      # Buku: 3 x 1.000
    budi.kembalikan_item(perpus.cari_by_id("M001"), hari_terlambat=3) # Majalah: 3 x 2.000
    perpus.tampilkan_semua()

    # 6. Bukti encapsulation
    print("\n--- 5. Uji Encapsulation ---")
    try:
        buku.is_dipinjam = True
    except AttributeError:
        print("is_dipinjam read-only: tidak bisa diubah langsung (AttributeError)")


if __name__ == "__main__":
    main()
