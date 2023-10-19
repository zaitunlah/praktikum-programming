import os
os.system('clear')


nim = ['6','0','0','2','0','1','0','1','4']
# nim2 = '600201014'
print(nim)
# print(nim2[1:3])

# akses item
print(f'item indeks 0: {nim[0]}')
print(f'item indeks 4: {nim[4]}')
print(f'item indeks terakhir: {nim[len(nim)-1]}')

# akses indeks negatif
print(f'item indeks terakhir: {nim[-1]}')
print(f'item indeks pertama: {nim[-len(nim)]}')
print(f'item indeks 6 [-3]: {nim[-3]}')
print(f'item indeks 4 [-5]: {nim[-5]}')
print(f'item indeks 7 [-2]: {nim[-2]}')

# akses indeks batas
print(f'item indeks 1,2,...: \n {nim[1:]}')
print(f'item indeks 3,4,...: \n {nim[3:]}')
print(f'item indeks 0,1,2: \n {nim[:3]}')
print(f'item indeks 0,1,2,3: \n {nim[:4]}')
print(f'item indeks semua: \n {nim[:]}')
print(f'item indeks [:8]: \n {nim[:-1]}')
print(f'item indeks [:6]: \n {nim[:-3]}')

# pengirisan
print(f'item indeks 1,2 : \n {nim[1:3]}')
print(f'item indeks 2,3,4 : \n {nim[2:5]}')
print(f'item indeks kosong : \n {nim[3:3]}')
print(f'item indeks [8:8] kosong : \n {nim[-1:-1]}')
print(f'item indeks [1:8]: \n {nim[1:-1]}')
print(f'item indeks [2:7]: \n {nim[2:-2]}')


data = [['Thomas',2023,'Aktif'],
[90,89,93,97],
[20,22],
['S1-Reguler','Ganjil']]

matkul = ['Matkul1','Matkul2','Matkul3','Matkul4']
sks    = [2,3,3,2]
# Menambahkan matkul dan sks ke dalam data (di akhir)
data.append(matkul)
data.append(sks)

# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
# Mata kuliah 3: Matkul3 dengan jumlah 3 sks
# Mata kuliah 4: Matkul4 dengan jumlah 2 sks
data[4].append('Matkul5')
data[5].append(2)
# print(data)
# Tambahkan 3 matkul dengan sks nya

# Mata kuliah 6: Matkul6 dengan jumlah .. sks
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
# Mata kuliah 8: Matkul8 dengan jumlah .. sks

# Tambahkan 8 nilai masing-masing

print(data[0][0])
print(data[-1][0])
print(data[2][0:])

# >> Tugas: Nama Mahasiswa Thomas dengan NIM: 600201014
# >> Program pendidikan Thomas: S1-Reguler
print(f'Program pendidikan {data[0][0]}: {data[-1][0]}')
# >> Angkatan : 2023-Ganjil
print(f'Angkatan : {data[0][1]}-{data[-1][1]}')
# >> Jumlah nilai Thomas adalah: 4
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')
# >> Data terbesar Thomas adalah: 97
print(f'Data terbesar {data[0][0]} adalah: {max(data[1])}')
# >> Data terkecil Thomas adalah: 89
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}')
# >> Rata-rata nilai Thomas adalah: 92.25
x_bar = sum(data[1])/len(data[1])
print(f'Rata-rata nilai {data[0][0]} adalah: {x_bar}')






