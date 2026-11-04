"""Tugas 2: Program Pengelolaan Data Nilai Mahasiswa."""

BOBOT_UTS = 0.30
BOBOT_UAS = 0.40
BOBOT_TUGAS = 0.30

data_mahasiswa = [
    {"nama": "Fauzan Habib Pratama", "nim": "124140017",
     "nilai_uts": 88, "nilai_uas": 92, "nilai_tugas": 90},
    {"nama": "Rizky Ramadhan", "nim": "124140021",
     "nilai_uts": 80, "nilai_uas": 75, "nilai_tugas": 82},
    {"nama": "Alya Kusuma Dewi", "nim": "124140052",
     "nilai_uts": 72, "nilai_uas": 65, "nilai_tugas": 70},
    {"nama": "Dimas Aditya Putra", "nim": "124140048",
     "nilai_uts": 60, "nilai_uas": 55, "nilai_tugas": 65},
    {"nama": "Nadia Putri Anindya", "nim": "124140034",
     "nilai_uts": 70, "nilai_uas": 68, "nilai_tugas": 75},
    {"nama": "Bagus Prasetyo", "nim": "124140063",
     "nilai_uts": 40, "nilai_uas": 38, "nilai_tugas": 45},
]


def hitung_nilai_akhir(uts: float, uas: float, tugas: float) -> float:
    """Menghitung nilai akhir (30% UTS + 40% UAS + 30% Tugas).

    Parameter:
        uts (float): nilai UTS.
        uas (float): nilai UAS.
        tugas (float): nilai tugas.
    Return:
        float: nilai akhir.
    """
    return BOBOT_UTS * uts + BOBOT_UAS * uas + BOBOT_TUGAS * tugas


def tentukan_grade(nilai_akhir: float) -> str:
    """Menentukan grade huruf dari nilai akhir.

    Parameter:
        nilai_akhir (float): nilai akhir mahasiswa.
    Return:
        str: grade A, B, C, D, atau E.
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


def proses_data(daftar: list) -> list:
    """Menambahkan 'nilai_akhir' dan 'grade' ke setiap mahasiswa.

    Parameter:
        daftar (list): list dictionary data mahasiswa.
    Return:
        list: list dictionary yang sudah dilengkapi nilai akhir dan grade.
    """
    hasil = []
    for mhs in daftar:
        nilai_akhir = hitung_nilai_akhir(
            mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"]
        )
        data_baru = dict(mhs)
        data_baru["nilai_akhir"] = nilai_akhir
        data_baru["grade"] = tentukan_grade(nilai_akhir)
        hasil.append(data_baru)
    return hasil


def tampilkan_tabel(daftar: list) -> None:
    """Mencetak tabel data mahasiswa dengan perataan f-string.

    Parameter:
        daftar (list): list dictionary dengan nilai akhir dan grade.
    """
    garis = "+" + "+".join("-" * n for n in (5, 22, 12, 13, 7)) + "+"
    print(garis)
    print(f"| {'No':<3} | {'Nama':<20} | {'NIM':<10} | "
          f"{'Nilai Akhir':>11} | {'Grade':^5} |")
    print(garis)
    for no, mhs in enumerate(daftar, start=1):
        print(f"| {no:<3} | {mhs['nama']:<20} | {mhs['nim']:<10} | "
              f"{mhs['nilai_akhir']:>11.2f} | {mhs['grade']:^5} |")
    print(garis)


def tampilkan_info(judul: str, mhs: dict) -> None:
    """Mencetak informasi lengkap satu mahasiswa.

    Parameter:
        judul (str): judul yang ditampilkan.
        mhs (dict): data mahasiswa.
    """
    print(f"\n{judul}")
    print(f"  Nama        : {mhs['nama']}")
    print(f"  NIM         : {mhs['nim']}")
    print(f"  Nilai Akhir : {mhs['nilai_akhir']:.2f}")
    print(f"  Grade       : {mhs['grade']}")


def main():
    """Menjalankan program pengelolaan nilai mahasiswa."""
    hasil = proses_data(data_mahasiswa)

    print("=== DATA NILAI MAHASISWA ===")
    tampilkan_tabel(hasil)

    tertinggi = max(hasil, key=lambda m: m["nilai_akhir"])
    terendah = min(hasil, key=lambda m: m["nilai_akhir"])

    tampilkan_info("Mahasiswa dengan nilai akhir TERTINGGI:", tertinggi)
    tampilkan_info("Mahasiswa dengan nilai akhir TERENDAH:", terendah)


if __name__ == "__main__":
    main()