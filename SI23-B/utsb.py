''' SOAL
Misalkan anda diberikan tugas untuk membuat program struk pembelian pada kasir di perusahaan Alat Tulis Kantor (ATK). Pilih 5 barang ATK dengan harga masing-masing barang kemudian buatkan program dan ouputnya seperti berikut.

- Buat list data perusahaan
mdata = [Nama Lengkap,
         mahasiswa@ith.ac.id,
         PT. ABC Design,
         JL. BALAIKOTA NO.1,
         PAREPARE,
         Nama Kasir,
         25 Oktober 2023]
(NOTED: ubah Nama Lengkap, e-mail, Nama Kasir, Tanggal-Bulan-Tahun Lahir)

- Buat Nested list 5 barang:
djual = [['Barang1','Barang2','Barang3','Barang4','Barang5'],
         ['B2001','B2002','B2003','B2004','B2005'],
         [55,25,150,5,10],
         [2,2,2,2,2]]
(NOTED: ubah nama barang dan harga barang sesuai keinginan)

- Hasil Runing

                                   PT. ABC DESIGN
                            JL. BALAIKOTA NO.1 PAREPARE
                            e-Mail: mahasiswa@ith.ac.id


MANAJER           : Nama Lengkap
KASIR             : Nama Kasir
Tanggal Pembelian : 25 Oktober 2023
|-|--   13    --|--       19      --|--     15    --|--  8 --|--    14    --| 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
No. Kode Barang |    Nama Barang    |   H. Satuan   | Jumlah |     Total    |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1   B2001       | Barang1           |      Rp27000,-|    2   |     Rp54000,-|
2   B2002       | Barang2           |      Rp75000,-|    2   |    Rp150000,-|
3   B2003       | Barang3           |      Rp12000,-|    2   |     Rp24000,-|
4   B2004       | Barang4           |      Rp10000,-|    2   |     Rp20000,-|
5   B2005       | Barang5           |       Rp3000,-|    2   |      Rp6000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                    SUBTOTAL:           10   |    Rp254000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|-----------------------------------77--------------------------------------|
Summary:
Harga tertinggi adalah    : Rp750000,- (B2002 - Barang 2)
Harga terendah  adalah    : Rp3000,-   (B2005 - Barang 5)
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
Kelas\t\t: Sistem Informasi B''')

#Answer in below
mdata = ['Nama Lengkap',
         'mahasiswa@ith.ac.id',
         'PT. ABC Design',
         'JL. BALAIKOTA NO.1 ',
         'PAREPARE',
         'Nama Kasir',
         '25 Oktober 2023']

djual = [['Barang1','Barang2','Barang3','Barang4','Barang5'],
         ['B2001','B2002','B2003','B2004','B2005'],
         [55,25,150,5,10],
         [2,2,2,2,2]]
r=1000
#   PT. ABC DESIGN
print(mdata[2].center(77))
print((mdata[3]+mdata[4]).center(77))
print(mdata[1].center(77))
print('\n')
                            # JL. BALAIKOTA NO.1 PAREPARE
                            # e-Mail: mahasiswa@ith.ac.id
print(f'''MANAJER           : {mdata[0]}
KASIR             : {mdata[5]}
Tanggal Pembelian : {mdata[-1]}''')

print('-'*77)
print('No.'+'|'+'Kode Barang'.center(13)+'|'+'Nama Barang'.center(19)+'|'+'H.Satuan'.center(15)+'|'+'Jumlah'.center(8)+'|'+'Total'.center(13)+'|')
print('-'*77)
print('1. '+'|'+djual[1][0].ljust(13)+'|'+djual[0][0].ljust(19)+'|'+f'Rp{djual[2][0]*r},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{2*r*djual[2][0]},-'.rjust(13)+'|')
print('2. '+'|'+djual[1][1].ljust(13)+'|'+djual[0][1].ljust(19)+'|'+f'Rp{djual[2][1]*r},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{2*r*djual[2][1]},-'.rjust(13)+'|')
print('3. '+'|'+djual[1][2].ljust(13)+'|'+djual[0][2].ljust(19)+'|'+f'Rp{djual[2][2]*r},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{2*r*djual[2][2]},-'.rjust(13)+'|')
print('4. '+'|'+djual[1][3].ljust(13)+'|'+djual[0][3].ljust(19)+'|'+f'Rp{djual[2][3]*r},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{2*r*djual[2][3]},-'.rjust(13)+'|')
print('5. '+'|'+djual[1][4].ljust(13)+'|'+djual[0][4].ljust(19)+'|'+f'Rp{djual[2][4]*r},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{2*r*djual[2][4]},-'.rjust(13)+'|')
print('-'*77)
print(f'SubTotal = Rp{2*r*sum(djual[2])},-'.rjust(77))
print('-'*77)
print(f'''Summary:
Harga tertinggi adalah    : Rp{max(djual[2])*r},- ({djual[1][1]} - {djual[0][1]})
Harga terendah  adalah    : Rp3000,-   (B2005 - Barang 5)
Harga rata-rata pembelian : Rp ,-''')

