print('Praktikum-2\n\n')


a = True
b = False
print('=============Ini and=============')
hasil = a and a
print('Nilai',a,'and',a,'adalah',hasil)
hasil = a and b
print('Nilai',a,'and',b,'adalah',hasil)
hasil = b and a
print('Nilai',b,'and',a,'adalah',hasil)
hasil = b and b
print('Nilai',b,'and',b,'adalah',hasil)

print('\n=============Ini or=============')
hasil = a or a
print('Nilai',a,'or',a,'adalah',hasil)
hasil = a or b
print('Nilai',a,'or',b,'adalah',hasil)
hasil = b or a
print('Nilai',b,'or',a,'adalah',hasil)
hasil = b or b
print('Nilai',b,'or',b,'adalah',hasil)

print('\n=============Ini not=============')
hasil = not a
print('Hasil not',a,'adalah',hasil)
hasil = not b
print('Hasil not',b,'adalah',hasil)

print('\n=============Ini xor=============')
hasil = a ^ a
print('Nilai',a,'xor',a,'adalah',hasil)
hasil = a ^ b
print('Nilai',a,'xor',b,'adalah',hasil)
hasil = b ^ a
print('Nilai',b,'xor',a,'adalah',hasil)
hasil = b ^ b
print('Nilai',b,'xor',b,'adalah',hasil)

print('\n=============Ini nand=============')
hasil = not (a and a)
print('Nilai',a,'nand',a,'adalah',hasil)
hasil = not (a and b)
print('Nilai',a,'nand',b,'adalah',hasil)
hasil = not (b and a)
print('Nilai',b,'nand',a,'adalah',hasil)
hasil = not (b and b)
print('Nilai',b,'nand',b,'adalah',hasil)

print('\n=============Ini nor=============')
hasil = not (a or a)
print('Nilai',a,'nor',a,'adalah',hasil)
hasil = not (a or b)
print('Nilai',a,'nor',b,'adalah',hasil)
hasil = not (b or a)
print('Nilai',b,'nor',a,'adalah',hasil)
hasil = not (b or b)
print('Nilai',b,'nor',b,'adalah',hasil)

print('\n=============Ini nxor=============')
hasil = a ^ a
print('Nilai',a,'nxor',a,'adalah',not hasil)
hasil = a ^ b
print('Nilai',a,'nxor',b,'adalah',not hasil)
hasil = b ^ a
print('Nilai',b,'nxor',a,'adalah',not hasil)
hasil = b ^ b
print('Nilai',b,'nxor',b,'adalah',not hasil)

print('\n ================ IS')
a = 5
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)
a = 6
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

print('\n ================ IS NOT')
a = 5
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)
a = 6
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)

print('\n ================ in')
nama = 'Bacharuddin Jusuf Habibie'

test = 'rud'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'bach'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'ib'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('\n ================ not in')
# Tugas Buat nama menjadi nama lengkap masing2

print('\n ================ in')
data = ['Institut',
        'Teknologi',
        'Bacharuddin',
        'Jusuf',
        'Habibie']
print('Data adalah',data)
test1 = 'Habibie'
test2 = 'Parepare'
test3 = 'Kampus'
test4 = 'Institut'

cek = test1 in data
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 in data
print(test2,'terdapat di data adalah '+str(cek))
cek = test3 in data
print(test3,'terdapat di data adalah '+str(cek))
cek = test4 in data
print(test4,'terdapat di data adalah '+str(cek))

print('\n ================ not in')
# TUGAS dengan cara yang sama buat operator untuk not in

# INI OPERATOR BITWISE
a = 22 #isi dengan tangal lahir
b = 19 #isi dengan bulan lahir
b += 80
print('\n ================ AND')
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('---------------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'biner adalah',format(c,'08b'))

print('\n ================ OR')
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('---------------------------------------OR')
c = a | b
print('Nilai',a,'|',b,'biner adalah',format(c,'08b'))

# Tugas untuk operator XOR, c = a ^ b
# Tugas untuk operator not, c = ~a
# Tugas untuk operator not, c = ~b
# Tugas untuk operator geser kanan, c = a >> 2 
# Tugas untuk operator geser kiri, c = a << 2
# Tugas untuk operator not and, c = ~ (a & b)
# Tugas untuk operator not or, c = ~ (a | b)
# Tugas untuk operator not xor, c = ~ (a ^ b)
# Tugas untuk operator not geser kanan, c = ~(a >> 2) 
# Tugas untuk operator not geser kiri, c = ~(a << 2)



































print('\n'*3)

