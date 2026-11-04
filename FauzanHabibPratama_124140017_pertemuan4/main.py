"""Program utama: menggunakan modul math_operations."""

# Cara impor 1: seluruh modul (dipanggil dengan prefix nama modul)
import math_operations

# Cara impor 2: fungsi spesifik langsung ke namespace
from math_operations import luas_lingkaran, keliling_lingkaran
from math_operations import celsius_ke_kelvin

# Cara impor 3: memakai alias
import math_operations as mo


def garis(judul: str) -> None:
    """Mencetak judul bagian dengan pembatas.

    Parameter: judul (str).
    """
    print(f"\n{'=' * 8} {judul} {'=' * 8}")


def main():
    """Menjalankan pengujian seluruh fungsi modul math_operations."""
    print(f"Konstanta PI dari modul: {math_operations.PI}")

    garis("PERSEGI")
    for sisi in (4, 7.5):
        luas = math_operations.luas_persegi(sisi)
        keliling = math_operations.keliling_persegi(sisi)
        print(f"Sisi {sisi:<4} -> Luas: {luas:>8.2f} | "
              f"Keliling: {keliling:>8.2f}")

    garis("PERSEGI PANJANG")
    for panjang, lebar in ((10, 5), (8.5, 3.2)):
        luas = math_operations.luas_persegi_panjang(panjang, lebar)
        keliling = math_operations.keliling_persegi_panjang(panjang, lebar)
        print(f"{panjang} x {lebar:<4} -> Luas: {luas:>8.2f} | "
              f"Keliling: {keliling:>8.2f}")

    garis("LINGKARAN")
    for r in (7, 10.5):
        print(f"Jari-jari {r:<4} -> Luas: {luas_lingkaran(r):>8.2f} | "
              f"Keliling: {keliling_lingkaran(r):>8.2f}")

    garis("KONVERSI SUHU")
    for c in (0, 37, 100):
        fahrenheit = mo.celsius_ke_fahrenheit(c)
        print(f"{c:>3} C -> {fahrenheit:>7.2f} F | "
              f"{celsius_ke_kelvin(c):>7.2f} K")


if __name__ == "__main__":
    main()