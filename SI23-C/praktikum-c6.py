import os
os.system('clear')

a = True

while a:
    pilih = input('Apakah ingin melanjutkan? [y/n]')
    if pilih == 'y':
        print('Terima kasih!')
        a = False
    elif pilih == 'n':
        print('Sampai jumpa lagi :)')
        a = False
    else:
        print('Jangan aneh deh! :(')