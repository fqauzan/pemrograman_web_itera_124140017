# ==============================================================================
# Berkas: library_item.py
# Deskripsi: Abstract class LibraryItem beserta subclass Book dan Magazine
# ==============================================================================
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Kelas abstrak dasar untuk semua item perpustakaan.

    Encapsulation:
      - _item_id, _judul : protected (untuk class ini & subclass)
      - __dipinjam       : private (hanya diubah lewat pinjam()/kembalikan())
    """

    def __init__(self, item_id: str, judul: str):
        self._item_id = item_id
        self._judul = judul
        self.__dipinjam = False

    # ---------- Properties (getter read-only) ----------
    @property
    def item_id(self) -> str:
        """ID unik item (read-only)."""
        return self._item_id

    @property
    def judul(self) -> str:
        """Judul item (read-only)."""
        return self._judul

    @property
    def is_dipinjam(self) -> bool:
        """Status peminjaman (read-only dari luar class)."""
        return self.__dipinjam

    # ---------- Method abstract: wajib di-override subclass ----------
    @abstractmethod
    def get_detail(self) -> str:
        """Mengembalikan detail lengkap item."""

    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> int:
        """Menghitung denda keterlambatan (Rupiah)."""

    @abstractmethod
    def durasi_pinjam(self) -> int:
        """Lama peminjaman maksimal (hari)."""

    # ---------- Concrete methods ----------
    def pinjam(self) -> bool:
        """Menandai item dipinjam. False jika sudah dipinjam."""
        if self.__dipinjam:
            return False
        self.__dipinjam = True
        return True

    def kembalikan(self) -> bool:
        """Menandai item dikembalikan. False jika memang tidak dipinjam."""
        if not self.__dipinjam:
            return False
        self.__dipinjam = False
        return True

    def __str__(self) -> str:
        """Representasi teks: ID, detail item, dan status ketersediaan."""
        status = "Dipinjam" if self.__dipinjam else "Tersedia"
        return f"[{self._item_id}] {self.get_detail()} - {status}"


class Book(LibraryItem):
    """Buku: durasi pinjam 14 hari, denda Rp 1.000/hari."""
    DENDA_PER_HARI = 1000

    def __init__(self, item_id: str, judul: str, penulis: str, jumlah_halaman: int):
        super().__init__(item_id, judul)
        self.penulis = penulis
        self.jumlah_halaman = jumlah_halaman

    def get_detail(self) -> str:
        """Implementasi abstract method: detail item."""
        return f"Buku '{self._judul}' oleh {self.penulis} ({self.jumlah_halaman} hlm)"

    def hitung_denda(self, hari_terlambat: int) -> int:
        """Implementasi abstract method: denda = hari terlambat x tarif."""
        return max(0, hari_terlambat) * self.DENDA_PER_HARI

    def durasi_pinjam(self) -> int:
        """Implementasi abstract method: lama peminjaman (hari)."""
        return 14


class Magazine(LibraryItem):
    """Majalah: durasi pinjam 7 hari, denda Rp 2.000/hari."""
    DENDA_PER_HARI = 2000

    def __init__(self, item_id: str, judul: str, edisi: str, penerbit: str):
        super().__init__(item_id, judul)
        self.edisi = edisi
        self.penerbit = penerbit

    def get_detail(self) -> str:
        """Implementasi abstract method: detail item."""
        return f"Majalah '{self._judul}' edisi {self.edisi} ({self.penerbit})"

    def hitung_denda(self, hari_terlambat: int) -> int:
        """Implementasi abstract method: denda = hari terlambat x tarif."""
        return max(0, hari_terlambat) * self.DENDA_PER_HARI

    def durasi_pinjam(self) -> int:
        """Implementasi abstract method: lama peminjaman (hari)."""
        return 7
