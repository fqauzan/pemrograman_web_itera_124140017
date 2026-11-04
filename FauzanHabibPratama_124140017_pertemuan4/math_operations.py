"""Modul math_operations: geometri dan konversi suhu."""

PI = 3.14159


# ---------- Geometri ----------
def luas_persegi(sisi: float) -> float:
    """Menghitung luas persegi.

    Parameter: sisi (float). Return: luas (float).
    """
    return sisi * sisi


def keliling_persegi(sisi: float) -> float:
    """Menghitung keliling persegi.

    Parameter: sisi (float). Return: keliling (float).
    """
    return 4 * sisi


def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang.

    Parameter: panjang, lebar (float). Return: luas (float).
    """
    return panjang * lebar


def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung keliling persegi panjang.

    Parameter: panjang, lebar (float). Return: keliling (float).
    """
    return 2 * (panjang + lebar)


def luas_lingkaran(jari_jari: float) -> float:
    """Menghitung luas lingkaran.

    Parameter: jari_jari (float). Return: luas (float).
    """
    return PI * jari_jari ** 2


def keliling_lingkaran(jari_jari: float) -> float:
    """Menghitung keliling lingkaran.

    Parameter: jari_jari (float). Return: keliling (float).
    """
    return 2 * PI * jari_jari


# ---------- Konversi Suhu ----------
def celsius_ke_fahrenheit(celsius: float) -> float:
    """Mengonversi suhu Celsius ke Fahrenheit.

    Parameter: celsius (float). Return: suhu Fahrenheit (float).
    """
    return celsius * 9 / 5 + 32


def celsius_ke_kelvin(celsius: float) -> float:
    """Mengonversi suhu Celsius ke Kelvin.

    Parameter: celsius (float). Return: suhu Kelvin (float).
    """
    return celsius + 273.15


if __name__ == "__main__":
    print("[TEST MODUL] Luas lingkaran r=7 :", luas_lingkaran(7))
    print("[TEST MODUL] 100 C ke Fahrenheit:", celsius_ke_fahrenheit(100))