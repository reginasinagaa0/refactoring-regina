# Tugas Konstruksi Perangkat Lunak
**Nama:** Regina Sinaga  
**Username GitHub:** reginasinagaa0  
**Mata Kuliah:** Konstruksi Perangkat Lunak

## Deskripsi Project
Aplikasi manajemen nilai mahasiswa yang dibangun mengikuti coding standards 
dan telah melalui proses refactoring dari kode awal yang mengandung code smells.

## Riwayat Refactoring
| Commit | Perubahan |
|--------|-----------|
| Initial commit | Kode awal dengan code smells |
| Refactor 1 | Perbaikan penamaan & ekstrak magic number jadi konstanta |
| Refactor 2 | Eliminasi duplikasi, terapkan OOP, hapus global variable |
| Refactor 3 | Tambah docstring, type hints, terapkan coding standards PEP8 |

## Code Smells yang Diperbaiki
- **Duplicated Code** – logika grade ditulis berulang di dua fungsi
- **Bad Naming** – nama fungsi dan variabel tidak deskriptif
- **Long Parameter List** – terlalu banyak parameter di fungsi
- **Global Variable** – variabel global diganti dengan class
- **Magic Number** – angka batas grade dijadikan konstanta

## Cara Menjalankan
```bash
python nilai.py
```