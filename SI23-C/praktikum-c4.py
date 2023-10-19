import os
os.system('clear')

nim = ['6','0','0','2','0','1','0','1','4']

print(nim)

print('item indeks 0 (pertama)',nim[0])
print('item indeks 1 (kedua)',nim[1])

print(f'item indeks 0 (pertama) {nim[0]}')
print(f'item indeks 1 (kedua)   {nim[1]}')
print(f'item indeks terakhir {nim[len(nim)-1]}')
print(f'item indeks terakhir {nim[-1]}')
print(f'item indeks (pertama) {nim[-len(nim)]}')

data = ['Von Neumann',2023,'Aktif']
nilai= [90,89,93,97]
print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])

# >> Von Neumann status Kuliah: Aktif
print(f'{data[0]} status Kuliah: {data[2]}')
# >> Data terbesar nilai adalah: 97
print(f'Data terbesar nilai adalah: {max(nilai)}')
# >> Data terkecil nilai adalah: 89
print(f'Data terkecil nilai adalah: {min(nilai)}')
# >> Rata-rata nilai adalah: 92.25
rataan = sum(nilai)/len(nilai)
print(f'Rata-rata nilai adalah: {rataan}')
# >> Jumlah nilai mahasiswa adalah: 4
print(f'Jumlah nilai {data[0]} adalah: {len(nilai)}')

data = [['Von Neumann',2023,'Aktif'],
        [90,89,93,97],
        [20,22],
        ['S1-Reguler','Ganjil']]

matkul = ['Matkul1',
          'matkul2',
          'matkul3',
          'matkul4',
          'matkul5']
sks = [2,3,2,3,3]

# Tambahkan matkul dan sks ke dalam data (pakai append)

print(data[0][0])
print(data[-1][0])
print(data[2][0:])

# Daftar Mata kuliah
# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
# Mata kuliah 3: Matkul3 dengan jumlah 2 sks
# Mata kuliah 4: Matkul4 dengan jumlah 3 sks
# Mata kuliah 5: Matkul5 dengan jumlah 3 sks
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
# Mata kuliah 8: Matkul8 dengan jumlah .. sks

# Tambah Nilai jadi 8 (pakai append)

# Nama mahasiswa: Von Neumann
# Inisial Von Neumann: V N
# NIM Von Neumann: 600201014
# Program Von Neumann: S1-Reguler Sistem Informasi B
# Angkatan Von Neumann: Ganjil-2023
# Total sks Von Neumann adalah: 11
# Jumlah Nilai Von Neumann: 5
# Nilai tertinggi Von Neumann: 99
# Nilai terendah Von Neumann: 76
# Rata-rata nilai Von Neumann: 92.25

