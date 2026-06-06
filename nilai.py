# nilai.py - afterperbaikan penamaan dan magic number

BATAS_GRADE_A = 75
BATAS_GRADE_B = 70
BATAS_GRADE_C = 55
BATAS_GRADE_D = 40

def tentukan_grade(rata_rata):
    if rata_rata >= BATAS_GRADE_A:
        return "A"
    elif rata_rata >= BATAS_GRADE_B:
        return "B"
    elif rata_rata >= BATAS_GRADE_C:
        return "C"
    elif rata_rata >= BATAS_GRADE_D:
        return "D"
    else:
        return "E"

def hitung_rata_rata(daftar_nilai):
    return sum(daftar_nilai) / len(daftar_nilai)

mahasiswa = []

def tambah_mahasiswa(nama, daftar_nilai):
    rata_rata = hitung_rata_rata(daftar_nilai)
    grade = tentukan_grade(rata_rata)
    mahasiswa.append([nama, daftar_nilai, rata_rata, grade])

def tampilkan_semua():
    for data in mahasiswa:
        print(f"Nama: {data[0]}, Rata-rata: {data[2]:.2f}, Grade: {data[3]}")

tambah_mahasiswa("Budi", [80, 75, 90, 85, 70])
tambah_mahasiswa("Ani", [60, 55, 65, 70, 50])
tambah_mahasiswa("Citra", [40, 45, 35, 50, 30])
tampilkan_semua()