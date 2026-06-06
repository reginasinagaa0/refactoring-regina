# nilai.py = eliminasi duplikasi dengan OOP

BATAS_GRADE = {
    "A": 75,
    "B": 70,
    "C": 55,
    "D": 40,
}

class Mahasiswa:
    def __init__(self, nama, daftar_nilai):
        self.nama = nama
        self.daftar_nilai = daftar_nilai
        self.rata_rata = self._hitung_rata_rata()
        self.grade = self._tentukan_grade()

    def _hitung_rata_rata(self):
        return sum(self.daftar_nilai) / len(self.daftar_nilai)

    def _tentukan_grade(self):
        for grade, batas in BATAS_GRADE.items():
            if self.rata_rata >= batas:
                return grade
        return "E"

    def tampilkan(self):
        print(f"Nama: {self.nama}, Rata-rata: {self.rata_rata:.2f}, Grade: {self.grade}")


class KelasNilai:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah(self, nama, daftar_nilai):
        mhs = Mahasiswa(nama, daftar_nilai)
        self.daftar_mahasiswa.append(mhs)

    def tampilkan_semua(self):
        for mhs in self.daftar_mahasiswa:
            mhs.tampilkan()


if __name__ == "__main__":
    kelas = KelasNilai()
    kelas.tambah("Budi", [80, 75, 90, 85, 70])
    kelas.tambah("Ani", [60, 55, 65, 70, 50])
    kelas.tambah("Citra", [40, 45, 35, 50, 30])
    kelas.tampilkan_semua()