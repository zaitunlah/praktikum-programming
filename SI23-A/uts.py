import os
os.system('clear')
nama = 'Nama Lengkap'
nim  = '6002201014'
prodi= 'Sistem Informasi A'
th_masuk = 2023
sem  = 'Ganjil'
lahir = 'Parepare, 25 Oktober 2023'
matkul1 = ['Pengantar Pemrograman',
           '22A111209',
           '3',
           'Senin',
           '07.30-09.10']

print('INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE'.center(72))
print('JURUSAN SAINS'.center(72))
print('KARTU RENCANA STUDI MAHASISWA'.center(72))
print('\n')
print(f'''Nama Mahasiswa\t: {nama}
NIM\t\t: {nim}
Program/prodi\t: S1/{prodi}
Tahun Masuk\t: {th_masuk} {sem}''')
print('- '*36)
print('No.'.ljust(3)+'|'+'Kode'.center(12)+'|'+'Mata Kuliah'.center(24)+'|'+'SKS'.center(5)+'|'+'Hari'.center(8)+'|'+'Jadwal'.center(14)+'|')
print('- '*36)
print('1'.ljust(3)+'|'+matkul1[1].ljust(12)+'|'+matkul1[0].ljust(24)+'|'+matkul1[2].center(5)+'|'+matkul1[3].ljust(8)+'|'+matkul1[4].rjust(14)+'|')

print('2'.ljust(3)+'|'+'22A111210'.ljust(12)+'|'+'Kalkulus Dasar I'.ljust(24)+'|'+'3'.center(5)+'|'+'Selasa'.ljust(8)+'|'+'07.30-09.10'.rjust(14)+'|')
print('3'.ljust(3)+'|'+'22A111211'.ljust(12)+'|'+'Agama Islam'.ljust(24)+'|'+'3'.center(5)+'|'+'Rabu'.ljust(8)+'|'+'07.30-09.10'.rjust(14)+'|')
print('4'.ljust(3)+'|'+'22A111212'.ljust(12)+'|'+'CINTA'.ljust(24)+'|'+'3'.center(5)+'|'+'Kamis'.ljust(8)+'|'+'07.30-09.10'.rjust(14)+'|')
print('5'.ljust(3)+'|'+'22A111213'.ljust(12)+'|'+'Pancasila'.ljust(24)+'|'+'3'.center(5)+'|'+'Jum\'at'.ljust(8)+'|'+'07.30-09.10'.rjust(14)+'|')
print('- '*36)
print(lahir.rjust(36*2))
print('\n'*2)
print(nama.upper().center(len(lahir)).rjust(72))
print(('-'*len(nama)).center(25).rjust(72))