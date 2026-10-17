
const form = document.querySelector("#formTugas");
const daftarTugas = document.querySelector("#daftarTugas");

const ambilData = () =>
    JSON.parse(localStorage.getItem("tugasITERA")) || [];

const simpanData = (data) => {
    localStorage.setItem("tugasITERA", JSON.stringify(data));
};

class TaskItem {
    constructor(data) {
        this.id = data.id;
        this.nama = data.nama;
        this.matkul = data.matkul;
        this.kategori = data.kategori;
        this.deadline = data.deadline;
        this.prioritas = data.prioritas;
        this.catatan = data.catatan || "";
        this.selesai = data.selesai || false;
    }
}

class DashboardApp {
    constructor() {
        this.tugas = ambilData().map((data) => new TaskItem(data));

        this.tampilkanTanggal();
        this.tampilkanMotivasi();
        this.tampilkanTugas();
        this.ambilCuaca();

        form.addEventListener("submit", (event) => {
            event.preventDefault();
            this.simpanTugas();
        });

        daftarTugas.addEventListener("click", (event) => {
            const tombol = event.target.closest("button");
            if (!tombol) return;

            const { id, aksi } = tombol.dataset;

            if (aksi === "edit") this.editTugas(id);
            if (aksi === "hapus") this.hapusTugas(id);
        });

        daftarTugas.addEventListener("change", (event) => {
            if (event.target.matches(".cek-tugas")) {
                this.ubahStatus(event.target.dataset.id);
            }
        });

        document.querySelector("#tombolBatal").addEventListener("click", () => {
            this.resetForm();
        });
    }

    simpanTugas() {
        const id = document.querySelector("#idTugas").value;

        const data = new TaskItem({
            id: id || String(Date.now()),
            nama: document.querySelector("#nama").value.trim(),
            matkul: document.querySelector("#matkul").value.trim(),
            kategori: document.querySelector("#kategori").value,
            deadline: document.querySelector("#deadline").value,
            prioritas: document.querySelector("#prioritas").value,
            catatan: document.querySelector("#catatan").value.trim(),
            selesai: false
        });

        if (id) {
            const lama = this.tugas.find((tugas) => tugas.id === id);

            this.tugas = this.tugas.map((tugas) =>
                tugas.id === id
                    ? { ...data, selesai: lama.selesai }
                    : tugas
            );
        } else {
            this.tugas.push(data);
        }

        this.simpanDanTampilkan();
        this.resetForm();
    }

    tampilkanTugas() {
        if (this.tugas.length === 0) {
            daftarTugas.innerHTML =
                '<p class="kosong">Belum ada tugas. Silakan tambahkan tugas.</p>';
            return;
        }

        daftarTugas.innerHTML = this.tugas.map((tugas) => `
            <div class="item-tugas ${tugas.selesai ? "tugas-selesai" : ""}">
                <input type="checkbox" class="cek-tugas"
                    data-id="${tugas.id}" ${tugas.selesai ? "checked" : ""}>

                <div class="info-tugas">
                    <h3>${this.aman(tugas.nama)}</h3>
                    <span class="label-kategori">${this.aman(tugas.kategori)}</span>
                    <p>${this.aman(tugas.matkul)} · ${this.aman(tugas.deadline)}</p>
                    <p>Prioritas: ${this.aman(tugas.prioritas)}</p>
                    ${tugas.catatan ? `<p>${this.aman(tugas.catatan)}</p>` : ""}
                </div>

                <div class="aksi">
                    <button class="edit" data-aksi="edit" data-id="${tugas.id}">Edit</button>
                    <button class="hapus" data-aksi="hapus" data-id="${tugas.id}">Hapus</button>
                </div>
            </div>
        `).join("");
    }

    editTugas(id) {
        const tugas = this.tugas.find((item) => item.id === id);
        if (!tugas) return;

        document.querySelector("#idTugas").value = tugas.id;
        document.querySelector("#nama").value = tugas.nama;
        document.querySelector("#matkul").value = tugas.matkul;
        document.querySelector("#kategori").value = tugas.kategori;
        document.querySelector("#deadline").value = tugas.deadline;
        document.querySelector("#prioritas").value = tugas.prioritas;
        document.querySelector("#catatan").value = tugas.catatan;

        document.querySelector("#tombolSimpan").textContent = "Simpan";
        document.querySelector("#tombolBatal").hidden = false;

        form.scrollIntoView({ behavior: "smooth" });
    }

    hapusTugas(id) {
        if (!confirm("Hapus tugas ini?")) return;

        this.tugas = this.tugas.filter((tugas) => tugas.id !== id);
        this.simpanDanTampilkan();
    }

    ubahStatus(id) {
        this.tugas = this.tugas.map((tugas) =>
            tugas.id === id
                ? { ...tugas, selesai: !tugas.selesai }
                : tugas
        );

        this.simpanDanTampilkan();
    }

    simpanDanTampilkan() {
        simpanData(this.tugas);
        this.tampilkanTugas();
    }

    resetForm() {
        form.reset();
        document.querySelector("#idTugas").value = "";
        document.querySelector("#tombolSimpan").textContent = "Tambah";
        document.querySelector("#tombolBatal").hidden = true;
    }

    tampilkanTanggal() {
        document.querySelector("#tanggal").textContent =
            new Date().toLocaleDateString("id-ID", {
                timeZone: "Asia/Jakarta",
                day: "numeric",
                month: "short",
                year: "numeric"
            });
    }

    tampilkanMotivasi() {
        const daftar = [
            "Sedikit demi sedikit, tugas pasti selesai.",
            "Jangan menunda tugas yang bisa dikerjakan hari ini.",
            "Tetap semangat belajar dan berproses."
        ];

        const nomor = Math.floor(Math.random() * daftar.length);
        document.querySelector("#motivasi").textContent = daftar[nomor];
    }

    async ambilCuaca() {
        const elemen = document.querySelector("#cuaca");

        try {
            const respons = await fetch(
                "https://api.open-meteo.com/v1/forecast?latitude=-5.36&longitude=105.31&current=temperature_2m&timezone=Asia%2FJakarta"
            );

            if (!respons.ok) throw new Error("Cuaca gagal dimuat");

            const data = await respons.json();
            const { temperature_2m } = data.current;

            elemen.textContent = `📍 ITERA: ${temperature_2m}°C`;
        } catch (error) {
            elemen.textContent = "Cuaca tidak tersedia";
        }
    }

    aman(teks) {
        return String(teks).replace(/[&<>"']/g, (huruf) => ({
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#39;"
        })[huruf]);
    }
}

const dashboard = new DashboardApp();
