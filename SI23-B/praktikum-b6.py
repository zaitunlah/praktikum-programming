# Buat file python dengan nama praktikum-b6.py

# Buat program perulangan while dengan jumlah perulangan sebanyak 3 kali

import os
os.system('clear')

a = True
i = 0
limit = 5

while a:
    i += 1         # i = i + 1
    if i <= limit:
        print('Selamat Bergabung',limit-i+1)
    else:
        a = False

