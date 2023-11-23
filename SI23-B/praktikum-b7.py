import os
os.system('clear')

a = True

while a:
    jawab = input('Apakah ingin lanjutkan? (y/n)')
    if jawab == 'y':

        os.system('clear')
        print('Selamat Datang Lagi!')
        a = True

    elif jawab == 'n':

        print('Sampai Ketemu Lagi :D')
        a = False

    else:
        
        os.system('clear')
        print('Jangan aneh-aneh deh :.)')
        a = True
