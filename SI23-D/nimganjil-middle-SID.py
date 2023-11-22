'''
Misalkan anda diberikan tugas untuk membuat program struk pembelian pada kasir di perusahaan alat-alat komputer. Pilih 5 barang Alat Komputer dengan harga masing-masing barang kemudian buatkan program dan ouputnya seperti berikut.

- Buat list data perusahaan
mdata = [PT. XYZ Komputer,
        JL. BALAIKOTA NO.1,
        Kota Parepare,
        Nama Lengkap,
        mahasiswa@ith.ac.id,
        Nama Kasir,
        25 Oktober 2023]
(NOTED: ubah Nama Lengkap, e-mail, Nama Kasir, Tanggal-Bulan-Tahun Lahir)

- Buat Nested list untuk 5 barang:

djual = [['D0001','D0002','D0003','D0004','D0005'],
        ['Barang1','Barang2','Barang3','Barang4','Barang5'],
        [15,5,75,3,10],
        [3,3,3,3,3]]
(NOTED: ubah nama barang dan harga barang sesuai keinginan)

- Hasil Runing
                                 PT. XYZ KOMPUTER
                          JL. BALAIKOTA NO.2 KOTA PAREPARE
                             e-Mail: mahasiswa@ith.ac.id


MANAJER           : Nama Lengkap
KASIR             : Nama Kasir
Tanggal Pembelian : 25 Oktober 2023
|--     16    --|--       19      --|--     15    --|--  8 --|--    14    --| 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
No. Kode Barang |    Nama Barang    |   H. Satuan   | Jumlah |     Total    |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1   D1101       | Barang1           |      Rp15000,-|    3   |     Rp45000,-|
2   D1102       | Barang2           |       Rp5000,-|    3   |     Rp15000,-|
3   D1103       | Barang3           |      Rp50000,-|    3   |    Rp150000,-|
4   D1104       | Barang4           |       Rp3000,-|    3   |     Rp15000,-|
5   D1105       | Barang5           |      Rp10000,-|    3   |     Rp30000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                    SUBTOTAL:           15   |    Rp245000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Summary:
Harga tertinggi adalah    : Rp50000,-  (D1103 - Barang3)
Harga terendah  adalah    : Rp3000,-   (D1104 - Barang4)
Harga rata-rata pembelian : Rp ,-
                                                   Parepare, 25 Oktober 2023
                                          



                                                         NAMA LENGKAP      
                                                         ------------
                                                            MANAJER

'''


# Write your code in below!

print('''
Nama\t\t: Nama Lengkap
NIM\t\t: NIM-Anda
Nomor Komputer\t: 00
Kelas\t\t: Sistem Informasi D''')

#Answer in below

mdata = ['PT. XYZ Komputer',
        'JL. BALAIKOTA NO.1',
        'Kota Parepare',
        'Nama Lengkap',
        'mahasiswa@ith.ac.id',
        'Nama Kasir',
        '25 Oktober 2023']

djual = [['D0001','D0002','D0003','D0004','D0005'],
        ['Barang1','Barang2','Barang3','Barang4','Barang5'],
        [15,5,75,3,10],
        [3,3,3,3,3]]
r = 1000
                                 # PT. XYZ KOMPUTER
print(mdata[0].center(72))
print(mdata[1].center(72))
print(mdata[4].center(72))
print('\n')
print(f'''MANAJER           : {mdata[3]}
KASIR             : {mdata[-2]}
Tanggal Pembelian : {mdata[-1]}''')
print('-'*(77))
print('No. Kode Barang'.ljust(16)+'|'+'Nama Barang'.center(19)+'|'+'H. Satuan'.center(15)+'|'+'Jumlah'.center(8)+'|'+'Total'.center(14)+'|')
print('-'*(77))

print(f'1.  {djual[0][0]}'.ljust(16)+'|'+f' {djual[1][0]}'.ljust(19)+'|'+f'Rp{djual[2][0]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*djual[2][0]*r},-'.center(14)+'|')
print(f'1.  {djual[0][0]}'.ljust(16)+'|'+f' {djual[1][0]}'.ljust(19)+'|'+f'Rp{djual[2][0]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*djual[2][0]*r},-'.center(14)+'|')
print(f'1.  {djual[0][0]}'.ljust(16)+'|'+f' {djual[1][0]}'.ljust(19)+'|'+f'Rp{djual[2][0]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*djual[2][0]*r},-'.center(14)+'|')
print(f'1.  {djual[0][0]}'.ljust(16)+'|'+f' {djual[1][0]}'.ljust(19)+'|'+f'Rp{djual[2][0]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*djual[2][0]*r},-'.center(14)+'|')

print('-'*(77))
                        #   JL. BALAIKOTA NO.2 KOTA PAREPARE
                        #      e-Mail: mahasiswa@ith.ac.id 

