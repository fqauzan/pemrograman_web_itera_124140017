# ==============================================================================
# Berkas: member.py
# Deskripsi: Class Member (anggota perpustakaan)
# ==============================================================================
from library_item import LibraryItem


class Member:
    """Anggota perpustakaan. Daftar pinjaman bersifat private."""
    MAKS_PINJAM = 3

    def __init__(self, member_id: str, nama: str):
        self.member_id = member_id
        self.nama = nama
        self.__daftar_pinjam = []  # private

    @property
    def jumlah_pinjaman(self) -> int:
        """Jumlah item yang sedang dipinjam anggota."""
        return len(self.__daftar_pinjam)

    def pinjam_item(self, item: LibraryItem) -> bool:
        """Meminjam item jika kuota masih ada dan item tersedia."""
        if self.jumlah_pinjaman >= self.MAKS_PINJAM:
            print(f"{self.nama} sudah mencapai batas {self.MAKS_PINJAM} pinjaman.")
            return False
        if not item.pinjam():
            print(f"'{item.judul}' sedang dipinjam orang lain.")
            return False
        self.__daftar_pinjam.append(item)
        print(f"{self.nama} berhasil meminjam '{item.judul}' (maks {item.durasi_pinjam()} hari).")
        return True

    def kembalikan_item(self, item: LibraryItem, hari_terlambat: int = 0) -> bool:
        """Mengembalikan item dan menampilkan denda sesuai tipe item."""
        if item not in self.__daftar_pinjam:
            print(f"{self.nama} tidak meminjam '{item.judul}'.")
            return False
        item.kembalikan()
        self.__daftar_pinjam.remove(item)
        denda = item.hitung_denda(hari_terlambat)
        print(f"{self.nama} mengembalikan '{item.judul}'. Denda: Rp {denda:,}")
        return True

    def daftar_pinjaman(self) -> list:
        """Mengembalikan salinan daftar agar list asli tidak bisa diubah dari luar."""
        return list(self.__daftar_pinjam)
