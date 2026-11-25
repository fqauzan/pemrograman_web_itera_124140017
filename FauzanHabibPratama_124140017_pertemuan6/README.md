\# Pyramid RESTful API: Mahasiswa \& Matakuliah



\## Identitas

\- Nama Lengkap : Fauzan Habib Pratama

\- NIM          : 124140017

\- Kelas        : RB



\## Deskripsi

Aplikasi RESTful API berbasis Pyramid Framework dan PostgreSQL untuk

mengelola data Mahasiswa dan Matakuliah. Aplikasi memakai SQLAlchemy ORM,

migrasi database dengan Alembic, dan mengembalikan respons berformat JSON.



\## Instalasi

Prasyarat: Python 3.12, PostgreSQL, Git.



&#x20;   python -m venv venv

&#x20;   venv\\Scripts\\activate.bat

&#x20;   python -m pip install --upgrade pip setuptools

&#x20;   pip install -e ".\[testing]"

&#x20;   pip install psycopg2-binary



\## Konfigurasi Database

Buat database dan user di PostgreSQL:



&#x20;   CREATE DATABASE pyramid\_mahasiswa;

&#x20;   CREATE USER pyramid\_user WITH ENCRYPTED PASSWORD 'pyramid\_pass';

&#x20;   GRANT ALL PRIVILEGES ON DATABASE pyramid\_mahasiswa TO pyramid\_user;

&#x20;   ALTER DATABASE pyramid\_mahasiswa OWNER TO pyramid\_user;



Pada `development.ini`, `sqlalchemy.url` memakai driver psycopg2:



&#x20;   sqlalchemy.url = postgresql+psycopg2://pyramid\_user:pyramid\_pass@localhost:5432/pyramid\_mahasiswa



\## Migrasi dan Seeding



&#x20;   alembic -c development.ini upgrade head

&#x20;   python -m pyramid\_mahasiswa.scripts.initialize\_db development.ini



\## Menjalankan Server



&#x20;   pserve development.ini --reload



Server berjalan di http://localhost:6543



\## Daftar Endpoint



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



Validasi Matakuliah: `kode\_mk`, `nama\_mk`, `sks`, dan `semester` wajib diisi,

`sks` dan `semester` harus bilangan bulat lebih dari 0, dan `kode\_mk` harus unik.



\## Bukti Pengujian (cURL)



\### Matakuliah

GET semua: !\[mk get all](screenshots/mk\_1\_get\_all.png)



GET satu: !\[mk get one](screenshots/mk\_2\_get\_one.png)



POST: !\[mk post](screenshots/mk\_3\_post.png)



POST 400 (field kosong): !\[mk 400 kosong](screenshots/mk\_4\_post\_400\_kosong.png)



POST 400 (sks tidak valid): !\[mk 400 sks](screenshots/mk\_5\_post\_400\_sks.png)



PUT: !\[mk put](screenshots/mk\_6\_put.png)



DELETE: !\[mk delete](screenshots/mk\_7\_delete.png)



GET 404: !\[mk 404](screenshots/mk\_8\_get\_404.png)



\### Mahasiswa

GET semua: !\[mhs get all](screenshots/mhs\_1\_get\_all.png)



GET satu: !\[mhs get one](screenshots/mhs\_2\_get\_one.png)



POST: !\[mhs post](screenshots/mhs\_3\_post.png)



POST 400: !\[mhs 400](screenshots/mhs\_4\_post\_400.png)



PUT: !\[mhs put](screenshots/mhs\_5\_put.png)



DELETE: !\[mhs delete](screenshots/mhs\_6\_delete.png)



GET 404: !\[mhs 404](screenshots/mhs\_7\_get\_404.png)

