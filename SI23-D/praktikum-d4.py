import os
os.system('clear')

a = [6,0,0,2,0,1,0,1,4]
# akses item
print(a)
print(f'item indeks:0 {a[0]}')
print(f'item indeks:3 {a[3]}')
print(f'item indeks:terakhir {a[len(a)-1]}')
# akses item indeks negatif
print(f'item indeks:terakhir (-1) {a[-1]}')
print(f'item indeks:pertama  (-9) {a[-len(a)]}' )
print(f'item indeks:1 (-8) {a[-8]}')
print(f'item indeks:5 (-4) {a[-4]}')
# akses indeks batas
print(f'item indeks:1,2,... {a[1:]}')
print(f'item indeks:3,4,... {a[3:]}')
print(f'item indeks:0,1,2 {a[:3]}')
print(f'item indeks:0,1,2,3,4 {a[:5]}')
print(f'item indeks:semua {a[:]}')
# pengirisan indeks
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:2,3,4 {a[2:5]}')
print(f'item indeks:[1:8] {a[1:-1]}')

# Nested list
kelas = [('Matkul1',3),
         ('Matkul2',2),
         ('Matkul3',2)
         ]
print(f'data kelas {kelas}')
kelas.append(('matkul4',3))
#tambah matkul5 dan jumlah sks
print(f'data kelas {kelas}')

# Nama Mata kuliah 1: Matkul1 dengan jumlah sks:3
# Nama Mata kuliah 2: Matkul2 dengan jumlah sks:2
# Nama Mata kuliah 3: Matkul3 dengan jumlah sks:2
# Nama Mata kuliah 4: Matkul4 dengan jumlah sks:3
# Nama Mata kuliah 5: Matkul5 dengan jumlah sks:3

data = [('Thomas',2023,'Aktif'),
        (90,89,93,97,100),
        (20,22),
        ('S1-Reguler','Sistem Informasi D','Ganjil')]

#  Nama Mahasiswa: Thomas
#  NIM Thomas: 600201014
#  Program pendidikan Thomas: Sistem Informasi D S1-Reguler
#  Angkatan Thomas: 2023-Ganjil
#  Jumlah nilai Thomas adalah: 5
#  Data terbesar Thomas adalah: 100
#  Data terkecil Thomas adalah: 89
#  Rata-rata nilai Thomas adalah: 92.25 

