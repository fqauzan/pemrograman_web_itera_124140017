# ==============================================================================
# Berkas: library.py
# Deskripsi: Class Library untuk mengelola koleksi item perpustakaan
# ==============================================================================
from library_item import LibraryItem


class Library:
    """Mengelola koleksi. Koleksi disimpan di atribut private __koleksi."""

    def __init__(self, nama: str):
        self.nama = nama
        self.__koleksi = {}  # {item_id: LibraryItem}

    def tambah_item(self, item: LibraryItem) -> bool:
        """Menambahkan item baru; id harus unik."""
        if item.item_id in self.__koleksi:
            print(f"Gagal: ID {item.item_id} sudah terdaftar.")
            return False
        self.__koleksi[item.item_id] = item
        print(f"Item ditambahkan: {item.judul}")
        return True

    def tampilkan_tersedia(self):
        """Menampilkan item yang belum dipinjam (polymorphism via get_detail)."""
        print(f"\n=== Katalog Tersedia - {self.nama} ===")
        tersedia = [i for i in self.__koleksi.values() if not i.is_dipinjam]
        if not tersedia:
            print("(tidak ada item tersedia)")
        for item in tersedia:
            print(" ", item)

    def tampilkan_semua(self):
        """Menampilkan seluruh koleksi beserta status ketersediaannya."""
        print(f"\n=== Semua Koleksi - {self.nama} ===")
        for item in self.__koleksi.values():
            print(" ", item)

    def cari_by_id(self, item_id: str):
        """Mencari item berdasarkan ID. Mengembalikan None jika tidak ada."""
        return self.__koleksi.get(item_id)

    def cari_by_judul(self, kata_kunci: str) -> list:
        """Pencarian judul (tidak peka huruf besar/kecil, cocok sebagian)."""
        kata = kata_kunci.lower()
        return [i for i in self.__koleksi.values() if kata in i.judul.lower()]

    def __len__(self) -> int:
        """len(perpus) = jumlah item dalam koleksi."""
        return len(self.__koleksi)
