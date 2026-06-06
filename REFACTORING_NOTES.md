# Catatan Refactoring

## Code Smells yang Ditemukan

### 1. Duplicated Code
Logika perhitungan rata-rata dan juga penentuan grade ditulis dua kali
di fungsi `hitung()` dan `simpan()`. Ini melanggar prinsip DRY 

### 2. Bad Naming
- Nama fungsi `hitung`, `simpan`, `tambah`, `tampil` kurang deskriptif
- Parameter `a, b, c, d, e` tidak jelas maksudnya nilai apa
- Variabel `x` di loop tidak bermakna

### 3. Long Parameter List
Fungsi menerima 5-6 parameter sekaligus. Sebaiknya dikelompokkan (struktur data).

### 4. Global Variable
Variabel `mahasiswa` dibuat global, ini berbahaya dan susah di-maintain.

### 5. Magic Number
Angka 75, 70, 55, 40 langsung ditulis di kode tanpa penjelasan artinya apa.