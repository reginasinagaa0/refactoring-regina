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
    """Representasi data mahasiswa beserta nilainya."""

    def __init__(self, nama: str, daftar_nilai: List[float]) -> None:
        """
        Inisialisasi objek Mahasiswa.

        Args:
            nama: Nama lengkap mahasiswa.
            daftar_nilai: List nilai ujian mahasiswa.
        """
        self.nama = nama
        self.daftar_nilai = daftar_nilai
        self.rata_rata = self._hitung_rata_rata()
        self.grade = self._tentukan_grade()

    def _hitung_rata_rata(self) -> float:
        """Menghitung nilai rata-rata dari daftar nilai."""
        return sum(self.daftar_nilai) / len(self.daftar_nilai)

    def _tentukan_grade(self) -> str:
        """Menentukan grade berdasarkan rata-rata nilai."""
        for grade, batas in BATAS_GRADE.items():
            if self.rata_rata >= batas:
                return grade
        return "E"

    def tampilkan(self) -> None:
        """Menampilkan informasi mahasiswa ke konsol."""
        print(f"Nama: {self.nama}, Rata-rata: {self.rata_rata:.2f}, Grade: {self.grade}")


class KelasNilai:
    """Mengelola kumpulan data mahasiswa dalam satu kelas."""

    def __init__(self) -> None:
        """Inisialisasi kelas dengan daftar mahasiswa kosong."""
        self.daftar_mahasiswa: List[Mahasiswa] = []

    def tambah(self, nama: str, daftar_nilai: List[float]) -> None:
        """
        Menambahkan mahasiswa baru ke dalam kelas.

        Args:
            nama: Nama mahasiswa.
            daftar_nilai: List nilai ujian.
        """
        mahasiswa = Mahasiswa(nama, daftar_nilai)
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_semua(self) -> None:
        """Menampilkan data seluruh mahasiswa dalam kelas."""
        for mahasiswa in self.daftar_mahasiswa:
            mahasiswa.tampilkan()


if __name__ == "__main__":
    kelas = KelasNilai()
    kelas.tambah("doni", [80, 75, 90, 85, 70])
    kelas.tambah("Ana", [60, 55, 65, 70, 50])
    kelas.tambah("Cici", [40, 45, 35, 50, 30])
    kelas.tampilkan_semua()