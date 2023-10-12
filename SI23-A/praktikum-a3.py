import os
os.system('clear')

nama = 'nama lengkap'
nim  = '6002201014'
meet = 'praktikum 3'
prodi= 'sistem informasi A'
email= 'zaitun.99zt@ith.ac.id'
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
print(meet.capitalize().rjust(sp))
print(prodi.title().rjust(sp))
print(email.rjust(sp))
print('-'*sp)

print(f'''Halo, nama saya {nama.title()} dengan NIM {nim} dari prodi {prodi.title()}, ini adalah file {meet.capitalize()}. Terima kasih.
      ''')

print(f'''Biodata saya,
Nama\t: {nama.title()}
NIM\t: {nim}
Prodi\t: {prodi.title()}
TTL\t: {ttl}
Alamat\t: {alamat}
Asal\t: {asal}
Hobi\t: {hobi}
Tinggi\t: {tinggi}cm
      ''')

stat = 'Newton Frankel Issac'
up   = stat.upper()
print(up)
up = up.split() # up menjadi list n item
print(up)
print(up[-1][0],' '.join(up[0:-1])) #N SIR ISSAC
print('F SIR ISSAC NEWTON')

print(up[-1],up[0][0],up[1][0])
print('NEWTON S I')

print()

stat2 = '&sir$ @issac# *newton.'
up2   = stat2.upper()
print(up2)
up2   = up2.split() 
print(up2)
print(up2[0][1:-1],up2[1][1:-1],up2[2][1:-1])
print(up2[0].strip('&$'),up2[1].strip('@#'),up2[2].strip('*.'))
print('SIR ISSAC NEWTON')



















print()