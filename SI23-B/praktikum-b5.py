import os
os.system('clear')

nim = [6,0,0,2,0,1,0,1,4]
print(nim)
# akses item
print('item indeks 0:',nim[0])
print('item indeks 3:',nim[3])
print('item indeks terakhir:',nim[len(nim)-1])
# akses indeks negatif
print('item indeks terakhir:',nim[-1])
print('item indeks pertama:',nim[-len(nim)])
print('item indeks 3: [-6] ',nim[-6])
print('item indeks 5: [-4] ',nim[-4])
print('item indeks -7: [2] ',nim[2])
print('item indeks 2: [-7] ',nim[-7])
# akses indeks batas
print(f'item indeks 1,2,....: {nim[1:]}')
print(f'item indeks 3,4,....: {nim[3:]}')
print(f'item indeks 0,1,2,3: {nim[:4]}')
print(f'item indeks 0: {nim[:1]}')
print(f'item indeks semua: {nim[:]}')
print(f'item indeks [:8]: {nim[:-1]}')
print(f'item indeks [:4]: {nim[:-5]}')
# pengirisan
print(f'item indeks 1,2: {nim[1:3]}')
print(f'item indeks []: {nim[3:3]}')
print(f'item indeks 2,3,4: {nim[2:5]}')
print(f'item indeks [1:8]: {nim[1:-1]}')
print(f'item indeks [2:7]: {nim[2:-2]}')
# Nested List
kelas = [('Matkul1',2),
         ('Matkul2',3)]
print(kelas)
kelas.append(('matkul3',2))
print(kelas)
# tambahkan matkul 4 dan 5 dan sksnya

# Mata kuliah 1: Matkul1 dengan 2 sks
# Mata kuliah 2: Matkul2 dengan 3 sks
# Mata kuliah 3: Matkul3 dengan 2 sks
# Mata kuliah 4: Matkul4 dengan .. sks
# Mata kuliah 5: Matkul5 dengan .. sks

data = [('Frankel',2023,'Aktif'),
        (76,98,89,97,99),
        [2,3,2,2,2],
        ('S1-Reguler','Sistem Informasi B','Ganjil')]

# Nama mahasiswa: Frankel
# Inisial Frankel: F
# NIM Frankel: 600201014
# Program Frankel: S1-Reguler Sistem Informasi B
# Angkatan Frankel: Ganjil-2023
# Total sks Frankel adalah: 11
# Jumlah Nilai Frankel: 5
# Nilai tertinggi Frankel: 99
# Nilai terendah Frankel: 76
# Rata-rata nilai Frankel: 92.25







