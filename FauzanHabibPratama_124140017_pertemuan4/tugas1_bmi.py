"""Tugas 1: Program Penghitung BMI (Body Mass Index) sederhana."""


def hitung_bmi(berat: float, tinggi: float) -> float:
    """Menghitung nilai BMI.

    Parameter:
        berat (float): berat badan dalam kilogram.
        tinggi (float): tinggi badan dalam meter.
    Return:
        float: nilai BMI = berat / (tinggi * tinggi).
    """
    return berat / (tinggi * tinggi)


def tentukan_kategori(bmi: float) -> str:
    """Menentukan kategori berat badan berdasarkan nilai BMI.

    Parameter:
        bmi (float): nilai BMI.
    Return:
        str: kategori berat badan.
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi < 25:
        return "Berat badan normal"
    elif bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


def main():
    """Meminta input, menghitung BMI, lalu mencetak hasilnya."""
    print("=== KALKULATOR BMI ===")
    try:
        berat = float(input("Masukkan berat badan (kg) : "))
        tinggi = float(input("Masukkan tinggi badan (m) : "))
    except ValueError:
        print("Input tidak valid! Masukkan angka (contoh: 65 atau 1.70).")
        return

    if berat <= 0 or tinggi <= 0:
        print("Berat dan tinggi harus lebih besar dari 0.")
        return

    bmi = hitung_bmi(berat, tinggi)
    kategori = tentukan_kategori(bmi)

    print("\n--- HASIL ---")
    print(f"Berat badan : {berat:.1f} kg")
    print(f"Tinggi badan: {tinggi:.2f} m")
    print(f"Nilai BMI   : {bmi:.2f}")
    print(f"Kategori    : {kategori}")


if __name__ == "__main__":
    main()