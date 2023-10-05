print('praktikum-a2\n')

print('NAMA     : NAMA')
print('NIM      : NIM')
print('Prodi    : Sistem Informasi A\n')

# INI OPERATOR ASSIGNMENT
a = 19
print('Nilai a adalah',a)
a += 3
print('Nilai a+=3 adalah',a)

a = 19
print('Nilai a adalah',a)
a -= 3
print('Nilai a-=3 adalah',a)

a = 19
print('Nilai a adalah',a)
a *= 2
print('Nilai a*=2 adalah',a)

a = 19
print('Nilai a adalah',a)
a /= 2
print('Nilai a/=2 adalah',a)

a = 3
print('Nilai a adalah',a)
a **= 2
print('Nilai a**=2 adalah',a)

a = 35
print('Nilai a adalah',a)
a %= 32
print('Nilai a%=32 adalah',a)

a = 35
print('Nilai a adalah',a)
a //= 32
print('Nilai a//=32 adalah',a)

# Tugas melanjutkan untuk operator selanjutnya line 25-line 59

# OPERATOR PERBANDINGAN
a = 9
b =13
print('\n--------- Besar dari 13 #ujung nim')
hasil = a > 13 #ujung nim
print(a,'> 13 adalah',hasil)
hasil = b > 13 #ujung nim
print(b,'> 13 adalah',hasil)

print('\n--------- Kecil dari 13 #ujung nim')
hasil = a < 13 #ujung nim
print(a,'< 13 adalah',hasil)
hasil = b < 13 #ujung nim
print(b,'< 13 adalah',hasil)

print('\n--------- Besar atau Sama dari 13 #ujung nim')
# hasil = a >= 13
# hasil = b >= 13

print('\n--------- Kecil atau Sama dari 13 #ujung nim')
# hasil = a <= 13
# hasil = b <= 13

print('\n--------- Sama dari 13 #ujung nim')
# hasil = a == 13
# hasil = b == 13

print('\n--------- Tidak Sama dari 13 #ujung nim')
# hasil = a != 13
# hasil = b != 13

# OPERATOR LOGIKA
a = True
b = False
print('\n==========AND===========')

hasil = a and a
print(a,'and',a,'hasilnya =',hasil)

hasil = a and b
print(a,'and',b,'hasilnya =',hasil)

hasil = b and a
print(b,'and',a,'hasilnya =',hasil)

hasil = b and b
print(b,'and',b,'hasilnya =',hasil)

print('\n==========OR===========')
# Tugas hasil = a or a
# Tugas hasil = a or b
# Tugas hasil = b or a
# Tugas hasil = b or b

print('\n==========XOR===========')

hasil = a ^ a
print(a,'xor',a,'hasilnya =',hasil)

hasil = a ^ b
print(a,'xor',b,'hasilnya =',hasil)

hasil = b ^ a
print(b,'xor',a,'hasilnya =',hasil)

hasil = b ^ b
print(b,'xor',b,'hasilnya =',hasil)

print('\n==========NOT===========')

hasil = not a
print('not',a,'hasilnya =',hasil)
hasil = not b
print('not',b,'hasilnya =',hasil)

# OPERATOR MEMBERSHIP
print('\n===================IN')
nama = 'Habibie'

test = 'bi'
cek = test in nama
print(test,'terdapat di',nama,'adalah',cek)

test = 'ib'
cek = test in nama
print(test,'terdapat di',nama,'adalah',cek)
print()
test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print(test1,'terdapat di',nama,'adalah',cek)
cek = test2 in nama
print(test2,'terdapat di',nama,'adalah',cek)
cek = test3 in nama
print(test3,'terdapat di',nama,'adalah',cek)
cek = test4 in nama
print(test4,'terdapat di',nama,'adalah',cek)
cek = test5 in nama
print(test5,'terdapat di',nama,'adalah',cek)

print('\n===================NOT IN')
# Tugas Lanjutkan untuk NOT IN dengan cara yang sama












print('\n'*2)