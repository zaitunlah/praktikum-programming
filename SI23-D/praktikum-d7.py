import os
os.system('clear')

pwd_benar = 'si23d'
a = True
limit = 3
i = 0
while a:
    i += 1
    pwd = input('Masukkan Password: ')
    if pwd == pwd_benar:
        print('Password Benar! Selamat Anda Login')
        a = False
    else:
        print('Password Salah!')
        if i == limit:
            print('Kesempatan Anda Habis!')
            a = False
        else:
            print(f'Kesempatan anda tersisa {limit-i} kali')


# Tugas: Buat Password Berlapis 3
# jika Salah pertama: Password salah, anda gagal pada halaman 1
# jika Salah ke-2: Password salah, anda gagal pada halaman 2
# jika Salah ke-3: Password salah, anda gagal pada halaman 3

# jika Benar Pertama: Password Benar, Selamat Datang di halaman 1
# jika Benar ke-2: Password Benar, Selamat Datang di halaman 2
# jika Benar ke-3: Password Benar, Selamat Anda Berhasil Login

# Tiap halaman, memiliki kesempatan 3 kali masukkan password


