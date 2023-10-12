import os
os.system('clear')

nama = 'nama lengkap'
nim  = '6002201014'
meet = 'Praktikum 3 (String)'
prodi= 'Sistem Informasi C'
email= 'Zaitun.99zt@ith.ac.id'
ttl = '12-12-2005'
alamat = 'Jl. Balaikota'
asal = 'Parepare'
hobi = 'Olahraga'
tinggi = 160

sp = 40
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.lower().rjust(sp))
print('-'*sp)

print(f'''\tHalo, nama saya {nama} dengan NIM {nim} dari prodi {prodi}, ini adalah file {meet}. Terima kasih.\n''')

print(f'''Biodata saya,
Nama\t: {nama.upper()}
NIM\t: {nim}
Prodi\t: {prodi}
TTL\t: {ttl}
Alamat\t: {alamat}
Asal\t: {asal}
hobi\t: {hobi}
tinggi\t: {tinggi}cm
      ''')

stat1 = 'duFort Frankel Sir Issac'
# Issac duFort Frankel Sir

stat2 = 'duFort Frankel Sir Issac'
# d F S Issac

stat3 = 'duFort Frankel Sir Issac'
# duFort F S I

stat4 = 'duFort Frankel Sir Issac'
# I duFort Frankel Sir

stat5 = 'duFort Frankel Sir Issac'
# Issac d F S

stat6 = 'duFort Frankel Sir Issac'
# ISSAC D F S

stat7 = '#duFort Frankel Sir Issac$'
# duFort Frankel Sir Issac

stat8 = '#duFort-Frankel-Sir-Issac$'
# duFort Frankel Sir Issac

stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
# duFort Frankel Sir Issac

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
# DUFORT FRANKEL SIR ISSAC




print()