def hitung(a, b, c, d, e):
    total = a + b + c + d + e
    rata = total / 5
    if rata >= 75:
        print("A")
    elif rata >= 70:
        print("B")
    elif rata >= 55:
        print("C")
    elif rata >= 40:
        print("D")
    else:
        print("E")

def simpan(nama, a, b, c, d, e):
    total = a + b + c + d + e
    rata = total / 5
    if rata >= 75:
        grade = "A"
    elif rata >= 70:
        grade = "B"
    elif rata >= 55:
        grade = "C"
    elif rata >= 40:
        grade = "D"
    else:
        grade = "E"
    data = [nama, a, b, c, d, e, rata, grade]
    return data

mahasiswa = []

def tambah(nm, n1, n2, n3, n4, n5):
    mahasiswa.append(simpan(nm, n1, n2, n3, n4, n5))

def tampil():
    for x in mahasiswa:
        print(x[0], x[6], x[7])

tambah("rena", 80, 75, 90, 85, 70)
tambah("susi", 60, 55, 65, 70, 50)
tambah("didi", 40, 45, 35, 50, 30)
tampil()