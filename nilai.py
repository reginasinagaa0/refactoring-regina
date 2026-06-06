"""
Modul manajemen nilai mahasiswa.
Menghitung rata-rata dan menentukan grade berdasarkan standar penilaian.
"""

from typing import List

BATAS_GRADE: dict = {
    "A": 75,
    "B": 70,
    "C": 55,
    "D": 40,
}

class Mahasiswa:

    def __init__(self, nama: str, daftar_nilai: List[float]) -> None:
        self.nama = nama
        self.daftar_nilai = daftar_nilai
        self.rata_rata = self._hitung_rata_rata()
        self.grade = self._tentukan_grade()

    def _hitung_rata_rata(self) -> float:
        return sum(self.daftar_nilai) / len(self.daftar_nilai)

    def _tentukan_grade(self) -> str:
        for grade, batas in BATAS_GRADE.items():
            if self.rata_rata >= batas:
                return grade
        return "E"

    def tampilkan(self) -> None:
        print(f"Nama: {self.nama}, Rata-rata: {self.rata_rata:.2f}, Grade: {self.grade}")


class KelasNilai:

    def __init__(self) -> None:
        self.daftar_mahasiswa: List[Mahasiswa] = []

    def tambah(self, nama: str, daftar_nilai: List[float]) -> None:
        mahasiswa = Mahasiswa(nama, daftar_nilai)
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_semua(self) -> None:
        for mahasiswa in self.daftar_mahasiswa:
            mahasiswa.tampilkan()


if __name__ == "__main__":
    kelas = KelasNilai()
    kelas.tambah("doni", [80, 75, 90, 85, 70])
    kelas.tambah("Ana", [60, 55, 65, 70, 50])
    kelas.tambah("Cici", [40, 45, 35, 50, 30])
    kelas.tampilkan_semua()