# Pyramid RESTful API: Mahasiswa & Matakuliah

## Identitas
- Nama Lengkap : Fauzan Habib Pratama
- NIM          : 124140017
- Kelas        : RB

## Deskripsi
Aplikasi RESTful API berbasis Pyramid Framework dan PostgreSQL untuk
mengelola data Mahasiswa dan Matakuliah. Aplikasi memakai SQLAlchemy ORM,
migrasi database dengan Alembic, dan mengembalikan respons berformat JSON.

## Instalasi
Prasyarat: Python 3.12, PostgreSQL, Git.

    python -m venv venv
    venv\Scripts\activate.bat
    python -m pip install --upgrade pip setuptools
    pip install -e ".[testing]"
    pip install psycopg2-binary

## Konfigurasi Database
Buat database dan user di PostgreSQL:

    CREATE DATABASE pyramid_mahasiswa;
    CREATE USER pyramid_user WITH ENCRYPTED PASSWORD 'pyramid_pass';
    GRANT ALL PRIVILEGES ON DATABASE pyramid_mahasiswa TO pyramid_user;
    ALTER DATABASE pyramid_mahasiswa OWNER TO pyramid_user;

Pada `development.ini`, `sqlalchemy.url` memakai driver psycopg2:

    sqlalchemy.url = postgresql+psycopg2://pyramid_user:pyramid_pass@localhost:5432/pyramid_mahasiswa

## Migrasi dan Seeding

    alembic -c development.ini upgrade head
    python -m pyramid_mahasiswa.scripts.initialize_db development.ini

## Menjalankan Server

    pserve development.ini --reload

Server berjalan di http://localhost:6543

## Daftar Endpoint

| Method | URL | Keterangan |
|--------|-----|------------|
| GET | /api/mahasiswa | Semua mahasiswa |
| GET | /api/mahasiswa/{id} | Detail mahasiswa |
| POST | /api/mahasiswa | Tambah mahasiswa |
| PUT | /api/mahasiswa/{id} | Ubah mahasiswa |
| DELETE | /api/mahasiswa/{id} | Hapus mahasiswa |
| GET | /api/matakuliah | Semua matakuliah |
| GET | /api/matakuliah/{id} | Detail matakuliah (404 jika tidak ada) |
| POST | /api/matakuliah | Tambah matakuliah (400 jika tidak valid) |
| PUT | /api/matakuliah/{id} | Ubah matakuliah |
| DELETE | /api/matakuliah/{id} | Hapus matakuliah |

Validasi Matakuliah: `kode_mk`, `nama_mk`, `sks`, dan `semester` wajib diisi,
`sks` dan `semester` harus bilangan bulat lebih dari 0, dan `kode_mk` harus unik.

## Bukti Pengujian (cURL)

### Matakuliah

**1. GET semua matakuliah**

Menampilkan seluruh data matakuliah.

<img src="screenshots/mk_1_get_all.png" alt="GET semua matakuliah" width="800">

**2. GET satu matakuliah**

Menampilkan detail matakuliah berdasarkan ID.

<img src="screenshots/mk_2_get_one.png" alt="GET satu matakuliah" width="800">

**3. POST tambah matakuliah**

Menambah matakuliah baru dengan data yang valid.

<img src="screenshots/mk_3_post.png" alt="POST matakuliah" width="800">

**4. POST dengan field kosong (400 Bad Request)**

Ditolak karena ada field wajib yang kosong.

<img src="screenshots/mk_4_post_400_kosong.png" alt="POST matakuliah field kosong" width="800">

**5. POST dengan sks tidak valid (400 Bad Request)**

Ditolak karena `sks` bukan bilangan bulat lebih dari 0.

<img src="screenshots/mk_5_post_400_sks.png" alt="POST matakuliah sks tidak valid" width="800">

**6. PUT ubah matakuliah**

Mengubah data matakuliah berdasarkan ID.

<img src="screenshots/mk_6_put.png" alt="PUT matakuliah" width="800">

**7. DELETE hapus matakuliah**

Menghapus matakuliah berdasarkan ID.

<img src="screenshots/mk_7_delete.png" alt="DELETE matakuliah" width="800">

**8. GET matakuliah yang sudah dihapus (404 Not Found)**

Data tidak ditemukan karena sudah dihapus.

<img src="screenshots/mk_8_get_404.png" alt="GET matakuliah 404" width="800">

### Mahasiswa

**1. GET semua mahasiswa**

Menampilkan seluruh data mahasiswa.

<img src="screenshots/mhs_1_get_all.png" alt="GET semua mahasiswa" width="800">

**2. GET satu mahasiswa**

Menampilkan detail mahasiswa berdasarkan ID.

<img src="screenshots/mhs_2_get_one.png" alt="GET satu mahasiswa" width="800">

**3. POST tambah mahasiswa**

Menambah mahasiswa baru dengan data yang valid.

<img src="screenshots/mhs_3_post.png" alt="POST mahasiswa" width="800">

**4. POST tanpa NIM (400 Bad Request)**

Ditolak dengan pesan "Field nim wajib diisi!".

<img src="screenshots/mhs_4_post_400.png" alt="POST mahasiswa 400" width="800">

**5. PUT ubah mahasiswa (200 OK)**

Jurusan mahasiswa berhasil diubah.

<img src="screenshots/mhs_5_put.png" alt="PUT mahasiswa" width="800">

**6. DELETE hapus mahasiswa (200 OK)**

Mahasiswa berhasil dihapus.

<img src="screenshots/mhs_6_delete.png" alt="DELETE mahasiswa" width="800">

**7. GET mahasiswa yang sudah dihapus (404 Not Found)**

Data tidak ditemukan karena sudah dihapus.

<img src="screenshots/mhs_7_get_404.png" alt="GET mahasiswa 404" width="800">
